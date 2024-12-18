import numpy as np


def swap_rows(M, row_index_1, row_index_2):
    """
    Swap rows in the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to perform row swaps on.
    - row_index_1 (int): Index of the first row to be swapped.
    - row_index_2 (int): Index of the second row to be swapped.
    """

    # Copy matrix M so the changes do not affect the original matrix.
    M = M.copy()
    # Swap indexes
    M[[row_index_1, row_index_2]] = M[[row_index_2, row_index_1]]
    return M


def get_index_first_non_zero_value_from_column(M, column, starting_row):
    """
    Retrieve the index of the first non-zero value in a specified column of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - column (int): The index of the column to search.
    - starting_row (int): The starting row index for the search.

    Returns:
    int: The index of the first non-zero value in the specified column, starting from the given row.
                Returns -1 if no non-zero value is found.
    """
    # Get the column array starting from the specified row
    column_array = M[starting_row:, column]
    for i, val in enumerate(column_array):
        # Iterate over every value in the column array.
        # To check for non-zero values, you must always use np.isclose instead of doing "val == 0".
        if not np.isclose(val, 0, atol=1e-5):
            # If one non zero value is found, then adjust the index to match the correct index in the matrix and return it.
            index = i + starting_row
            return index
    # If no non-zero value is found below it, return -1.
    return -1


def get_index_first_non_zero_value_from_row(M, row, augmented=False):
    """
    Find the index of the first non-zero value in the specified row of the given matrix.

    Parameters:
    - matrix (numpy.array): The input matrix to search for non-zero values.
    - row (int): The index of the row to search.
    - augmented (bool): Pass this True if you are dealing with an augmented matrix, 
                        so it will ignore the constant values (the last column in the augmented matrix).

    Returns:
    int: The index of the first non-zero value in the specified row.
                Returns -1 if no non-zero value is found.
    """

    # Create a copy to avoid modifying the original matrix
    M = M.copy()

    # If it is an augmented matrix, then ignore the constant values
    if augmented == True:
        # Isolating the coefficient matrix (removing the constant terms)
        M = M[:, :-1]

    # Get the desired row
    row_array = M[row]
    for i, val in enumerate(row_array):
        # If finds a non zero value, returns the index. Otherwise returns -1.
        if not np.isclose(val, 0, atol=1e-5):
            return i
    return -1


def augmented_matrix(A, B):
    """
    Create an augmented matrix by horizontally stacking two matrices A and B.

    Parameters:
    - A (numpy.array): First matrix.
    - B (numpy.array): Second matrix.

    Returns:
    - numpy.array: Augmented matrix obtained by horizontally stacking A and B.
    """
    augmented_M = np.hstack((A, B))
    return augmented_M

# GRADED FUNCTION: row_echelon_form


def row_echelon_form(A, B):
    """
    Utilizes elementary row operations to transform a given set of matrices, 
    which represent the coefficients and constant terms of a linear system, into row echelon form.

    Parameters:
    - A (numpy.array): The input square matrix of coefficients.
    - B (numpy.array): The input column matrix of constant terms

    Returns:
    numpy.array: A new augmented matrix in row echelon form with pivots as 1.
    """

    # Before any computation, check if matrix A (coefficient matrix) has non-zero determinant.
    # It will be used the numpy sub library np.linalg to compute it.

    det_A = np.linalg.det(A)

    # Returns "Singular system" if determinant is zero
    if np.isclose(det_A, 0) == True:
        return 'Singular system'

    # Make copies of the input matrices to avoid modifying the originals
    A = A.copy()
    B = B.copy()

    # Convert matrices to float to prevent integer division
    A = A.astype('float64')
    B = B.astype('float64')

    # Number of rows in the coefficient matrix
    num_rows = len(A)

    ### START CODE HERE ###

    # Transform matrices A and B into the augmented matrix M
    M = augmented_matrix(A, B)

    # Iterate over the rows.
    for row in range(num_rows):

        # The first pivot candidate is always in the main diagonal, let's get it.
        # Remember that the diagonal elements in a matrix has the same index for row and column.
        # You may access a matrix value by typing M[row, column]. In this case, column = None
        pivot_candidate = M[row, row]

        # If pivot_candidate is zero, it cannot be a pivot for this row.
        # So the first step you need to take is to look at the rows below it to check if there is a non-zero element in the same column.
        # The usage of np.isclose is a good practice when comparing two floats.
        if np.isclose(pivot_candidate, 0) == True:
            # Get the index of the first non-zero value below the pivot_candidate.
            first_non_zero_value_below_pivot_candidate = get_index_first_non_zero_value_from_column(
                M, row, row)

            # Swap rows
            M = swap_rows(M, row, first_non_zero_value_below_pivot_candidate)

            # Get the pivot, which is in the main diagonal now
            pivot = M[row, row]

        # If pivot_candidate is already non-zero, then it is the pivot for this row
        else:
            pivot = pivot_candidate

        # Now you are ready to apply the row reduction in every row below the current

        # Divide the current row by the pivot, so the new pivot will be 1. You may use the formula current_row -> 1/pivot * current_row
        # Where current_row can be accessed using M[row].
        M[row] = 1/pivot * M[row]

        # Perform row reduction for rows below the current row
        for j in range(row + 1, num_rows):
            # Get the value in the row that is below the pivot value.
            # Remember that, since you are dealing only with non-singular matrices, the pivot is in the main diagonal.
            # Therefore, the values in row j that are below the pivot, must have column index the same index as the column index for the pivot.
            value_below_pivot = M[j, row]

            # Perform row reduction using the formula:
            # row_to_reduce -> row_to_reduce - value_below_pivot * pivot_row
            M[j] = M[j] - value_below_pivot*M[row]

    ### END CODE HERE ###

    return M

# GRADED FUNCTION: back_substitution


def back_substitution(M):
    """
    Perform back substitution on an augmented matrix (with unique solution) in reduced row echelon form to find the solution to the linear system.

    Parameters:
    - M (numpy.array): The augmented matrix in row echelon form with unitary pivots (n x n+1).

    Returns:
    numpy.array: The solution vector of the linear system.
    """

    # Make a copy of the input matrix to avoid modifying the original
    M = M.copy()

    # Get the number of rows (and columns) in the matrix of coefficients
    num_rows = M.shape[0]

    ### START CODE HERE ####

    # Iterate from bottom to top
    for row in reversed(range(num_rows)):
        substitution_row = M[row, None]

        # Get the index of the first non-zero element in the substitution row. Remember to pass the correct value to the argument augmented.
        index = get_index_first_non_zero_value_from_row(M, row, augmented=True)

        # Iterate over the rows above the substitution_row
        for j in range(row):

            # Get the row to be reduced. The indexing here is similar as above, with the row variable replaced by the j variable.
            row_to_reduce = M[j]

            # Get the value of the element at the found index in the row to reduce
            value = row_to_reduce[index]

            # Perform the back substitution step using the formula row_to_reduce -> row_to_reduce - value * substitution_row
            row_to_reduce = row_to_reduce - value*substitution_row

            # Replace the updated row in the matrix, be careful with indexing!
            M[j, :] = row_to_reduce

    ### END CODE HERE ####

     # Extract the solution from the last column
    solution = M[:, -1]

    return solution


A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
B = np.array([[5], [6], [7]])
M = augmented_matrix(A, B)
print(back_substitution(M))
