import argparse
import logging
try:
    from calculate_annual_tax import GetAnnualTax
except ModuleNotFoundError:
    from generate_monthly_payslip.calculate_annual_tax import GetAnnualTax
try:
    from calculate_net_monthly_income_details import SalaryDetails
except ModuleNotFoundError:
    from generate_monthly_payslip.calculate_net_monthly_income_details import SalaryDetails
try:
    from print_employee_monthly_payslip import Employee
except ModuleNotFoundError:
    from generate_monthly_payslip.print_employee_monthly_payslip import Employee
try:
    import logging_config
except ModuleNotFoundError:
    import generate_monthly_payslip.logging_config


log = logging.getLogger('generate_monthly_payslip.app')
# log.setLevel('INFO')

def GetEmployeeAnnualTax(grossAnnualSalary):
    return GetAnnualTax(grossAnnualSalary)

def GetEmployeeMonthlyIncomeDetails(grossAnnualSalary, annualTaxToBePaid):
    return SalaryDetails(grossAnnualSalary, annualTaxToBePaid)

def ValidateConvertAnnualSalary(grossAnnualSalary):
    assert isinstance(int(grossAnnualSalary), int), 'Gross Annual Salary is not int'
    grossAnnualSalaryInt = int(grossAnnualSalary)
    assert grossAnnualSalaryInt >= 0, 'Gross Annual Salary cannot be less than 0'
    return grossAnnualSalaryInt

def ValidateName(fullName):
    for name in fullName.split(' '):
        assert name.isalpha(), 'Name can contain only alphabets and spaces'

def Run(employeeFullName, grossAnnualSalaryInput):
    log.debug('Validating name')
    ValidateName(employeeFullName)
    log.debug('Validating gross annual salary')
    grossAnnualSalary = ValidateConvertAnnualSalary(grossAnnualSalaryInput)
    log.debug('Calculating Annual tax payable')
    annualTaxPayable = GetEmployeeAnnualTax(grossAnnualSalary)
    log.debug('Calculating Salary details for 1 month')
    grossMonthlySalary, monthlyTaxPayable, netMonthlySalary = SalaryDetails(grossAnnualSalary, annualTaxPayable)
    log.debug('Instantiating Employee object')
    employeeSelected = Employee(employeeFullName, grossMonthlySalary, monthlyTaxPayable, netMonthlySalary)
    log.debug('Printing Payslip')
    return employeeSelected.PrintEmployeePayslip()

if __name__ == '__main__':
    log.info('Welcome to the world of "Plutus". Starting payslip generator application.')
    parser = argparse.ArgumentParser(description='Generate Payslip for an employee')
    parser.add_argument('--employee-full-name', '-efn', required=True, dest='employeeFullName', help='Full name of employee')
    parser.add_argument('--gross-annual-salary', '-gas', required=True, dest='grossAnnualSalary', help='gross annual salary of employee')
    log.debug('Parsing parameters')
    args = parser.parse_args()
    Run(args.employeeFullName, args.grossAnnualSalary)
