import numpy as np
# numpy as a python library supported by c which makes the operations faster than python list and it is also more memory efficient than python list
# print(np.__version__)  # to check the version of numpy we are usong

# my_list = [1,2,3,4,5]
# my_list = my_list * 2    # python list are slow and this is not a good way to do it
# print(my_list)  # this will print [1,2,3,4,5,1,2,3,4,5]

# my_arr = np.array([1,2,3,4,5])  # this will creagte a numpy arr which is 10X faster than python list
# my_arr = my_arr * 2  # this will multiply each element of the array by 2 and this is much faster than python list
# print(my_arr)
#   # this will print [2,4,6,8,10]

# print(type(my_arr))


# dtype in numpy is akeyword arguement that tells numpy what kind of values are stored in array otherwise numpy guesses the best data type based on your data manually seting dtype improves performance especally with dealing with large data sets

# <----- dtypes in numpy ----->

# integer (int) : int8, int16, int32, int64  # the number after int represent the no of bits used to store the integer.

# float : float16, float32, float64  # the number after float represent the no of bits used to store the float.

# boolean (bool_)
# string (str_)
# object (object)  # this is a general data type that can store any kind of data but it is not as efficient as other data types.

# array = np.array(['uv', 'yuvraj',1,2,3,3.56], dtype=np.object_)
# print(array)
# print(array.dtype)
# print(f"{array.nbytes} bytes")

# anything which is non  zero when covered to boolen is considered as True and zero is considered as False.


# using object dtype we can sotre mixed data types of elements in a array but it is not recommended as it is not memory efficient and it is also slower than other data types.


# arr = np.array([  
#       [[1,2],[3,4]],
#       [[5,6],[6,7]],
#       [[5,6],[7,8]]
# ])
# print(arr.ndim)  # ndimm attribute returns the dimension of arr


# print(arr.shape)


# indexing 
# numpy allows multidimensional indexing
# dept in index is the no of 2d array inside a stack
# word = arr[0,2,0] + arr[0,2,2] + arr[0,1,2]   #for 3d indexing (dept,rows,columns)
# print(word)
# ----------------------------------------------

# reshape() = changes the shape of an array without altering its underlying data

# arr = np.array([1,2,3,4,5,5,6,6])
# arr = arr.reshape(1,-1)
# print(arr)
# print(arr.shape)

# if we set a negitive value in reshape function as peremeter then  numpy automatically updates it


# -------------------------------------------------------------

#Slicing in numpy

# arr = np.array([[1,2,3,4],
#                 [5,6,7,8],
#                 [9,10,11,12],
#                 [13,14,15,16]])

# # arr[start:ending-1:step]

# # print(arr[::-2])

# print(arr[0:2,2:4])  # outof all the rows of an arr return first column of the all the matrix


# _______-----------------------------

# arithmetic operation in numpy

# scalar arithmetic

# arr = np.array([1.3,2.9,3.8])

# print(arr + 2)
# print(arr-1)
# print(arr *3)
# print(arr /4)
# print(arr **2)

# vectorization math functions
# print(np.sqrt(arr))
# print(np.round(arr))
# print(np.ceil(arr))
# print(np.pi)

# ceil - convert number to nearest greatest number (2.5 -> 3)
# round - converts number to its nearest number as possible ( 2.5 - > 2)

# radii = np.array([1,2,3])

# print(f"Area :{np.pi * radii **2}")
 

# element -wise arithmetics

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# print(arr1 + arr2)
# print(arr1 - arr2)
# print(arr1 * arr2)

# caparsion operators - returns a boolean dtype as an outpiut

# scores = np.array([91,71,100,73,82,64])
# print(scores > 60) 

# Broadcasting allows numpy to perform operstion on arrays with diff shapes by virtually expanding dimension so they matches the larger arr 's shape  for it happen dimension have the same size or one of its dimision has size of 1 .........


# arr1 = np.array([[1,2,3,4],[5,6,7,8]
#                  ])
# arr2 = np.array([[1],[2],[3],[4]])

# print(arr1.shape)
# print(arr2.shape)

# print(arr1 * arr2)

# arr1 = np.array([[1,2,3,4,5,6,8,9,10]])
# arr2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
# print(arr1 * arr2)

# zeros - arr of zero 
# ones - arr of one 
# 1d
# arr1 = np.zeros((5))
# print(arr1)

# # 2d
# arr2 = np.zeros((5,2))
# print(arr2)

# # 3d
# arr3 = np.ones((2,3,4))
# print(arr3)

# full -  to create arr of same element we use full function.

# arr1 = np.full((2,3,4),9)
# print(arr1)

#eye - creates a identity matrix

# arr1= np.eye(2)
# print(arr1)

# empty - it is faster than zeros arr but when we genrally use them when we required to create an arr which we are going to fill in the future


# arr1 = np.empty((2,3))
# print(arr1)

#arange() - it gtakes three arguements start,stop-1 ,steps

# arr1 = np.arange(100,0,-1)
# print(arr1)

# linspace - creates an arr with evenly spacecd values, it also takes three arguemnts start ,stop , nums ---- differnce from arange function is that we define how , what spaces we wanted

# arr1 = np.linspace(0,10,6)
# print(arr1)

# ---------------------------------------------------

# Aggregates function - summarizes data and tpyically returns a single value


# arr = np.array([[1,2,3,4,5],
#                [6,7,8,9,10]])

