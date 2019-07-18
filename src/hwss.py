# Create Heavy Weight Space Ship
def hwss(initial_state, row, col):
    # first row
    initial_state[row][col] = 0
    initial_state[row][col+1] = 0
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+4] = 1
    initial_state[row][col+5] = 1
    initial_state[row][col+6] = 0

    # second row
    row += 1
    initial_state[row][col] = 0
    initial_state[row][col+1] = 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+4] = 1
    initial_state[row][col+5] = 1
    initial_state[row][col+6] = 1

    # third row
    row += 1
    initial_state[row][col] = 1
    initial_state[row][col+1] = 1
    initial_state[row][col+2] = 0
    initial_state[row][col+3] = 1
    initial_state[row][col+4] = 1
    initial_state[row][col+5] = 1
    initial_state[row][col+6] = 1

    # forth row
    row += 1
    initial_state[row][col] = 0
    initial_state[row][col+1] = 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 0
    initial_state[row][col+4] = 0
    initial_state[row][col+5] = 0
    initial_state[row][col+6] = 0

    return initial_state
