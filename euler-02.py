fibonacci_list = [1, 2]
max = 4000000
quit = False
while not quit:
    new_number = fibonacci_list[-2] + fibonacci_list[-1]
    if new_number > max:
        quit = True
    else:
        fibonacci_list.append(new_number)

result = 0
for i in range(len(fibonacci_list)):
    if fibonacci_list[i] % 2 == 0:
        result += fibonacci_list[i]
print(result)