first=int(input("введите число"))
second=int(input("введите число"))
third=int(input("введите число"))
if first == second != third or first == third != second or second == third != first:
    print(2)
elif first==second==third:
    print(3)
else:
    print(0)
