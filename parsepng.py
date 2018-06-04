# -*- coding: UTF-8 -*-

from chunk import Chunk
from drawchunk import drawchunk


fileName = "Cookie.png"
PNG_MAGIC = b'\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

pngfile = open(fileName, 'rb')
pngMagic = pngfile.read(8)
allchunk = []

if pngMagic == PNG_MAGIC:
    while True:
        print('-----------------')
        chunk = Chunk()
        allchunk.append(chunk)
        chunk.parse(pngfile)
        chunk.print_chunk()
        if chunk.name == 'IEND':
            break

drawchunk(allchunk)

pngfile.close()
