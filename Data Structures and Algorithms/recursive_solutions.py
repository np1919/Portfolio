### TOOLS (use @LRU cache?)

def wrapper(func, m, n):
    '''making my own cache'''
    memo = dict() # make a new dictionary
    return func(m, n, memo=memo) # pass it to the named variable memo


### RECURSIVE/MEMOIZATION 


# def sub_1(m):
#     ''' subtract 1 from m until you reach 0'''
    
#     # Base Case; 
#     # m reaches 0.
#     if m == 0:
#         return True
#     if m > 0:
#         # verbose
#         print(m, end='\t')       
#         # call the function inside itself (recursively). 
#         return sub_1(m-1)

    
def can_sum(m:int, n:list, memo:dict()):
    """ accepts:
                m: integer
                n: list of integers
        returns:
            bool;
             whether or not any combination of the integers in `n` can sum to the target, `m`.
            replacement is permitted. all integers in n will be non-negative.
        """
    #### Base Case/Win Condition; subtract successfully to 0.
    if m == 0: 
        return True

    #### Lose Condition; subtracted too far. Return False
    if m < 0:
        memo[m] = False
        return False
    
    #### Early Return --> target already in memory
    if m in memo:
        return memo[m]

    
    
    #### Branching/Recursive Logic;
            # Iterate through integers in `n`
    for element in n:
            # subtract `element` from m. Pass the remainder into a recursive call.
        remainder = m - element
            # calculate that branch/node;
        result = can_sum(remainder, n, memo)
        
            # if ever a node reaches 0, we can return True early. --> we Can Sum to the target. 
        if  result == True:
            memo[m] = True
            return True
        else:
            # if not, return False. Memo-ize in either case. As long as a recursive call is still running from this branch, 
            # the value at this stage of `m` will not be set to False in the dictionary
            memo[m] = False
            return False
        
        
        
def grid_traveler(m:int, n:int, memo:dict()):
    '''beginning at the top left of a 2-D grid, 
        and moving only DOWN or to the RIGHT;
         HOW MANY WAYS can you travel to the goal?'''

    # Base Cases;
    if m == 1 and n == 1:# Win -> you've reached the bottom right corner.
        return 1
    
    if m == 0 or n == 0: # Lose -> you're out of bounds.
        return 0

     
    # Memoization
    if (m, n) in memo: 
        return memo[(m, n)]
    if (n, m) in memo:
        return memo[(n, m)]

    
    go_down = grid_traveler(m-1, n, memo) # move down
    go_right = grid_traveler(m, n-1, memo) # move right
    
    total = go_down + go_right # the total will be the sum of the potential paths stemming from this node
    memo[(m, n)] = total # since the underlying grid will never change, keep cache in func.

    return total


def how_sum(m:int, n:list, memo:dict()):
    '''return one possible combination of sub-arrays in `n` which sum to produce `m` '''
    # Base case; you've removed a sub-array from m and m is now 0; you win.
    if m == 0:
        return []
    # Base failure case; you've removed a sub-array from m and m is now less than 0; you lose.
    if m < 0:
        return None
    
    # If you've done this before, don't.
    if m in memo:
        return memo[m]
    
    # iterate through elements in n.
    for num in n:
        remainder = m - num # create all possible remainders.
        chain = how_sum(remainder, n, memo) # for each remainder, create a chain recursive call.
        if chain is not None:            # when one eventually resolves, concatenate with this node and pass upwards
            result = chain + [num]       #
            memo[m] = result             # store the result and return it
            return result
        
        else:                           # if the recursive call finishes and has no hits, this node is also a dud.
            memo[m] = None
            
            
def best_sum(m:int, n:list, memo:dict()):
    """accept:
        m: int -> the target sum
        n: list: -> a list of integers with which to create the sum
        memo: dict -> defaults to an empty dictionary. To save results simply
        pass another dictionary.
        
        returns:
             the shortest possible array of numbers from `n` which sum to `m`
     
     """
    # Base Case: Win; you've called recursively with an m value of 0.
    if m == 0:
        return []
    # Base Case: Lose; you've gone too far.
    if m < 0:
        return None
    if m in memo:
        return memo[m]
    
    shortest = None # could easily be adapted to also provide the Longest combination
    
    for num in n:
        remainder = m - num
        chain = best_sum(remainder, n, memo) # returns a list, or None

        if chain is not None:
            combination = chain + [num] # chain returns as the shortest combination of the recursive call below

            if shortest == None: # first time through
                shortest = combination
            if len(combination) < len(shortest): # check that this combination is the shortest one.
                shortest = combination
         
            memo[m] = shortest # store in memory
    
    return shortest # return the shortest combination.             
          
    
    
    
    #### Branching/Recursive Logic;
            # Iterate through integers in `n`
    for element in n:
            # subtract `element` from m. Pass the remainder into a recursive call.
        remainder = m - element
            # calculate that branch/node;
        result = can_sum(remainder, n, memo)
        
            # if ever a node reaches 0, we can return True early. --> we Can Sum to the target. 
        if  result == True:
            memo[m] = True
            return True
        else:
            # if not, return False. Memo-ize in either case. As long as a recursive call is still running from this branch, 
            # the value at this stage of `m` will not be set to False in the dictionary
            memo[m] = False
            return False

        
def can_construct(m:str, n:list, memo=dict()):
    """ define a function can_construct:
    accepts:
        `m` : a sequence
        `n` : list of (sub)sequences, which can be used with replacement
        optional: a memo-ization object, or cache; to store the results of our recursive calls. Defaults to an empty dictionary.
    returns:
        boolean value; whether the m, `m`, can be created from the elements of list, `n`
        """
        #### Base Case/Win Condition --> m sequence `m` goes to 0.
            #### Return True.
    if m == "":
        memo[m] = True
        return True
    
        #### Early Return --> Already in Memo
    if m in memo:
        return memo[m]
    
        #### Branch Logic;
        #### Iterate through elements of sequence `n` and look for a prefix (match) with the current `m` value. Subtract it
        #### and keeping going

    for word in n:
        if m.startswith(word): # if word is a prefix of m;
            chain = can_construct(m[len(word):], n) # call recursively on the remainder of the list
            if chain == True: # Return early on the first True
                memo[m] = True 
                return True

        # If the whole chain isn't true by the end of the loops;
        # save this `m` value in memory as False and return False
    memo[m] = False
    return False


def all_construct(m, n):
    """ 
    accepts:
        m: a string
        n: a list of (sub-)strings, which can be used with replacement

    returns:
        2-D array of all combinations of n which produce m
        """
        # Base Case; you've removed elements and found str(len(0)). You win.
    if m == "":
        return [[]]
    
        # container to hold all possible combinations
    results = []
    for word in n:
        if m.startswith(word): # for this 'suffix', `m`;
            results += [[word] + x for x in all_construct(m[len(word):], n)] 
                        # prepend word to each inner list of the list returned by the recursive call
            # for each nested list returned from the recursive call, add this word to that list and pass 
            # the full list of combinations from this node upwards.

        # return the container of all possible combinations from this node's branches and leaves. 
    return results
        