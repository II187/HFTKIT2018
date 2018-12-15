"""works only for the two potency"""
x = int(input("Eingabe Basis:"))
y = int(input("Eingabe Potenz"))

input_x = 0
for i in range (0, x):
    input_x = x + input_x


input_y = input_x
for i in range(0, (y-2)):
    input_y = x + input_y

print(input_y)