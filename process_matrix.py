from functools import reduce

def process_matrix(matrix):
    """
    Receives a matrix and returns a new one based on it.
    Each new element is based on the average of the old element and its neighbors.
    """
    new_matrix = []

    if validate(matrix):
        for i, row in enumerate(matrix):
            new_list = []
            new_matrix.append(new_list)
            for j, value in enumerate(row):
                new_value = process_element(i, j, matrix)
                new_list.append(new_value)
    else:
        raise Exception("Matrix not valid")

    return new_matrix

def not_empty_matrix(matrix):
    """
    Returns False if the matrix is empty
    """
    answer = True
    if not any(matrix):
        #in case of an empty matrix
        answer = False 
    return answer

def is_numerical_matrix(matrix):
    """
    Returns False if the if the matrix is not numerical
    """
    answer = True
    for i, column in enumerate(matrix):
        for j, value in enumerate(column):
            if type(value) != int:
                answer = False
    return answer 

def validate(matrix):
    """
    Returns False if the matrix is not valid to 
    """
    answer = True 
    if not_empty_matrix(matrix) and is_numerical_matrix(matrix):
        answer = False

def process_element(i, j, matrix):
    """
    Receives the position of an element of a matrix, the matrix,
    calculates its average with its neighbors, and returns that average
    """
    values = get_neighbors_values(i, j, matrix)
    average = get_average(values)

    return average

def get_neighbors_values(i, j, matrix):
    """
    Receives the position of an element of a matrix, the matrix,
    and returns a list of the element and its neigbors
    """

    values = []
    rows = len(matrix)
    cols = len(matrix[0])

    if rows == 1:
        #in case of a one row matrix
        values = one_row_matrix(i, j, matrix, cols)

    elif cols == 1:
        #in case of a one column matrix
        values = one_col_matrix(i, j, matrix, rows)

    elif i == 0 and j == 0:
        #top left corner            
        values.append(matrix[i][j + 1])
        values.append(matrix[i + 1][j])

    elif i == 0 and j == (cols - 1):
        #top right corner
        values.append(matrix[i][j - 1])
        values.append(matrix[i + 1][j])

    elif i == (rows - 1) and j == 0:
        #bottom left corner
        values.append(matrix[i][j + 1])
        values.append(matrix[i - 1][j])
    
    elif i == (rows - 1) and j == (cols - 1):
        #bottom right corner 
        values.append(matrix[i][j - 1])
        values.append(matrix[i - 1][j])
        
    elif i == 0:
        #top edge
        values.append(matrix[i][j - 1])
        values.append(matrix[i][j + 1])
        values.append(matrix[i + 1][j])

    elif j == 0:
        #leftr edge
        values.append(matrix[i + 1][j])
        values.append(matrix[i - 1][j])
        values.append(matrix[i][j + 1])

    elif i == (rows - 1):
        #bottom edge
        values.append(matrix[i][j - 1])
        values.append(matrix[i][j + 1])
        values.append(matrix[i - 1][j])

    elif j == (cols - 1):
        #right edge
        values.append(matrix[i + 1][j])
        values.append(matrix[i - 1][j])
        values.append(matrix[i][j - 1])

    else:
        #normal cases 
        values.append(matrix[i][j + 1])
        values.append(matrix[i][j - 1])
        values.append(matrix[i + 1][j])
        values.append(matrix[i - 1][j])

    #add the value of the element
    values.append(matrix[i][j])
    
    return values  

def get_average(values):
    """
    Receives a list and returns the average of its elements
    """
    return reduce(lambda a, b : a + b, values, 0) / len(values)

def one_row_matrix(i, j, matrix, cols):
    """
    Returns a list of the neighbors of an element of a one row matrix
    """
    values = []

    if j == 0:
        values.append(matrix[i][j + 1])

    elif j == (cols - 1):
        values.append(matrix[i][j - 1])

    else:        
        values.append(matrix[i][j + 1])
        values.append(matrix[i][j - 1])
    
    return values 


def one_col_matrix(i, j, matrix, rows):
    """
    Returns a list of the neighbors of an element of a one column matrix
    """
    values = []

    if i == 0:
        values.append(matrix[i + 1][j])

    elif i == (rows - 1):
        values.append(matrix[i - 1][j])
        
    else:
        values.append(matrix[i + 1][j])
        values.append(matrix[i - 1][j])

    return values 