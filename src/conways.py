import pygame
import random

# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
MARGIN = 1
SQUARE_SIZE = 10
SQUARES_PER_ROW = 100
SQUARES_PER_COL = 50

#  calculate the windowns size dynamically
ROW_SIZE = (SQUARES_PER_ROW + 1) * MARGIN + SQUARES_PER_ROW * SQUARE_SIZE
COL_SIZE = (SQUARES_PER_COL + 1) * MARGIN + SQUARES_PER_COL * SQUARE_SIZE
BTN_SIZE = 30
BOTTOM_SIZE = BTN_SIZE + 20

generation = 0
time_step = 5
runnig = True

pygame.init()

# Set the width and height of the screen [width, height]
size = (ROW_SIZE, COL_SIZE + BOTTOM_SIZE)
screen = pygame.display.set_mode(size)

# Set up initial state
row = [0] * SQUARES_PER_ROW
initial_state = []
for i in range(SQUARES_PER_COL):
    initial_state.append(row.copy())

# randomize it
for r in range(SQUARES_PER_COL):
    for col in range(SQUARES_PER_ROW):
        initial_state[r][col] = random.randint(0, 1)


# Add a title
pygame.display.set_caption("Conway's Game of Life")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# Get alive neighbours:
def get_alive_neighbours(row, col, arr, row_len, col_len):
    alive_neighbours = 0

    left = col - 1 >= 0
    right = col + 1 < row_len
    top = row - 1 >= 0
    bot = row + 1 < col_len

    # left
    if left and arr[row][col - 1]:
        alive_neighbours += 1

    # right
    if right and arr[row][col + 1]:
        alive_neighbours += 1

    # top
    if top and arr[row - 1][col]:
        alive_neighbours += 1

    # top left
    if top and left and arr[row - 1][col - 1]:
        alive_neighbours += 1

    # top right
    if top and right and arr[row - 1][col + 1]:
        alive_neighbours += 1

    # bot
    if bot and arr[row + 1][col]:
        alive_neighbours += 1

    # bot left
    if bot and left and arr[row + 1][col - 1]:
        alive_neighbours += 1

    # bot right
    if bot and right and arr[row + 1][col + 1]:
        alive_neighbours += 1

    return alive_neighbours


# Get next state:
def get_next_state(alive_neighbours, current_state):
    if not current_state and alive_neighbours == 3:
        return 1
    elif current_state and alive_neighbours < 2:
        return 0
    elif current_state and alive_neighbours == 3:
        return current_state
    elif current_state and alive_neighbours == 2:
        return current_state
    elif current_state and alive_neighbours > 3:
        return 0
    else:
        return current_state


# Setup font
myfont = pygame.font.Font('freesansbold.ttf', 13)


# -------- Main Program Loop -----------
while not done:
    # --- Game logic should go here
    if runnig:
        new_row = [0] * SQUARES_PER_ROW
        new_state = []
        for i in range(SQUARES_PER_COL):
            new_state.append(new_row.copy())

        for r in range(len(initial_state)):
            for c in range(len(initial_state[0])):
                # check state of neigbours here
                alive_neighbours = get_alive_neighbours(
                    r, c, initial_state, SQUARES_PER_ROW, SQUARES_PER_COL)

                # update new state for that square
                new_state[r][c] = get_next_state(
                    alive_neighbours, initial_state[r][c])

        # update new state
        initial_state = new_state
        generation += 1

    # --- Screen-clearing code goes here

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code should go here
    y = MARGIN
    r = 0
    while y < COL_SIZE:
        c = 0
        x = MARGIN
        while x < ROW_SIZE:
            if initial_state[r][c] == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(
                    x, y, SQUARE_SIZE, SQUARE_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(
                    x, y, SQUARE_SIZE, SQUARE_SIZE))
            x += MARGIN + SQUARE_SIZE
            c += 1
        r += 1
        y += MARGIN + SQUARE_SIZE

    # Add generation count rectangle
    gen_count = pygame.draw.rect(screen, GRAY, pygame.Rect(
        10, COL_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))

    gen_text = myfont.render(f'Generation: {generation}', True, WHITE)
    gen_text_rect = gen_text.get_rect()
    gen_text_rect.center = (gen_count.center[0], gen_count.center[1])
    screen.blit(gen_text, gen_text_rect)

    # Add speed count rectangle
    speed_count = pygame.draw.rect(screen, GRAY, pygame.Rect(
        3*10 + 3 * BTN_SIZE, COL_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))

    speed_text = myfont.render(f'Speed: {time_step}', True, WHITE)
    speed_text_rect = speed_text.get_rect()
    speed_text_rect.center = (speed_count.center[0], speed_count.center[1])
    screen.blit(speed_text, speed_text_rect)

    # Add faster button
    faster = pygame.draw.rect(screen, BLACK, pygame.Rect(
        6*10 + 6 * BTN_SIZE, COL_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    fast_text = myfont.render('Faster', True, WHITE)
    fast_text_rect = fast_text.get_rect()
    fast_text_rect.center = (faster.center[0], faster.center[1])
    screen.blit(fast_text, fast_text_rect)

    # Add slower button
    slower = pygame.draw.rect(screen, BLACK, pygame.Rect(
        9*10 + 9 * BTN_SIZE, COL_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    slow_text = myfont.render('Slower', True, WHITE)
    slow_text_rect = slow_text.get_rect()
    slow_text_rect.center = (slower.center[0], slower.center[1])
    screen.blit(slow_text, slow_text_rect)

    # Add restart button
    restart = pygame.draw.rect(screen, BLACK, pygame.Rect(
        12*10 + 12 * BTN_SIZE, COL_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    restart_text = myfont.render('Restart', True, WHITE)
    restart_text_rect = restart_text.get_rect()
    restart_text_rect.center = (restart.center[0], restart.center[1])
    screen.blit(restart_text, restart_text_rect)

    # Add pause/play button
    pause = pygame.draw.rect(screen, BLACK, pygame.Rect(
        15*10 + 15 * BTN_SIZE, COL_SIZE + 10, 3 * BTN_SIZE, BTN_SIZE))
    pause_text = myfont.render('Stop/Play', True, WHITE)
    pause_text_rect = pause_text.get_rect()
    pause_text_rect.center = (pause.center[0], pause.center[1])
    screen.blit(pause_text, pause_text_rect)

    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = pygame.mouse.get_pos()

            if faster.collidepoint(click_position) and time_step <= 20:
                time_step += 1

            elif slower.collidepoint(click_position) and time_step > 1:
                time_step -= 1

            elif restart.collidepoint(click_position):
                generation = 0
                time_step = 5
                for r in range(SQUARES_PER_COL):
                    for col in range(SQUARES_PER_ROW):
                        initial_state[r][col] = random.randint(0, 1)

            elif pause.collidepoint(click_position) and runnig:
                runnig = False

            elif pause.collidepoint(click_position) and not runnig:
                runnig = True

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 5 frames per second
    clock.tick(time_step)

# Close the window and quit.
pygame.quit()
