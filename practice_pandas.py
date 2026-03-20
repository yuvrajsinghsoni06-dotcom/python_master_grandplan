import pandas as pd


# print(pd.__version__)


# ----------------------------------
# Series -  a 1-d pandas dimensional labelled array that can hold any data type
# (like a single column in excel sheet)

# data = [100,102,104,200,202]

# arr = pd.Series(data, index=["a","b","c","d","e"])
# # arr.loc["a"] = 200
# # print(arr.loc["a"])   # loc argument is used to select a labelled valued(specifically used to access/ modified a labelled location)


# # print(arr.iloc[1])
#  # loc property is used to access value like loc but in integer format


# # filtering in pandas is same as in numpy

# print(arr[arr <= 200])

# calories = {"day 1": 1750, "day 2": 2100, "day 3": 1700}
# arr = pd.Series(calories)
# # arr.loc["day 3"] += 500
# print(arr[arr < 2000])

# ---------------------------------

# dataFrame -   a tabular data structure with rows and column ( 2d pandas data strucuture) similar to excel sheet.


# data = {
#     "Name": ["Spongbob","patrick","Squidward"],
#     "Age": [30,35,50]
#     }

# df = pd.DataFrame(data, index=["Employee 1","Employee 2","Employee 3"])
# # print(df.loc["Employee 1"])
# # print(df.iloc[1])

# # Add a new Column --->
# df["Job"] = ["Cook","N/A","Cashier"]

# # add a New rows ----->
# new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28,"Job": "Engineer"},{"Name": "fisher", "Age": 58,"Job": "scientest"}], index =["Employee 4","Employee 5"])
# df = pd.concat([df,new_row])

# print(df)


# --------------------------------------------


# importing file ( Csv/JSON file) -  using Pandas

df = pd.read_csv("pokemon.csv", index_col="Name") # read_csv(): helps us to import csv files.
# print(df) # when we just do like this it will print only first five and last five elements from the files

# print(df.to_string())    # to_string() - help us to dispaly all  the data form the the file . caution - don't use it when data is too big


# df = pd.read_json("pokemon.json")    # read_json is a function used to import json file's data
# print(df)

# ----------------------------------------------------
 # index_col = helps us to set a column we want to serve as the index for each rows


# Selection Techniques-- used to applied on csv and json file data

# Selection By Column -  in this we specifically selected the data we want to be visual to us.
# print(df["Name"].to_string())
# print(df["Height"].to_string())
# print(df["Type1"].to_string())
# # print(df["Type2"].to_string())
# print(df["Weight"].to_string())

# Selection of utiple columns in pandas - 

# print(df[["Name","Height","Weight"]])     - returns a mutiple selected columns 


# Selction By Rows: -  since pandas have the default property that it assign index to each rows in pandas

# print(df.loc[0])
# print(df.loc["Pikachu"])

# print(df.loc["Charizard":"Blastoise", ["Height" , "Weight"]])

# print(df.iloc[0:11:2,0:3])

# pokemon = input("Enter a POkemon name: ")

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} doesn't exist")

# ----------------------------------------------------------

# Filtering - df[df[specified data column] caparies ]

# tall_pokemon = df[df["Height"] >= 2]
# print(tall_pokemon)

# heavy_pokemon = df[df["Weight"] >= 100 ]
# print(heavy_pokemon)

# legendary_pokemon = df[df["Legendary"] == True]
# print(legendary_pokemon)

# water_pokemon = df[df["Type1"]== "Water"]   # while using logical operator we inclose our condition and selected data in ()
# print(water_pokemon)
# water_pokemon = df[(df["Type1"]== "Water") & (df["Type2"] == "water") ]  
# print(water_pokemon)

