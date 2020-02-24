class Employee:
    def __init__(self, fullName, grossMonthlySalary, netMonthlyTaxPayable, netMonthlySalary):
        self.__employeeFullName = fullName
        self.__employeeGrossMonthlySalary = grossMonthlySalary
        self.__employeeNetMonthlyTaxPayable = netMonthlyTaxPayable
        self.__employeeNetMonthlySalary = netMonthlySalary

    def PrintEmployeePayslip(self):
        payslipOutputMessage = 'Monthly Payslip for: "' + self.__employeeFullName + '"\n'
        payslipOutputMessage += 'Gross Monthly Income: $' + str(self.__employeeGrossMonthlySalary) + '\n'
        payslipOutputMessage += 'Monthly Income Tax: $' + str(self.__employeeNetMonthlyTaxPayable) + '\n'
        payslipOutputMessage += 'Net Monthly Income: $' + str(self.__employeeNetMonthlySalary)
        print(payslipOutputMessage)
        return payslipOutputMessage
