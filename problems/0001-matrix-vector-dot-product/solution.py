def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.

    # 1. Check whether dimensions match
    if len(a[0]) != len(b) in b:
        return -1

    # 2. Create something to store answers
    result = []

    # 3. Go through each row
    for row in a :

        # 4. Calculate dot product
        dot_product=0
        for x, y in zip(row, b):
            p = x * y
            dot_product = dot_product + p

        # 5. Store it
        result.append(dot_product)

    return result

