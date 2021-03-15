# 12.	 Write code that retrieves and unpickles the dictionary that you pickled in Algorithm
# Workbench 11.

import pickle

fileToRead = open('mydata.dat', 'rb')
myDict = pickle.load(fileToRead)
print(myDict)
fileToRead.close()