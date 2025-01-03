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
Part 1 works with brute force. It took way longer than it should have to come up with, remember string transitions and then just keep a count of strings. I left the thought process in the one linked above. [Here](day11v2.py) is a cleaned up version

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
Ugg! Not the old int-code computer, reverse engineer what the program is doing puzzle! Part one is always to get the computer simulator to work, not a problem. Part two is always challenging, but I see that new entries are added on powers of 8 and I need 15, so the minimum bound is 8^15. Is there a way I could match back from the end? It took some time, but got this to both work and run in <3 seconds. I am now a full three days behind!

## [Day 18: RAM Run](day18.py)
Both parts were fine using NetworkX. Again, took <3 seconds for both parts and was pretty straight forward

## [Day 19: Linen Layout](day19.py)
Each part was medium tricky and I needed to cache function results to make it happen for both parts. I used the itertools lru cache function to make that part easy. Again, runs in <3 seconds for both parts

## [Day 20: Race Condition](day20.py)
The first part I did in an inefficient way (>1 min, <2), but it worked. The second part I did more efficiently, but it still took about 10 seconds. It included my first time using a nested defaultdict

## [Day 21: Keypad Conundrum](day21.py)
Finally got something to run fine for part 1. Needed to just do a smallest unit (one num pad move) instead of trying to track an entire code at a time. This approach fails early in part 2, so we need something new. Tried dropping all paths with more than one turn and that helped, but still will not finish. After much more time, I think we want to take paths that are closer to 'A' on the keypad as that will end up with fewer presses for downstream robots. For instance, from '^' to '>' you can take a path through 'v' or 'A'. Through 'A' should result in fewer downstream presses. Just turns may be enough for num pad moves. There are only four paths with options and only two of those probably matter. I made a module with that variable to just look up the paths I selected as the best. Turns out the 3->7 path matters in the example. We should go left before going up. We can do the same as for the key pad and manually edit those. Works for the short example and my input for part 1. Well, we can do 12 robot hops in reasonable time, but then it gets too slow. Is this just the lantern fish problem from 2019, similar to day 11 this year, yet again? It requires a bit of a different setup, but that approach works. I also made some bad assumptions about the best keypad paths that worked for part one, but not part 2. I also had trouble getting the robot count loop setup correctly. Tough day that took several days. I put part 2 [here](day21-p2.py) and I hand edited some parts of paths.py, so if it does not work for your input I would look at the numpad paths there

## [Day 22: Monkey Market](day22.py)
Part one was just following the instructions and so was easy. Part 2 looks harder, so I will post part 1 and update with part 2. It was not too bad, but had run times of ~3 seconds for part 1 and ~21 seconds for part 2. Meaning... it would be a good one to come back and try some optimizations on, but I would like to finish the final three days first

## [Day 23: LAN Party](day23.py)
Not too bad and a good practice run with NetworkX. Got to learn some new functions it has

## [Day 24: Crossed Wires](day24.py)
Part 1 is fine and didn't take too long. Part 2 is a debug-the-system type problem. The system is a bitwise added and I will guess it is a "full" adder given the gates we implemented. So... can we pull up each pair of bits in turn and check that the gates involved with those are doing [this](https://en.wikipedia.org/wiki/Adder_(electronics)#/media/File:Fulladder.gif)? There were many extra, non-damaging swaps, so I needed to get the real addition result, change that to binary and compare with the result from my input. After that, I started manually fixing swaps starting with the least significant missmatch. There is some output noise to help me debug and to make the portion of the bit checking I was working on fit in the terminal

## [Day 25: Code Chronicle](day25.py)
Not too bad as is usual for day 25 part 1.
