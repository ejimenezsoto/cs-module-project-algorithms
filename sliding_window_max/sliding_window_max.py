'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):
    # Plan
    # create a new_array
    new_array = []
    # set start
    start = 0
    # check for base case
    # k contains certain indices
    # k increments 1 index at a time
    # numbers have a start and an end
    #  use some sort of iterator
    # k must be smaller  or equal than nums
    while start + k <= len(nums):
        # k is a slice of nums
        new_array.append(max(nums[start:(k + start)]))
        # max identifies the highest
        start += 1

        # return max items
    return new_array


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
