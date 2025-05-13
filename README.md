# Nonogram Helper
Simple script to help with solving Nonograms

Input the length of the row or column you're working into the first field
In the second field, input your clue numbers
Seperate numbers with a comma

It will calculate whether or not there are guaranteed, overlapping squares and display an example of the row or column.

Upon starting the program, select Helper or Solver. (Solver WIP)

Helper:
In the first entry box, input the length of the row or column you are working on.
In the second box, list out the clues given on the left or top of the puzzle.

Hitting 'Find Remainder' will calculate how many spaces remain after filling boxes in one direction. The remainder can be compared to the clues. If a clue is greater than the remainder, then there are overlapping squares if it were to fill from the opposite side. An example of the row or column and it's overlapping squares will be drawn below.

In nonograms, when you fill squares in one direction and fill squares in the opposite direction; you can guarantee that, no matter how many blanks squares are between filled, those will always be filled.

Solver:
Still a work in progress. You will be able to input the size of the grid and all of the clues and generate the completed puzzle.