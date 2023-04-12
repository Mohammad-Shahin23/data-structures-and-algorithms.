def sum_rows(matrix):
    # Initialize an empty list to hold the sums of each row
    row_sums = []
    
    # Iterate over each row of the matrix
    for row in matrix:
        # Initialize a variable to hold the sum of the current row
        row_sum = 0
        
        # Iterate over each element of the row
        for elem in row:
            # Add the element to the row sum if it's not None, otherwise add 0
            row_sum += elem if elem is not None else 0
        
        # Append the row sum to the list of row sums
        row_sums.append(row_sum)
    
    # Return the list of row sums
    return row_sums


matrix = [[1, 2, 3], [3, 5, 7], [1, 7, 10]]
result = sum_rows(matrix)
print(result)