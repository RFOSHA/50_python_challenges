# A school has asked you to write a program that will calculate
# teachers' salaries. The program should ask the user to enter the
# teacher’s name, the number of periods taught in a month, and
# the rate per period. The monthly salary is calculated by
# multiplying the number of periods by the monthly rate. The
# current monthly rate per period is $20. If a teacher has more than
# 100 periods in a month, everything above 100 is overtime.
# Overtime is $25 per period. For example, if a teacher has taught
# 105 periods, their gross monthly salary should be $2,125. Write
# a function called "your_salary" that calculates a teacher’s gross
# salary. The function should return the teacher’s name, periods
# taught, and gross salary. Here is how you should format your
# output:
# Teacher: John Kelly,
# Periods: 105
# Gross salary:2,125


def your_salary():
    name = input("enter your name: ")
    num_periods = int(input("enter the number periods you worked: "))
    if num_periods - 100 > 0:
        extra_periods = num_periods - 100
    else:
        extra_periods = 0

    salary = (extra_periods * 25) + ((num_periods - extra_periods) * 20)

    return(name, num_periods, salary)

answer = your_salary()
print(answer)
