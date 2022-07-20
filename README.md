# Cube
A Rubik's Cube which can solve itself!

The project is all made in Python 3.9.7

This small project presents a model of a Rubik's cube with both 2D and 3D interactive interfaces, in order to preview the cube status at any moment during resolution.

It consists in 6 different files, one being the database for the cube's algorithms, and each of the other 5 focusing on a specific functionallity related with the cube.

cubeV2.py is the main file of the project. It contains the 3D implementation of the cube, as well as all the components of the cube itself and his methods.

cube_resolution.py is the file which contain every function related with the resolution of the cube once it is scrambled.

db_access.py is a small file with only two functions to access the database of the cube.

cube_interface.py contains the 2D interface of the cube, with some buttons to interact with it. Said interface is made using PySimpleGUI
This is the file you wanna execute for the program to work, it will open the 3D interface in your browser (localhost) and the 2D interface in a different window, from where you can interact with the cube, rotating each face, scrambling or solving it.

finally cube_controller is a file containing a controller class between the interface and the rest of the code.


This is one of my first projects using python, after ~ 8 months using it, so some errors and inefficiencies are expected, any advice is welcomed in the comments!

Thank you for reading this.
