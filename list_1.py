""" <!-- my_list = [10, 20, 30, 40, 50]
Perform following operations on given list

Access Elements: Print the third element.
List Length: Print the number of elements in the list
Check if Empty: Write a code to check is list empty.
Expected Output:

Initial list: [10, 20, 30, 40, 50]

Third item:  30
Length of the list: 5
list is not empty --> """
i= 0
if i >0:
    my_list = [10, 20, 30, 40, 50]
    print("third item:", my_list[2])
    len(my_list)
    print("Length of the list:", len(my_list))
    print(my_list )
    if len(my_list) == 0:
        print("list is empty")  

        my_list = [10, 20, 30, 40, 50]

    """   Exercise 2  
    Perform following list manipulation operations on given list

    Change Element: Change the second element of a list to 200 and print the updated list.
    Append Element: Add 600 o the end of a list and print the new list.
    Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
    Remove Element (by value): Remove 600 from the list and print the list.
    Remove Element (by index): Remove the element at index 0 from the list print the list. """

    my_list[1] = 200
    print("Updated list after changing second element:", my_list)
    my_list.append(600)
    print("List after appending 600:", my_list)
    my_list.insert(2, 300)
    print("List after inserting 300 at index 2:", my_list)
    my_list.remove(600)
    print("List after removing 600:", my_list)
    my_list.pop(0)
    print("List after removing element at index 0:", my_list)   
    my_list.pop(4)
    print("List after removing element at index 4:", my_list)   

    """ Exercise 3: Sum and average of all numbers in a list
    Calculate and print the sum and average of all numbers in a list. """

    numbers = [10, 20, 30, 40, 50]
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    print("Sum of all numbers:", total_sum)
    print("Average of all numbers:", average)

    """ Exercise 4: Reverse a list
    Given:


    Expected output:

    [500, 400, 300, 200, 100] """

    list1 = [100, 200, 300, 400, 500]

    print("Initial list:", list1)
    list1 = [100, 200, 300, 400, 500]
    reversed_list = list1[::-1] 
    print("Reversed list:", reversed_list)
    list1.reverse()
    print("Reversed list using reverse() method:", list1)
    list2 = reversed_list.copy()
    print("Copied list:", list2)


    """ Exercise 5: Turn every item of a list into its square
    Given a list of numbers. write a program to turn every item of a list into its square.

    Given:

    numbers = [1, 2, 3, 4, 5, 6, 7]
    Expected output:

    [1, 4, 9, 16, 25, 36, 49] """

    numbers = [1, 2, 3, 4, 5, 6,7,7]
    squared_numbers = [x**2 for x in numbers]   
    print("Original list:", numbers)
    print("List with squared values:", squared_numbers) 

    squared_numbers_set = {x**2 for x in numbers}   
    print("Set with squared values:", squared_numbers_set)

    """ Exercise 6: Find Maximum and Minimum
    Find and print the largest and smallest number in a list [8, 2, 15, 1, 9].

    Given:

    data = [8, 2, 15, 1, 9]
    Expected Output:

    Largest number: 15
    Smallest number: 1 """

    list1= [10, 20, 30]
    data = list1[::] 
    data1 = list(reversed(data))
    print("data:", data)
    print("data1:", data1 )
    data_copy = data1.copy()
    print("data1_copy:", data_copy)

    #combine two list
    list1= [x for x in range (1,10)]
    list2= [y for y in range (11,20)]
    combined_list = list1 + list2
    print("Combined list:", combined_list)
    print("list1:", list1)
    print("list2:", list2)
    extended_list = list1.extend(list2)
    print("Extended list1:", list1) 


    words = ['apple', '','', 'cherry','', 'date',"","", "end"]
    word2 = list(words )
    i=words.count('')
    for w in words:
        if w =='' or w=="":
            word2.remove(w)


    word1 = [w for w in words if w]
    print("words after removing empty string using list comprehension:", word1) 
    i=words.count('')
    print("words after removing empty string:", word2,i )

    data = [8, 2, 12,12,12, 15, 1,9,9 ,9, 444]
    data_set = set(data)
    data1 = list(data_set)
    print(f"{data},\n removed the dupicates\n {data1 } " )

    list1 = [5, 20, 15, 20, 25, 50, 20]
    list2 = [x for x in list1 if x != 20]
    x = list1.count(20)
    print("Count of 20 in list1:", x)
    for i in range(x):
        list1.remove(20)

    print("list1 after removing all occurrences of 20:", list1)

    print("list2 after removing all occurrences of 20:", list2)

    my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
    print ("Original list:", my_list)
    my_list2 = [x for x in my_list if isinstance(x, int)]
    print("List after removing strings:", my_list2)
    my_list3 = [x for x in my_list if isinstance(x, str)]
    print("List after removing integers:", my_list3)

    nested_list = [1, 2, [3, 4], [5, 6], 7, 8, [9, 10]]
    flat_list = [x for item in nested_list for x in (item if isinstance(item, list) else [item])]
    print("Flattened list:", flat_list)

    #sets = set(nested_list )
    print("Original nested list:", nested_list)
    print

    list1 = ["M", "na", "i", "Ke"]
    list2 = ["y", "me", "s", "lly"]
    list1.extend(list2)
    print("Extended list1:", list1)
    list1 = list1 + list2
    print("Concatenated list1 and list2:", list1) 

    list1 = ["Hello ", "take "]
    list2 = ["Dear", "Sir"]
    list3 = []
    i =0
    for w in    list1:
        for x in list2:
            list3.append(w + x)
    print("Combined list:", list3)

    list1 = [10, 20, 30, 40]
    list2 = [100, 200, 300, 400]
    list3 =[]
    for x in list1:
        for y in  list2:
            list3.append(x + y)
    print("Combined list using list comprehension:", list3)

    list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
    id = list1.index(20)
    print("Index of 20 in list1:", list1.index(20)) 
    list1.insert(id + 1, [7000,800])
    print("Updated list1 after adding 7000:", list1)    


    def flatten(nested_list):   
        flat_list = []
        for item in nested_list:
            if isinstance(item, list):
                flat_list.extend(flatten(item))
            else:
                flat_list.append(item)
        return flat_list

    print("Flattened list:", flatten(list1))


    list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

    # sub list to add
    sub_list = ["h", "i", "j"]

    def add_sublist(nested_list, sub_list): 
        
        for item in nested_list:
            if isinstance(item, list):
                add_sublist(item, sub_list)
            else :  
                if item == "f":
                    #id =len(nested_list) 
                    nested_list.extend(sub_list)  
            
        return nested_list


    updated_list = add_sublist(list1, sub_list)
    print("Updated list after adding sublist:", updated_list)

    """ list1 = [5, 10, 15, 20, 25, 50, 20]
    Expected output:
    [5, 10, 15, 200, 25, 50, 20]
    """
    list1 = [5, 10, 15, 20, 25, 50, 20]
    id = list1.index(20)    
    list1[id] = 200
    print("Updated list1 after changing first occurrence of 20 to 200:", list1) 


 # Write a program to accept two integer numbers from the user and calculate their product.
    input1 = input("Enter first integer: ")
    if input1.isdigit():
        num1 = int(input1)    
    else:
        print("Invalid input. Please enter an integer.")
        exit()    

    str1 = 'My'
    str2 = 'Name'
    str3 = 'Is'
    str4 = 'James'
    full_str = f"{str1+"**"} {str2+"**"}{str3+"**"} {str4+"**"}"
    print("Full string:", full_str)



