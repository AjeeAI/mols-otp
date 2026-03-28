#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import random

# Function to generate Latin squares
def latin_square(size, formula_x, formula_y):
    result = []
    for a in range(1, size):
        latin_square = []
        for x in range(size):
            row = []
            for y in range(size):
                element = ((a * formula_x(x)) + formula_y(y)) % size
                element = size if element == 0 else element
                row.append(element)
            latin_square.append(row)
        result.append(latin_square)
    return result

# Define fixed formulas
def formula_x(x):
    return x + 2

def formula_y(y):
    return 2 * y + 1

# Function to find positions where a value appears in a Latin square
def find_positions(ls, value):
    positions = []
    for i in range(ls.shape[0]):
        for j in range(ls.shape[1]):
            if ls[i, j] == value:
                positions.append(i * ls.shape[0] + j + 1)
    return positions

# Function to check if two Latin squares are mutually orthogonal
def is_mols(latin_square1, latin_square2):
    size = len(latin_square1)
    pairs = set()
    for i in range(size):
        for j in range(size):
            pair = (latin_square1[i][j], latin_square2[i][j])
            if pair in pairs:
                return False
            pairs.add(pair)
    return True

# Function to find MOLS between two Latin squares
def find_mols_between(latin_square1, latin_square2):
    size = len(latin_square1)
    mols_between = []
    for i in range(size):
        mols_between.append([(latin_square1[i][j], latin_square2[i][j]) for j in range(size)])
    return mols_between

# Function to generate RBIBDs
def generate_rbibd(latin_squares):
    rbibds = []

    # Generate the first extra RBIBD (rbibd1)
    rbibd1 = {f'rbibd1': {}}
    for i, row in enumerate(range(1, len(latin_squares[0]) ** 2 + 1, len(latin_squares[0]))):
        rbibd1['rbibd1'][i + 1] = [num for num in range(row, row + len(latin_squares[0]))]
    rbibds.append(rbibd1)

    # Generate the transpose of the first extra RBIBD (rbibd2)
    rbibd2 = {f'rbibd2': {}}
    for i in range(1, len(latin_squares[0]) + 1):
        rbibd2['rbibd2'][i] = []
    for num, positions in rbibd1['rbibd1'].items():
        for i, pos in enumerate(positions, start=1):
            rbibd2['rbibd2'][i].append(pos)

    rbibds.append(rbibd2)

    # Generate RBIBD for each Latin square
    for i, LS in enumerate(latin_squares):
        rbibd_dict = {}

        # Generate RBIBD by listing numbers from 1 to square of the size of the Latin square
        for num in range(1, len(LS) ** 2 + 1):
            positions = find_positions(np.array(LS), num)
            if positions:
                rbibd_dict[num] = positions

        # Append the RBIBD to the list
        rbibds.append({f'rbibd{i+3}': rbibd_dict})

    return rbibds

# Function to print a row from a Latin square
def print_latin_square_row(latin_squares, next_ls_index, chosen_row):
    next_ls = latin_squares[next_ls_index]
    available_rows = [row for row in next_ls if row[0] != chosen_row[0]]  # Filter out rows with the same first element
    if available_rows:
        random_row = random.choice(available_rows)
        
        return random_row
    else:
        print("No available row in the next Latin square chosen.")
        return None

# Function to calculate and print the superimposition equivalent of a row between two Latin squares
def print_superimposition_equivalent(latin_squares, chosen_ls_index, chosen_row_index, next_ls_index):
    chosen_ls = latin_squares[chosen_ls_index]
    next_ls = latin_squares[next_ls_index]
    
    chosen_row = chosen_ls[chosen_row_index]
    next_row = next_ls[chosen_row_index]  # Superimpose with the row at the same index in the next Latin square
    
    # Superimpose the chosen row with the next row
    superimposition = [(chosen_row[i], next_row[i]) for i in range(len(chosen_row))]
    
    # Flatten the superimposition to digits
    flattened_superimposition = flatten_to_digits(superimposition)
    
    return flattened_superimposition


# Function to convert multi-digit numbers to individual digits
def flatten_to_digits(auth):
    flattened = []
    for item in auth:
        if isinstance(item, tuple):
            flattened.extend(flatten_to_digits(item))
        else:
            flattened.extend([int(digit) for digit in str(item)])
    return flattened

