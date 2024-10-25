num_rows =int(input('Enter The number of rows: '))
current_number = 1 #start from 1


for row in range(1, num_rows + 1):
    for col in range (1, row + 1):
        print(col, end='')
        current_number += 1
    print()