# Make program do Pythagorean formula

from math import sqrt
from banner import banner
banner("PYTHAGOREAN CALCULATOR","Skyler P")

print("Do you need help with your Pythagorean questions well look no further i am here to help. The lengths of the two legs are 'a' and 'b', and the length of the hypotenuse is 'c'.")
print("")


formula = input("Which side (a,b,c) do you wish to calculate: ")

if formula == "c":
    side_a = int(input("input the length of side a: "))
    side_b = int(input("input the length of side b: "))

    side_c = sqrt(side_a * side_a + side_b * side_b)

    print("Your missing side is c and it's length is:")
    print(side_c)


elif formula == "a":
    side_b = int(input("input the length of side b: "))
    side_c = int(input("input the length of side c: "))

    side_a = sqrt((side_c * side_c) - (side_b * side_b))

    print("Your missing side is a and it's length is:")
    print(side_a)



elif formula == "b":
    side_a = int(input("input the length of side a: "))
    side_c = int(input("input the length of side c: "))

    side_b = sqrt(side_c * side_c - side_a * side_a)

    print("Your missing side is b and it's length is:")
    print(side_b)


else:
    print("Please select a side between a,b,c")


