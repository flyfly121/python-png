# -*- coding: UTF-8 -*-

from utils import parse_length


class IHDR(object):
    """docstring for IHDR"""

    def __init__(self):
        super(IHDR, self).__init__()
        self.width = None
        self.height = None
        self.bit_depth = None
        self.color_type = None
        self.compression = None
        self.filter = None
        self.interlace = None

    def parse(self, filename):
        self.width = parse_length(filename, 4)
        self.height = parse_length(filename, 4)
        self.bit_depth = parse_length(filename, 1)
        self.color_type = parse_length(filename, 1)
        self.compression = parse_length(filename, 1)
        self.filter = parse_length(filename, 1)
        self.interlace = parse_length(filename, 1)

    def print_ihdr(self):
        print('width : ', self.width)
        print('height : ', self.height)
        print('bit depth : ', self.bit_depth)
        print('color type : ', self.color_type)
        print('compression method : ', self.compression)
        print('filter method : ', self.filter)
        print('interlace method : ', self.interlace)
