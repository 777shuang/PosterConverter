import re
import TkEasyGUI as eg
from convert import convert

INPUT = 'input'
OUTPUT = 'output'
HSPLIT = 'hsplit'
UP = 'up'
DOWN = 'down'

layout = [
    [eg.Text('変換するPDF'), eg.Input(key=INPUT), eg.FileBrowse(file_types=(("PDF", "*.pdf"),))],
    [eg.Text('水平方向分割数:'), eg.Input('3', key=HSPLIT, readonly=True), eg.Button('▲', key=UP), eg.Button('▼', key=DOWN)],
    [eg.Text('保存先'), eg.Input(key=OUTPUT), eg.FileSaveAs(file_types=(("PDF", "*.pdf"),))],
    [eg.Button('OK')]
]

window = eg.Window('ポスター変換器', layout)

while window.is_alive():
    event, values = window.read()

    if event == "OK":
        convert(values[INPUT], values[OUTPUT], int(values[HSPLIT]))
        break
    elif event == UP:
        window[HSPLIT].update(str(int(values[HSPLIT])+1))
    elif event == DOWN:
        hsplit = int(values[HSPLIT])
        if hsplit != 1:
            window[HSPLIT].update(str(hsplit-1))

window.close()