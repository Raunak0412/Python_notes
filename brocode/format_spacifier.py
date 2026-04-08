price1=3.1321
price2=-987.65
price3=11212.341

print(f"price 1 is:{price1:.2f}") # so here in {value:flags} format a value based on things are inserted we use [.f] to round up the decimal 

# to allocate spce  we k=just add the value of space needed to show that value 

print(f'price 2 is: {price2:10}') #o\p will be in 10 spaces 

#  now if we want zero padded we just add 0 before 10

print(f'price 3 is:{price3:010}')

# justify the text 

print(f"price 3 is:{price3:>10}")

print(f"price 3 is:{price3:<10}")

print(f"price 3 is: {price3:^}")

#  to show +ive sign in this 
print(f"price 3 is:{price3:+}")


# all flags at the same syntax 
print(f"price 3 is:{price3:+,.2f}")

