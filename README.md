# PySimDiceGame
Assignment from my Brother's maths/stats course on KU.
Solved in Python, will see about including a copy of the code in R as well.

## Simulation task
Play dice game and determine the winning changes.

Play a game where a game board with four fields is used.
The four fields contain the numbers 4-24:
- Field1: 4, 5, 6, 7, 8, 9
- Field2: 10, 11, 12, 13, 14
- Field3: 15, 16, 17, 18
- Field4: 19, 20, 21, 22, 23, 24

A player puts 1 DKK on one of the four fields, then throws 4 dice and sums the score of the dice.
If the sum is one of the numbers in that field, the player gets 3 DKK (i.e. the ante + 2 DKK), if the sum is in one of the other fields the ante is lost.

### Section 3.1
Use simulation to determine the winning chances for each of the four fields.
Estimate how precise the probabilities are determined.
Consider which fields are sensible to play.

## Addition
We now make the game more concrete and assume the player has 2x1 DKK he wants to play.
We imagine he draws lots amongst the four fields about where to place each coin. The lots are drawn such that each of the four fields have an equal probability to be chosen.
When he has placed the two DKKs, the four dice are rolled and there is a sum to be win as per above.
Thus with each roll, the player gets 0, 3 or 6 DKK.

### Section 3.2
Use simulation to determine the probability for respectively 0, 3, and 6 DKK, when 2x1 DKK are played as per the strategy above.
Also determine the average winnings and finally evaluate whether it's a fair game to participate in.


## R notation:
The sum of 4 dice rolls can be done by:
```dice_rolls <- sum(sample(1:6,4,replace=TRUE))```

And the `field` variable can be set to `1` if the dice roll sums is 9 or lower as ```if (dice_rolls <= 9) field <- 1```
