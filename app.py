#declare variable and types in Python


# age = 10
# price = 19.98
# first_name = 'Elijah'
# is_online = True
# print(age, price, first_name, is_online)


# #inputs
# #concating inputs. The space is required and you would answer in the terminal.
# greeting = input('How are you doing? ')
# # print('Good ' + greeting)

# #type convertion
# birth_Year = input("Enter your birth year: ")
# age = 2022 - int(birth_Year)
# # print(age)

#Calculator exercise
# value1 = input("First: ")
# value2 = input("Second: ")
# total = float(value1) + float(value2)
# print(total)

#strings
# course = 'Python for beginners'
# print(course.upper())
# print(course.lower())
# #finds the input at the index. Starts at 0
# print(course.find('y'))
# #search if a string is in a variable
# print('Python' in course)
# print(course.replace('beginners', 'seniors'))
# print(course)

#Math stuff
# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
#double // returns number as an integer where one / returns floating
# print(10 // 3)
# print(10 % 3)
# #exponent
# print(10 ** 3)

# #Logical Operators
# price = 25
# print(price > 10 and price < 30)
# print(price > 10 or price < 30)
# #not inverses the boolean
# print(not price > 10 )

#if statements
# temperature = 25

# if temperature > 30:
#     print("It's pretty hot")
#     print("drink more water")
# elif temperature > 20: 
#     print("it's a nice day")
# elif temperature > 10:
#     print("It's a bit cold")
# else:
#     print("It's cold")
#     #shift + tab to end if block
# print("done")

#Exercise
# weight = int(input("Weight: "))
# type = input("(K)g or (L)bs: ")
# if type.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in Lbs: " + str(converted))15-
# else:
#     converted = weight * 0.45
#     print("Weight in Kgs: " + str(converted))


# #while loops
# i = 1
# while i <= 5:
#     print(i * '*')
#     i = i + 1

# #list
# names = ["Elijah", "Bob", "Mary"]
# print(names)
# print(names[0])
# print(names[-1])
# print(names[-2])
# names[0] = "Eli"
# print(names)
# #returns all list up to the stopping index and DOES NOT include the stopping index
# #does not change original list
# print(names[0:2])

#List Methods
# numbers = [1, 2, 3, 4, 5, 6]
# #adds number to end
# numbers.append(7)
# print(numbers)
# #insert number into list
# numbers.insert(0, -1)
# print(numbers)
# #remove items
# numbers.remove(7)
# print(numbers)
# print(1 in numbers)
# print(len(numbers))
# #delete all in list
# numbers.clear()
# print(numbers)

# #For Loops
# numbers = [1, 2, 3, 4, 5, 6]
# for item in numbers:
#     print(item)

#Range() Function
numbers = range(5, 10)
for number in numbers:
    print(number)