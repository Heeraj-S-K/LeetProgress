class Solution(object):
    def isValid(self, s):
        # Dictionary to map closing brackets to their opening counterparts
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped element doesn't match the required opening bracket
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all brackets matched
        return not stack

