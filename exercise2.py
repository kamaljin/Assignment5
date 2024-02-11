list = []

# Continuously prompt the user for numbers until they enter an empty string
while True:
        number = input("Enter a number (press Enter to quit): ")
        if number == "":
            break
        else:
            number1 = int(number)
            list.append(number1)
(list.sort(reverse=True))
print("\nThe five greatest numbers are:")
for i in range(min(5, len(list))):
 print(list[i])
