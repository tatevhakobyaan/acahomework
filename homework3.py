"""Salaries
Given the salaries of three employees working at a department, find the amount of money by which the salary of the highest-paid employee differs from the salary of the lowest-paid employee. The input consists of three positive integers - the salaries of the employees. Output a single number, the difference between the top and the bottom salaries
"""

salary1 = int(input())
salary2 = int(input())
salary3 = int(input())

maximum = salary1
if salary2 > salary1 and salary2> salary3:
  maximum = salary2
if salary3 > salary1 and salary3 > salary2:
  maximum = salary3

minimum = salary1
if salary2 < salary1 and salary2> salary3:
  minimum = salary2
if salary3 < salary1 and salary3 > salary2:
  minimum = salary3

print(maximum-minimum)

"""
*Boring Numbers * A natural number is said to be boring if all its digits are the same. Determine if the given number is boring.

"""
boring_number = int(input())
lst = []

while boring_number > 0:
  digit = boring_number % 10
  boring_number //= 10
  lst.append(digit)

  
#for i in range(1,len(lst)):
if lst.count(lst[0]) == len(lst):
    print("Boring")
else:
    print("Interesting")
   
"""
*Largest Number * You are given a natural number. If it is possible to rearrange/ shuffle its digits and get a larger number than the one you started with, output “Yes”. Otherwise, output “No”. For example, given 3112 you can rearrange the digits and get 3211, which is larger than 3112, hence the answer is Yes. In contrast, no matter how you rearrange the digits of 987, you will not be able to get a larger number, hence the answer for 987 should be No.
"""

nat_number = int(input())

lst = []

while nat_number > 0:
  digit = nat_number % 10
  nat_number //= 10
  lst.append(digit)

is_descending = True

for i in range(1,len(lst)):
  if lst[i] < lst[i-1]:
    is_descending = False

if is_descending:
  print("No")
else:
  print("Yes")
  
 """
 Line Segment Intersection
 """

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 > b1:
  lower_line1 = b1
  upper_line1 = a1
else:
  lower_line1 = a1
  upper_line1 = b1

if a2 > b2:
  lower_line2 = b2
  upper_line2 = a2
else:
  lower_line2 = a2
  upper_line2 = b2

if lower_line1 > lower_line2 and upper_line2 > lower_line1 and upper_line1 > upper_line2:
  intersection = upper_line2 - lower_line1
  print(intersection)
if lower_line1 > lower_line2 and upper_line1 < upper_line2:
  intersection = Upper_line1 - lower_line1
  print(intersection)
if lower_line1 < lower_line2 and upper_line1 > upper_line2:
  intersection = upper_line2 - lower_line2
  print(intersection)
if lower_line1 < lower_line2 and upper_line1 > lower_line2 and upper_line1 < upper_line2:
  intersection = upper_line1 - lower_line2
  print(intersection)
else:
  print("There is no intersection") 
 
#Number of Divisors

x = int(input())

x > 0

divisors = 0
for y in range(1,x+1):
  if x%y == 0:
    divisors += 1

print(divisors)


#Quadratic Equation
#ax**2 + bx + c = 0

a = float(input())
b = float(input())
c = float(input())

D = b * b - 4 * a * c

if a == 0:
  print("Non-quadratic equation")
else:
  print("Quadratic equation")
  print("Discriminant: ", D)

x1 = (-b + D ** 0.5)/(2 * a)
x2 = (-b - D ** 0.5)/(2 * a)

print(x1)
print(x2)
#print("Infinite Solutions")

if a * x1 * x1 + b * x1 + c == 0 and a * x2 * x2 + b * x2 + c == 0:
  print("Two Solutions:",x1, x2)
elif a * x1 * x1 + b * x1 + c == 0 and a * x2 * x2 + b * x2 + c != 0:
  print("One Solution:",x1)
elif a * x1 * x1 + b * x1 + c != 0 and a * x2 * x2 + b * x2 + c == 0:
  print("One Solution:",x2)
elif a * x1 * x1 + b * x1 + c != 0 and a * x2 * x2 + b * x2 + c != 0:
  print("No Solutions")
  
  # Convert a list of characters into a string

lst = ['a','b','c','d']

str1 = ''
for i in range(len(lst)):
  str1 += lst[i]

print(str1)

#find the second smallest number in the list

n = int(input())

lst = []

for _ in range(n):
 lst.append(int(input()))

#lst.sort(reverse=True)

for i in range(n):
  for j in range(i+1, n):
   if lst[i] < lst[j]:
    lst[i], lst[j] = lst[j], lst[i]
    
lst.reverse()

print(lst[1])
