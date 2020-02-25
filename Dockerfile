FROM python:3.6

RUN pip install pipenv

WORKDIR /app
COPY Pipfile Pipfile.lock setup.cfg /app/
COPY go.sh /app/go.sh
COPY scripts /app/scripts
RUN ./go.sh setup

COPY generate_monthly_payslip /app/generate_monthly_payslip
COPY tests /app/tests

CMD ./go.sh run