email=input("Enter ur email:")
index=email.index("@")

username= email[:index]
domain=email[index:]

print("Username=",username)
print("domain=",domain)
