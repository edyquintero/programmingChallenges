def calculate_square_number(number):
    return number * number

list_of_squares = []
list_of_numbers = []

for i in range(1, 101):
    list_of_numbers.append(i)
    list_of_squares.append(calculate_square_number(i))

print(calculate_square_number(sum(list_of_numbers)) - sum(list_of_squares))