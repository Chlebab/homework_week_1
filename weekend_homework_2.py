# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers =[]
for number in numbers:
    if(number%2==0):
        even_numbers.append(number)
print(even_numbers)
print("==================================")


# 2. Print the difference between the largest and smallest value:
numbers.sort()
print(numbers)
print("The number of items in the array is:",len(numbers))
print("The highest number is: ",numbers[len(numbers)-1])
print("The lowest number is: ",numbers[0])

difference = numbers[len(numbers)-1] - numbers[0]
print("The difference is:" ,difference)
print("==================================")

# 3. Print True if the list contains a 2 next to a 2 somewhere.
n=0
while(n<len(numbers)-1):
<<<<<<< HEAD
    if (numbers[n] == 1 and numbers[n+1] == 1):
=======
    if (numbers[n] == 5 and numbers[n+1] == 5):
>>>>>>> 796ca57 (homework saved)
        print(True)
        break
    else:
        n +=1
<<<<<<< HEAD
=======

>>>>>>> 796ca57 (homework saved)
print("==================================")

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
numbers = [1, 6, 2, 2, 7, 1, 10, 6, 13, 99, 7, 5]

ignore_section = False
total_sum = 0

for num in numbers:
    if num == 6:
        ignore_section = True
    if num == 7:
        ignore_section = False
    elif not ignore_section:
        total_sum += num

print(total_sum)
print("==================================")

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 
numbers = [1, 6, 2, 2, 7, 1, 10, 6, 13, 99, 7, 5]
#numbers = [1, 13, 5]
#ignore_section = False
total = 0
x = numbers.index(13)
#print(x)
del numbers[x:]
print (numbers)
for number in numbers:
    total +=number

#for number in numbers:
#    if 

#for number in numbers:
#    if number == 13:
#        ignore_section = True
#    elif not ignore_section:
#        total += number

print(total)
