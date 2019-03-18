import numpy as np
from numba import njit
from itertools import permutations

@njit
def validate(pieces):
    """Validate if pieces are assembled in a valid configuration.
    
    Parameters
    ----------
    pieces : array like
        an array with 19 numbers, each number being 
        a number between 1 and 19, and allowing no 
        number to repeat.
    
    Returns
    -------
    result : Boolean
        Returns True if solution is valid, otherwise returns False.
    """ 

    ans = np.array(pieces)
    # check if pieces is a valid input
    if sorted(ans) != np.arange(1,20):
        raise ValueError('Pieces must be any ordering of output: list(range(1,20))')
   
    # create board configurations
    configs = np.array([ans, rotate_pieces(ans)])
    configs.append(rotate_pieces(configs[1]))

    # check sums
    result = all(np.array([all(check_rows(config)) for config in configs]))
    return result

def brute_force():
    """Solve puzzle via brute force."""
    pass

def rotate_pieces(ans):
    """Rotates the puzzle board.
    
    Parameters
    ----------
    ans : array like
        an array with 19 numbers, each number being 
        a number between 1 and 19, and allowing no 
        number to repeat.
    
    Returns
    -------
    : np.array
        Returns ans rearranged to reflect board rotation.
    """ 
    return np.array([
        ans[2], ans[6], ans[11],
        ans[1], ans[5], ans[10], ans[15],
        ans[0], ans[4], ans[9],  ans[14], ans[18],
        ans[3], ans[8], ans[13], ans[17], 
        ans[7], ans[12],ans[16]
    ])

def check_rows(ans):
    """Checks whether sums of each horizontal row is 38
    
    Parameters
    ----------
    ans : array like
        an array with 19 numbers, each number being 
        a number between 1 and 19, and allowing no 
        number to repeat.
    
    Returns
    -------
    : np.array([Boolean, ..., Boolean])
        Returns five booleans, each boolean signifying whether its corresponding row
        sums up to 38.
    """ 
    return np.array([
        sum(ans[:3]) == 38, 
        sum(ans[3:7]) == 38,
        sum(ans[7:12]) == 38,
        sum(ans[12:16]) == 38,
        sum(ans[16:]) == 38,
    ])