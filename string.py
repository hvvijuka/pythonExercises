def reverse_string(s: str) -> str:
    """Return the reverse of the input string."""
    return s[::-1]  


print(reverse_string(input("Enter a string to reverse: ")))
str = input('Enter a string: ')
print(str[1:3])


sports = ['Cricket', 'Football', 'Hockey', 'Football', 'Tennis']
i= sports.count('Football')
print("sports.count('Football')",i)

numbers = [5, 2, 8, 1, 9]
print("Original list:", numbers)
numbers.sort()
print("Sorted list:", numbers)
sorted_numbers = sorted(numbers, reverse=True)
print("Sorted list in descending order:", sorted_numbers) 
sorted_numbers = sorted(numbers)
print("Sorted list in ascending order using sorted():", sorted_numbers)   