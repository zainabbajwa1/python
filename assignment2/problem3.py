end_other=('abZZc', '1abXbc')
a=""
b=""
def end_other(a, b):

    a1 = a.lower()
    b1 = b.lower()
 
    if a1.endswith(b1) or b1.endswith(a1):
        # print(a1, b1)
        return True
    else:
        return False

result=end_other(a, b)
print(result)