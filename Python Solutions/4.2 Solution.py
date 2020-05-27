import itertools

def solution(num_buns, num_required):
    buns_list = [i for i in range(num_buns)]
    
    bunny_key_assign = list(itertools.combinations(buns_list, num_buns - num_required + 1))
    # (num_buns C (num_buns - num_required + 1))
    # the first index of this array (bunny_key_assign)
    # would be a key represented as an array of bunnies to
    # which the key is assigned
    
    num_keys = len(bunny_key_assign)
    
    final_list = [[] for i in range(num_buns)]
    
    for a_key in range(num_keys):
        for bunny_to_give_key in bunny_key_assign[a_key]:
            final_list[bunny_to_give_key].append(a_key)
    
    return final_list