
import random
import sys
import os


print("Hello World")

name = ("Christine")
print(name)
name = 15

print("5 + 2 =", 5+2)
print("5-2 =", 5-2)
print("5*2 =", 5*2)
print("5/2 =", 5/2)
print("5%2 =", 5%2)
print("5**2 =", 5**2)

quote = "\"Always remember you are unique"

multi_line_quote = ''' just
like everyone else'''

print("%s %s %s " % ('i like the quite',quote,multi_line_quote))

grocery_list =['Juice', 'Tomatoes', 'Potatoes',
               'Bananas']

print('First Item',grocery_list[0])

grocery_list[0] = "Green Juice"
print('First Item', grocery_list[0])

print(grocery_list[1:3])

other_events = ['Wash Car', 'Pick Up Kids',
                'Cash Check']

to_do_list = [other_events, grocery_list]
print(to_do_list)

print((to_do_list[1][1]))

grocery_list.append('Onions')
print(to_do_list)

grocery_list.insert(1, "Pickle")

grocery_list.remove("Pickle")

grocery_list.sort()

grocery_list.reverse()

del grocery_list[4]
print(to_do_list)

to_do_list2 = other_events + grocery_list

print(len(to_do_list2))
print(max(to_do_list2))
print(min(to_do_list2))

super_villains = {'Fiddler' : 'Isaac Bowin',
                  'Captain Cold' : 'Leonard Snart',
                  'Weather Wizard' : 'Mark Mardon',
                  'Mirror Master' : 'Sam Scudder',
                  'Pied Piper' : 'Thomas Peterson'}
                  
print(super_villains['Captain Cold'])

del super_villains['Fiddler']

super_villains['Pied Piper'] = 'Hartley Rathaway'

print (len(super_villains))

print(super_villains.get("Pied Piper"))

print(super_villains.keys())

print(super_villains.values())



age = 21

if age > 16 :
    print('You are old enough to drive')
else :
    print('You are not old enough to drive')
    
if age >= 21 :
    print('You are old enough to drive a tractor trailer')
elif age >=16:
    print('You are old enough to drive a car')
else :
    print('You asre not old enough to drive')
    


if ((age >= 1) and (age <=18)):
    print("You get a birthday")
elif (age ==21) or (age >=65):
    print("You get a birthday")
elif not(age == 30):
    print("You don't get a birthday")
else:
    print("You get a birthday party yeah")

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") 
queue.append("Graham")
queue.popleft()
queue.popleft()
print(queue)

        
