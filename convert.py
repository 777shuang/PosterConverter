import os
import subprocess
import shutil
import sys
from math import sqrt
import pypdf as pdf

def convert(input: str, output: str, hsplit: int):
    reader = pdf.PdfReader(input)
    writer = pdf.PdfWriter()

    width = reader.pages[0].mediabox.right
    height = reader.pages[0].mediabox.height

    ROOT2 = sqrt(2)

    width_split = width / hsplit
    height_split = width_split / ROOT2
    for i in range(hsplit):
        j = 0
        while True:
            h = height_split * j # 処理する垂直位置
            if h >= height: break
            p1 = reader.pages[0]
            p1.cropbox.lower_left = (width_split*i, h,)
            p1.cropbox.upper_right = (width_split*(i+1), h+height_split,)
            writer.add_page(p1)
            j+=1

    os.chdir(os.path.dirname(__file__))
    writer.write('output.pdf')
    subprocess.run('latexmk -lualatex poster.tex')
    shutil.move('poster.pdf', output)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('コマンドライン引数は')
        print('input.pdf output.pdf 水平方向分割数(整数)')
        print('のみ受け付けます。')
    else:
        convert(sys.argv[1], sys.argv[2], int(sys.argv[3]))