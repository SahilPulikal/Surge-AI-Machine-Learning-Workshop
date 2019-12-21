# # if else
# a=100
# b=100

# if a>b:
#     print (" a greater than b")
# elif a<b:
#     print("a less than b")
# else:
#     print ('a=b')

# # while
# i=1

# while i<6:
#     print (i)
#     i=i+1
    
# # break and continue
# i=1

# while (i<6):
#     print (i)
#     i+=1
#     if(i==3):
#         continue

# # to get only int values from list    
# colors= [11,34.1,98.2,123]

# for c1 in colors:
#     if isinstance(c1,int):
#         print(c1)

# print only keys using for loop
# dict1 = {1:'abc',2:'xyz','ABC':"dictionary"}
# print(dict1.keys())
# print(dict1.items())
# print(dict1.values())

# for d1 in dict1.items():
#     print(d1)

   
# username=""

# if username!="pypy":
#     username=input(print("enter name"))


# a=0
# while a<5:
#     a=a+1
#     print(a)


# # functions in python
# def sum(a,b):
#     return a+b

# a=int(input("Enter value of a"))
# b=int(input("Enter value of b"))

# print("Sum is :",sum(a,b))    


# Call by reference
# Passing mutable object(list)

# def change_list(list1):
#     list1.append(20)
#     list1.append(30)
#     print("list inside function =",list1)

# list1 = [10,30,40,50]

# change_list(list1)
# print("List outside function =",list1)


# # Passing immutable object(string)
# def change_string(str):
#     str = str + "Hows you"
#     print("printing the string inside function:",str)

# string1 = "Hi I am there"

# change_string(string1)

# print("printing the string outside the function:", string1)

# # Lambda function
# x= lambda a:a+10
# print("sum=",x(20))

# Lambda function with filter
# program to filter out the list which contains odd nos

list1 = {1,2,3,4,10,123,22}
oddlist= list(filter(lambda x : (x%3 == 0),list1))
print(oddlist)

# lambda function wih map
list2 = {1,2,3,4,10,123,22}
new_list= list(filter(lambda x : (x*3 == 0),list2))
print(new_list)