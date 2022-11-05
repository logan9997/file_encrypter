import time, random

def tuple_test(nums):
    start = time.time()
    nums_tuple = nums
    new_tuple = ()
    for i in nums_tuple:
        new_tuple += (i,)
    fin = time.time() - start
    return fin

def list_test(nums):
    start = time.time()
    nums_list = nums
    new_list = []
    for i in nums_list:
        new_list.append(i)
    fin = time.time() - start
    return fin

'''nums = [random.randint(1,99) for i in range(25000)]

list_time = list_test(nums)
tuple_time = tuple_test(nums)

print(f"\n\n\ntuple - {round(tuple_time, 9)} | list - {round(list_time, 9)}")'''

word = "hello_ENCRYPTED_.jpg"

new = "".join(word.split("_ENCRYPTED_"))

print(new)