import os

#change working dir to current dir
os.chdir(os.getcwd())

file=open('rosalind_ini5_1_dataset.txt', 'r')

for each in file:
    if each % 2:
        print(each)