#!/usr/bin/python
import os
import sys
import getopt

def parse_input(argv):
	inputFile = ''
	try:
		opts, args = getopt.getopt(argv, "hi:o:", ["input="])
	except getopt.GetoptError:
		print('test.py -i <inputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print('test.py -i <inputfile>')
			sys.exit()
		elif opt in ("-i", "--input"):
			inputFile = arg
	return inputFile


if __name__ == "__main__":
	inputFile = parse_input(sys.argv[1:])

	from PIL import Image
	img = Image.open(inputFile)
	
	import numpy as np
	lr_img = np.array(img)

	from ISR.models import RDN
	rdn = RDN(weights='noise-cancel')
	sr_img = rdn.predict(lr_img)

	inputFileTokens = os.path.splitext(inputFile)
	outputFile = inputFileTokens[0] + "-hd" + inputFileTokens[1]
	Image.fromarray(sr_img).save(outputFile)
