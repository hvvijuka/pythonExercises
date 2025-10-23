#try:
#
#    name1,name2,name3 = input("Enter three names separated by commas: ").split(' ' )
#except ValueError:
#    print("Please enter exactly three names separated by spaces.")
#    exit()
#print("Name 1:", name1.strip())
#print("Name 2:", name2.strip())     
#print("Name 3:", name3.strip())
def get_name(): 
  while True:
    input_name = input("Enter your name: ")
    if input_name.isalpha() :
        return input_name.strip()  


def get_age(): 
  while True:
    input_name = input("Enter your age: ")
    if input_name.isdigit() :
        return int(input_name)

def get_salary(): 
  while True:
    input_name = input("Enter your salary: ")
    if input_name.isdigit() :
        return int(input_name)

name = get_name( )
age = get_age( )
salary = get_salary( )
statement = "your name is {0}, your age is {1} and your salary is {2}"
print (statement.format(name, age, salary) )
       