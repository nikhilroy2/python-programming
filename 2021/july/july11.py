def demo(*nums):
    total = 0
    for a in nums:
        return nums[a]


#print(demo(3,2,4,2))

def factorial(n):
    if n== 1:
        return 1
    else:
        result = n * factorial(n-1)
    return result

print(factorial(4))
           