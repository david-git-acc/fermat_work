import numpy as np
from matplotlib import pyplot as plt

px = 1/96 # Conversion rate: 1 inch = 96 pixels
resolution = 2500 # Square-resolution in pixels per quadrant
                 # e.g r.=50 means that each quadrant will have an area of 50*50 = 2500 pixels

matrix4 = 1j*np.arange(resolution,-resolution-1,-1 , dtype=int)[:,np.newaxis] + np.arange(-resolution,resolution+1 , dtype=int)
# Generating the matrix of values - using imaginary component to represent y coordinates

n = -2  # Value of n to use for a^n + b^n = c^n

pythagify = (matrix4.real ** n + matrix4.imag ** n) ** (1/n)
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


fig , (ax1,ax2) = plt.subplots(nrows=1,ncols=2 , figsize=(1920*px,1080*px))
# Generating both plots - the first for continuous solutions, which show the decimal part and how close to an integer value
# And the second plot for just plotting only the integer solutions

# Plots the continuous solutions
showCont = ax1.imshow(trueInts , extent = [-resolution,resolution,-resolution,resolution])
showCont.set_cmap("Blues_r")

# Plots the absolute solutions
showAbs = ax2.imshow(plotting , extent = [-resolution,resolution,-resolution,resolution])
showAbs.set_cmap("Blues_r")

# Create a colourbar for the continuous values to act as a legend
bar = plt.colorbar(ax=ax1,
                   mappable=showCont , 
                   label = f"Distance from 0.5 (0.5 = integer)" , 
                   extend = "both" , 
                   orientation = "horizontal" , 
                   shrink=1,
                   pad=0.15)

# Need a boolean legend for the absolute plot, but no direct support for this with imshow
# Dummy plots made so that a legend can be created
ax2.plot(0,0,label="Integer",color="white")
ax2.plot(0,0,label="Decimal",color="darkblue")

# Annotations and labels

ax1.set_xlabel("a value")
ax2.set_xlabel("a value")
ax1.set_ylabel("b value")
ax2.set_ylabel("b value")

ax1.set_title("Continuous solutions")
ax2.set_title("Absolute solutions")
plt.suptitle(f"aⁿ + bⁿ = cⁿ, a visualisation (n={n}) ")

ax2.legend(loc="lower left")
plt.savefig("fermatDiagram2.png")
plt.show()

