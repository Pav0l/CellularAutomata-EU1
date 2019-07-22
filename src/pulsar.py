# Create Pulsar
def pulsar(initial_state, row, col):
    default_row = row
    """
    TOP LEFT
    """
    # first row
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+4] = 1

    # second row is empty
    row += 1

    # third - fifth row
    for _ in range(3):
        row += 1
        initial_state[row][col] = 1
        initial_state[row][col+5] = 1

    # sixth row
    row += 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+4] = 1

    """
    BOTTOM LEFT
    """
    row += 1
    # first row
    row += 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+4] = 1

    # second - forth row
    for _ in range(3):
        row += 1
        initial_state[row][col] = 1
        initial_state[row][col+5] = 1

    # fifth row is empty
    row += 1

    # sixth row
    row += 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+4] = 1

    """
    TOP RIGHT
    """
    row = default_row
    col += 8
    # first row
    initial_state[row][col+1] = 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1

    # second row is empty
    row += 1

    # third - fifth row
    for _ in range(3):
        row += 1
        initial_state[row][col] = 1
        initial_state[row][col+5] = 1

    # sixth row
    row += 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+1] = 1

    """
    BOTTOM RIGHT
    """
    row += 1
    # first row
    row += 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+1] = 1

    # second - forth row
    for _ in range(3):
        row += 1
        initial_state[row][col] = 1
        initial_state[row][col+5] = 1

    # fifth row is empty
    row += 1

    # sixth row
    row += 1
    initial_state[row][col+2] = 1
    initial_state[row][col+3] = 1
    initial_state[row][col+1] = 1

    return initial_state
