# # class Solution:
# #     def solve(self, nums: list):
# #         # Edge case: Return 0 and an empty list if the input is empty
# #         if not nums:
# #             return 0, []
            
# #         insert = 1 
        
# #         for i in range(1, len(nums)):
# #             if nums[i-1] != nums[i]:
# #                 nums[insert] = nums[i]
# #                 insert += 1

# #         # Return a tuple: (count of unique items, the cleaned sliced array)
# #         # nums[:insert] grabs everything from the start up to (but not including) the insert index
# #         return insert, nums[:insert]
    
# # # --- Testing it in a simulated pipeline ---
# # obj = Solution()
# # raw_data = [0, 1, 1, 2, 2, 2]

# # # Unpack the returned tuple into two separate variables
# # unique_count, clean_data = obj.solve(raw_data)

# # print(f"Total Unique Records: {unique_count}")
# # print(f"Cleaned Dataset to pass forward: {clean_data}") 
# # # Output: Cleaned Dataset to pass forward: [0, 1, 2]




# class Solution:
#     def solve(self,nums:list):
#         if not nums:
#             return 0,[]
#         insert = 1                         # insert local variable is doing two tasks one is to calculate total unique numbers , that will 
#         for i in range(1,len(nums)):
#              if nums[i-1] != nums[i]:
#                  nums[insert] = nums[i]
#                  insert +=1
#         return insert,nums[:insert]

# obj = Solution()
# # raw_data = [0,1,1,1,1,1,3,3,3]
# a,b =obj.solve(raw_data)

# print(f"Total number of unique number: {a}")
# print(f"Array with  no Duplicay: {b}")


class Solution:
    def solve(self,nums:list,val: int):
        ins = 0
        if not nums:
            return 0
        ins = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[ins] = nums[i]
                ins +=1
        return ins, nums[:ins]
    
o = Solution()
a,b = o.solve([0,1,9,8,5,6,3,1,3,5,3,4,2,1],3)
print(f"k ( number after removal of ele equal):{a}")
print(f"k : array ( number after removal of ele equal):{b}")
    






















