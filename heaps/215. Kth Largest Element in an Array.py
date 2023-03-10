import heapq


def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)[-1]


nums = [3, 2, 1, 5, 6, 4]
k = 2
print(findKthLargest(nums, k))
