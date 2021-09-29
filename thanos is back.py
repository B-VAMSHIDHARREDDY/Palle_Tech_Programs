# def cp(str):
#     count = 1
#     li = list(str)
#     for i in range(len(li)-1):
#         if li[i] is not li[i+1]:
#             count +=1
#     if len(str)%2 != 0:
#         count += 1
#     return count
# str="))()()("
# res = cp(str)
# print(res)


# Python3 code to Check for balanced parentheses in an expression

# def check(my_string):
# 	brackets = ['()', '{}', '[]']
# 	while any(x in my_string for x in brackets):
# 		for br in brackets:
# 			my_string = my_string.replace(br, '')
# 	return not my_string
#
# # Driver code
# string = "{[]{()}}"
# print(string, "-", "Balanced"
# 	if check(string) else "Unbalanced")
# Python3 code to Check for
# balanced parentheses in an expression
# open_list = ["[","{","("]
# close_list = ["]","}",")"]
# Function to check parentheses
# def check(myStr):
# 	stack = []
# 	for i in myStr:
# 		if i in open_list:
# 			stack.append(i)
# 		elif i in close_list:
# 			pos = close_list.index(i)
# 			if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
# 				stack.pop()
# 			else:
# 				return "Unbalanced"
# 	if len(stack) == 0:
# 		return "Balanced"
# 	else:
# 		return "Unbalanced"

