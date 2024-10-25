#ENTER NUMBER
row_count = int(input('Enter the number of rows: ')) 


#PROCESSING HERE
num = 1 
triangle_row = ''
if row_count > 0: 

  for row in range(1, row_count + 1): 

    for column in range(row): 

      triangle_row += str(num) + ' ' 

      num += 1 

    print(triangle_row) 

    triangle_row = '' 
else: 
   print("Invalid number of rows.") 
