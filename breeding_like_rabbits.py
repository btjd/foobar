"""
Breeding like rabbits
=====================

As usual, the zombie rabbits (zombits) are breeding... like rabbits! But instead of following the Fibonacci sequence like all good rabbits do, the zombit population changes according to this bizarre formula, where R(n) is the number of zombits at time n:

R(0) = 1
R(1) = 1
R(2) = 2
R(2n) = R(n) + R(n + 1) + n (for n > 1)
R(2n + 1) = R(n - 1) + R(n) + 1 (for n >= 1)

(At time 2, we realized the difficulty of a breeding program with only one zombit and so added an additional zombit.)

Being bored with the day-to-day duties of a henchman, a bunch of Professor Boolean's minions passed the time by playing a guessing game: when will the zombit population be equal to a certain amount? Then, some clever minion objected that this was too easy, and proposed a slightly different game: when is the last time that the zombit population will be equal to a certain amount? And thus, much fun was had, and much merry was made.

(Not in this story: Professor Boolean later downsizes his operation, and you can guess what happens to these minions.)

Write a function answer(str_S) which, given the base-10 string representation of an integer S, returns the largest n such that R(n) = S. Return the answer as a string in base-10 representation. If there is no such n, return "None". S will be a positive integer no greater than 10^25.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (string) str_S = "7"
Output:
    (string) "4"

Inputs:
    (string) str_S = "100"
Output:
    (string) "None"

General approach: When computing R() over a small sample we notice that even
times always attain higher values first. We implement R()using memoization.
In order to find a subset interval of time where to search n for based on
input S by incrementing our interval by a factor of 10 until we find our
target range. We then use binary search to find n. Our modified binary search
can search odd or even values of n based on a binary 'switch' param. We first
search odds, in case of duplicates, odd returns the higher n, if not found,
we redo the search on evens. if we still find nothing we return None
"""
# Memoization
def memoize(f):
    memo = {0: 1, 1: 1, 2: 2}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

# Define R() using memoization function
# as a decorator
@memoize    
def R(time):
    n = 0
    if time == 0 or time == 1:
        return 1
    elif time  == 2:
        return 2
    elif time%2 == 0:
        n = time/2
        return R(n) + R(n+1) + n
    else:
        n = (time-1)/2
        return R(n-1) + R(n) + 1

# Figure out subset interval of 0-to-10^25 max where we
# perform our binary search. Increase interval by factor
# of 10 until we hit out target.
def n_range(z):
    end = 10
    found = False
    while not found and end <= 10**25:
        if R(end+1) >= z:
            found = True
            return end+1
        else:
            end *= 10

def binary_search(zombits, switch):
    interval = n_range(zombits)
    first = 0
    last = interval
    found = False
    
    while first <= last and not found:
        # Find midpoint in current interval
        mid = first + ((last - first)//2)
        # Use xor to adjust midpoint to an
        # odd or even value. even & 1 = 0
        # Odd & 1 = 1
        mid += (mid & 1) != switch
        # z is our target
        z = R(mid)
        
        # This case happens when searching an even
        # value with switch = 1
        if first == last and not found: return None
        # We found our target
        elif z == zombits:
            found = True
        else:
            # Redo search on left side of midpoint
            if zombits < z:
                last = mid - 1
            # Redo search on right side of midpoint
            else:
                first = mid + 1
    return mid
            
def answer(str_S):
    # Change input to int
    goal = int(str_S, 10)
    # Only search odd values of n first
    odd_solution = binary_search(goal, 1)
    if odd_solution:
        return str(odd_solution)
    # If odds can't find it search evens
    else:
        even_solution = binary_search(goal, 0)
        return str(even_solution)


