def string_compare(s1, s2):
    """Given two strings, figure out if they are exactly the same (without using ==).

    Put runtime here:
    -----------------
    [     O(n)      ]


    """

    if len(s1) != len(s2):          # O(1) for checking equality
        return False                # O(1) for return

    for i in range(len(s1)):        # O(n)  for 'for loop'
        if s1[i] != s2[i]:          # O(1)  for checking equality
            return False            # O(1)  for return

    return True                     # O(1)  for return


def has_exotic_animals(animals):
    """Determine whether a list of animals contains exotic animals.

    Put runtime here:
    -----------------
    [    O(n)       ]   #O(n) + O(n) = O(2n). The limit of this is O(n). 
 
    """

    if "hippo" in animals or "platpypus" in animals: #O(n) + O(n) for two hidden loops
        return True                                  #O(1) for return.
    else:                                            #O(1) for else. 
        return False                                 #O(1) for return. 


def sum_zero_1(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [      O(n^2)    ]  #Because you multiply O(n)*O(n) since the if loop is 
                        #inside of the for loop. Add to that result the O(n) from
                        #s, and you get O(n) + O(n^2). The limit of this is O(n^2).

    """

    result = []

    # Hint: the following line, "s = set(numbers)", is O(n) ---
    # we'll learn exactly why later
    s = set(numbers)        #O(n) for turning a list into a set. 

    for x in s:             #O(n) for 'for loop.'
        if -x in s:         #O(n) for hidden loop.
            result.append([-x, x])       #O(1) for an append. 

    return result              #O(1) for return. 


def sum_zero_2(numbers):
    """Find pairs of integers that sum to zero.

    Put runtime here:
    -----------------
    [     O(n^2)     ]  #Because loop inside of a loop. 

    """

    result = []

    for x in numbers:           #O(n) for 'for loop.'
        for y in numbers:       #O(n) for 'for loop'
            if x == -y:         #O(1) for checking equality. 
                result.append((x, y))   #O(1) for appending. 
    return result               #O(1) for return


def sum_zero_3(numbers):
    """Find pairs of integers that sum to zero.

    This version gets rid of duplicates (it won't add (1, -1) if (-1, 1) already there.

    Put runtime here:
    -----------------
    [      O(n^2)    ]  #O(n)*O(n)*O(n) = O(n^3) which rounds to O(n^2)

    """

    result = []

    for x in numbers:       #O(n) for 'for loop'
        for y in numbers:   #O(n) for 'for loop'
            if x == -y and (y, x) not in result:    #O(1) for equality check 
                result.append((x, y))               #O(n) for not in hidden loop.
    return result                                   #O(1) for append and return
