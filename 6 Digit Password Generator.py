Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
>>> special_signs = ['-', '_', '#', '$', '&', '*', '@']
>>> def main():
...     letter_1 = random.choice(letters)
...     x = random.choice(numbers)
...     y = random.choice(numbers)
...     z = random.choice(numbers)
...     sign = random.choice(special_signs)
...     letter_2 = random.choice(letters)
...     password = letter_1.capitalize() + x + sign + y + z + letter_2
...     print(password)
... 
...     
>>> main()
A9#83t
