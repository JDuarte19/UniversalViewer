# Will contain basic statistical methods
# Mean, median, range
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def mean(list, n):
    #sum of all values is needed
    sum = 0
    mean = sum/n
    return mean
    
def median(list, n):
    #assumes sorted from least to greatest
    median = 0
    if n % 2 != 0:
        median = list[n//2]
    else:
        a = list[n//2]
        b = list[(n//2) + 1]
        median = (a + b) / 2

    return median

def freq(list, value):
    #works
    total = 0
    print(type(list))
    for i in range(0,len(list)):
        if list[i] == value:
            total += 1
    
    return total

def rel_freq(list, value):
    count = freq(list,value)
    n = len(list)
    percent = count / n
    print(count, percent)
    return percent

def linear_line(bound):
    #creates a y=x line from the bounds given
    #
    x = [range(0,bound)]
    y = []
    for value in x:
        n_y = value
        y.append(n_y)
    print("x: ",x, " y:",y)
    plt.scatter(x,y)
    plt.show()

def display_image(image):
    """A function to display image"""
    display = Image.fromarray(image)
    display.show()
    return

def create_image(size):
    image = np.zeros((size,size))
    display_image(image)
    return

#start of testing
list = [1,1,1,1,1,3,4,5]

#gives count and returns relative freq of value
#   rel_freq(list,1)
#   linear_line(10)

create_image(100)


