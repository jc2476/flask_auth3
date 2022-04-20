import datetime
import os
from os import getenv

def test_context_variables_environment(client):
    """This test checks if the environment is printed"""
    response = client.get("/")
    env = getenv('FLASK_ENV', None)
    test_string = f"Environment: {env}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

def test_context_variables_year(client):
    """This tests checks if the copyright and current year are printed"""
    response = client.get("/")
    current_date_time = datetime.datetime.now()
    date = current_date_time.date()
    year = date.strftime("%Y")
    test_string = f"Copyright: {year}"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

def test_context_currency_format(client):
    """This tests checks if the copyright and current year are printed"""
    response = client.get("/")
    test_string = f"$100"
    content = bytes(test_string, 'utf-8')
    assert response.status_code == 200
    assert content in response.data

root = os.path.dirname(os.path.abspath(__file__))
logdir = os.path.join(root, '../app/logs')

def debug_log_test():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/debugs.log')
    assert os.path.exists(logfile) is True