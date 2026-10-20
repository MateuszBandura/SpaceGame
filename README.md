# SpaceGame

Simple arcade game built with **Pygame Zero**. Control a spaceship, dodge incoming meteors, and survive as long as possible to increase your score.

## Requirements

- Python 3.8+
- [pgzero](https://pypi.org/project/pgzero/) (includes pygame dependency support)

## Installation

```bash
pip install pgzero
```

## Run

From the project root:

```bash
pgzrun gra.py
```

## Controls

- **Arrow Up**: move up
- **Arrow Down**: move down
- **Arrow Left**: move left
- **Arrow Right**: move right

## Gameplay

- Meteors spawn from the right side of the screen and move left.
- Each meteor you avoid increases your score by 1.
- Collision with a meteor ends the game.
