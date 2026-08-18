g=input("enter gendre : ")

if g=="f":
    print(" ticket free")
elif g=="" or g!="m":
    print("enter proper gender")
else:
    age=int(input("enter age : "))

    if age<5:
        print("ticket free")
    elif age<12:
        print(" ticket is half price")
    elif age >60:
        p=input("wheather passanger is friend of conducter : ")
        if p=="yes":
            print("ticket free")
        else:
            print("ticker half proce bcoz senior citizon")

    else:
        print("pay full price")