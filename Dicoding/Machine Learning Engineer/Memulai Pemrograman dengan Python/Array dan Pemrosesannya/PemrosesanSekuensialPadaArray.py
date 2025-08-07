# 1
var_arr = [1, 2, 3, 4, 5]

for i in range(len(var_arr)):
    current = var_arr[i]
    next_idx = i+1

    if next_idx < len(var_arr):
        next_element = var_arr[i+1]
    else:
        next_element = "None"

    print(f"Current Element: {current}, Next Element: {next_element}")
"""
Output:
Current Element: 1, Next Element: 2
Current Element: 2, Next Element: 3
Current Element: 3, Next Element: 4
Current Element: 4, Next Element: 5
Current Element: 5, Next Element: None
"""