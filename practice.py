A = (1, 2, 3, 4, 5)
lenth = len(A)
print(lenth)

V = [1]
V.append([2,3,4,5])
print(V)

score = 60
if score >= 90:
    print('Your final grade is A')
elif score >= 85:
    print('Your final grade is B')
elif score >= 70:
    print('Your final grade is C')
else:
    print('Talk to your instructor about your grade!')
    
    
nums = [1,2,3,4,5]
for num in nums:
    print(num + 1)
    

for i in range(10):
    print(i)
    
teams = [['Joy', 'Abel'],['Abhishek', 'Kim'], ['Tayler', 'Jen']]
for team in teams:
    for name in teams:
        print(name)
        
names = ['Joyce', 'Hannah', 'Manny', 'Manoj', 'Ezekiel']        
for name in names:
    if 'h' in name.lower():
        break
    else:
        print(name)
  
      
def odd_nums(my_list):
    for item in my_list:
        if item % 2 == 0:
            print(item)
numbers = [1, 2, 3, 5, 6, 7, 9, 13, 17, 15, 23, 27, 87, 45] 
odd_nums(numbers) 

def divisible_by_ten(nums):
    count = 0
    for number in nums:
        if (number % 10 == 0):
            count += 1
    return count

        
        
        
def greetings(language):
    if language == 'Spanish':
        greeting = 'Hola'
        
    elif language == 'English':
        greeting == 'Hello'
        
    elif language == 'French':
        greeting = 'Bonjour'
        
    print(greeting)
greetings(language='Spanish')


class dog:
    pass
pepper = dog()
print(pepper)

class ClassSchedule:
    def __init__(self, course):
        self.course= course
first = ClassSchedule('Chemistry')
print(first.course) 

class UserInfo:
    def __init__(self, username, email_address):
        self.username = username
        self.email_address = email_address
        
user = UserInfo('user1234', 'abc@efg.hij')

user.username
user.email_address

list1={'abel', 'jac', 'vic','rio'}
list2={'dan', 'ellah', 'james', 'tonny', 'joy'}
list3 = list1.union(list2)
print(list3)

points = 30
if points >= 70:
    print("You will be sponsered by government")
elif points <= 70:
    print('You are a private student or Self sponsered student')
    
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 27, 67, 89, 99, 101]
for number in numbers:
    print(number + 1)  
    
    
for i in range(4):
    print(i)  
    
members = [['Abeby', 'joh'], ['Kama', 'Holb'], ['Toto', 'Gabby']]
for member in members:
    for name in member:
        print(name) 
        
i =1
while i < 6:
    
    print(i)
    
    i += 1
    
cars = ['Audi', 'Mercedes', 'VW','Mark X', 'Lexus', 'Lumboghini', 'Auris', 'BMW', 'Rav4', 'Tesla','Dutsun']
for car in cars: 
    if 'l' in car.lower():
        continue
    elif 'o' in car.lower():
        pass
    elif 'n' in car.lower():
        break
    else:
        print(car)
        
def Mult(a,b):
    z = a*b
    return z
print(Mult(7, 'Rio DeJanairo')) 


def NoWork():
    pass
print(NoWork())

def EngNames(Engineers):
    for Engineer in Engineers:
        print(Engineers)
        EngNames('Vick', 'Ken', 'Rio', 'Kamenju','Vin', 'Kim') 
    
    

    



    
    