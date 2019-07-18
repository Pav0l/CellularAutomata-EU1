# Create Penta-decathlon starting state
def penta_decathlon(initial_state, row, col):
    # start point
    start_row = row
    start_col = col

    initial_state[start_row][start_col] = 0
    initial_state[start_row+1][start_col] = 1
    initial_state[start_row+2][start_col] = 1
    initial_state[start_row][start_col+1] = 1
    initial_state[start_row][start_col+2] = 1
    initial_state[start_row][start_col+3] = 1
    initial_state[start_row+1][start_col+4] = 1
    initial_state[start_row+2][start_col+4] = 1
    initial_state[start_row+3][start_col+1] = 1
    initial_state[start_row+3][start_col+2] = 1
    initial_state[start_row+3][start_col+3] = 1

    start_row = start_row + 8
    initial_state[start_row+1][start_col] = 1
    initial_state[start_row+2][start_col] = 1
    initial_state[start_row][start_col+1] = 1
    initial_state[start_row][start_col+2] = 1
    initial_state[start_row][start_col+3] = 1
    initial_state[start_row+1][start_col+4] = 1
    initial_state[start_row+2][start_col+4] = 1
    initial_state[start_row+3][start_col+1] = 1
    initial_state[start_row+3][start_col+2] = 1
    initial_state[start_row+3][start_col+3] = 1

    return initial_state
