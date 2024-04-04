#1)
#Write a Python program to filter a list of integers using Lambda. Go to the editor
#Original list of integers:
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#Even numbers from the said list:
#[2, 4, 6, 8, 10]
even_num_list = list(filter(lambda num: num % 2 == 0, num_list))
print(even_num_list)

#Odd numbers from the said list:
#[1, 3, 5, 7, 9]
odd_num_list = list(filter(lambda num: num % 2 == 1, num_list))
print(odd_num_list)


#2)
#find which days of the week have exactly 6 characters.

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

char_list = list(filter(lambda day: len(day) == 6, weekdays))
print(len(char_list))


#3)
#remove specific words from a given list 
#Original list:
color_list = ['orange', 'red', 'green', 'blue', 'white', 'black']

#Remove words:
remove_list = ['orange', 'black']
remov_color_list = list(filter(lambda color: color not in remove_list, color_list))

#After removing the specified words from the said list:
#['red', 'green', 'blue', 'white']

print(remov_color_list)


#4)
#remove all elements from a given list present in another list
#Original lists:
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

#Remove all elements from 'list1' present in 'list2:
#[1, 3, 5, 7, 9, 10]

new_list1 = list(filter(lambda num: num not in list2, list1))
print(new_list1)


#5)
#find the elements of a given list of strings that contain specific substring using lambda
#Original list:
color_list = ['red', 'black', 'white', 'green', 'orange']

#Substring to search:
removal1 = "ack"
new_color_list = list(map(lambda color: color.strip(removal1), color_list))

#Elements of the said list that contain specific substring:
#['black']
print(new_color_list)

#Substring to search:
removal2 = "abc"
new_color_list = list(map(lambda color: color.strip(removal2), color_list)) #fix this function, cuts off the "a" in "black"

#Elements of the said list that contain specific substring:
#[]
print(new_color_list)







#number 5 needs fixing before you move on
''' 6)
check whether a given string contains a capital letter, a lower case letter, a number and a minimum length of 8 characters.
(This is like a password verification function, HINT: Python function 'any' may be useful)
'''

str1 = "Hello8world"
str1 = "HELLO"
str1= "hello"












''' 7)
Write a Python program to sort a list of tuples using Lambda.

# Original list of tuples:
original_scores = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

# Expected Result:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
'''
