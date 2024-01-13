# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# git add . && git commit -m "completed evaluate_reverse_polish_notation" && git push && exit

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()

        for token in tokens:
            if token in ['*','-','+','/']:
                another = stack.pop()
                result = stack.pop()
                if token == '+':
                    result += another
                elif token == '-':
                    result -= another
                elif token == '/':
                    result = result/another
                    if result < 0:
                        result = math.ceil(result)
                    else:
                        result = math.floor(result)
                elif token == '*':
                    result *= another

                stack.append(result)
            else:
                stack.append(int(token))

        return stack.pop()

# faster version

# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         stack = deque()
#         for token in tokens:
#             if token == '+':
#                 another = stack.pop()
#                 result = stack.pop()
#                 result += another
#                 stack.append(result)
#             elif token == '-':
#                 another = stack.pop()
#                 result = stack.pop()
#                 result -= another
#                 stack.append(result)
#             elif token == '/':
#                 another = stack.pop()
#                 result = stack.pop()
#                 result = result/another
#                 if result < 0:
#                     result = math.ceil(result)
#                 else:
#                     result = math.floor(result)
#                 stack.append(result)
#             elif token == '*':
#                 another = stack.pop()
#                 result = stack.pop()
#                 result *= another
#                 stack.append(result)
#             else:
#                 stack.append(int(token))
#
#         return stack.pop()
