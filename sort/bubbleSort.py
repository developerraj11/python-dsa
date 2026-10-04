def bubble_sort(arr):
	"""Sort a list in ascending order using bubble sort and return it."""
	n = len(arr)

	for end in range(n - 1, 0, -1):
		swapped = False

		for index in range(end):
			if arr[index] > arr[index + 1]:
				arr[index], arr[index + 1] = arr[index + 1], arr[index]
				swapped = True

		if not swapped:
			break

	return arr