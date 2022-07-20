
import math
import numpy as np
import txaio as tx
import vpython as vp
from random import choice
from scipy.spatial.transform import Rotation as rot


tx.use_asyncio()

ROTATION_SPEED = 7   # Speed of the rotations in the animation

# All the possible rotations the cube can do
ROTATIONS = ['R','Ri','L','Li','U','Ui','D','Di','F','Fi','B','Bi']


#-------------------------CLASS-PIECE-------------------------


class Piece:
    '''The parts which the cube is made of.
       Each piece has a tuple of up to 3 colors,
       and a position determined by a tuple of x, y, z coordinates from -1 to 1'''

    def __init__(self, colors, pos):
        '''Creates a Piece object given his colors and axis'''
        self.colors = list(colors)
        self.c1, self.c2, self.c3 = self.colors
        self.position = pos
        self._set_piece_type()
        self.rotated = False


    def __str__(self):
        '''Returns the impression of a Corner object'''
        colors = ''.join(c for c in self.colors if c is not None)
        return f'({self.type}, {colors}, {self.position})'


    def _set_piece_type(self):
        '''Set the piece's type to corner, edge or center, depending on how many colors it has'''
        if self.colors.count(None) > 1:
            self.type = 'Center'
        elif None in self.colors:
            self.type = 'Edge'
        else:
            self.type = 'Corner'


    def get_position(self):
        '''Returns a tuple of the piece position'''
        x,y,z = self.position

        return int(x), int(y), int(z)


    def rotatePiece(self, face):
        '''Permutes the piece colours along the given face (or axis)'''
        rot_angle = np.radians(90) if len(face) > 1 else np.radians(-90)    # Angle of the rotation

        if face[0] == 'R': face = (1, 0, 0)
        elif face[0] == 'L': face = (-1, 0, 0)
        elif face[0] == 'U': face = (0, 1, 0)
        elif face[0] == 'D': face = (0, -1, 0)
        elif face[0] == 'F': face = (0, 0, 1)
        elif face[0] == 'B': face = (0, 0, -1)
        elif face[0] == 'M': face = (1, 0, 0)

        perm1 = face.index(0)  # Index of the first color to permute
        perm2 = face.index(0, face.index(0) + 1)  # Index of the second color to permute
        self.colors[perm1], self.colors[perm2] = self.colors[perm2], self.colors[perm1]
        self.c1, self.c2, self.c3 = self.colors

        self.updatePosition(rot_angle, face)


    def updatePosition(self, angle, axis):
        '''Updates the piece position aplying a rotation of the given angle along the given axis'''
        rotation_vector = angle * np.array(axis)
        rotation = rot.from_rotvec(rotation_vector)
        self.position = rotation.apply(self.position)
        self.rotated = True


#-------------------------CLASS-CUBE3D-------------------------


class Cube3D:
    '''Is the 3D representation of a Cube object.
       It's made of pieces, each one with 1 to 3 stickers of different colours'''

    def __init__(self):
        '''Creates a Cube3D object'''
        self.faces = {'D': (vp.color.white, vp.vector(0, -1, 0)),       # Down face
                      'U': (vp.color.yellow, vp.vector(0, 1, 0)),       # Up face
                      'L': (vp.color.blue, vp.vector(-1, 0, 0)),        # Left face
                      'R': (vp.color.green, vp.vector(1, 0, 0)),        # Right face
                      'B': (vp.color.orange, vp.vector(0, 0, -1)),      # Back face
                      'F': (vp.color.red, vp.vector(0, 0, 1))}          # Front face

        self.stickers = []
        for face_color, axis in self.faces.values():
            for x in (-1, 0, 1):                        #Starts with all the stickers up
                for y in (-1, 0, 1):                    #then we rotate them to their position

                    sticker = vp.box(color=face_color, pos=vp.vector(x, y, 1.5), length=0.98, height=0.98, width=0.05)

                    #Cosine of the angle between Z axis and face axis
                    cos_angle = vp.dot(vp.vector(0, 0, 1), axis)
                    #Axis in which the sticker will rotate
                    pivot = vp.cross(vp.vector(0, 0, 1), axis) if cos_angle == 0 else vp.vector(1, 0, 0)

                    sticker.rotate(vp.acos(cos_angle), pivot, vp.vector(0, 0, 0))
                    self.stickers.append(sticker)


    def rotate3D(self, face):
        '''Makes a 90 degrees 3D rotation of the given face and all his stickers.
           It does a rotation like a Rubik's cube do, pivoting on the center of the cube'''
        dot_value = 1.0
        if face[0] == 'M':
            face = 'R' if len(face) == 1 else 'Ri'
            dot_value = 0.0

        face_color, axis = self.faces[face[0]]

        # Makes the rotation clockwise or counterclockwise, depending on the given face
        angle = math.radians(90) if len(face) > 1 else math.radians(-90)   # A way of having a conditional in just 1 line

        for _ in np.arange(0, angle, angle / 30):
            vp.rate(30 * ROTATION_SPEED)  # Here the speed of the animation is determined.
            for sticker in self.stickers:
                if dot_value - 0.59 <= vp.dot(sticker.pos, axis) <= dot_value + 0.59:
                    sticker.rotate(angle / 30, axis, vp.vector(0, 0, 0))


