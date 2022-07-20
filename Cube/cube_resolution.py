
import time
from db_access import *


def retrieve_algorithm(piece, final_position, table):
    '''Returns the algorithm from the given table that has to be executed
    in order to bring the given piece to the given final position'''
    x,y,z = piece.position
    algorithm = get_algorithm((int(x),int(y),int(z)), final_position, table)
    return algorithm if algorithm != '0' else ''


#-------------------------WHITE-CROSS-RESOLUTION-------------------------


def get_white_edges(cube):
    '''Returns a list of the 4 white edge pieces'''
    white_edges = [piece for piece in cube.edges if 'W' in piece.colors]

    return white_edges


def get_white_cross_algorithm(piece):
    '''Returns the algorithm that has to be executed in order to bring the given piece to his correct position'''
    if 'B' in piece.colors:
        return retrieve_algorithm(piece, (-1, -1, 0), 'white_cross')
    if 'O' in piece.colors:
        return retrieve_algorithm(piece, (0, -1, -1), 'white_cross')
    if 'R' in piece.colors:
        return retrieve_algorithm(piece, (0, -1, 1), 'white_cross')
    if 'G' in piece.colors:
        return retrieve_algorithm(piece, (1, -1, 0), 'white_cross')


def white_cross_orientation(cube):
    '''Corrects the white cross orientation'''
    orientation = {'B':'LiFUFiLL', 'O':'BiLULiBB', 'R':'FiRURiFF', 'G':'RiBUBiRR'}
    for edge in get_white_edges(cube):
        if edge.colors[1] != 'W':
            cube.exec_algorithm(orientation[edge.colors[1]])


def solve_white_cross(cube):
    '''Solves the white cross of the cube'''
    for edge in get_white_edges(cube):
        algorithm = get_white_cross_algorithm(edge)
        cube.exec_algorithm(algorithm)

    white_cross_orientation(cube)


#-------------------------WHITE-CORNERS-RESOLUTION-------------------------


def get_white_corners(cube):
    '''Returns a list of the 4 white corners pieces'''
    white_corners = [piece for piece in cube.corners if 'W' in piece.colors]

    return white_corners


def get_white_corners_algorithm(piece):
    '''Returns the algorithm that has to be executed in order to bring the given piece to his correct position'''
    if 'B' in piece.colors and 'O' in piece.colors:
        return retrieve_algorithm(piece, (-1, -1, -1), 'white_corners')
    if 'B' in piece.colors and 'R' in piece.colors:
        return retrieve_algorithm(piece, (-1, -1, 1), 'white_corners')
    if 'G' in piece.colors and 'O' in piece.colors:
        return retrieve_algorithm(piece, (1, -1, -1), 'white_corners')
    if 'G' in piece.colors and 'R' in piece.colors:
        return retrieve_algorithm(piece, (1, -1, 1), 'white_corners')


def white_corners_orientation(cube):
    '''Corrects the white corners orientation'''
    orientation = [('BWO','LULiUiLULi'), ('BWR', 'FUFiUiFUFi'), ('GWO', 'BUBiUiBUBi'), ('GWR', 'RURiUiRURi')]
    counter = 0
    for corner in get_white_corners(cube):
        while corner.colors != list(orientation[counter][0]):
            cube.exec_algorithm(orientation[counter][1])
        counter += 1


def solve_white_corners(cube):
    '''Solves the white corners of the cube'''
    for corner in get_white_corners(cube):
        algorithm = get_white_corners_algorithm(corner)
        cube.exec_algorithm(algorithm)

    white_corners_orientation(cube)


#-------------------------SECOND-LAYER-RESOLUTION-------------------------


def get_color_edges(cube):
    '''Returns a list of the 4 non-yellow color edge pieces'''
    color_edges = [piece for piece in cube.edges if 'W' not in piece.colors and 'Y' not in piece.colors]

    return color_edges


def get_second_layer_algorithm(piece):
    '''Returns the algorithm that has to be executed in order to bring the given piece to his correct position'''
    if 'B' in piece.colors and 'O' in piece.colors:
        return retrieve_algorithm(piece, (-1, 0, -1), 'second_layer')
    if 'B' in piece.colors and 'R' in piece.colors:
        return retrieve_algorithm(piece, (-1, 0, 1), 'second_layer')
    if 'G' in piece.colors and 'O' in piece.colors:
        return retrieve_algorithm(piece, (1, 0, -1), 'second_layer')
    if 'G' in piece.colors and 'R' in piece.colors:
        return retrieve_algorithm(piece, (1, 0, 1), 'second_layer')


