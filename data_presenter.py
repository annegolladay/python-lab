# Part 2

# Loop through all the data and print each row.
open_file = open('Cupcakeinvoices.csv')

# for line in open_file:
    # print(line)

# Loop through all the data and print the type of cupcakes purchased.
# for line in open_file:
#     flavor = line.split(',')
#     print(flavor[2])
        

# Loop through all the data and print out the total for each invoice (Note: this data is not provided by the csv, you will need to calculate it. Also, keep in mind the data from the csv comes back as a string, you will need to convert it to a float. Research how to do this.).

# for line in open_file:
#     numbers = line.split(',')
#     line_total = float(numbers[3]) * float(numbers[4])
#     print(line_total)
    
# Loop through all the data, and print out the total for all invoices combined.

# total = 0

# for line in open_file:
#     numbers = line.split(',')
#     line_total = float(numbers[3]) * float(numbers[4])
#     total += line_total
    
# print(total)

#  Further
chocolate = 0
vanilla = 0
strawberry = 0

for line in open_file:
    value = line.split(',')
    line_total = float(value[3]) * float(value[4])
    if value[2] == 'Chocolate':
        chocolate += line_total
    elif value[2] == 'Vanilla':
        vanilla += line_total
    elif value[2] == 'Strawberry':
        strawberry += line_total

print(chocolate)
print(vanilla)
print(strawberry)


# import matplotlib.pyplot as plt
# import numpy as np

# y = np.array([35, 25, 25, 15])

# plt.pie(y)
# plt.show() 