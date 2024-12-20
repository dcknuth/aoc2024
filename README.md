# AoC2024
Advent of Code 2024

## [Day 1: Historian Hysteria](day01.py)
Brute force is fine and the day seems much easier than last year's day 1

## [Day 2: Red-Nosed Reports](day02.py)
Brute forced, simple loop for part 1. For part 2 I just dropped every level and short circuited when a good run was found. Both parts ran in a second, so good enough.

## [Day 3: Mull It Over](day03.py)
Had to relearn regular expressions (for the 20th time), but after that it was OK

## [Day 4: Ceres Search](day04.py)
Started trying with NetworkX, but gave that up for a more standard walk in part 1. For part two I did another simple walk with a test function. Also considered NumPy with sub-matrixes and flattening, but seemed best to just do the walk and it finished in a second. It was a bit of code and the example didn't leave out any tricky cases, so got lucky there

## [Day 5: Print Queue](day05.py)
It has messy use of globals and is not DRY, but works. I like the sort function that I came up with

## [Day 6: Guard Gallivant](day06.py)
Again, not dry and a little long. Brute force finished in 82 seconds with the luck of a non-diabolical puzzle input. Would be a good one to parallelize and might add a v2 with that later

**Update:** I added [a version](day06v2.py) to do part 2 in parallel and it ran in 4 seconds. It was harder to get a parallel version to run than I thought. First, I had to add a main loop and a work function. Then, there was trouble with passing multiple parameters and with variables that had to be moved outside main to make them global and accessible (yes, I could have passed them also). After that, it did use all virtual CPUs (32) and run a lot faster.

## [Day 7: Bridge Repair](day07.py)
Part two took 20 seconds to run and getting a good start overall took way longer than it should have, but done.

## [Day 8: Resonant Collinearity](day08.py)
Some parts to keep track of, but brute-force works and is fast for both parts

## [Day 9: Disk Fragmenter](day09.py)
Brute force again and it took about 5 seconds for each part. Probably could have used some hashes instead of lists and cut the time down, but done

## [Day 10: Hoof It](day10.py)
NetworkX saves the day! About two seconds for each part and written pretty quick

## [Day 11: Plutonian Pebbles](day11.py)
Part 1 works with brute force. It took way longer than it should have to come up with, remember string transitions and then just keep a count of strings. I left thought process in the one linked above. [Here](day11v2.py) is a cleaned up version

## [Day 12: Garden Groups](day12.py)
Part 1 was not too bad, but part 2 was tricky and I gave up [an attempt](day12_fail.py). Sometimes it's good to just start again with a new idea and no clutter

## [Day 13: Claw Contraption](day13.py)
Part 1 was about 4 seconds with brute force. Part 2 I looked at the [algebra solver](https://github.com/dcknuth/Algebra_solver/blob/master/Equations%20Solver.ipynb) I had done many years ago. I did make a silly error that cost me some debugging time though.

## [Day 14: Restroom Redoubt](day14.py)
I thought I had a nice part 1 that would be fast for a longer part 2, but it didn't work out that way. Then I tested for a tree outline, which also didn't work. It was a filled in tree, but got there eventually. This could be one that a nicer NumPy use would probably speed up a good bit

## [Day 15: Warehouse Woes](day15.py)
Part 1 was non-trivial, but a simple while loop could propagate a move. For part 2 a more complex recursive check was needed to see if a move was possible and then to do the move in the Y direction. This took a good bit more code and debugging of edge cases and I needed to create a bunch of test files to handle those

## [Day 16: Reindeer Maze](day16.py)
I tried to use NetworkX again, but it was looking unusable due to the turns. However, after I was well on the way to implementing my own Dykstra's algorithm, I was given an idea to do it with extra nodes for turns. I ended up using this graph with all turns and NX. Part 2 was not too bad since NetworkX has an "all shortest" function

## [Day 17: Chronospatial Computer](day17.py)
Ugg! Not the old int-code computer, reverse engineer what the program is doing puzzle! Part one is always to get the computer simulator to work, not a problem. Part two is always challenging, but I see that new entries are added on powers of 8 and I need 15, so the minimum bound is 8^15. Is there a way I could match back from the end? It took some time, but got this to both work and run in <3 seconds. I am now a full three days behind

## Day 18: RAM Run

## Day 19: Linen Layout

## Day 20: Race Condition