# print(np.sum(arr)) # returns a sum of all ele in an array
# print(np.mean(arr))  reurns the avg of the of an aray
# print(np.std(arr))  # returns  the standard deviation of an array
# print(np.var(arr))  # returns the variance of an array

# print(np.min(arr))  # returns the min value element in an arr
# print(np.max(arr))  # return the max value element in an arr

# print(np.argmin(arr))  # return the position of minmum value
# print(np.argmax(arr))  # return the position of maximum value

# print(np.sum(arr , axis=0)) # to apply function to se=precfic rows / column we use axis argument axis = 1 ( apply function to rows) axis = 0 (apply function to column)



# ----------------------------------------------

# filterimg 

# ages = np.array([[21,17,19,20,30,18,65],
#                  [39,22,15,99,18,19,20]])

# teenager = ages[ages < 18]  # boolen indexing will falten our 2d - 1d 
# adults = ages[(ages >= 18) & (ages > 65)]
# even = ages[ages % 2 == 0]
# print(teenager)
# print(adults)
# # print(ages)
# print(even)

# filtering  = array[condition of filtering ]

# adults = np.where(ages >= 18, ages, 0)  # where function takes three argument which (condition,arrayon to which cindition to be applied, modifiation to made on the unmatched condtion  data)  # also retains the origienal shape
#  # ut's slower than booleen indexing

# print(adults)


# -------------------------------------------------

# random numbers

# rng = np.random.default_rng(seed=2) # seed is used to preproduce same result
# print(rng.integers(low=1,high=101,size=(3,2)))

# print(np.random.unifrom(low=-1 , high = 1))

# -------------------------------------------------------

# saving in numpy

# arr = np.array([[1,2,3],[4,5,6]])
# np.save("C:\\Users\\1000\\OneDrive\\Desktop\\Resume_Matcher", arr)
# array = np.load("C:\\Users\\1000\\OneDrive\\Desktop\\Resume_Matcher")
# print(array)

# save = saves the array data in a specifiedd location 
#load = loads the stores value from stored location


# arr1 = np.array([[1,2,3],[4,5,6]])
# arr2 = np.array([1.1,1.2,1.3])
# arr3 = np.array([2025,2026,2027,2028])

# np.savez_compressed("data2", arr1, arr2, arr3)      # savez() - function helps use to save multiple array files
# print("Numpy array are saved! ")
 # z means zipt  savez_compressed - saves the data in some less memeory

# to load multiple arrays

# arrays = np.load("data.npz")
# array1 = arrays["arr_0"]
# array2 = arrays["arr_1"]
# print(array1)
# print(array2)


#   Broadcasting - allow operation to apply when shape of the element are same or either of them had one in thier same.

# a = np.array([1,2,30])   # shape = (1,3)
# b = np.array([[4],[5]])   # shape = (2,1)

# # print(a.shape)
# print(a + b)

# a= np.array([[2,4,9],
#              [8,1,6],
#              [7,5,3]])
# print(a[0:8:2,0:4:1])
# print(a[:,1, np.newaxis])  # np.newaxis also depends on where you Are use if used in row column of index then it will return selected element horizonatally(with extra dimension) and if done in column row it would return vertically with extra dimension .

# print(a[[0,1,2],[0,1,2]])     # for dimensionallity indexing we use extra square bracket in it.

# print(a[:,[True,False,True]])

# print(a[[[True,False,True],[True,False,True],[True,False,True]]]) # this type of indexing is also callled boolean masking


#   Sorting and searching in numpy----------------->

# there are two ways to sort an array in numpy >>> 1> array_name.sort()----- it will return a sorted version of our array ,,, 2> np.sort() - it will also return a sorted version of our version without modifying the original array

# print(np.sort(np.sort(a, axis=0),axis=1)) # it wouldn't course return same same in thier approx order
      
# # print(a)


# a.sort(axis=0)
# print(a)


# print(np.sort(a.flatten()).reshape(a.shape)) --- it will return same array in thier proper order.

# searching --> it is the opposite of indexing in it we give the value and it returns a indexes of the value

# Softmax - function gives you the probabilities for individual classes

# print(np.argmax(a)) # argmax- function which return the index of value which ahs maximum value...

# print(np.argmin(a))  # argmin - function opp of argmax returns min, value index....

# print(np.nonzero(a))  # nonzero - function returns all indexes of value which are non zero......

# where is used three peremeter (condition,outputs,value if condition false)

# a = np.array([12,23,34,45,56,67,78,89,100])
# print(np.where(a >= 50,a,"uv"))


# iteration in Numpy

# a = np.arange(12).reshape(3,4)
# print(a)

# for rows in a:
#     for ele in rows:
#         print(ele, end=' ') # traditional method for iterqation in numpy

# for element in np.nditer(a):  # nditer is a function in numpy that is used for efficiently iterating over multi dimensional array..
#     print(element, end=' ')


# for element in np.nditer(a, order="C"):   # order = "c" - default value for , order = "f" - returns in column manner. 
#     print(element, end=' ')

# with np.nditer(a, op_flags=['readwrite']) as it:
#     for element in it:
#         element[...] = element ** 2

# print(a)




# Masking - - is used for those perpose where we want to exclude ele in our calculation
# import numpy.ma as ma
# arr = np.array([1,2,np.nan,4,np.inf])   # np.nan - is passed null value in array and np.inf - is used to pass infinty as element to array
# # print(arr.mean())

# masked_arr = ma.masked_array(arr, mask=[0,0,1,1,1])

# print(masked_arr.mean())
# print(masked_arr)



