str1 = str(input("Please enter a string for the variable chars: "))
print("The original string is: " + str1)
first_part, second_part = str1[:len(str1)//2], str1[len(str1)//2:]
word = str(input("Please enter a work to insert into the middle of the chars:"))
print(first_part + word + second_part)