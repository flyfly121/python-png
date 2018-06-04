# -*- coding: UTF-8 -*-

from chunk import Chunk


fileName = "Cookie.png"
PNG_MAGIC = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

pngfile = open(fileName, 'rb')
pngMagic = pngfile.read(8)

if pngMagic == PNG_MAGIC:
    chunk = Chunk()
    while True:
        print('-----------------')
        chunk.parse(pngfile)
        chunk.print_chunk()
        if chunk.name == 'IEND':
            break

pngfile.close()
