# -*- coding: UTF-8 -*-

import struct

def parse_length(file, size):
	chunk_length = file.read(size)
	if size > 1:
		chunk_length = chunk_length[::-1]
		chunk_length, = struct.unpack('i', chunk_length)
	elif size == 1:
		chunk_length, = struct.unpack('b', chunk_length)
	return chunk_length