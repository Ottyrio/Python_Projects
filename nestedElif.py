Smith = float(input("Enter Smith's age: "))
Rio =  float(input("Enter Rio's age; "))
Ellah = float(input("Enter Ellah's age; "))
if Smith > Rio and Smith > Ellah:
    print("Smith is the eldest")
else:
    if Rio > Ellah:
        print("Rio is the eldest")
    else:
        print("Ellah is the eldest")