def reverse_string(s: str) -> str:
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ""
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

# Example usage:
input_string = "world"
output_string = reverse_string(input_string)
print(f"Input: {input_string}")    # Output: "world"
print(f"Output: {output_string}")  # Output: "dlrow"
