s2=input("Enter String - ")
s2.capitalize()
print(s2)

s='am'
print(s2.count(s))
print(s2.find(s))

s2.strip()
print(s2)

#Case Sensitive Comparison
if s2==s2[::-1]:
    print(s2, "is a pallindrome")
else:
    print(s2, "is not a pallindrome")

#Case Insensitive Comparison

if s2.upper()==s2[::-1].upper():
    print("Pallindrome")

else:
    print("Not One")
