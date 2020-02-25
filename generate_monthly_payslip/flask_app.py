import flask
from flask import request
from app import Run as PayslipApp

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Plutus</h1>
<p>Generate payslip for an employee.</p>'''

@app.errorhandler(404)
def PageNotFound(): #changed PageNotFound(e) to PageNotFound()
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/employee', methods=['GET'])
def GetEmployeeMonthlyPayslip():
    employeeInputs = request.args
    employeeFullName = employeeInputs.get('fullName').replace('%20', ' ')
    grossAnnualIncome = employeeInputs.get('grossAnnualIncome')
    employeePayslip = PayslipApp(employeeFullName, grossAnnualIncome)
    print('\n')
    return employeePayslip + '\n'

app.run()
