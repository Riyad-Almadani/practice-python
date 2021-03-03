x = 42
y = 0
print()
try:
    print(x / y)
except ZeroDivisionError as e:
    print('Not allowed to divide by zero')
else:
    print('Something else wet wrong')
finally:
    print('This is our cleanup code')

print()