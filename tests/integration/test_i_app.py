import os
import subprocess

def test_system_integration_message(capsys):
    # expectedOutput = '[\'python3\', \'/home/svishal/git-repos/generate_payslip/plutus/generate_monthly_payslip/app.py\', \'-efn\', \'Mary Song\', \'-gas\', \'60000\']\nMonthly Payslip for: "Mary Song"\r\nGross Monthly Income: $5000\r\nMonthly Income Tax: $500\r\nNet Monthly Income: $4500'
    expectedOutput = '''['python3', '/home/svishal/git-repos/generate_payslip/plutus/generate_monthly_payslip/app.py', '-efn', 'Mary Song', '-gas', '60000']
Monthly Payslip for: "Mary Song"
Gross Monthly Income: $5000
Monthly Income Tax: $500
Net Monthly Income: $4500'''
    testCmd = ["python3", os.getcwd() + '/generate_monthly_payslip/app.py', "-efn", "Mary Song", "-gas", "60000"]
    print(testCmd)
    encoding = 'utf-8'
    result = subprocess.check_output(testCmd).decode(encoding)
    print(result)
    captured = capsys.readouterr()
    realOutput = captured.out.rstrip()
    print(captured)
    print(os.getcwd())
    print('captured out is:')
    print(realOutput)
    print('expected out is:')
    print(expectedOutput)
    assert realOutput == expectedOutput, 'Expected output not observed. Integration test failed.'
