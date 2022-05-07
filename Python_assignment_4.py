# Q-1 Python program to find smallest number in a list

# python program to find the smallest number

# list of numbers
a = [18, 52, 23, 41, 32]

# find smallest number using min() function
smallest = min(a)

# print the smallest number
print(f'Smallest number in the list is : {smallest}.')

#Q-2 Python program to find largest number in a list
# Python Program to find Largest Number in a List 

a = [10, 50, 60, 120, 20, 15]

print("The Largest Element in this List is : ", max(a))


#Q-3 Python program to find second largest number in a list
# Python program to find second largest
# number in a list
 
# list of numbers - length of
# list should be at least 2
list1 = [10, 20, 4, 45, 99]
 
mx=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])
n =len(list1)
for i in range(2,n):
    if list1[i]>mx:
        secondmax=mx
        mx=list1[i]
    elif list1[i]>secondmax and \
        mx != list1[i]:
        secondmax=list1[i]
 
print("Second highest number is : ",\
      str(secondmax))

#Q-4 Python program to find N largest elements from a list
# Python3 code to demonstrate working of
# Indices of N largest elements in list
# using sorted() + lambda + list slicing
  
# initialize list
test_list = [5, 6, 10, 4, 7, 1, 19]
  
# printing original list
print("The original list is : " + str(test_list))
  
# initialize N 
N = 4
  
# Indices of N largest elements in list
# using sorted() + lambda + list slicing
res = sorted(range(len(test_list)), key = lambda sub: test_list[sub])[-N:]
  
# printing result
print("Indices list of max N elements is : " + str(res))

#Q-5 Python program to print even numbers in a list
# Python program to print Even Numbers in a List
 
# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
 
# iterating each number in list
for num in list1:
 
    # checking condition
    if num % 2 == 0:
        print(num, end=" ")

#Q-6 Python program to print odd numbers in a List

# Python program to print odd Numbers in a List
  
# list of numbers
list1 = [10, 21, 4, 45, 66, 93]
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num % 2 != 0:
       print(num, end = " ")

#Q-7 Python program to print all even numbers in a range
# Python program to print Even Numbers in given range
 
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
 
# iterating each number in list
for num in range(start, end + 1):
     
    # checking condition
    if num % 2 == 0:
        print(num, end = " ")

#Q-8 Python program to print all odd numbers in a range

# Python program to print odd Numbers in given range
  
start, end = 4, 19
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num % 2 != 0:
        print(num, end = " ")

#Q-9 Python program to print positive numbers in a list
# Python program to print positive Numbers in a List
 
# list of numbers
list1 = [11, -21, 0, 45, 66, -93]
 
# iterating each number in list
for num in list1:
     
    # checking condition
    if num >= 0:
       print(num, end = " ")
#Q-10 Python program to print negative numbers in a list
# Python program to print negative Numbers in a List
  
# list of numbers
list1 = [11, -21, 0, 45, 66, -93]
  
# iterating each number in list
for num in list1:
      
    # checking condition
    if num < 0:
       print(num, end = " ")

#Q-11 Python program to print all positive numbers in a range

# Python program to print positive Numbers in given range
  
start, end = -4, 19
  
# iterating each number in list
for num in range(start, end + 1):
      
    # checking condition
    if num >= 0:
        print(num, end = " ")