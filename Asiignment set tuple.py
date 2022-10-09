'''

#3) x=[1,4,5,3,1,4] reverse the list and remove the dulicates using set ?
x=[1,4,5,3,1,4]
y=list(reversed(x))
z=set(y)
print(y)
print(z)



#4. take two sets get unique values from set ?
x={10,20,30,40}
y={30,40,50,60}
print(x.symmetric_difference(y))


#5. how to concatinate two sets ? write an example?
#The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)


#6. write a program to get  common elements from  two sets ?
x={10,20,30,40}
y={30,40,50,60}
print(x.intersection(y))


#7. write a example for tuple comprehension ?
x  = (10,6,45,89,90,1,225,76)
tuple1 = tuple((i for i in x if i % 5 == 0))
tuple2 = tuple([i for i in x if i%5 == 0])
tuple3 = (i for i in x if i%5 == 0),
print(tuple1,  type(tuple1))
print(tuple2,  type(tuple2))
print(tuple3,  type(tuple3))



#8.x=[6,3,2,5,1]  sort the list elements without using sort function ? op : [1,2,3,5,6]
x=[6,3,2,5,1]
for i in range(len(x)):
  for j in range(i + 1, len(x)):
      if x[i] > x[j]:
        x[i],x[j] = x[j],x[i]
print(x)


#9. write a program to change tuple values using list ?
x = (10, 28,'python')
print(x,type(x))
y = list(x)
print(y,type(y))
y[-1]='java'
z=tuple(y)
print(z,type(z))


#10.print the multiplication table using loops -> input should b taken from keyboard ?

num = int(input("Display multiplication table of= "))
for i in range(1, 21):
   print(num, 'x', i, '=', num*i)

'''






