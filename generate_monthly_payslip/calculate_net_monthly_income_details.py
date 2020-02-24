def CalculateNetMonthlyIncome(grossMonthlyIncome,netMonthlyTax):
    return int(grossMonthlyIncome-netMonthlyTax)

def CalculateGrossMonthlyIncome(grossAnnualIncome):
    return int(grossAnnualIncome/12)

def CalculateNetMonthlyTax(annualTaxToBePaid):
    return int(annualTaxToBePaid/12)

def SalaryDetails(grossAnnualIncome,annualTaxToBePaid):
    grossMonthlySalary=CalculateGrossMonthlyIncome(grossAnnualIncome)
    monthlyTaxPayable=CalculateNetMonthlyTax(annualTaxToBePaid)
    netMonthlySalary=CalculateNetMonthlyIncome(grossMonthlySalary,monthlyTaxPayable)
    return grossMonthlySalary,monthlyTaxPayable,netMonthlySalary
