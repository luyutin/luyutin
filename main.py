import argparse
import time
import struct as st

def main(struct, input_file, output_file):
	if struct == 'queue':
		test = st.queue()
	else:
		test = st.stack()

	input = open(input_file)
	output = open(output_file, 'a')

	# TODO: your should parse the input commands here
	line = input.readline()
	while line:
		line = line.split()
		if line[0] == "PUSH":
			n = st.node(None)
			n.value = '{0[1]}'.format(line)
			test.push(n)
		else:
			if test.num_element >= 1:
				test.pop()
		line = input.readline()
		output.write(str(test))
		output.write('\n')
	input.close()

    

if __name__ == '__main__':
	# Do Not Change the code here
	parser = argparse.ArgumentParser()
	parser.add_argument('--structure', choices=['queue', 'stack'], default='stack')
	parser.add_argument('--input', default='./input.txt')
	parser.add_argument('--output', default='./output.txt')
	args = parser.parse_args()
	ts = time.time()
	main(args.structure, args.input, args.output)
	te = time.time()
	print('Ruun Time: {:.5f}s'.format(te-ts))
