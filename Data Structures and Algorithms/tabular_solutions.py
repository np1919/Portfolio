### TOOLS
import pandas as pd
import numpy as np


### TABULATION

def fib(n):
    current, previous = 0, 1
    for x in range(n):
        current, previous = current + previous, current # quick and easy tuple unpacking.
    return current


def tab_grid_traveler(m, n):
    '''accept:
            cartesian coordinates (m, n)
            
        return:
            number of paths to (1,1)
    '''
    mat = np.zeros((m+1, n+1)) # form the grid
    table = pd.DataFrame(mat)
    start = table.iloc[1,1] = 1 # seed the table
    for rowidx, row in table.iterrows(): 
        for colidx, col in enumerate(row): # for each position, moving from top left;
            try:
                table.iloc[rowidx+1, colidx] += table.iloc[rowidx, colidx] # add the cell values to the one below
            except:
                pass        # naive exception handling deals with moving out-of-bounds
            try:
                table.iloc[rowidx, colidx+1] += table.iloc[rowidx, colidx] # add the cell values to the one to the right
            except:
                pass
   
    
    return int(table.iloc[-1,-1]) # can be easily modified to return the actual df; currently returns the count at (1,1)


def tab_can_sum(m, n):
    '''
    accept:
    m; integer
    n; list of integers
    
    return:
     ; bool
         whether or not the target sum, `m`, can be constructed using the elements of `n`
         with replacement
     '''
    arr = pd.Series(False, index=range(m+1)) # starting at base case 0 (index 0);
    arr[0] = True # seed True value at m==0;
    for idx, val in enumerate(arr): 
        if val == True: # if the cell has been seeded;
            for num in n: 
                if not idx+num > m: # if the resulting index is not out of bounds;
                    arr[idx+num] = True # seed the cell
    
    return  arr.index[m], arr[m]


def tab_how_sum(m, n):
    '''
          stores only one value in each cell.
        iterates backwards over the list to 'pick up' the stored values.
    
    accepts:
            m: integer
            n: list of integers
        returns:
            one possible combination of elements from `n`, with replacement, which sum to produce `m`.
            
      
    '''
    

    # create table
    arr = [None for x in range(m+1)] # we're summing to a number, index m+1
    arr[0] = [] # seed the table. this is our winning 'base case'.
    
        # container for return values
    output = []
    

    for idx, val in enumerate(arr):
        if val is not None: # if you're at a proven viable position; 
            for num in n: # for each element in `n`.
                if idx+num < len(arr): # limit so you won't move out of bounds;
                    
                    if arr[idx+num] is not None:
                        if num > arr[idx+num]: ####### check if the stored value is the largest... 
                                                ############ this isn't Necessarily the best route, but it is the biggest step.
                                
                            arr[idx+num] = num # assign the number that got you there to the resulting index.
                    else:
                        arr[idx+num] = num # assign the number that got you there to the resulting index.

                    
                    
            # then simply iterate backwards and pick up your numbers.
    if arr[m] is not None:
        position = m
        while position != 0:
            output.append(arr[position])
            position = position - arr[position] 
    return output


def tab_how_sum2(m, n):
    ''''version two!
         instead of iterating backwards to 'pick up' the elements, it concatenates them in the forward iteration
        (no chance to filter)    
        
    accepts:
            m: integer
            n: list of integers
        returns:
            one possible combination of elements from `n`, with replacement, which sum to produce `m`.
            
               
    '''
    
    arr = [None for x in range(m+1)] # we're summing to a number, index m+1M
    arr[0] = [] # seed the table

    for idx, val in enumerate(arr): 
        if val is not None: 
            for num in n:
                if idx+num < len(arr):
                    if arr[idx+num] == None:
                        arr[idx+num] = val + [num]  
                    else:  
                        arr[idx+num] = val + [num]
                        
                        
    return arr[m]


def tab_best_sum(m, n):
    ''' accepts:
            m: an integer
            n: a list of integers
    
    returns:
        the SHORTEST combination of elements of `n` which sum to `m`
    '''
    output = []
    arr = [None for x in range(m+1)] 
    arr[0] = [] 

    for idx, val in enumerate(arr): 
        if val is not None:
            for num in n:
                if idx+num < len(arr):
                    if arr[idx+num] == None:
                        arr[idx+num] = val + [num]  
                    elif len(val + [num]) < len(arr[idx+num]):#### Add condition 
                                                              #### (that the replacement is shorter)
                        arr[idx+num] = val + [num]

    return arr[m]


def tab_can_construct(m, n):
    '''accept:
            m: a string
            n: a list of strings
            
        return:
            BOOL 
            
            whether or not the target string`m`
            can be constructed 
            using the elements from `n `
            with replacement'''
 

    # create table of length target string + 1
    arr = pd.Series(index=[x for x in m] + ['Final'], data = False)
    arr[0] = True # seed the viable case
    
    for idx, (key, val) in zip(range(len(m)+1), arr.iteritems()): # for each possible starting position
        if arr[idx] == True: # if it has been proven viable (we move right-wise)
            current_letter = arr.index[idx]            
            for sub in n: # check each subsequence in n   
                if sub.startswith(current_letter) and (idx+len(sub) < len(arr)):
                    arr[idx+len(sub)] = True
    return arr[-1]



def tab_count_construct(m, n):
    '''accept:
            m: a string
            n: a list of strings
            
        return:
                INT
                
            HOW MANY WAYS `m`can be constructed 
            using the elements from `n `
            with replacement'''
 

    # create table of length target string + 1
    arr = pd.Series(index=[x for x in m] + ['Final'], data = 0)
    arr[0] = 1 # seed the viable case
    
    for idx, (key, val) in zip(range(len(m)+1), arr.iteritems()): # for each possible starting position
        if arr[idx] > 0: # if it has been proven viable (we move right-wise)
            for sub in n:
                    # determine potential next index, based on subsequences in n
                next_index = idx+len(sub)
                    # check each subsequence in n against the suffix (m[idx:next_index]) 
                    # if the substring matches; and the next_index is valid;
                if sub == m[idx:next_index] and (next_index < len(arr)): #len is indexed from 1
                    arr[idx+len(sub)] += arr[idx] 
                        # add the paths to the next index
    return arr[-1]


def tab_all_construct(m, n):
    '''accept:
            m: a string
            n: a list of strings
            
        return:
            2-D array of ALL WAYS `m`can be constructed 
            using the elements from `n `
            with replacement'''
    n = set(n)
    m_string = [x for x in m] + ['Final'] # m+1
    arr = [None for x in m_string] # matching list
    arr[0] = [[]] # seed the viable case

    for idx, char in enumerate(m_string):
        suffix = m[idx:]
        if isinstance(arr[idx], list): # a list; a viable path.
            for sub in n: # check each subsequence in n
                if suffix.startswith(sub):
                    next_index = idx+len(sub)
                    # everything in arr[idx] -> next_idx
                    if arr[next_index] == None:    
                        arr[next_index] = [x+[sub] for x in arr[idx]]
                    else:
                        arr[next_index] += [x+[sub] for x in arr[idx]]

    return pd.Series(arr, index=m_string)[-1]