def second_layer_orientation(cube):
    '''Corrects the second layer orientation'''
    orientation = [('B', 'LULiUiBiUiBUiLULiUiBiUiB'), ('B', 'FUFiUiLiUiLUiFUFiUiLiUiL'),
                   ('G', 'RiUiRUBUBiURiUiRUBUBi'), ('G', 'RURiUiFiUiFUiRURiUiFiUiF')]
    counter = 0
    for edge in get_color_edges(cube):
        if edge.colors[0] != orientation[counter][0]:
            cube.exec_algorithm(orientation[counter][1])
        counter += 1


def solve_second_layer(cube):
    '''Solves the second_layer of the cube'''
    for edge in get_color_edges(cube):
        algorithm = get_second_layer_algorithm(edge)
        cube.exec_algorithm(algorithm)

    second_layer_orientation(cube)


#-------------------------YELLOW-CROSS-RESOLUTION-------------------------


def get_yellow_edges(cube):
    '''Returns a list of the 4 yellow edge pieces'''
    yellow_edges = [piece for piece in cube.edges if 'Y' in piece.colors]

    return yellow_edges


def get_yellow_edges_up(cube):
    '''Returns a list of the yellow edges that have yellow facing up'''
    yellows = [edge for edge in get_yellow_edges(cube) if edge.colors[1] == 'Y']

    return yellows


def get_algorithm_yellow_cross(edge_list):
    '''Returns the algorithm the cube has to do to solve the yellow cross'''
    edge1, edge2 = edge_list
    pos1, pos2 = edge1.get_position(), edge2.get_position()

    if (pos1 == (-1, 1, 0) and pos2 == (0, 1, 1)) or (pos2 == (-1, 1, 0) and pos1 == (0, 1, 1)):
        return 'BiRiUiRURiUiRUB'

    elif (pos1 == (-1, 1, 0) and pos2 == (0, 1, -1)) or (pos2 == (-1, 1, 0) and pos1 == (0, 1, -1)):
        return 'UiBiRiUiRURiUiRUB'

    elif (pos1 == (0, 1, -1) and pos2 == (1, 1, 0)) or (pos2 == (0, 1, -1) and pos1 == (1, 1, 0)):
        return 'UUBiRiUiRURiUiRUB'

    elif (pos1 == (0, 1, 1) and pos2 == (1, 1, 0)) or (pos2 == (0, 1, 1) and pos1 == (1, 1, 0)):
        return 'UBiRiUiRURiUiRUB'

    elif (pos1 == (0, 1, -1) and pos2 == (0, 1, 1)) or (pos2 == (0, 1, -1) and pos1 == (0, 1, 1)):
        return 'UBiRiUiRUB'

    else:
        return 'BiRiUiRUB'


def solve_yellow_cross(cube):
    '''Solves the yellow cross of the cube'''
    yellows = get_yellow_edges_up(cube)

    if not yellows:
        cube.exec_algorithm('BiRiUiRUBUUBiRiUiRURiUiRUB')

    elif len(yellows) == 2:
        cube.exec_algorithm(get_algorithm_yellow_cross(yellows))


#-------------------------LAST-LAYER-ORIENTATION-------------------------


def get_last_layer_algorithm(position, table, cube):
    '''Returns the algorithm that has to be executed to orientate the last layer'''
    algorithm = get_LL_algorithm(position, table)

    while algorithm == '0':
        cube.rotate('U')
        position = get_yellow_stickers_positions(cube)
        algorithm = get_LL_algorithm(position, table)

    return algorithm


def get_yellow_stickers_positions(cube):
    '''Returns a list of all the yellows stickers and their position'''
    stickers_positions = [color for row in cube.U_face for piece in row for color in piece.colors]
    yellow_stickers = ''
    for sticker in stickers_positions:
        yellow_stickers += sticker if sticker == 'Y' else '0'

    return yellow_stickers


def orientate_last_layer(cube):
    '''Orientates the last layer of the cube'''
    position = get_yellow_stickers_positions(cube)
    algorithm = get_last_layer_algorithm(position, 'last_layer_orientation', cube)

    cube.exec_algorithm(algorithm)


#-------------------------LAST-LAYER-RESOLUTION-------------------------


