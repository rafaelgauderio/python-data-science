# slice
# first digit is inclusive, second exclude

# Using list slicing, obtain the numbers 100 and 120.
Numbers = [15, 40, 50, 100, 120, 140, 180, 210]
slice_list = Numbers[3:5]
print(slice_list)

# Using slicing, extract the first five elements from the list.
# start on index zero, the 5 is exclusionary
print(Numbers[:5])

# Using slicing, extract all the elements from the list from the 3rd position onwards.
# start on index zero, including 3rd position
print(Numbers[2:])

# Using slicing, extract the last 3 elements from the list.
print(Numbers[-3:])

Negatives = [-20,-40];
all_numbers = [Numbers, Negatives];
print(all_numbers);
Numbers.sort(reverse=True);
print(Numbers);