#Display Decimal Number to Octal using print() function
def octal_conversion(decimal_number: int, reminder: str) -> str:
    """Convrt a decimal number to its octal representation."""
    if decimal_number == 0:
        print("quoteind:", decimal_number, "remindr:", reminder)
        return reminder
    quoteind = int( decimal_number/8)
    remindr = str (decimal_number % 8)
    oct = remindr + reminder 
    octal_conversion (quoteind, ) 
    print("quoteind:", quoteind, "remindr:", remindr)
    return (oct  )
    



    input1 = input("Enter a decimal number: ")
    if input1.isdigit():
        decimal_number = int(input1)    
        octal_number = oct(decimal_number)
        print(f"The octal representation of {decimal_number} is {octal_number}")    

    #  i= octal_conversion(decimal_number,0)
        print("Octal conversion using function:", i)

    else:
        print("Invalid input. Please enter an integer.")
import math
# Display float number in specified decimal points.
num = 458.541315
print("Original number:", num)
print("Number formatted to 2 decimal places: {:.4f}".format(num))   
i =0
list = []
while True:
    
    input1 = input("Enter a float number: ")
    """ if input1.replace('.','',1).isdigit():
        list.append(float(input1))
        i = i+1
        print("i:", i)
        if i >5:
             break """
    
    
    if float(input1) == math.floor(float(input1)):
        list.append(float(input1))
        i+=1
        print("i:", i)
        if i >5:
            break


print("List with the entered float number:", list)