def check_correct_position(piece):
    '''Check if piece is in correct position'''
    correct_positions = {'BYO': (-1,1,-1), 'BYR': (-1,1,1), 'GYO': (1,1,-1), 'GYR': (1,1,1)}
    piece_position = ''.join(color for color in piece.colors)

    return piece_position in correct_positions and correct_positions[piece_position] == piece.get_position()


def orientate_yellow_corners(cube):
    '''Return a list of the correctly orientated yellow corners'''
    yellow_corners = [check_correct_position(piece) for row in cube.U_face for piece in row if piece.type == 'Corner']

    while yellow_corners.count(True) < 2:
        cube.rotate('U')
        yellow_corners = [check_correct_position(piece) for row in cube.U_face for piece in row if piece.type == 'Corner']

    return yellow_corners


def solve_last_corners(cube):
    '''Solves the corners of the last layer of the cube'''
    corners_positions = orientate_yellow_corners(cube)
    if corners_positions.count(True) == 2:
        first_index = corners_positions.index(True)
        second_index = corners_positions.index(True, first_index + 1)

        if first_index == 0:
            if second_index == 1:
                cube.exec_algorithm('RURiUiRiFRRUiRiUiRURiFi')
            elif second_index == 2:
                cube.exec_algorithm('UiRURiUiRiFRRUiRiUiRURiFiU')
            elif second_index == 3:
                cube.exec_algorithm('UFRUiRiUiRURiFiRURiUiRiFRFiUi')

        elif first_index == 1:
            if second_index == 2:
                cube.exec_algorithm('FRUiRiUiRURiFiRURiUiRiFRFi')
            elif second_index == 3:
                cube.exec_algorithm('URURiUiRiFRRUiRiUiRURiFiUi')

        elif first_index == 2 and second_index == 3:
            cube.exec_algorithm('UURURiUiRiFRRUiRiUiRURiFiUU')


def solve_last_edges(cube):
    '''Solves the edges of the last layer of the cube'''
    yellow_edges = [piece for row in cube.U_face for piece in row if piece.type == 'Edge']
    edges_colors = ''.join(color for edge in yellow_edges for color in edge.colors if color and color != 'Y')
    algorithm = get_LL_algorithm(edges_colors, 'last_layer_edges')

    cube.exec_algorithm(algorithm)


def solve_last_layer(cube):
    '''Solves the last layer of the cube'''
    solve_last_corners(cube)
    solve_last_edges(cube)


#-------------------------ENTIRE-CUBE-RESOLUTION-------------------------


def execute_resolution(cube):
    '''Executes the entire resolution of teh given cube'''
    solve_white_cross(cube)
    print('white cross done')
    time.sleep(1)
    solve_white_corners(cube)
    print('white face done')
    time.sleep(1)
    solve_second_layer(cube)
    print('second layer done')
    time.sleep(1)
    solve_yellow_cross(cube)
    print('yellow cross done')
    time.sleep(1)
    orientate_last_layer(cube)
    print('last layer orientation done')
    time.sleep(1)
    solve_last_layer(cube)
    print('last layer permutation done')
    

'''
First we look for white edges and their position.
Always get them in same order, blue, orange, red, green, so same order we place in.
We apply the rotation corresponding with those positions.
We check if it is oriented, colors[1] == W.
If not oriented, we do the orientation.
First layer done, now we do the second one.
We look for the 4 edges in order blue-orange, blue-red, green-orange, green-red.
We place them and we make sure they are oriented.
Second layer done, now we do third layer.
First we make list of yellow edges and and check how many are facing U face.
If 0, we do algorithm BiRiUiRUBUUBiRiUiRURiUiRUB. 
If 2, we check positions of Y being colors[1].
If they are next to each other (make function to check that) we check if they are in (-1, 1, 0) and (0, 1, 1).
If so we do algorithm BiRiUiRURiUiRUB, otherwise rotate U and check till they are.
If they are not next, we check if yellow_edges[0].colors[1] == 'Y'. 
If so, we do algorithm BiRiUiRURiUiRUB, else we do U rotation and then the algorithm.
Then we should have the yellow cross.
After that we do orientation of last layer, 
checking the yellow stickers facing up and executing their corresponding algorithms.
Finally we do permutation of last layer.
First we solve yellow corners checking their positions and applying their algorithms.
Then we only have yellow edges left, check their positions and apply their algorithms.
FINISH, cube is now solved.
'''
