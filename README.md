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

## Day 11: ???
