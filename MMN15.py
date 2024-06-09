import numpy as np

def gaussian_elimination_scaled_partial_pivoting(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    # Scale factors
    scale = np.max(np.abs(A), axis=1)

    # Forward elimination with scaled partial pivoting
    for k in range(n - 1):
        # Determine the row with the largest scaled value
        max_row_index = np.argmax(np.abs(A[k:n, k]) / scale[k:n]) + k
        if max_row_index != k:
            # Swap the rows in A
            A[[k, max_row_index]] = A[[max_row_index, k]]
            # Swap the corresponding values in b
            b[[k, max_row_index]] = b[[max_row_index, k]]
            # Swap the scale factors
            scale[[k, max_row_index]] = scale[[max_row_index, k]]

        # Eliminate entries below the pivot
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


def gaussian_elimination_scaled_partial_pivoting_with_epsilon(A, b, epsilon):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)

    # Scale factors
    scale = np.max(np.abs(A), axis=1)

    # Forward elimination with scaled partial pivoting
    for k in range(n - 1):
        # Determine the row with the largest scaled value
        max_row_index = np.argmax(np.abs(A[k:n, k]) / scale[k:n]) + k
        if np.abs(A[max_row_index, k]) < epsilon:
            raise ValueError(f"Pivot element is too small (less than epsilon={epsilon})")
        if max_row_index != k:
            # Swap the rows in A
            A[[k, max_row_index]] = A[[max_row_index, k]]
            # Swap the corresponding values in b
            b[[k, max_row_index]] = b[[max_row_index, k]]
            # Swap the scale factors
            scale[[k, max_row_index]] = scale[[max_row_index, k]]

        # Eliminate entries below the pivot
        for i in range(k + 1, n):
            factor = A[i, k] / A[k, k]
            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]

    # Back substitution
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if np.abs(A[i, i]) < epsilon:
            raise ValueError(f"Diagonal element is too small (less than epsilon={epsilon})")
        x[i] = (b[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

A = [[4,1.33,0],
     [3,1,1],
     [3,2,1]]
b = [5.33, 5, 6]

epsilon = pow(10, -10)
print(gaussian_elimination_scaled_partial_pivoting(A, b))
x = gaussian_elimination_scaled_partial_pivoting_with_epsilon(A, b, epsilon)

# Print solution in the desired format
solution = ', '.join([f'x{i+1} = {value:.6f}' for i, value in enumerate(x)])
print(f"Solution: [{solution}]")

