import numpy as np
from matplotlib import pyplot as plt
from itertools import count
from matplotlib.animation import FuncAnimation

intervalValue = 50

resolution = 800 # Square-resolution in pixels per quadrant
                 # e.g r.=50 means that each quadrant will have an area of 50*50 = 2500 pixels

matrix = 1j*np.arange(resolution,0-1,-1 , dtype=int)[:,np.newaxis] + np.arange(0,resolution+1 , dtype=int)
# Generating the matrix of values - using imaginary component to represent y coordinates

n = -0.2 # Value of n to use for a^n + b^n = c^n

pythagify = (matrix.real ** n + matrix.imag ** n) ** (1/n)
# Performs the calculation on every element in the matrix 
# Returns as a new matrix called pythagify


fig , ax1 = plt.subplots()
# Generating both plots - the first for continuous solutions, which show the decimal part and how close to an integer value
# And the second plot for just plotting only the integer solutions

index = count()

n = 0.028 + next(index) / 10 ** (1/n)

intValues = abs(np.modf(pythagify)[0])
# Retrieves the decimal value of each element in the matrix, returns as new intValues matrix

trueInts = abs(intValues - 0.5)
# We want to know how "close" we are to an integer solution - the further away from 0.5, the closer to an integer value

plotting = np.ones(intValues.shape) 
# Generates a "template matrix" for us to use, consisting entirely of ones with the same shape as the intValues matrix

plotting[intValues == 0] *= 100
# Every value in the template matrix whose index matches an integer solution from intValues will be multiplied by a scalar


# Plots the continuous solutions
showCont = ax1.imshow(trueInts , extent = [0,resolution,0,resolution])
showCont.set_cmap("Blues_r")

def animate(i):
    n = -3.5 + next(index) / 10 ** 2

    try:
        pythagify = (matrix.real ** n + matrix.imag ** n) ** (1/n)
    except:
        return
    # Performs the calculation on every element in the matrix 
    # Returns as a new matrix called pythagify

    intValues = abs(np.modf(pythagify)[0])
    # Retrieves the decimal value of each element in the matrix, returns as new intValues matrix

    trueInts = abs(intValues - 0.5)
    # We want to know how "close" we are to an integer solution - the further away from 0.5, the closer to an integer value

    plotting = np.ones(intValues.shape) 
    # Generates a "template matrix" for us to use, consisting entirely of ones with the same shape as the intValues matrix

    plotting[intValues == 0] *= 100
    # Every value in the template matrix whose index matches an integer solution from intValues will be multiplied by a scalar

    plt.cla() # Clears the previous screen
    
    plt.suptitle(f"n={round(n,2)} ")
    # Plots the continuous solutions
    showCont = ax1.imshow(trueInts , extent = [0,resolution,0,resolution])
    showCont.set_cmap("Blues_r")
    ax1.set_xlabel("a value")
    ax1.set_ylabel("b value")
    ax1.set_title("Integer solutions for aⁿ + bⁿ = cⁿ")



# Annotations and labels





ani = FuncAnimation(fig , animate , interval = intervalValue)

# Create a colourbar for the continuous values to act as a legend
bar = plt.colorbar(ax=ax1,
                mappable=showCont , 
                label = f"Distance from 0.5 (0.5 = integer)" , 
                extend = "both" , 
                orientation = "horizontal" , 
                shrink=0.55,
                pad=0.15)


plt.show()
