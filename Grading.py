pos = int(input("What is the maximum points possible?"))
got = int(input("What did the student get?"))

per = (got / pos * 100)
round_per = round(per, 2)
print ("The student got a " + str(round_per) + " Percent")
if per >= 89:
    print("The student got an A")
if per >= 76 and per <= 88:
    print("The student got an B")
if per >= 61 and per <= 75:
    print("The student got an C")
if per >= 51 and per <= 60:
    print("The student got an D")
if per < 60:
    print("The student got an F")
