def partition(array, low, high):

	# choose the rightmost element as pivot
	pivot = array[low]

	# pointer for greater element
	i = low + 1

	# traverse through all elements
	# compare each element with pivot
	for j in range(low + 1, high):
		if array[j] < pivot:

			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])
			i += 1

	# Swap the pivot element with the greater element specified by i
	(array[i - 1], array[low]) = (array[low], array[i - 1])

	# Return the position from where partition is done
	return i 

data = [1, 7, 4, 5, 10, 9, -2]
print('Sebelum partitioning :', data)
partition(data,0,len(data))
print('Setelah partitioning:', data)