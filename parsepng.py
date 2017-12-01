# -*- coding: UTF-8 -*-
import struct
import zlib

fileName = "Cookie.png"
fileName1 = "container.jpg"
PNG_MAGIC = '\x89\x50\x4e\x47\x0d\x0a\x1a\x0a'

png = open(fileName, 'rb')
print 'current file position :',png.tell()
pngMagic = png.read(8)
print type(pngMagic), len(pngMagic)

# print png chunk details
def print_png(png_file, chunk_length, desc):
    chunk = png_file.read(chunk_length)
    if chunk_length > 1:
        chunk = chunk[::-1]
        chunk, = struct.unpack('i', chunk)
    elif chunk_length == 1:
        chunk, = struct.unpack('b', chunk)
    print desc+' ('+str(chunk_length)+') :',chunk
    return chunk

def check_png_chunk_crc(file):
    # length = file.read(4)
    # length = length[::-1]
    # length, = struct.unpack('i', length)
    length = print_png(file, 4, 'Length')
    name = file.read(4)
    data = file.read(length)
    file.seek(- (length + 4), 1)
    name_data = file.read(4 + length)
    calculate_crc = zlib.crc32(name_data)
    print u'计算得出的CRC：',calculate_crc
    crc = print_png(png, 4, 'CRC')
    if calculate_crc == crc:
        print name, u' CRC校验通过！！！'
    else:
        print crc, u'CRC校验失败！！！'
    return (length, name, data, crc)

isPNG = pngMagic == PNG_MAGIC

if isPNG:
    print 'You got a PNG file.'
    print '-------------------',png.tell()
    # length
    png_ihdr_length = print_png(png, 4, 'IHDR length')
    # name
    print png.read(4)
    # data
    print_png(png, 4, 'width')
    print_png(png, 4, 'height')
    print_png(png, 1, 'bit depth')
    print_png(png, 1, 'color type')
    print_png(png, 1, 'compression method')
    print_png(png, 1, 'filter method')
    print_png(png, 1, 'interlace method')
    # CRC
    png.seek(- (4 + png_ihdr_length), 1)
    name_data = png.read(4 + png_ihdr_length)
    crc = zlib.crc32(name_data)
    print crc

    png_ihdr_crc = print_png(png, 4, 'CRC')
    print crc == png_ihdr_crc
    
    while 1:
        print '-----------------',png.tell()
        chunk = check_png_chunk_crc(png)
        if chunk[1] == 'tEXt':
            print chunk[2]
        if chunk[1] == 'IEND':
            break
else:
    print 'What a pity! this is not a PNG file, Sorry!'

png.seek(0)
x = png.read(1)
index = 0
while x:
    y = x.encode('hex')
    print y,
    x = png.read(1)
    index += 1
    if index % 16 == 0:
        print ''

png.close()