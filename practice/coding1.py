# # # def factorial(n):
# # #     if n == 0:
# # #         return 1
# # #     else:
# # #         return n * factorial(n-1)

# # # print(factorial(5))

# # # def recursion(n):
# # #     total = 0
# # #     if n > 0:
# # #         rem = n % 10
# # #         n = n // 10
# # #         total = rem + recursion(n)
# # #         return total
# # #     else:
# # #         return(0)
# # # print(recursion(123))

# # def reverse(words : str):
# #     if len(words) == 0:
# #         return ""
# #     else:
# #         return words[-1] + reverse(words[:-1])
# # print(reverse("Hello World"))

# # def fibonacci(n):
# #     number =0
# #     a = 0
# #     b = 1
# #     for i in range(n):
# #         number += a
# #         a, b = b , a + b
# #     return f"{n}th Fibonacci number is {a}"
    
# # print(fibonacci(5))

# # def palindrome(word: str):
# #     # 1. Base Case: 0 or 1 letter is always a palindrome
# #     if len(word) <= 1:
# #         return True
    
# #     # 2. Check the outer layer (First vs Last)
# #     if word[0] == word[-1]:
# #         # 3. Recursive Step: Check the inner part (Peel the onion)
# #         return palindrome(word[1:-1])
# #     else:
# #         # If outer layers don't match, it's game over.
# #         return False

# # print(palindrome("madam"))  # True
# # print(palindrome("hello"))  # False


# class Solution:
#     def solve(self, strs: list):
#         if not strs: # More Pythonic check for empty list
#             return ""
        
#         min_length = min(len(s) for s in strs)
#         result = ""
        
#         for i in range(min_length):
#             current = strs[0][i] # Fixed the 'strs' typo
            
#             # Check if this character matches in ALL strings
#             for s in strs:
#                 if s[i] != current:
#                     return result # Return immediately if any string differs
            
#             # ONLY add to result after the inner loop confirms ALL strings matched
#             result += current
            
#         return result

# # 1. Instantiate the class
# obj = Solution() 

# 2. Call the method and store the output
# ans = obj.solve(["flow", "flight", "float"])

# # 3. Print the result, not the object itself
# print(ans)
                

        




    


