
from cubeV2 import *
from cube_resolution import *


class Cube_Controller:
    '''The intermediate controller that gives access from the interface to the Cube class'''

    @staticmethod
    def get_rotations():
        '''Returns a list of all the possible rotations of the cube'''
        return ROTATIONS

    @staticmethod
    def get_cube_layout():
        '''Returns a string of the cube layout'''
        return cube.layout

    @staticmethod
    def scramble_cube():
        '''Calls the scrambleCube method of the cube'''
        cube.scrambleCube()

    @staticmethod
    def rotate_face(face):
        '''Calls the rotate method of the cube'''
        cube.rotate(face)

    @staticmethod
    def solve_cube():
        '''Solves the entire cube'''
        execute_resolution(cube)

    @staticmethod
    def solve_white_cross():
        '''Solves the white cross'''
        solve_white_cross(cube)

    @staticmethod
    def solve_white_corners():
        '''Solves the white corners'''
        solve_white_corners(cube)

    @staticmethod
    def solve_second_layer():
        '''Solves the second layer'''
        solve_second_layer(cube)

    @staticmethod
    def solve_yellow_cross():
        '''Solves the yellow cross'''
        solve_yellow_cross(cube)

    @staticmethod
    def orientate_last_layer():
        '''Orientates the last layer'''
        orientate_last_layer(cube)

    @staticmethod
    def solve_last_layer():
        '''Solves the last layer'''
        solve_last_layer(cube)
