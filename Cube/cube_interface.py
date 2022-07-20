
import PySimpleGUI as sg
from cube_controller import Cube_Controller

controller = Cube_Controller()
ROTATIONS = controller.get_rotations()
LAYOUT = controller.get_cube_layout()

def color(face):
    '''Transform the initial of a color into the entire color name'''
    if face == 'O': return 'Orange'
    elif face == 'R': return 'Red'
    elif face == 'B': return 'Blue'
    elif face == 'G': return 'Green'
    elif face == 'Y': return 'Yellow'
    elif face == 'W': return 'White'


def update_layout():
    '''Updates the layout of the interface to match the actual colors of the cube'''
    LAYOUT = controller.get_cube_layout()
    counter = 0
    for i in range(1, len(window.element_list())):
        # Only applies the update to the Text elements of the interface (they are the cube stickers)
        if isinstance(window.element_list()[i], sg.Text):
            window.element_list()[i].update(background_color=color(LAYOUT[counter]))
            counter += 1


def create_window(theme):
    '''Creates a new window with a given theme'''
    sg.theme(theme)
    sg.set_options(font = 'Franklin 10')
    SIZE = (4,2)
    BUTTON_SIZE = (4, 3)
    layout = [
        [sg.Text('2D View', font = 'Franklin 25', justification = 'left', expand_x = True, pad = (10, 10)), sg.Button(button_text='SCRAMBLE IT ALL', border_width=5, size = (20, 1), pad=(10, 10), button_color=('Darkblue', 'pink'), font='"Racing Sans One" 20 bold')],
        [sg.Button(button_text='R', size = BUTTON_SIZE, pad=((20, 1), 5), button_color='Grey'), sg.Button(button_text='Ri', size = BUTTON_SIZE, pad=((1, 5), 5), button_color='Grey'), sg.Button(button_text='L', size = BUTTON_SIZE, pad=((5, 1), 5), button_color='Grey'), sg.Button(button_text='Li', size = BUTTON_SIZE, pad=((1, 5), 5), button_color='Grey'), sg.Button(button_text='U', size = BUTTON_SIZE, pad=((5, 1), 5), button_color='Grey'), sg.Button(button_text='Ui', size = BUTTON_SIZE, pad=(1, 5), button_color='Grey'), sg.Button(button_text='D', size = BUTTON_SIZE, pad=((10, 1), 5), button_color='Grey'), sg.Button(button_text='Di', size = BUTTON_SIZE, pad=((1, 5), 5), button_color='Grey'), sg.Button(button_text='F', size = BUTTON_SIZE, pad=((5, 1), 5), button_color='Grey'), sg.Button(button_text='Fi', size = BUTTON_SIZE, pad=((1, 5), 5), button_color='Grey'), sg.Button(button_text='B', size = BUTTON_SIZE, pad=((5, 1), 5), button_color='Grey'), sg.Button(button_text='Bi', size = BUTTON_SIZE, pad=(1, 5), button_color='Grey')],
        [sg.Text(size = SIZE, pad=((158, 5), (20, 5)), background_color=f'{color(LAYOUT[0])}'), sg.Text(size = SIZE, pad=(5, (20, 5)), background_color=f'{color(LAYOUT[1])}'), sg.Text(size = SIZE, pad=(5, (20, 5)), background_color=f'{color(LAYOUT[2])}')],
        [sg.Text(size = SIZE, pad=((158, 5), 5), background_color=f'{color(LAYOUT[3])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[4])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[5])}')],
        [sg.Text(size = SIZE, pad=((158, 5), 5), background_color=f'{color(LAYOUT[6])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[7])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[8])}')],
        [sg.Text(size = SIZE, pad=((20, 5), 5), background_color=f'{color(LAYOUT[9])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[10])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[11])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[12])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[13])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[14])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[15])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[16])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[17])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[18])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[19])}'), sg.Text(size = SIZE, pad=((5, 20), 5), background_color=f'{color(LAYOUT[20])}')],
        [sg.Text(size = SIZE, pad=((20, 5), 5), background_color=f'{color(LAYOUT[21])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[22])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[23])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[24])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[25])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[26])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[27])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[28])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[29])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[30])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[31])}'), sg.Text(size = SIZE, pad=((5, 20), 5), background_color=f'{color(LAYOUT[32])}')],
        [sg.Text(size = SIZE, pad=((20, 5), 5), background_color=f'{color(LAYOUT[33])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[34])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[35])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[36])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[37])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[38])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[39])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[40])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[41])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[42])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[43])}'), sg.Text(size = SIZE, pad=((5, 20), 5), background_color=f'{color(LAYOUT[44])}')],
        [sg.Text(size=SIZE, pad=((158, 5), 5), background_color=f'{color(LAYOUT[45])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[46])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[47])}')],
        [sg.Text(size=SIZE, pad=((158, 5), 5), background_color=f'{color(LAYOUT[48])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[49])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[50])}')],
        [sg.Text(size=SIZE, pad=((158, 5), 5), background_color=f'{color(LAYOUT[51])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[52])}'), sg.Text(size = SIZE, background_color=f'{color(LAYOUT[53])}')],
        [sg.Button(button_text='CLICK TO SOLVE THE CUBE', border_width=5, size = (35, 1), pad=(10, 10), button_color=('Darkblue', 'pink'), font='"Racing Sans One" 20 bold')]
    ]

    return sg.Window("RUBIK'S CUBE", layout)

window = create_window('dark')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if 'SCRAMBLE' in event:
        controller.scramble_cube()

    if event in ROTATIONS:
        controller.rotate_face(event)

    if 'CLICK' in event:
        controller.solve_white_cross()
        update_layout()
        window.refresh()
        controller.solve_white_corners()
        update_layout()
        window.refresh()
        controller.solve_second_layer()
        update_layout()
        window.refresh()
        controller.solve_yellow_cross()
        update_layout()
        window.refresh()
        controller.orientate_last_layer()
        update_layout()
        window.refresh()
        controller.solve_last_layer()

    update_layout()

window.close()