import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22])
y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 66, 67, 70, 75, 76, 78, 79, 90, 99, 99, 100])

myline = np.linspace(1, 22, 100)

# Scatter plot of (x, y) values
plt.scatter(x, y)

# Perform polynomial fit for degrees 1 to 5
degrees = [1, 2, 3, 4, 5]
colors = ['r', 'g', 'b', 'c', 'm']

# Loop over the degrees and corresponding colors
for deg, color in zip(degrees, colors):
    # Perform polynomial fitting
    coeffs = np.polyfit(x, y, deg)
    mymodel = np.poly1d(coeffs)
    # Plot the model fit
    plt.plot(myline, mymodel(myline), color, label=f"Degree {deg}")

plt.legend()
plt.show()


'''

Findings: As the degree of the polynomial increases,
the model becomes more complex and has the potential
to capture more intricate patterns in the data. However,
there is a trade-off between complexity and overfitting.
Higher-degree polynomials may fit the given data well,
but they run the risk of being more sensitive to noise
and may not generalize well to new data points

'''