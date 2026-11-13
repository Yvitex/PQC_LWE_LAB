


# TODO: Method that finds the secret ased on A, b, q
def solve_mod():
    # Convert A into new array but modulo it by q
    # Convert b into new array but modulo it by q
    # Combine A and b to a single matrix

    # Loop per number of rows
    # Find the pivot starting from the rows to the last column of that row, e.g, row = 0, evaluate combination to C[0, 0 to n], row = 1, then C[1, 1 to n]
    # Raise error fi there's none
    # If pivot is found, switch current row to the pivot row.
    # For each item in the row , multiply by the inverse of the pivot number (which means row, col where row and col is the same num) modulo q
    # Check all remaining row 
