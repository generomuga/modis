from spectral import *
import numpy as np


img = open_image('2003001_ref.hdr').read_band(0)

file_save = open('band1.txt','w')


ctr = 0

for i in xrange(0,520):
	for x in img[i]:
		if ctr < 498:
			ctr = ctr + 1
			file_save.write(str(x)+'\t')
		else:
			file_save.write('\n')
			ctr = 0


