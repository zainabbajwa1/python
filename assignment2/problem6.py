myList =([2, 2, 0])
myList =([2, 1, 2, 3, 4])
myList =([1, 3, 5])

def count_evens(myList):
  count=0
  for num in myList:
      if (num%2==0):
          count+=1
  print(count)

count_evens(myList)