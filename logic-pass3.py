def main():
    #ask user to input some text
    string = input("input some text: ")
    #ask user to input the latter that want to count it and check it only 1 latter not more
    while True:
        latter = input("input the char that want to count: ")
        if len(latter) == 1:
            break
    #print the result of count
    print(count(string, latter))

#function to count the latter
def count(str, lat):
    count = 0
    for i in str:
        if i == lat:
            count = count + 1
    return count

main ()