from ...generate_monthly_payslip.calculate_annual_tax import  GetAnnualTax as GetAnnualTax
from ...generate_monthly_payslip.read_tax_slab import  ReadTaxFile as ReadTaxFile
from ...generate_monthly_payslip.calculate_net_monthly_income_details import SalaryDetails
from ...generate_monthly_payslip.print_employee_monthly_payslip import Employee
import os

def test_calculate_tax():
    assert GetAnnualTax(60000) == 6000, 'Tax calculation not correct'

def test_read_static_tax_file():
    maxSlabAnnualIncome, maxSlabTaxRate, tax_slab_rate_list = ReadTaxFile()
    assert maxSlabAnnualIncome == 180000, 'Maximum Tax Slab annual income not correct'
    assert maxSlabTaxRate == 40, 'Maximum Tax Slab annual income not correct'
    assert tax_slab_rate_list == [[0, 20000, 0], [20000, 40000, 10], [40000, 80000, 20], [80000, 180000, 30]] , 'Tax Slab rate is not correct'

def test_calculate_salary_details():
    grossMonthlySalary, monthlyTaxPayable, netMonthlySalary=SalaryDetails(60000,6000)
    assert grossMonthlySalary == 5000, 'Gross monthly income not calculated correctly'
    assert monthlyTaxPayable == 500, 'Monthly tax payable not calculated correctly'
    assert netMonthlySalary == 4500, 'Net monthly salary not calculated correctly'

def test_print_employee_monthly_payslip():
    employeeSelected = Employee('Mary Song',5000,500,4500)
    employeeSelected.PrintEmployeePayslip()
    expectedOutput = 'Monthly Payslip for: "Mary Song"\nGross Monthly Income: $5000\nMonthly Income Tax: $500\nNet Monthly Income: $4500'
    assert employeeSelected.PrintEmployeePayslip() == expectedOutput , 'Payslip output is not matching as expected'

def test_tax_slab_file_exists():
    assert os.path.isfile(os.getcwd() + '\\generate_monthly_payslip\\static_input\\tax_slab.csv'),'Tax slab file does not exists in specified folder'