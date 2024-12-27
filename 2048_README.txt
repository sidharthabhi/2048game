# 2048 Game

This repository contains a Python implementation of the popular game **2048** using the `pygame` library. This project allows players to enjoy the classic tile-merging game in various grid sizes.

Features:

- Playable on grid sizes of 4x4, 5x5, or 6x6.
- Smooth animations and visually appealing design.
- Tracks and displays the player's score.
- Game over detection and automatic handling.

How to Run the Game

Prerequisites

1. Python: Ensure Python 3.6 or higher is installed on your system.
2. pygame: Install `pygame` by running the following command:
   ```bash
   pip install pygame
   ```

Steps to Run

1. Clone the repository or download the script.
2. Open a terminal in the directory containing the `2048code.py` file.
3. Run the script using:
   ```bash
   python 2048code.py
   ```
4. Enter the desired grid size (4, 5, or 6) when prompted.

Gameplay Instructions

- Use the arrow keys to move the tiles:
  - Left Arrow: Move tiles left.
  - Right Arrow: Move tiles right.
  - Up Arrow: Move tiles up.
  - Down Arrow: Move tiles down.
- Combine tiles with the same number to merge them and earn points.
- Aim to reach the 2048 tile or achieve the highest score possible before the board fills up.

Code Structure

- `Game2048` class:
  - Handles grid initialization, tile addition, and game logic.
  - Includes methods for moving tiles (`move_left`, `move_right`, `move_up`, `move_down`).
  - Manages grid transformations such as compression, merging, reversing, and transposing.
  - Detects game-over conditions.
- `main()` function:
  - Initializes the game and pygame display.
  - Captures user input for movement.
  - Handles the game loop, rendering, and exit conditions.

Customization

- Modify the `CELL_COLOR` dictionary to change tile colors.
- Adjust the `WINDOW_SIZE` variable for different screen sizes.
- Enhance the game by adding new features like undo, higher tile goals, or multiplayer modes.

Example Gameplay

Here is an example of how the game looks during play:

```
+------+------+------+------+
|  2   |  4   |  8   |  16  |
+------+------+------+------+
|  32  |  64  |  128 |  256 |
+------+------+------+------+
|  512 | 1024 | 2048 |      |
+------+------+------+------+
|      |      |      |      |
+------+------+------+------+
```

License

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments

- Inspired by the original 2048 game by Gabriele Cirulli.
- Built with Python and the `pygame` library.
