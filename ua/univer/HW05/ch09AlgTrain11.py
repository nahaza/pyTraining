# 11.	 Assume the variable dct references a dictionary. Write code that pickles the dictionary
# and saves it to a file named mydata.dat.

import pickle

fileToWrite = open('mydata.dat', 'wb')
pickle.dump(dct, fileToWrite)
fileToWrite.close()
