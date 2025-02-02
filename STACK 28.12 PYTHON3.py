
res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        
        return "".join(res)
    
    class Solution:
    def removeDuplicates(self, s: str) -> str:
         # Create a stack to store characters.
        st = []

        # Iterate through each character of the input string.
        for char in s:
            # Check if the stack is not empty.
            if st:
                # If the current character is equal to the top of the stack, remove the duplicate.
                if st[-1] == char:
                    st.pop()
                else:
                    # Push the current character onto the stack.
                    st.append(char)
            else:
                # If the stack is empty, push the current character onto the stack.
                st.append(char)

        # Build the result string by joining characters from the stack.
        result = ''.join(st)

        return result
    
    class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth -= 1 if depth > 0 else 0
            elif log == "./":
                depth += 0
            else:
                depth += 1
        return depth
    
    class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0

        for num in target:
            while i < num -1:
                ans.append("Push")
                ans.append("Pop")
                i += 1

            ans.append("Push")
            i += 1
        return ans
    
    stack = []
        num = 0
        prev_operator = '+'
        
        for i in range(len(s) + 1):
            ch = s[i] if i < len(s) else '\0'
            
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if not ch.isdigit() and ch != ' ' or i == len(s):
                if prev_operator == '+':
                    stack.append(num)
                if prev_operator == '-':
                    stack.append(-num)
                if prev_operator == '*':
                    stack.append(stack.pop() * num)
                if prev_operator == '/':
                    stack.append(int(stack.pop() / num))
                
                prev_operator = ch
                num = 0
        
        return sum(stack)