def rehash():
    new_table = [None] * (len(table) * 2)
    # pseudocode
    '''
    for each slot in table:
        for each element in the linked list in that slot:
            PUT that element in new_table
    '''