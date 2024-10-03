import turtle
import random
import pygame  # Cross-platform sound library

# Initialize pygame for sound
pygame.mixer.init()

# Define program constants
WIDTH = 800
HEIGHT = 600
DELAY = 200  # Milliseconds
FOOD_SIZE = 32
SNAKE_SIZE = 20
PAUSE = False  # State for pause functionality

offsets = {
    "up": (0, SNAKE_SIZE),
    "down": (0, -SNAKE_SIZE),
    "left": (-SNAKE_SIZE, 0),
    "right": (SNAKE_SIZE, 0)
}

# High score
high_score = 0

# Load the high score if it exists
try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    pass


def update_high_score():
    global high_score
    if score > high_score:
        high_score = score
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))


def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("up"), "Up")
    screen.onkey(lambda: set_snake_direction("down"), "Down")
    screen.onkey(lambda: set_snake_direction("left"), "Left")
    screen.onkey(lambda: set_snake_direction("right"), "Right")
    screen.onkey(toggle_pause, "p")  # Pause functionality


def set_snake_direction(direction):
    global snake_direction
    if not PAUSE:
        if direction == "up" and snake_direction != "down":
            snake_direction = "up"
        elif direction == "down" and snake_direction != "up":
            snake_direction = "down"
        elif direction == "left" and snake_direction != "right":
            snake_direction = "left"
        elif direction == "right" and snake_direction != "left":
            snake_direction = "right"


def toggle_pause():
    global PAUSE
    PAUSE = not PAUSE
    if PAUSE:
        display_text("Game Paused. Press 'P' to Resume", 0, 0, font_size=24)
    else:
        text_writer.clear()  # Clear pause text


def game_loop():
    if PAUSE:
        return

    stamper.clearstamps()

    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 or \
            new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
        play_game_over_sound()
        game_over()
    else:
        snake.append(new_head)

        # Check if food is eaten
        if not food_collision():
            snake.pop(0)

        # Draw snake
        stamper.shape("my_snake_game/assets/snake-head-20x20.gif")
        stamper.goto(snake[-1][0], snake[-1][1])
        stamper.stamp()
        stamper.shape("circle")
        for segment in snake[:-1]:
            stamper.goto(segment[0], segment[1])
            stamper.stamp()

        # Update score display
        update_score_display()

        # Call game_loop again after a delay
        screen.update()
        turtle.ontimer(game_loop, DELAY)


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score += 1
        update_high_score()
        play_eating_sound()
        food_pulse_animation()
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(- WIDTH // 2 + FOOD_SIZE, WIDTH // 2 - FOOD_SIZE)
    y = random.randint(- HEIGHT // 2 + FOOD_SIZE, HEIGHT // 2 - FOOD_SIZE)
    return (x, y)


def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    return distance


def reset():
    global score, snake, snake_direction, food_pos
    score = 0
    snake = [[0, 0], [SNAKE_SIZE, 0], [SNAKE_SIZE * 2, 0], [SNAKE_SIZE * 3, 0]]
    snake_direction = "up"
    food_pos = get_random_food_pos()
    food.goto(food_pos)
    update_score_display()
    game_loop()


def update_score_display():
    score_display.clear()
    score_display.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Arial", 24, "bold"))


def game_over():
    screen.clear()
    screen.bgcolor("#1F1F1F")

    display_text("GAME OVER", 0, 50, font_size=36)
    display_text("Press 'R' to Restart", 0, -50, font_size=24)

    screen.listen()
    screen.onkey(reset, "r")


def food_pulse_animation():
    food.shapesize(1.5, 1.5)
    screen.update()
    turtle.ontimer(lambda: food.shapesize(1, 1), 100)


def play_eating_sound():
    pygame.mixer.Sound("my_snake_game/assets/eat.wav").play()


def play_game_over_sound():
    pygame.mixer.Sound("my_snake_game/assets/game-over.wav").play()


# Create a window where we will do our drawing
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Snake Game")
screen.bgpic("my_snake_game/assets/bg3.gif")
screen.register_shape("my_snake_game/assets/snake-food-32x32.gif")
screen.register_shape("my_snake_game/assets/snake-head-20x20.gif")
screen.tracer(0)

# Create score display turtle
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("#FFFFFF")
score_display.goto(0, HEIGHT // 2 - 40)

# Create a turtle for displaying text
text_writer = turtle.Turtle()
text_writer.hideturtle()
text_writer.penup()
text_writer.color("#FFFFFF")


def display_text(message, x, y, font_size=24, font_type="Arial", font_style="bold"):
    """Display a message at the specified x, y position with the specified font."""
    text_writer.goto(x, y)
    text_writer.clear()  # Clear previous text before writing new text
    text_writer.write(message, align="center", font=(font_type, font_size, font_style))


# Event handlers
screen.listen()
bind_direction_keys()

# Create a turtle to represent the snake
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("#73A767")
stamper.penup()

# Create food turtle
food = turtle.Turtle()
food.shape("my_snake_game/assets/snake-food-32x32.gif")
food.shapesize(FOOD_SIZE / 20)
food.penup()

# Start the game
reset()
turtle.done()
