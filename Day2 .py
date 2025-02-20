#Building a tip calculator
print("Welcome to the tip calculator!")
bill=float(input("what is the total bill? ksh"))
tip=int(input("how much tip will you give?"))
person=int(input("how many people will split the bill?"))
tip_as_percent=tip / 100
total_tip_amount=bill + tip_as_percent
total_bill=bill + total_tip_amount
bill_per_person=total_bill / person
final_bill=round(bill_per_person ,2)# round function to make the number number to 2 nearest wholest number
print(f"The final bill is : ksh{final_bill}")#f string command to combine the string without using a + sign


