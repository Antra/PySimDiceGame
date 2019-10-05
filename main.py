import matplotlib.pyplot as plt
import random

# set the basic stuff -- it's actually easiest to run both 3.1 and 3.2 together.
n = 10000
board_results = []
winnings = []

field1 = [4, 5, 6, 7, 8, 9]
field2 = [10, 11, 12, 13, 14]
field3 = [15, 16, 17, 18]
field4 = [19, 20, 21, 22, 23, 24]


# how many simulations?
i = 0
while i < n:
    # remember to reset the won amount between simulations
    round_amount = 0

    # even though it's backwards, let's solve the assignments in the right order; so we begin with 3.1 and the dice rolls.
    t = random.randint(1, 6) + random.randint(1, 6) + \
        random.randint(1, 6) + random.randint(1, 6)
    if t in field1:
        board_results.append(1)
    if t in field2:
        board_results.append(2)
    if t in field3:
        board_results.append(3)
    if t in field4:
        board_results.append(4)

    # and then in the same loop, let's look at 3.2 and do the determination of how the player picks fields
    t1 = random.randint(1, 4)
    t2 = random.randint(1, 4)
    if t1 == board_results[i]:
        round_amount = round_amount + 3
    if t2 == board_results[i]:
        round_amount = round_amount + 3
    winnings.append(round_amount)

    # and then increment to the next simulation run
    i = i + 1

# calculate the frequencies for the fields
frequency = {}
for item in board_results:
    if (item in frequency):
        frequency[item] += 1
    else:
        frequency[item] = 1
sorted_freq_val = sorted(frequency.items(), key=lambda x: x[1])
sorted_freq_ord = sorted(frequency.items(), key=lambda x: x)
print('Frequencies matrix sorted by value; in a (category, count)-matrix:', sorted_freq_val)
print('Frequencies matrix sorted by order; in a (category, count)-matrix:', sorted_freq_ord)

# and the frequencies for the winnings
frequency = {}
for item in winnings:
    if (item in frequency):
        frequency[item] += 1
    else:
        frequency[item] = 1
sorted_freq_val = sorted(frequency.items(), key=lambda x: x[1])
sorted_freq_ord = sorted(frequency.items(), key=lambda x: x)
print('Frequencies matrix sorted by value; in a (category, count)-matrix:', sorted_freq_val)
print('Frequencies matrix sorted by order; in a (category, count)-matrix:', sorted_freq_ord)


# display the distribution of the game
bins = [1, 2, 3, 4, 5]
plt.hist(board_results, bins=bins)
plt.title("Histogram of results,\nnumber of runs: {}".format(str(n)))
plt.xticks(bins)
plt.xlabel("Board field")
plt.ylabel("Frequency")
plt.show()


# and display the distribution of the winnings
bins = [0, 3, 6, 9]
plt.hist(winnings, bins=bins)
plt.title("Histogram of results,\nnumber of runs: {}".format(str(n)))
plt.xticks(bins)
plt.xlabel("Winnings")
plt.ylabel("Frequency")
plt.show()
