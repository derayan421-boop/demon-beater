import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
#from kmk.modules.macros import Press, Release, Tap, Macros
from kmk.modules.mouse_keys import MouseKeys

keyboard = KMKKeyboard()

#enable mouse support
mouse = MouseKeys()
keyboard.modules.append(mouse)

PINS = [board.D1, board.D2, board.D3]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        KC.SPACE,
        KC.MB_LMB,
        KC.SPACE,  
    ]
]

if __name__ == '__main__':
    keyboard.go()
