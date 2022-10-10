def runningSum(nums):
    res = [0]
    for i in range(len(nums)):
        res.append(res[i] + nums[i])
    return res[1:]

nums = [1,2,3,4]
print(runningSum(nums))