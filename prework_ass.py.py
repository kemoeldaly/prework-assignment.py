#question 1
#Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
  print("Hello," + user_name+"!")

#question 2
#Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

for i in range(1,101):
        if i % 2 != 0:
         print(i)

#question 3
#write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
  max_num = 0
  for number in a_list:
    if number > max_num:
      max_num = number
  return max_num

#question 4
#Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
    if a_year % 400 == 0:
        return True
    elif a_year % 100 == 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False
is_leap_year()    


#question 5
#Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

def is_consecutive(a_list):
    if len(a_list) == 0:
        return True
    else:
        for i in range(1, len(a_list)):
            if a_list[i] - a_list[i-1] != 1:
                return False
        return True


  
   
