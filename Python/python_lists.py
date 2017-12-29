n = [[1, 2, 3, 4], [5, 6, 7, 8, 9]]
        
def single_list(x):
    new_list = []
    for index in x:
        for element in index:
            new_list.append(element)
    return new_list

print single_list(n)
