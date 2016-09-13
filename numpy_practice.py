# lessen 20 practice
import numpy as np

xa_high = np.loadtxt('data/xa_high_food.csv', comments='#')
xa_low = np.loadtxt('data/xa_low_food.csv', comments='#')

def xa_to_diameter(xa):
    """
    Convert an array of cross-sectional areas to diameters with commensurate units.
    """

    # Compute diameter from area
    # A = pi * d^2/4
    diameter = np.sqrt(xa * 4 / np.pi)

    return diameter

def easy_reshape(obj, ncols, order='C'):
    """
    Guarentee that reshapping works by defining only one shape parameter.
    """

    # Reshape
    arr = np.reshape(obj, (ncols, len(obj)/ncols), order)

    return arr


# A = np.array([[6.7, 1.3, 0.6, 0.7],
#              [0.1, 5.5, 0.4, 2.4],
#              [1.1, 0.8, 4.5, 1.7],
#              [0.0, 1.5, 3.4, 7.5]])

# b = np.array([1.1, 2.3, 3.3, 3.9])


# Print row 1 of A: A[1,:]

# Print columns 1 and 3 of A: A[:,[1,3]]

# Print the values of every entry in A that are greater than 2: A[A > 2]

# Print the values of diagnal of array np.diag(A)

# A x = b
