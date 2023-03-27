def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def print_matrix(arr):
    for row in arr:
        for item in row:
            print(item, end="\t")
        print()

def fill_matrix(arr):
    for i in range(len(arr)):
    	for j in range(len(arr[i])):
    		if i == 0 or j == 0:
    			arr[i][j] = '-'
    		elif i > j:
    			arr[i][j] = round((fibonacci(i) / fibonacci(j)), 1)
    		elif i < j:
    			arr[i][j] = round((fibonacci(j) / fibonacci(i)), 1)
    		elif i == j:
    			arr[i][j] = '*'
    return arr

if __name__ == "__main__":
    width = 7
    height = 7
    #creating a 7x7 2D list filled with 0.0 in each row and column
    arr = [[0.0 for _ in range(width)] for _ in range(height)]
    #passing the 7x7 2D list to your function 
    #and storing the function return value in arr
    arr = fill_matrix(arr)

	#if your function fill_matrix() is defined correctly
	#the below is the expected output for a 7x7 2D list 
    expected_arr = [
        ["-", "-", "-", "-", "-", "-", "-"],
        ["-", "*", 1.0, 2.0, 3.0, 5.0, 8.0],
        ["-", 1.0, "*", 2.0, 3.0, 5.0, 8.0],
        ["-", 2.0, 2.0, "*", 1.5, 2.5, 4.0],
        ["-", 3.0, 3.0, 1.5, "*", 1.7, 2.7],
        ["-", 5.0, 5.0, 2.5, 1.7, "*", 1.6],
        ["-", 8.0, 8.0, 4.0, 2.7, 1.6, "*"],
    ]

	#if your function returns the same 7x7 list as above expected_arr
	#you pass the test case
    if arr == expected_arr:
        print("Test case passed!")
        print("Output : \n")
    #if your function does not match the above expected 7x7 list
    #you are notified via some print statements
    else:
        print("Incorrect!")
        print("Expected output : \n")
        print_matrix(expected_arr)
        print("Your output : \n")

    print_matrix(arr) #prints the 7x7 list YOUR function produced
