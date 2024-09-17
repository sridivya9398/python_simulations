def findLargest(a_list):
    # Check if the list is empty
    if not a_list:
        raise ValueError("The list is empty")
    
    # Initialize the maximum value with the first element
    max_value = a_list[0]
    
    # Iterate through the list starting from the second element
    for element in a_list[1:]:
        if element > max_value:
            max_value = element
    
    return max_value
