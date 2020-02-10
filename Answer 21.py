##Answer 21:


import string
from collections import Counter  
def charcount (filename):
    dic={}
    with open(filename, "r")as f: 
        for line in f:
            new_line=line.replace(" ","")
            dic[line]=Counter(new_line.strip()).most_common(1)
        print ('character :  frequecy' )
        for keys  in dic:
            print (dic[keys][0][0],':',dic[keys][0][1])
