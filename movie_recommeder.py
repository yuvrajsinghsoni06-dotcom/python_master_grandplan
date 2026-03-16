import numpy as np

user_matrix = np.array([
    [5,4,0,0,1],   # user-1 loves Sci-fi and action
    [0,2,3,5,4],   # user-2 loves romance and comedy
    [4,5,1,0,0],   # user -3 loves Actiom and scifi
    [0,1,4,5,0]    # user -4 loves comedy and romance
])

new_user = np.array([5,5,0,0,0])

print("DataBase Shape:", user_matrix.shape)
print("new user shape:", new_user.shape)