# -*- coding: UTF-8 -*-

import zlib
from ihdr import IHDR
from utils import parse_length


class Chunk(object):
    """docstring for Chunk"""

    def __init__(self):
        super(Chunk, self).__init__()
        self.length = None
        self.name = None
        self.data = None
        self.crc = None
        self.crc_pass = None

    def parse(self, filename):
        self.length = parse_length(filename, 4)
        self.name = str(filename.read(4), encoding='utf-8')
        if self.name == 'IHDR':
            ihdr = IHDR()
            ihdr.parse(filename)
            self.data = ihdr
        else:
            self.data = filename.read(self.length)
        filename.seek(- (4 + self.length), 1)
        name_data = filename.read(4 + self.length)
        calculate_crc = zlib.crc32(name_data)
        self.crc = parse_length(filename, 4)
        self.crc_pass = self.crc == calculate_crc

    def print_chunk(self):
        print('name : ', self.name)
        print('length : ', self.length)
        if self.name == 'IHDR':
            self.data.print_ihdr()
        if self.name == 'tEXt':
            print('data : ', self.data)
        print('CRC : ', self.crc_pass)


