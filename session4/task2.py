numbers = [i for i in range(1, 51)]  #list numbers from 1-50
even_sum = sum(num for num in numbers if num % 2 == 0) #gets the sum of all even numbers
odd = [num for num in numbers if num % 2 != 0]  #gets the product of all odd numbers
largest_num = max(numbers) #gets the largest number 
print("sum of even numbers:", even_sum)
print("product of all odd numbers:", odd)
print("largest number:", largest_num)


# largest_number = max(numbers)
# print("Sum of even numbers:", even_sum)
# print("Product of odd numbers:", odd_product)
# print("Largest number:", largest_number)
