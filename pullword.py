# coding=utf-8
from pullword import pullword
fin = open("input.txt",'r')
fout = open("output.txt", 'a')
ftext = fin.readline()
while ('' != ftext):
    string = ftext.decode('utf-8')
    str = pullword(string)
    fout.write(str.encode('utf-8'))
    ftext = fin.readline()
fin.close()
fout.close()