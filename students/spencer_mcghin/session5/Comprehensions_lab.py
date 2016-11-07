# Coding Bat Count Even Numbers #

nums = range(0, 20)

def count_evens(nums):

    num_evens = [number for number in nums if number % 2 == 0]
    print(num_evens)


count_evens(nums)




