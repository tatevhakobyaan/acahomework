#*P1 *

#Given a list, find value 20 in the list, replace it with 200. Only update the first occurrence of a value.

lst1 = [5,   10,   15,   20,   25,   50,   20] 

a = lst1.index(20)

lst1.pop(a)

lst1.insert(a, 200)

print(lst1)


#*P2 * 
#Given a list, remove the first occurrence of 20 from the list.

lst2 = [5,   20,   15,   20,   25,   50,   20] 

b = lst2.index(20)

lst2.pop(b)

print(lst2)

#*P3 * 
#Given a list, print the second largest element.

lst3 = [5,   20,   15,   20,   25,   50,   20] 

lst3.sort(reverse=True)

print(lst3[1])

#*P4 * 
#Given 3 dictionaries, create a new dictionary, which contains all of them. 

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50, 6:60}

dic4 = dic1

dic4.update(dic2)

dic4.update(dic3)

print(dic4)

#*P5 * 
#Given a dictionary, remove the given key.

dic5 = {'a': 1, 'b': 2, 'c': 3,'d': 4}

dic5.pop('a')

print(dic5)

#P6
#Given a set, check if the given number exists.

s   =   {1,   10,   90,   9}  

90 in s 

#P7
#For a given n, create a list (using loops, or list comprehension), which contains all natural numbers less or equal n divisible by 7.



n = int(input())

lst4 = []

for i in range(1,n+1):
 if i%7 == 0:
  lst4.append(i)

print(lst4)



