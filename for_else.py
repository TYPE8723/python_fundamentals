# In this program, we have a list of numbers (numbers) and a search value (search_value). We iterate over each element in the numbers list using a for loop.

# Inside the loop, we check if the current number (num) matches the search value. If a match is found, we print "Number found!" and exit the loop using the break statement.

# The interesting part is the else block associated with the for loop. If the loop completes all iterations without encountering a break statement, the code inside the else block will execute. In this example, it will print "Number not found!".

# So, if the search value is present in the list, the program will print "Number found!". Otherwise, it will print "Number not found!".

# Note that the else block in a for loop is executed only when the loop completes all iterations without encountering a break statement.

numbers = [1, 2, 3, 4, 5]
search_value = 6

for num in numbers:
    if num == search_value:
        print("Number found!")
        break
else:
    print("Number not found!")
