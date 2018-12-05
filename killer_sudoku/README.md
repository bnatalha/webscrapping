# Killer Sudoku dataset

This dataset was generated using pandas. It contains Intermediate difficult killer sudokus scrapped from [Jim Bumgardner's online sudoku](https://krazydad.com/killersudoku/).

> "My Killer Sudoku puzzles are collected in **100 printable booklets** per __volume__. Within each volume, the puzzles are also **ordered by ascending difficulty** (book 100 is harder than book 1, but book 1 volume 9 is about the same as book 1, volume 1). Each booklet contains **eight puzzles**, instructions, and answers." - **Jim Bumgardner**.

## Explaining the dataset's columns

- **ptitle**: `string`; title of the puzzle.
- **vol**: `integer`; the book's volume from wich the puzzle was taken from (1-10).
- **book**: `integer`; the book's number from wich the puzzle was taken from (1-100).
- **puzzle**: `integer`; the numeration of the puzzle within the book (1-8).
- **puzz_color**: `string`; 82 character string; the first character ('K') must be dismissed ~~[(yeah it's K from **k**razydad)](https://krazydad.com/about.php)~~. Each of the remaining character represents a cell, reading the grid in a raster-scan style. For each new color/cage, a new letter is assigned following the A-Za-z order.
- **puzz_hint**: `string`; hint for every cage folowing the lexicographical ordering. The first number represents the hint for the 'A' cage, and so it follows.
- **solved**: `string`; solution, reading the grid in natural reading order.
- **sOrder**: `string`; the order that Jim's online player follows to show the solution on the sudoku's grid.