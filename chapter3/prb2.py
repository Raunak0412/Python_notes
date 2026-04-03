# write a prg to fill in a letter template using replace function
letter='''Dear <|Name|>,\nYou are selected!\n<|Date|>'''
A=letter.replace("<|Name|>","Raunak").replace("<|Date|>","12|04|05")
print(A)


