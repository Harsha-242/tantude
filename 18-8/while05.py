pin="1234"
attempts=0

while attempts<3:
    input_pin = input("pin : ")

    if input_pin ==  pin:

        print("correct")
        break

    else:
        print("incorrect")
        attempts += 1

else:
    print("please try after sime time")
