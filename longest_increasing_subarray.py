arr = [int(x) for x in input().split()]
print(arr)
si=0
ei=0
fsi=0
fei=0
i=0
max_length=0

# while start index is less than the array length
while(si < len(arr)):
	#if you see a increasing pattern, proceed with iteration
	if (i+1 < len(arr) and arr[i+1] > arr[i]):
		i += 1
	else:
		#freeze the end index
		ei = i
		# figure out if the difference between si and ei (subarray length) is bigger than the currently stored subarray length, if so record the new length and new final ei and final si
		if (ei-si > max_length):
			max_length = ei-si
			fei = ei
			fsi=si

		#reset the temporary start and end indices
		si = i+1
		i += 1
		ei = -1

print(fsi,fei)	
