# -*- coding: UTF-8 -*-
import struct
import zlib
from chunk import Chunk

fileName = "Cookie.png"
PNG_MAGIC = '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

png = open(fileName, 'rb')
pngMagic = png.read(8)

if pngMagic == PNG_MAGIC:
    chunk = Chunk()
    while 1:
        print '-----------------'
        chunk.parse(png)
        chunk.print_chunk()
        if chunk.name == 'IEND':
            break

png.close()