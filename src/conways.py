import pygame
import random
from penta_decathlon import penta_decathlon
from hwss import hwss
from pulsar import pulsar

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
BTN_HEIGHT = 30
BTN_WIDTH = ROW_SIZE // 6
BTN_MARGIN = 10

FOOTER_SIZE = BTN_HEIGHT + 20

if BTN_WIDTH > 110:
    BTN_WIDTH = 110

# Keep track of counters and other variables
generation = 0
time_step = 5
runnig = True
btn_count = 0

pygame.init()

# Set the width and height of the screen [width, height]
size = (ROW_SIZE, COL_SIZE + FOOTER_SIZE)
screen = pygame.display.set_mode(size)

# Set up initial state
row = [0] * SQUARES_PER_ROW
initial_state = []
for i in range(SQUARES_PER_COL):
    initial_state.append(row.copy())

# Randomize initial state
for r in range(SQUARES_PER_COL):
    for col in range(SQUARES_PER_ROW):
        initial_state[r][col] = random.randint(0, 1)

"""
If you want to initialize premade starting state
Comment out the nested for loop above (line 47 - 49)
And uncomment some lines below (line 57 - 63)
If you want to see Pulsar, run only that starting state (line 64)

Or just press the Disco button
"""
# initial_state = penta_decathlon(initial_state, 20, 5)
# initial_state = penta_decathlon(initial_state, 15, 15)
# initial_state = penta_decathlon(initial_state, 5, 25)
# initial_state = penta_decathlon(initial_state, 35, 50)
# initial_state = penta_decathlon(initial_state, 20, 85)
# initial_state = hwss(initial_state, 25, 50)
# initial_state = hwss(initial_state, 10, 75)
# initial_state = pulsar(initial_state, 20, 40)

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
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # mouse click events
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_position = pygame.mouse.get_pos()
            # run faster
            if faster.collidepoint(click_position) and time_step < 20:
                time_step += 1
            # run slower
            elif slower.collidepoint(click_position) and time_step > 1:
                time_step -= 1
            # restart the game (reset generation count, time_step and initial_state)
            elif restart.collidepoint(click_position):
                generation = 0
                time_step = 5
                for r in range(SQUARES_PER_COL):
                    for col in range(SQUARES_PER_ROW):
                        initial_state[r][col] = random.randint(0, 1)
            # pause game
            elif pause.collidepoint(click_position) and runnig:
                runnig = False
            # unpause game
            elif pause.collidepoint(click_position) and not runnig:
                runnig = True

            # disco game
            elif disco.collidepoint(click_position):
                generation = 0
                for r in range(SQUARES_PER_COL):
                    for col in range(SQUARES_PER_ROW):
                        initial_state[r][col] = 0
                initial_state = penta_decathlon(initial_state, 20, 5)
                initial_state = penta_decathlon(initial_state, 20, 85)
                initial_state = pulsar(initial_state, 20, 40)

    # --- Game logic

    # if not paused
    if runnig:
        # setup new state
        new_row = [0] * SQUARES_PER_ROW
        new_state = []
        for i in range(SQUARES_PER_COL):
            new_state.append(new_row.copy())

        for r in range(len(initial_state)):
            for c in range(len(initial_state[0])):
                # check state of neigbours here
                alive_neighbours = get_alive_neighbours(
                    r, c, initial_state, SQUARES_PER_ROW, SQUARES_PER_COL)

                # update new state for square at row r and col c
                new_state[r][c] = get_next_state(
                    alive_neighbours, initial_state[r][c])

        # update new state
        initial_state = new_state
        generation += 1

    # --- Screen-clearing code

    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)

    # --- Drawing code
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
        10, COL_SIZE + 10, BTN_WIDTH, BTN_HEIGHT))
    btn_count += 1
    gen_text = myfont.render(f'Generation: {generation}', True, WHITE)
    gen_text_rect = gen_text.get_rect()
    gen_text_rect.center = (gen_count.center[0], gen_count.center[1])
    screen.blit(gen_text, gen_text_rect)

    # Add speed count rectangle
    speed_count = pygame.draw.rect(screen, GRAY, pygame.Rect(
        10 + btn_count * (10 + BTN_WIDTH), COL_SIZE + 10, BTN_WIDTH, BTN_HEIGHT))
    btn_count += 1
    speed_text = myfont.render(f'Speed: {time_step}', True, WHITE)
    speed_text_rect = speed_text.get_rect()
    speed_text_rect.center = (speed_count.center[0], speed_count.center[1])
    screen.blit(speed_text, speed_text_rect)

    # Add faster button
    faster = pygame.draw.rect(screen, BLACK, pygame.Rect(
        BTN_MARGIN + btn_count * (BTN_MARGIN + BTN_WIDTH), COL_SIZE + BTN_MARGIN, BTN_WIDTH, BTN_HEIGHT))
    btn_count += 1
    fast_text = myfont.render('Faster', True, WHITE)
    fast_text_rect = fast_text.get_rect()
    fast_text_rect.center = (faster.center[0], faster.center[1])
    screen.blit(fast_text, fast_text_rect)

    # Add slower button
    slower = pygame.draw.rect(screen, BLACK, pygame.Rect(
        BTN_MARGIN + btn_count * (BTN_MARGIN + BTN_WIDTH), COL_SIZE + BTN_MARGIN, BTN_WIDTH, BTN_HEIGHT))
    btn_count += 1
    slow_text = myfont.render('Slower', True, WHITE)
    slow_text_rect = slow_text.get_rect()
    slow_text_rect.center = (slower.center[0], slower.center[1])
    screen.blit(slow_text, slow_text_rect)

    # Add restart button
    restart = pygame.draw.rect(screen, BLACK, pygame.Rect(
        BTN_MARGIN + btn_count * (BTN_MARGIN + BTN_WIDTH), COL_SIZE + BTN_MARGIN, BTN_WIDTH, BTN_HEIGHT))
    btn_count += 1
    restart_text = myfont.render('Restart', True, WHITE)
    restart_text_rect = restart_text.get_rect()
    restart_text_rect.center = (restart.center[0], restart.center[1])
    screen.blit(restart_text, restart_text_rect)

    # Add pause/play button
    pause = pygame.draw.rect(screen, BLACK, pygame.Rect(
        BTN_MARGIN + btn_count * (BTN_MARGIN + BTN_WIDTH), COL_SIZE + BTN_MARGIN, BTN_WIDTH, BTN_HEIGHT))
    btn_count += 1
    pause_text = myfont.render('Stop/Play', True, WHITE)
    pause_text_rect = pause_text.get_rect()
    pause_text_rect.center = (pause.center[0], pause.center[1])
    screen.blit(pause_text, pause_text_rect)

    # Add disco button
    disco = pygame.draw.rect(screen, BLACK, pygame.Rect(
        BTN_MARGIN + btn_count * (BTN_MARGIN + BTN_WIDTH), COL_SIZE + BTN_MARGIN, BTN_WIDTH, BTN_HEIGHT))
    btn_count += 1
    disco_text = myfont.render('Disco', True, WHITE)
    disco_text_rect = disco_text.get_rect()
    disco_text_rect.center = (disco.center[0], disco.center[1])
    screen.blit(disco_text, disco_text_rect)

    # Reset button count for next while loop
    btn_count = 0

    # --- Update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit frames per second
    clock.tick(time_step)

# Close the window and quit.
pygame.quit()
