first_number = int(input("Enter First Number: "))
second_number = int(input("Enter Second Number: "))
third_number = int(input("Enter Third Number: "))
if first_number > second_number and first_number > third_number:
    print("First Number is at First Position.")
    if second_number > third_number:
      print("Second Number is at Second Position")
      print("Third number is at Third Position")
    else:
      print("Second Number is at Third Position.")
      print("Third Number is at Second Position.")
if second_number > first_number and second_number > third_number:
    print("Second Number is at First Position")
    if first_number > third_number:
        print("First Number is at Second Position.")
        print("Third Number is at Third Position")
    else:
       print("First Number is at Third Position")
       print("Third Number is at Second Position")

elif third_number > first_number and third_number > second_number :
    print("Third Numbe is at First position")
    if first_number > second_number:
        print("First Number is at Second Positionn")
        print("Second number is at Third Position")
    else:
        print("First number is at Thid Position")
        print("Second Number is at Second Position")
