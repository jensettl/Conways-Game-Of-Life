# Conways-Game-Of-Life

## Description

Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.
Algorithmically predicting the fate of the game's patterns is impossible.

## Motivation

Never worked with PyGame before, so I decided to make a simple game to get familiar with it. I also wanted to implement Conway's Game of Life, as I had heard about it in a video by Veritasium.

## Rules

The game is played on a two-dimensional grid of cells, where each cell is either alive or dead. At each step in time, the following transitions occur:

1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Implementation

The game is implemented in Python using the Pygame library. The game's grid is represented as a 2D array of cells, where each cell is a boolean value. The game's state is updated by iterating through the grid and applying the rules to each cell. The game's state is rendered to the screen using Pygame's drawing functions.

## Usage

The game can be run by executing the following command:

```
python3 main.py
```

## Screenshots

<div style="display: flex; justify-content: space-between;">
    <img src="resources\game-of-life-generate-random-board.png" alt="Screenshot1" width="45%">
    <img src="resources\game-of-life-finished-board.png" alt="Screenshot2" width="45%">
</div>

## References

- [Wikipedia](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
- [Math's Fundamental Flaw](https://www.youtube.com/watch?v=HeQX2HjkcNo&t=3s&ab_channel=Veritasium)
