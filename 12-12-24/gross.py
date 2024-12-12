def gross_salary(basic):
    hra = 0
    da = 0
    if basic < 10000:
        hra = basic * 0.67
        da = basic * 0.73
    elif 10000 <= basic <= 20000:
        hra = basic * 0.69
        da = basic * 0.76
    else:
        hra = basic * 0.73
        da = basic * 0.89
    gs = hra + da + basic
    return gs

basic = int(input("Enter your basic salary: "))
print("The gross salary is:")
print(gross_salary(basic))
