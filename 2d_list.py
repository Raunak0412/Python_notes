# # 2D list is the list of multiple lists 

# fruits=["Apple" , "Guava" , "Banana" ]

# vegetables=['Peas' , 'Chilli' , 'Potato' ]

# meats=['Chicken' , 'Turkey' , 'Chicken' ]

# groceries=[ fruits , vegetables , meats ]


# # print(groceries)   # it will print all lists as a single list in linear form that didn't look alike a 2d list.

# for collections  in groceries:
#     for food in collections:
#         print( food ,end=" ")
#     print()



# print a num pad

num_pad = ((1 , 2 , 3),
            (4 , 5 , 6),
            (7 , 8 , 9),
           ("*" , 0 , "#") )
for row in num_pad :
    for num in row :
        print(num,end=" ")
    print() 




     