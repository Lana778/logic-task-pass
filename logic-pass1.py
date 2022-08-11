#aske user ro input his/her full name and check it only two name not more
while True:
    full_name = input("What's Your full name? ")
    if len(full_name.split())== 2:
        break

#split betwwen the two name
first_name, second_name = full_name.split()

#print the name without the second name
print(full_name.replace(second_name, ""))
