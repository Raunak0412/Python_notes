t1=(1,2,3,6,5,7)
print(t1[0])#access the value at index 0 
print(t1[2])#access the value at index 2

# here we can't change the valu of tuple as if at tup [2]=3 to we canat change that 
# t1[1]=4  

# creating empty tuple
tup=()
print(tup)
# creating a single element tuple 
tup1=(1,) # we add coma after element if there is only single element 
print(tup1)
print(type(tup1)) # printing the type of tuple 

# slicing in tuple is same as string or list

print(t1[2:5]) # here the index values from 2 to 5 will be printed of tuple t1=(1,2,3,6,5,7) i.e, 3,6,5

# now usong tuple methods 
#  1st- index method (return the index of first occurence of the element)

tup2=(1,2,1,2,3,4,4,4,5,5,6,3)
v=tup2.index(2)
print("number 2 first occurence at which index : ",v)

print("number 4 first occurence at which index : ",tup2.index(4))

# 2nd- count method (count the occurence of element in tuple)
print(tup.count(4)) 
print(tup2.count(4))