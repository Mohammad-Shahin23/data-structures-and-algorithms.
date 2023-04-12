# Code Challenge Class-04
## Made by Mohammad Shahin


![MarineGEO circle logo](/Sum_matrixs/cc%20intervew.png)

 Approach & Efficiency
    time:function is O(N^2), where N is the total number of elements in the input matrix.
    step space: unction is O(N), where N is the total number of elements in the input matrix.

# Solution
    def sum_rows(matrix):
    
    row_sums = []
    
    
    for row in matrix:
        
        row_sum = 0
        
       
        for elem in row:
            # Add the element to the row sum if it's not None, otherwise add 0
            row_sum += elem if elem is not None else 0
        
        
        row_sums.append(row_sum)
    
    
    return row_sums