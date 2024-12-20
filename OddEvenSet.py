
numbers = {12, 5, 3, 10, 8, 15, 6, 7, 14, 9, 4}

odd_numbers = {num for num in numbers if num % 2 != 0}
even_numbers = {num for num in numbers if num % 2 == 0}

print(f"Odd numbers: {odd_numbers}")  
print(f"Even numbers: {even_numbers}")  
