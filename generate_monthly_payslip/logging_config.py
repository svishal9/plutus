import logging
import os

log_level = os.environ.get('LOGGING_LEVEL', 'INFO')
logging.basicConfig(level=logging.__dict__[log_level])
logging.getLogger('generate_monthly_payslip').setLevel(logging.__dict__[log_level])
