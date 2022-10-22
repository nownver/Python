
name = input("Enter employee's name: ")
week_hour = int(input("Enter number of hours worked in a week: "))
pay_rate = float(input("Enter hourly pay rate: "))
federal_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

gross_pay = float(week_hour * pay_rate)
deduct_federal = gross_pay * federal_tax
deduct_state  = gross_pay * state_tax
format_deduct_federal = "{:.1f}".format(deduct_federal)
format_deduct_state = "{:.2f}".format(deduct_state)

deductions = float(format_deduct_federal) + float(format_deduct_state)

print("")
print(f"Employee's name: {name}")
print(f"Hourly Worked: {float(week_hour)}")
print(f"Pay Rate: ${pay_rate}")
print(f"Gross Pay: ${gross_pay}")
print("Deductions:")
print(f"    Federal Withholding({federal_tax * 100}%) : ${format_deduct_federal}")
print(f"    State Withholding({state_tax * 100}%) : ${format_deduct_state}")
print(f"    Total Deduction : ${deductions}")
print(f"Net Pay : ${gross_pay - deductions}")