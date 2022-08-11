#ask user to input the reange of number
lower_val = int(input("what’s the lower value? "))
upper_val = int(input("what’s the upper value? "))
#add one to upper value to take right range in for loop
new_upper_val = upper_val + 1

#loop to take the number in the range
for num in range(lower_val, new_upper_val):
    #check the number more than 1
    if num > 1:
        #make loop for the number between the 2 and the number in the first range
        for num1 in range(2, num):
            #divided the number of the firat range by the second reange if the result equal 0
            if (num % num1) == 0:
                #stop
                break
        # if the result not equal 0
        else:
            #print the result
            print(num)