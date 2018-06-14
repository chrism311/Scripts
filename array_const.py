'''
This script was used in my EEG signal classification research. The script unpacks the raw signals into rows of 500 ms 
epoch and labels them to their respectful stage of sleep.
'''

import csv

#Constructs arrays of length 500 ms from raw signals
def constructor(filename, new_file, start, stop, label):
	with open(filename, 'r') as fileRead:
		reader = csv.reader(fileRead, delimiter=',')
		for row in reader:
			if float(row[0]) == float(start):
				try:
					while float(row[0]) != float(stop):
						array = []
						print "Time Stamp: "+ str(float(row[0]))
						array.append(row[0])
						for i in range(50):
							array.append(row[1])
							row = next(reader)
						with open(new_file, 'ab') as fileWrite:
							array.append(label)
							writer = csv.writer(fileWrite)
							writer.writerow(array)
				except StopIteration:
					pass
			else:
				continue

if __name__ == '__main__':
	constructor('SC4001E0-PSG_data.csv', 'SC4001E0-FPZ-CZ.csv', 0, 30630 ,0)
