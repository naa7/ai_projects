import numpy as np
import matplotlib.pyplot as plt

# The third_degree_polynomial_fit function solves
# a set of linear equations using the Vandermonde
# matrix approach. It constructs the matrix X,
# calculates the matrix product X.T * X, and solves
# the system of equations to obtain the coefficients.
def third_degree_polynomial_fit(x, y):
    n = len(x)
    X = np.vstack([x**3, x**2, x, np.ones(n)]).T
    A = np.dot(X.T, X)
    b = np.dot(X.T, y)
    coeffs = np.linalg.solve(A, b)
    return coeffs

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 18, 19, 21, 22])
y = np.array([100, 90, 80, 60, 60, 55, 60, 65, 66, 67, 70, 75, 76, 78, 79, 90, 99, 99, 100])

# Scatter plot of (x, y) values
plt.scatter(x, y)

# Fit third-degree polynomial using custom algorithm
coeffs = third_degree_polynomial_fit(x, y)
mymodel = np.poly1d(coeffs)

# Plot the model fit
myline = np.linspace(1, 22, 100)
plt.plot(myline, mymodel(myline), 'r', label="Degree 3 (Custom)")

# Perform polynomial fit using numpy
numpy_coeffs = np.polyfit(x, y, 3)
numpy_model = np.poly1d(numpy_coeffs)
plt.plot(myline, numpy_model(myline), 'y', label="Degree 3 (NumPy)",)

plt.legend()
plt.show()

# Compare to the numpy library fit. Are there differences?
# Answer: No, there not.