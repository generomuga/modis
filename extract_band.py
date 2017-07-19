from spectral import *
import os

#input directory
modis_dir = os.getcwd()+'\\modis\\'
#output directory
modis_output = os.getcwd()+'\\output\\'
#list of directory item
modis_item = os.listdir(modis_dir)

def extract_band(dir,fname):
	for i in xrange(0,7):
		img = open_image(dir+fname).read_band(i)
		file_save = open(modis_output+str(fname[:7])+str(i+1)+'.txt','w')
		
		#get the shape size
		rows,cols = img.shape
	
		#saves the header
		file_save.write('ncols\t'+str(cols)+'\n'+
						'nrows\t'+str(rows)+'\n'+
						'xllcorner\t12815693.052\n'+
						'yllcorner\t1597502.247\n'+
						'cellsize\t463.31272\n')

		ctr = 0
		for i in xrange(0,520):
			for x in img[i]:
				if ctr < 498:
					ctr = ctr + 1
					file_save.write('\t'+str('%.4f' % x)+'\t')
				else:
					file_save.write('\n')
					ctr = 0

def open_directory():
	for filename in modis_item:
		if filename.endswith(".hdr"):
			print (modis_dir+filename)
			extract_band(modis_dir,filename)

if __name__ == '__main__':
	open_directory()
