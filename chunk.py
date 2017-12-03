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

	def parse_ihdr(self, file):
		pass

	def parse(self, file):
		self.length = parse_length(file, 4)
		self.name = file.read(4)
		if self.name == 'IHDR':
			ihdr = IHDR()
			ihdr.parse(file)
			self.data = ihdr
		else:
			self.data = file.read(self.length)
		file.seek(- (4 + self.length), 1)
		name_data = file.read(4 + self.length)
		calculate_crc = zlib.crc32(name_data)
		self.crc = file.read(4)
		self.crc_pass = self.crc == calculate_crc

	def print_chunk(self):
		print 'name : ', self.name
		print 'length : ', self.length
		if self.name == 'IHDR':
			self.data.print_ihdr()
		if self.name == 'tEXt':
			print 'data : ',self.data
		print 'crc : ', self.crc_pass


if __name__ == '__main__':
	x = Chunk(13, 'IEND', '', 123)
	print x.name
		