# Function to truncate authentication based on the given rules
def truncate_authentication_custom(auth):
    auth = flatten_to_digits(auth)
    n = len(auth)
    
   
   

    if n > 10:
        if n % 2 != 0:  # Odd length
            median_index = (n - 1) // 2
            left_index = max(median_index - 5, 0)
            right_index = min(median_index + 6, n)  # Inclusive of right bound
            
            # Print the median value and index
            median_value = auth[median_index]
           

            # Truncate the authentication string
            left_part = auth[left_index:median_index]
            right_part = auth[median_index + 1:right_index]
            auth = left_part + right_part[::-1]  # Reverse right part and combine
        else:  # Even length
            mid1 = n // 2 - 1  # First middle index
            mid2 = n // 2      # Second middle index
            left_index = max(mid1 - 4, 0)  # 4 to the left including mid1
            right_index = min(mid2 + 5, n)  # 4 to the right including mid2
            
            # Print the two middle values and their indices
            median_values = (auth[mid1], auth[mid2])
            
            # Truncate the authentication string
            left_part = auth[left_index:mid1 + 1]
            right_part = auth[mid2:right_index]
            auth = left_part + right_part[::-1]  # Reverse right part and combine
    
    return auth
sizes = [5,7,11]
size = random.choice(sizes)

# Generate Latin squares
latin_squares = latin_square(size, formula_x, formula_y)

# Display the Latin squares
for i, ls in enumerate(latin_squares):
   continue
# Find and display MOLS
mols_list = []

for i in range(len(latin_squares)):
    for j in range(i + 1, len(latin_squares)):
        if is_mols(latin_squares[i], latin_squares[j]):
            mols = find_mols_between(latin_squares[i], latin_squares[j])
            mols_list.append((i, j, mols))
            
            for row in mols:
                continue

# Generate and display RBIBDs
rbibds = generate_rbibd(latin_squares)
for rbibd in rbibds:
    rbibd_key, rbibd_data = list(rbibd.items())[0]
    
# Choose a random Latin square
chosen_ls_index = random.randint(0, len(latin_squares) - 1)
chosen_ls = latin_squares[chosen_ls_index]

# Choose a random row from the chosen Latin square
chosen_row_index = random.randint(0, size - 1)

# Print details of the chosen row

# Print a row from the next Latin square chosen at random
# Ensure the next Latin square index is different from the first one
next_ls_index = random.choice([i for i in range(len(latin_squares)) if i != chosen_ls_index])

# Randomly choose a row from the next Latin square
random_row = print_latin_square_row(latin_squares, next_ls_index, chosen_ls[chosen_row_index])


# Authentication 1
print("\nAuthentication 1:")
auth1 = chosen_ls[chosen_row_index] + [chosen_ls_index + 1, chosen_row_index + 1, next_ls_index + 1]
auth1 = truncate_authentication_custom(auth1)

print(''.join(map(str, auth1)))

# Authentication 2
print("\nAuthentication 2:")
if random.choice([True, False]):  # Randomly choose between random_row or MOLS row
    auth2 = random_row
else:
    # Print the superimposition equivalent of the chosen row
    auth2 = print_superimposition_equivalent(latin_squares, latin_squares.index(chosen_ls), chosen_row_index, next_ls_index)

auth2 = truncate_authentication_custom(auth2)

print(''.join(map(str, auth2)))


print("\nAuthentication 3:")

# Step 1: Randomly decide the counting direction (from first or last)
counting_direction = random.choice(['first', 'last'])

# Step 2: Calculate the average index based on the chosen direction
if counting_direction == 'first':
    average_index_auth3 = (next_ls_index + chosen_ls_index) // 2  # Averaging from the first
else:
    average_index_auth3 = (len(rbibds) - 1) - ((len(rbibds) - 1 - next_ls_index + len(rbibds) - 1 - chosen_ls_index) // 2)  # Averaging from the last

average_index_auth3 = min(average_index_auth3, len(rbibds) - 1)  # Ensure the index doesn't exceed the list

# Print the calculated average index for Authentication 3


# Step 3: Access the RBIBD using the calculated average index
rbibd_key_auth3 = f'rbibd{average_index_auth3 + 1}'  # Adjust for 1-based index in naming

# Step 4: Fetch the row from the chosen RBIBD using the row index of Authentication 1
try:
    chosen_row_index_auth3 = chosen_row_index + 1  # Adjust for 1-based index
    

    rbibd3 = rbibds[average_index_auth3][rbibd_key_auth3][chosen_row_index_auth3]
    rbibd3_str = ''.join(map(str, rbibd3))

    # Print the chosen RBIBD row for Authentication 3
    
except KeyError as e:
    print(f"Key error: {e}, please check the RBIBD generation and keys.")

# Step 5: Truncate the Authentication if necessary
auth3 = truncate_authentication_custom(rbibd3_str)

print(''.join(map(str, auth3)))


# In[ ]:





# In[ ]:





# In[ ]:




