# -*- coding: UTF-8 -*-

from chunk import Chunk


fileName = "Cookie.png"
PNG_MAGIC = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

png = open(fileName, 'rb')
pngMagic = png.read(8)

if pngMagic == PNG_MAGIC:
    chunk = Chunk()
    while True:
        print('-----------------')
        chunk.parse(png)
        chunk.print_chunk()
        if chunk.name == 'IEND':
            break
else:
    print("Python3")

png.close()
