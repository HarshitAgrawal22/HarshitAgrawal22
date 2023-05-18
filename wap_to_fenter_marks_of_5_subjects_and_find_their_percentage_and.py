physics_marks=int(input("enter physics marks out of 100: "))
chem_marks=int(input("enter chemistry marks out of 100: "))
bio_marks=int(input("enter biology marks out of 100: "))
maths_marks=int(input("enter maths marks out of 100: "))
computer_marks=int(input("enter computer marks out of 100: "))
sum_marks=physics_marks+chem_marks+bio_marks+maths_marks+computer_marks
total_marks=500
percentage=(total_marks/500)*100
if percentage>=90:
    print("GRADE A")
elif  (percentage>=80 and percentage<90):
    print("GRADE B")
elif (percentage>=70 and percentage<80):
    print("GRADE C")
elif (percentage>=60 and percentage<70):
    print("GRADE D")
elif (percentage>=40 and percentage<60):
    print("GRADE E")
else:
    print("GRADE F")