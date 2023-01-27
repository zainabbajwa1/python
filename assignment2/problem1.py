# arrayCheck=([1, 1, 2, 1, 2, 3])
nums=""
def arrayCheck(nums):
    sort_list= ''.join(str(i) for i in sorted(nums))
    if '123' in sort_list:
        print(nums)
        return True


result=arrayCheck(nums)
print(result)