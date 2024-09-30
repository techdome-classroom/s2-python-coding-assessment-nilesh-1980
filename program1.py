class Solution(object):
    def isValid(s: str) -> bool:
    # Stack to store opening brackets
    stack = []
    # Dictionary to map closing to opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    # Loop through each character in the string
    for char in s:
        # If it's a closing bracket, check for a match in the stack
        if char in bracket_map:
            # Pop the top of the stack if there's something, otherwise use a dummy value '#'
            top_element = stack.pop() if stack else '#'
            # If the top of the stack doesn't match the corresponding opening bracket
            if bracket_map[char] != top_element:
                return False
        else:
            # If it's an opening bracket, push it to the stack
            stack.append(char)

    # If the stack is empty, it means all brackets were properly closed
    return not stack






    



  

