

##Answer 20:
def myfunc(inpu=100):
    for num in range(1,inpu+1):
        if num % 3 == 0 and num % 5 == 0:
           print ("FizzBuzz" , end=" "),
        elif num % 3 == 0:
           print  ("Fizz" , end=" "),
        elif num % 5 == 0:
           print ("Buzz" , end=" ") ,
        else:
            print (num , end=" ")


# function call 
myfunc()  or myfunc(100)


###########3updating this file in new branch will push to branch and then 
####merge with master brach via pull request
