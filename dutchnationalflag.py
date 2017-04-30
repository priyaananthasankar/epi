arr = [int(x) for x in input().split()]
print(arr)
smaller =0
equal=0
larger=len(arr)-1
pivot = int(len(arr)/2)

print(smaller, equal, larger,pivot)

while(equal <= larger):
   if(arr[equal] < arr[pivot]):
      tmp = arr[equal]
      arr[equal] = arr[smaller]
      arr[smaller]= tmp
      equal += 1
      smaller += 1
      print("smaller ", arr,smaller,equal, larger)
   elif(arr[equal] == arr[pivot]):
      equal += 1
      print("equal ", arr,smaller,equal,larger)
   else:
      tmp = arr[equal];
      arr[equal] = arr[larger]
      arr[larger] = tmp
      larger -= 1
      print("larger ", arr,smaller, equal, larger)

print(arr)

