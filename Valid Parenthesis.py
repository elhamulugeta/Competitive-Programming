class Solution(object):
    def isValid(self, s):
        stack = []
        for i in range(0,len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                stack.append(s[i])
            elif s[i] == ")":
                if len(stack) == 0:
                    return False
                if stack[-1] != "(":
                    return False
                else:
                    stack.pop()
            elif s[i] == "}":
                if len(stack) == 0:
                    return False
                if stack[-1] != "{":
                    return False
                else:
                    stack.pop()
            elif s[i] == "]":
                if len(stack) == 0:
                    return False
                if stack[-1] != "[":
                    return False
                else:
                    stack.pop()
        if len(stack) != 0:
            return False
        return True
