#  lists are the storage to store a set of any dat types
friends=["apple","lists",0.2,9,False]
# print(friends[2],',',friends[4])

L1=[1,23,34,2,24,12,14,53,4,]
# operations using list functions
#.sort() for sorting the whole list 
L1.sort() #pehle func then  as string ke jese nahi like string new bnti thi after function  ,ushi list me conversion ho jayege
print(L1)

# append function add element at the end of the list 
friends.append("Append ho gyi re ")
print(friends)

friends.clear()
print("clear function ke baad list: ",friends)

L1.reverse()
print(L1) #yha pe list reverese ho gyi like (67,15,4,4,53,14,12,24,2,34 and more)\

friends.insert(2,3) # (jaha insert karna ha ,kya insert krna ha )
print(friends)

# pop function mein delete element at index _ and return its value 
L1.pop(2)
print(L1)


