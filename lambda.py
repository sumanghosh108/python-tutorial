# 4/10/15
# ---------------------------------------------------------------------
# s='dhfjd'
# odd_even=lambda num:print(num%2)
# odd_even(11)
# odd_even=lambda num:print('Odd' if num%2!=0 else 'Even')
# odd_even(11)
# odd_even=lambda num:'Odd' if num%2!=0 else 'Even'
# a=odd_even(11)
# print(a)

# 1. Multiply three numbers
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))

# 2. Square of a number
square = lambda x: x * x
print(square(4))

# 3. Find length of a string
length = lambda s: len(s)
print(length("Lambda"))

# 4. Convert Celsius to Fahrenheit
c_to_f = lambda c: (c * 9/5) + 32
print(c_to_f(0))

# 5. Reverse a string
reverse = lambda s: s[::-1]
print(reverse("Python"))
