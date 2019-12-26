def move_zeros(array):
    string_array = [i for i in array if i != 0 or i is False]
    zero_array = [j for j in array if j == 0 and j is not False]
    return string_array + zero_array

def move_zeros2(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))

my_array = [False,1,0,1,2,0,1,3,"a"]
altered_array = move_zeros(my_array)
print(altered_array)