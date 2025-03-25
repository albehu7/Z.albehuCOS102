def simple_interest(p, r, t):
    a = p * (1 + (r/100) * t)
    return a

def compound_interest(p, r, n, t):
    a = p * (1 + r/n ) ** n * t
    return a

def annuity_plan(pmt, r, t, n):
    a =  pmt * ((1 + r/n) ** n * t - 1) / (r/n)
    return a

p = float(input("Enter Principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time in years: "))
n = int(input("Enter number of times interest is compounded per year: "))
pmt = float(input("Enter periodic payments for annuity plan: "))

print("Simple interest: ", simple_interest(p, r, t))
print("compound interest: ", compound_interest(p,r,n, t))
print("Annuity plan: ", annuity_plan(pmt, r, t, n))
