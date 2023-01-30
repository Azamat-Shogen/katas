'''
        Given an array of items, an i-th index element denotes the 
        item id’s and given a number m, the task is to remove m elements 
        such that there should be minimum distinct id’s left.
        Print the number of distinct id’s.
'''

def solution(n, arr, m):
    products_dic = dict()
    for el in arr:
        if(f'item_{el}' in products_dic):
            products_dic[f'item_{el}'] += 1
        else:
            products_dic[f'item_{el}'] = 1


    list_values = list(products_dic.items())
    def sec(t):
        _, y = t
        return y
    
    list_values.sort(key=sec)
    
    def run(arr, num):
        if num == 0:
            return arr

        if arr[0][1] - 1 == 0:
            return run(arr[1:], num-1)
        else:
            temp_tuple = (arr[0][0], arr[0][1] - 1)
            arr[0] = temp_tuple
            return run(arr, num-1)     

    result = run(list_values, m)

    return result


# expamples:
n_1 = 6
ids_1 = [1, 1, 1, 2, 3, 2] # 2
m_1 = 2

n_2 = 8
ids_2 = [2, 4, 1, 5, 3, 5, 1, 3] # 3
m_2 = 2

n_3 = 6
ids_3 = [2, 4, 1, 5, 3, 5, 1, 3] # 3
m_3 = 3

n_4 = 6
ids_4 = [4, 1, 1, 1, 1, 2] # 1
m_4 = 2

# assert test cases
assert (len(solution(n_1, ids_1, m_1)) == 2)
assert (len(solution(n_2, ids_2, m_2)) == 3)
assert (len(solution(n_3, ids_3, m_3)) == 3)
assert (len(solution(n_4, ids_4, m_4)) == 1)