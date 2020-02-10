

##Answer 20:
def myfunc(inpu=100):
    for num in range(1,inpu+1):
        if num % 3 == 0 and num % 5 == 0:
           print ("FB" , end=" "),
        elif num % 3 == 0:
           print  ("F" , end=" "),
        elif num % 5 == 0:
           print ("B" , end=" ") ,
        else:
            print (num , end=" ")


# function call 
myfunc()  or myfunc(100)

