# Conway's Game of Life

This is an implementation of the classic game of life. 
- Living cells die if they are too crowded (>3 living neighbours)
- Living cells die if they are lonely (<2 living neighbours)
- Dead cells are brought to life if 3 nearby cells are alive

The purpose of this is to try out some OOP in python.

There will be two main classes, board and cell. 
### Cell
- Performs most of the game logic
- Is initialised with references to the surrounding cells as a list.
- Calculates its next status when #prep is called
- Updates its status when #update is called

### Board
- Will create the cells on init
- Will call the prep and update methods on each cell each tick/turn

There will likely also be a Timer class, and a visual interface class 
