nums, k = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3], 3
def bruteforce(nums, k):
    res = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            wholesum = sum(nums[i:j+1:])
            if wholesum == k:
                res += 1
    return res

