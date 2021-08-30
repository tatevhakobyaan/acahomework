#Index Sum

n = int(input())

A = []

for _ in range(n):
 A.append(float(input()))

m = int(input())

IND = []

for _ in range(m):
 IND.append(int(input()))

def sum_a(A):
  suma = 0
  for el in IND:
   suma += A[el]
  print(suma)
sum_a(A)


#The most divisor-rich number

a = int(input())

b = int(input())

a <= b

lst = []

for c in range(a,b+1):
 lst.append(c)


def number_of_divisors(x):
  divisors = 0
  for d in range(1,x+1):
    if x%d == 0:
        divisors += 1
  return divisors


def maximum_divisors(lst):
    result = lst[0]
    for n in lst[1:]: # start in 1 because 0 is already in result
        if number_of_divisors(n) > number_of_divisors(result):
            result = n
    return result 

print(maximum_divisors(lst))


#draw the * Tree with the given base width


#n=5;
def right_text(n):
 for i in range(1,n+1,2):
    print('')
    for j in range(i):
        print ('* ', end="")
    print('')

print(right_text(5))

#def reverse_text


#The Goldbach Conjecture

n = int(input())

def check_prime_argument(x):
  res = False
  if x > 2:
    for i in range(2, x):
      if (x % i) == 0:
        res = False
        break
      else:
        res = True
  if x == 2:
    res = True
  return res

def two_prime_numbers(y):
  for i in range(2,y):
    if check_prime_argument(i) == True:
      result = y - i
      if check_prime_argument(result) == True:
        return i, result
print(two_prime_numbers(n))


a = int(input())
b = int(input())

for num in range(a, b + 1):
    temp = num
    reverse = 0

    while(temp > 0):
        reminder = temp % 10
        reverse = (reverse * 10) + reminder
        temp = temp //10

    if(num == reverse):
        print(num, end = ' ')

#Suffix Sums

n = int(input())

A = []

for _ in range(n):
 A.append(float(input()))

B = []

def suffix_sums(i):
    sumi = 0
    for j in range(i,len(A)):
      sumi += A[j]
    return sumi

for num in range(len(A)):
  B.append((suffix_sums(num)))

print(B)







