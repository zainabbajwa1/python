def no_teen_sum(a, b, c):
  sum=fix_teen(a)+fix_teen(b)+fix_teen(c)
  print(sum)

def fix_teen(n):
    # CODE GOES HERE
     if ( 13<=n<20):
         return 0
     return n
no_teen_sum(2,13,1)