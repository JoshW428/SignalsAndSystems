import numpy as np
import math


def  myconv(x,h):
 
 

############################################################################
# A function to generate the output signal y as convolution of input signal
# x and impulse response signal h
############################################################################

# INPUT PARAMETERS---------------------------------------------------------
# x: input signal
# h: impulse response
    len_x = len(x) # length of x
    len_h = len(h) # length of h
############################################################################
# Data processing: convolution (TO BE COMPLETED BY STUDENTS)
############################################################################
# OUTPUT PARAMETERS--------------------------------------------------------
# y: output signal as convolution of input signal x and impulse response h

# Write the code including comments to explain what you are doing

# x = [0,0,0,1,2,3,4,5]
# h = [0,0,0,0,0,5,6,7]

    if (len(x)<len(h)):
        x, h = h, x

    len_x = len(x) # length of x
    len_h = len(h) # length of h



    for j in range(0, len_h):
        x.insert(j, 0)
        

    for i in range(0, len_x):
        h.append(0)


    len_x = len(x) 
    len_h = len(h)

    y = []

    print("x: ", x)
    print("h: ", h)
    print("y: ", y)
    print()

    len_x = len(x) # length of x
    len_h = len(h) # length of h

    print()
    print("len(x): ", len_x)
    print("len(h): ", len_h)

    print()

    for i in range(0, len_x+1):
        y.insert(i,0)
        for j in range(0, len_h):
            if (i-j+1 > 0):
                if(j!=0):
                    y[i] = y[i]+x[j]*h[i-j-1]
                
                
     #           print("y: ", y)
            else:
                break

    zeroCount = 0
    for q in range(0, len(y)):
        if(y[q] == 0):
            zeroCount = zeroCount + 1
            print("0: ", zeroCount)

    y = remove_values_from_list(y, 0)

    for w in range(0, zeroCount):
        y.append(0)
    
    
 

    print()
    print("x: ", x)
    print("h: ", h)
    print("y: ", y)
    
    
    return y


def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]




#myconv([3,7,5],[4,6,7,2,1])
