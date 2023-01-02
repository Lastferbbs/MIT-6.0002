###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.

    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)

    Returns: int, smallest number of eggs needed to make target weight
    """

    current_egg_number = 0
    eggs_from_category = 0
    temp_target_weight = target_weight
    if memo:
        for weight in reversed(egg_weights):
            if weight not in memo.keys():
                continue
            for number in range(memo[weight]):

                if temp_target_weight >= weight:
                    current_egg_number += 1
                    eggs_from_category += 1
                    temp_target_weight -= weight
                else:
                    break
            eggs_from_category = 0

            if memo[list(memo.keys())[-1]] > 0:
                memo[list(memo.keys())[-1]] -= 1
            else:
                del memo[list(memo.keys())[-1]]

        # TODO: Your code here
    if memo:
        other_egg_number = dp_make_weight(egg_weights, target_weight, memo)
    if other_egg_number < current_egg_number and current_egg_number > 0:
        return other_egg_number
    return current_egg_number


# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == "__main__":
    egg_weights = (1, 5, 10, 25)
    n = 99
    memo = {}
    for weight in egg_weights:
        memo[weight] = n // weight
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected output: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n, memo))
    print()
