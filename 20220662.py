#-------Continue or not------------
def ask_to_continue():
    respond = int(input("\nDo you want to continue? (If 'Yes' enter 1/ If 'No' enter 0) "))
    if(respond == 1):
        print("\n-------------------------------------")
        select_option()
    if(respond == 0):
        print("program is terminated")
#-------To select an option---------        
def select_option():
    x = int(input("\nPlease indicate your option : "))

    if x == 1:
        print("Enter a different option")
        select_option()
    elif x == 2:
#--------calculate highest value--------
        highest = number_list[0]
        for number in number_list:
          if number > highest:
            highest = number
        print("\nHighest value : ", highest)
        ask_to_continue()
    elif x == 3:
#-------calculate lowest value---------
        lowest = number_list[0]
        for number in number_list:
          if number < lowest:
            lowest = number
        print("\nLowest value : ", lowest)
        ask_to_continue()
    elif x == 4:
#-------calculate average value-------
        total = 0
        count = 0
        for number in number_list:
          total = total + number
          count = count + 1
        print("\nAverage value : ", total/count)
        ask_to_continue()
    elif x == 5:
#-------display even numbers--------
        print("Even numbers : ")
        for number in number_list:
          if (number%2 == 0):
            print(number)
        ask_to_continue()
    elif x == 6:
        print("program is terminated")
    else:
        print("Enter a valid option")
        select_option()

print("\t\t\tWonder Calculator")
print("\t\t\t=================")

print("\t\t\tMain Menu")

print("\t\t\t1.Enter positive integer numbers")
print("\t\t\t2.Display highest value")
print("\t\t\t3.Display lowest value")
print("\t\t\t4.Display average value")
print("\t\t\t5.Display even numbers")
print("\n\t\t\t6.Exit")

x = int(input("\nPlease indicate your option : "))

if(x>6):
    print("Please enter a valid option")
else:
    num = int(input("\nHow many numbers do you want to input? "))
    if (num>10):
        print("maximum is 10 numbers")
        num = int(input("\nHow many numbers do you want to input? "))

#--------To get the list of numbers the user input----------
    number_list = []
    for i in range(0, num):
        item =int(input("\nEnter a number : "))

        if (item<0):
            print("value cannot be negative")
            item =int(input("\nEnter a number : "))
        if (item==0): #if decimal
            print("value cannot be decimal")
            item =int(input("\nEnter a number : "))            
        number_list.append(item)  

    print("\nList of entered numbers : ", number_list)
    select_option()
