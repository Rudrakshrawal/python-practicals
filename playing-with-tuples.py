# Given tuple
t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)

# Print half the values in one line and the other half in the next line
half = len(t1) // 2
print("Half of the values in one line:")
print(t1[:half])
print("Other half of the values in the next line:")
print(t1[half:])



# Print another tuple with even numbers from t1
even_tuple = tuple(num for num in t1 if num % 2 == 0)
print("Tuple with even numbers from t1:", even_tuple)

# Concatenate t2=(11,13,15) with t1
t2 = (11, 13, 15)
concatenated_tuple = t1 + t2
print("Concatenated tuple of t1 and t2:", concatenated_tuple)

# Return maximum and minimum values from the tuple
max_value = max(t1)
min_value = min(t1)
print("Maximum value in t1:", max_value)
print("Minimum value in t1:", min_value)
