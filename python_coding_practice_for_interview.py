# 1. Find the second highest number in an array

def find_second_highest_number(arr):
    """
    Finds the second highest number in a list.
    Removes duplicates and sorts the list.
    Returns None if fewer than 2 unique numbers exist.
    """
    arr = list(set(arr))
    arr.sort()
    return arr[-2] if len(arr) >= 2 else None


numbers = [10, 20, 20, 30, 40, 40]
sec_high_number = find_second_highest_number(numbers)
print(f"The second highest number is : {sec_high_number}")

# Option 2
numbers = [10, 20, 20, 30, 40, 40]
unique_numbers = list(set(numbers))
unique_numbers.sort()
required_number = unique_numbers[-2]
print(required_number)

# 2. Check if a given number is a palindrome
def is_palindrome(num):
    """
    Checks if a number is a palindrome.
    Returns True if yes, else False.
    """
    str_num = str(num)
    reverse_num = str_num[::-1]
    return str_num == reverse_num


number = 121
if is_palindrome(number):
    print(f"The number {number} is palindrome")
else:
    print(f"The number {number} is not palindrome")

# 3. Find average of three numbers
def find_average(a, b, c):
    """
    Calculates the average of three numbers.
    """
    return (a + b + c) / 3


num_1 = 8
num_2 = 9
num_3 = 10
average = find_average(num_1, num_2, num_3)
print(f"The average of following numbers: {num_1}, {num_2}, {num_3} is {average}")

# Option 2
a, b, c = 10, 9, 8
print((a + b + c) / 3)

# 4. Check if the given number is even or odd
def check_even_or_odd(number):
    """
    Checks if a number is even or odd.
    """
    if number % 2 == 0:
        print(f"The given number {number} is even")
    else:
        print(f"The given number {number} is odd")


num = 5
check_even_or_odd(num)

# 5. Check if the number is prime or not
def is_prime(number):
    """
    Checks if a number is prime.
    Returns True if prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# 6. Convert Fahrenheit to Celsius
def convert_F_to_C(fahrenheit):
    """
    Converts Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * 5 / 9

fahrenheit_temp = 79
celsius_temp = convert_F_to_C(fahrenheit_temp)
print(celsius_temp)

def convert_C_to_F(celsius):
    """
    Converts Celsius to Fahrenheit.
    """
    return (celsius * 9 / 5) + 32

celsius_tem = 45
fahrenheit_tem = convert_C_to_F(celsius_tem)
print(fahrenheit_tem)

# 7. Generate random number between 1 and 100
import random
random_number = random.randint(1, 100)
print(f"The random number is {random_number}")
random_float = random.uniform(1, 100)
print(f"The random float number is {random_float}")

# 8. Reverse a string without using built-in functions
def reverse_string(input_str):
    """
    Reverses a string manually.
    """
    reverse_str = ''
    for char in input_str:
        reverse_str = char + reverse_str
    return reverse_str


original = "Hello"
reverse = reverse_string(original)
print(f"The original string is {original}")
print(f"The reversed string is {reverse}")

# 9. Count number of words in a string
def count_words(input_string):
    """
    Counts words in a given string.
    """
    words = input_string.split()
    return len(words)


sentence = "I love python programing language"
counted_words = count_words(sentence)
print(f"The number of words in the sentence '{sentence}' is {counted_words}")

# 10. Reverse a given string (slice method)
def reverse_str(given_str):
    """
    Reverses a string using slicing.
    """
    return given_str[::-1]


original_string = "I love programming"
reversed_str = reverse_str(original_string)
print(f"Original string is {original_string} and reversed string is {reversed_str}")

# Option 2: Using reverse()
def reverse_string_2(string):
    """
    Reverses a string using reverse().
    """
    str_list = list(string)
    str_list.reverse()
    return ''.join(str_list)


text = "I love Python"
reversed_text = reverse_str(text)
print(f'The original string is "{text}" and the revered one is {reversed_text}')

# 11. Check if year is leap year
def is_leap_year(year):
    """
    Determines if a year is a leap year.
    """
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


year = 2024
if is_leap_year(year):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")