#-------------------------CLASS-CUBE-------------------------


class Cube:
    '''It's the cube itself, with all the pieces (8 corners, 12 edges and 6 centers).
       It also has a layout to represent his status in 2D'''

    def __init__(self):
        '''Creates a Cube object'''
        self.cube3D = Cube3D()

        # The layout is a 54 lenght string that says the color of every sticker in the cube, in a determined order.
        self.layout = 'OOOOOOOOOBBBWWWGGGYYYBBBWWWGGGYYYBBBWWWGGGYYYRRRRRRRRR'
                    # X    Y    Z     X   Y   Z    axis
        BWO = Piece(('B', 'W', 'O'), (-1, -1, -1))
        BWR = Piece(('B', 'W', 'R'), (-1, -1, 1))
        BYO = Piece(('B', 'Y', 'O'), (-1, 1, -1))
        BYR = Piece(('B', 'Y', 'R'), (-1, 1, 1))
        GWO = Piece(('G', 'W', 'O'), (1, -1, -1))
        GWR = Piece(('G', 'W', 'R'), (1, -1, 1))
        GYO = Piece(('G', 'Y', 'O'), (1, 1, -1))
        GYR = Piece(('G', 'Y', 'R'), (1, 1, 1))
        YR = Piece((None, 'Y', 'R'), (0, 1, 1))     # Edges only have 2 colors so one of the values is always None
        BR = Piece(('B', None, 'R'), (-1, 0, 1))
        GR = Piece(('G', None, 'R'), (1, 0, 1))
        WR = Piece((None, 'W', 'R'), (0, -1, 1))
        BY = Piece(('B', 'Y', None), (-1, 1, 0))
        GY = Piece(('G', 'Y', None), (1, 1, 0))
        BW = Piece(('B', 'W', None), (-1, -1, 0))
        GW = Piece(('G', 'W', None), (1, -1, 0))
        YO = Piece((None, 'Y', 'O'), (0, 1, -1))
        BO = Piece(('B', None, 'O'), (-1, 0, -1))
        GO = Piece(('G', None, 'O'), (1, 0, -1))
        WO = Piece((None, 'W', 'O'), (0, -1, -1))   # Centers only have one color so two of the values are always None
        R = Piece((None, None, 'R'), (0, 0, 1))
        Y = Piece((None,'Y', None), (0, 1, 0))
        B = Piece(('B', None, None), (-1, 0, 0))
        G = Piece(('G', None, None), (1, 0, 0))
        W = Piece((None, 'W', None), (0, -1, 0))
        O = Piece((None, None, 'O'), (0, 0, -1))

        self.corners = [BWO, BWR, BYO, BYR, GWO, GWR, GYO, GYR]
        self.edges = [BW, BO, BR, BY, WO, WR, YO, YR, GW, GO, GR, GY]
        self.centers = [B, W, O, R, Y, G]

        self.position = [   [                       # It's a tridimensional array that
                                [BWO, BW, BWR],     # Represents the position of every piece in the cube.
                                [BO,   B,  BR],
                                [BYO, BY, BYR]
                            ],
                            [
                                [WO,  W,  WR],
                                [O, 'CORE',R],
                                [YO,  Y,  YR]
                            ],                      # This is how it will look if we rotate the R (right) face clockwise
                            [
                                [GWO, GW, GWR],     #       [GYO, GO, GWO]
                                [GO,   G,  GR],     #  -->  [GY,  G,   GW]
                                [GYO, GY, GYR]      #       [GYR, GR, GWR]
                            ]
                        ]

        self.updateFaces()
        self.updateLayout()


    def updateFaces(self):
        '''Updates the faces of the cube with their corresponding pieces'''
        self.R_face = self.position[2]
        self.L_face = self.position[0]
        self.U_face = [row for f in self.position for row in f if f.index(row) == 2]
        self.D_face = [row for f in self.position for row in f if f.index(row) == 0]
        self.F_face = [[self.position[i][j][2] for j in range(3)] for i in range(3)]
        self.B_face = [[self.position[i][j][0] for j in range(3)] for i in range(3)]
        self.M_face = self.position[1]


    def updateLayout(self):
        '''Updates the cube's layout to his actual one'''
        back = [self.B_face[j][i].colors[-1] for i in range(2,-1,-1) for j in range(3)]

        center1 = [piece.colors[0] for piece in self.B_face[0]][::-1] + [row[0].colors[1] for row in self.B_face] + \
                  [piece.colors[0] for piece in self.B_face[2]] + [row[2].colors[1] for row in self.B_face][::-1]

        center2 = [row[1].colors[0] for row in self.L_face][::-1] + [row[1].colors[1] for row in self.D_face] + \
                  [row[1].colors[0] for row in self.R_face] + [row[1].colors[1] for row in self.U_face][::-1]

        center3 = [piece.colors[0] for piece in self.F_face[0]][::-1] + [row[0].colors[1] for row in self.F_face] + \
                  [piece.colors[0] for piece in self.F_face[2]] + [row[2].colors[1] for row in self.F_face][::-1]

        front = [self.F_face[j][i].colors[-1] for i in range(3) for j in range(3)]

        self.layout = ''.join(back + center1 + center2 + center3 + front)


    def __str__(self):
        '''Returns the 2D impression of the cube'''
        template = ("    {}{}{}\n"
                    "    {}{}{}\n"  # Back = Orange
                    "    {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"  # Left, Down, Right, Up = Blue, White, Green, Yellow
                    "{}{}{} {}{}{} {}{}{} {}{}{}\n"
                    "    {}{}{}\n"
                    "    {}{}{}\n"  # Front = Red
                    "    {}{}{}")

        return template.format(*self.layout)


    def pos(self, pos1, pos2, pos3):
        '''Transform the format of the positions from -1,0,1 to 0,1,2'''
        print(self.position[pos1+1][pos2+1][pos3+1])
        return self.position[pos1+1][pos2+1][pos3+1]


    def rotate(self, face):
        '''Makes a 90 degrees rotation (clock or counterclockwise) of the given face and all his stickers'''
        self.cube3D.rotate3D(face)
        if face[0] == 'R':
            self.R_face = list(zip(*self.R_face[::-1])) if face == 'R' else list(zip(*self.R_face))[::-1]
            for i in range(3):
                for j in range(3):
                    self.position[2][i][j] = self.R_face[i][j]
                    self.R_face[i][j].rotatePiece(face)

        elif face[0] == 'L':
            self.L_face = list(zip(*self.L_face))[::-1] if face == 'L' else list(zip(*self.L_face[::-1]))
            for i in range(3):
                for j in range(3):
                    self.position[0][i][j] = self.L_face[i][j]
                    self.L_face[i][j].rotatePiece(face)

        elif face[0] == 'U':
            self.U_face = list(zip(*self.U_face))[::-1] if face == 'U' else list(zip(*self.U_face[::-1]))
            for i in range(3):
                for j in range(3):
                    self.position[i][2][j] = self.U_face[i][j]
                    self.U_face[i][j].rotatePiece(face)

        elif face[0] == 'D':
            self.D_face = list(zip(*self.D_face[::-1])) if face == 'D' else list(zip(*self.D_face))[::-1]
            for i in range(3):
                for j in range(3):
                    self.position[i][0][j] = self.D_face[i][j]
                    self.D_face[i][j].rotatePiece(face)

        elif face[0] == 'F':
            self.F_face = list(zip(*self.F_face[::-1])) if face == 'F' else list(zip(*self.F_face))[::-1]
            for i in range(3):
                for j in range(3):
                    self.position[i][j][2] = self.F_face[i][j]
                    self.F_face[i][j].rotatePiece(face)

        elif face[0] == 'B':
            self.B_face = list(zip(*self.B_face))[::-1] if face == 'B' else list(zip(*self.B_face[::-1]))
            for i in range(3):
                for j in range(3):
                    self.position[i][j][0] = self.B_face[i][j]
                    self.B_face[i][j].rotatePiece(face)

        if face[0] == 'M':
            self.M_face = list(zip(*self.M_face[::-1])) if face == 'M' else list(zip(*self.M_face))[::-1]
            for i in range(3):
                for j in range(3):
                    self.position[1][i][j] = self.M_face[i][j]
                    self.M_face[i][j].rotatePiece(face) if self.M_face[i][j] != 'CORE' else None

        self.updateFaces()
        self.updateLayout()


    def exec_algorithm(self, algorithm):
        '''Makes all the rotations in the given algorithm.
           The algorith must be a string containing only
           the possible rotations (R, L, U, D, F, B, M).
           If a "i" is given the previous rotation is made counterclockwise'''
        for i in range(len(algorithm)):
            try:
                if algorithm[i] == 'i':
                    pass
                elif algorithm[i+1] == 'i':
                    print(algorithm[i] + 'i')
                    self.rotate(algorithm[i] + 'i')
                else:
                    print(algorithm[i])
                    self.rotate(algorithm[i])
            except IndexError:
                print(algorithm[i])
                self.rotate(algorithm[i])


    def scrambleCube(self):
        '''Scrambles the cube randomly to be able to solve it'''
        scramble = [choice(ROTATIONS) for _ in range(20)]   # A random algorithm of 20 rotations
        self.exec_algorithm(scramble)


#-------------------------MAIN--------------------


cube = Cube()
print(cube)

