---
# Simple Snake Game in Django Using Turtle

## Overview

The **Simple Snake Game** is a fun and interactive game developed using Python's **Turtle Graphics** and integrated into a Django web framework. The game challenges the player to control a snake, eat food, and avoid running into walls or the snake’s own body. The game includes sound effects for food collection and game over events using the `pygame` library.

The game also implements a **high score** tracking system, pause functionality, and food pulse animation for a dynamic user experience.

## Features

- **Turtle Graphics** for snake movement and gameplay.
- **Real-time sound effects** using the `pygame` library for food collection and game over.
- **High Score System**: The game tracks and saves the highest score in a file (`high_score.txt`).
- **Pause/Resume Functionality**: Press 'P' to pause or resume the game.
- **Smooth snake movement** with customizable directions via arrow keys.
- **Restart Option**: Press 'R' to restart the game after game over.
- **Animated food** pulse effect when eaten.

## Technologies Used

- **Django**: Web framework for Python (used for web integration).
- **Turtle Graphics**: Built-in Python library for graphics and game rendering.
- **Pygame**: Used for sound effects.
- **Python**: Core programming language.
- **HTML5** and **CSS3** for web interface.

## Installation

### Prerequisites

Before running the game, ensure you have the following installed:

- [Python 3.8+](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Pygame](https://www.pygame.org/)
- [Turtle Graphics](https://docs.python.org/3/library/turtle.html) (comes pre-installed with Python)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/snake-game-django.git
   cd snake-game-django
   ```

2. **Install dependencies:**
   ```bash
   pip install pygame django
   ```

3. **Set up Django project:**
   Navigate to the root of the Django project and run:
   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000/` to play the game.

## How to Play

- **Control the snake**: Use the arrow keys (`Up`, `Down`, `Left`, `Right`) to change the direction of the snake.
- **Pause/Resume the game**: Press `P` to pause or resume the game.
- **Restart the game**: If the game is over, press `R` to restart.

## Game Features

1. **Snake Movement**: The snake grows longer each time it eats food.
2. **Collision Detection**: The game ends if the snake runs into itself or the walls.
3. **Score and High Score**: Keep track of your score during the session. If you beat the high score, it is saved and updated for the next session.
4. **Sound Effects**: 
   - **Eating sound** when food is collected.
   - **Game Over sound** when the snake collides.

## Files and Directories

```bash
snake-game-django/
│
├── my_snake_game/
│   ├── assets/                  # Contains images and sound files
│   │   ├── bg3.gif              # Background image for the game
│   │   ├── snake-food-32x32.gif # Food image
│   │   ├── snake-head-20x20.gif # Snake head image
│   │   ├── eat.wav              # Sound for food collection
│   │   └── game-over.wav        # Sound for game over
│   ├── __init__.py              # Django app initialization
│   ├── snake_game.py            # Main game logic
│   └── views.py                 # Django views for integrating the game
├── manage.py                    # Django management script
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

## Customization

### Changing Game Speed

You can adjust the game's speed by modifying the `DELAY` variable in `snake_game.py`:
```python
DELAY = 200  # Default is 200 milliseconds. Lower this value to increase speed.
```

### Adding New Sound Effects

You can replace or add new sound effects by placing `.wav` files in the `assets` directory and updating the respective functions `play_eating_sound()` and `play_game_over_sound()` in the `snake_game.py` file.

### Changing Snake and Food Graphics

Replace the `snake-head-20x20.gif` and `snake-food-32x32.gif` files in the `assets` folder with your desired images. Make sure the new images are in `.gif` format.

## Contributing

To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/new-feature`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature/new-feature`).
6. Open a pull request.


## Contact

For any inquiries or support:

- Email: support@snakegame.com
- GitHub: [niral-nadisara](https://github.com/niral-nadisara)
---
