'''
Simple script that opens the folders of the given datasets,
taking in the source and destination. It assigns unique
labels to each dataset and outputs it as csv file

'''
import numpy as np
import os
import csv
print "Enter source path"
inp = raw_input()
print "Enter destination file"
inp2 = raw_input()
# bashCommand = "ls /home/shrenik/datasets/ImageNetCustom/ImageNetCustom > folders.txt"
bashCommand = "ls "+ inp + " > " + inp2
os.system(bashCommand);
ar = np.genfromtxt(inp2,'string')
x=1
final = dict()
for i in ar:
	final[i] = x
	x=x+1
writer = csv.writer(open(inp2, 'wb'))
for key, value in final.items():
   writer.writerow([key, value])

    
    