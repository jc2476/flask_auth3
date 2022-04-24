import os

def test_debug_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    debugLog = os.path.join(root, '../app/logs/debugs.log')
    assert os.path.exists(debugLog) == True

def test_error_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    errorLog = os.path.join(root, '../app/logs/errors.log')
    assert os.path.exists(errorLog) == True

def test_flask_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    flaskLog = os.path.join(root, '../app/logs/flask.log')
    assert os.path.exists(flaskLog) == True

def test_info_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    infoLog = os.path.join(root, '../app/logs/info.log')
    assert os.path.exists(infoLog) == True

def test_myapp_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    myappLog = os.path.join(root, '../app/logs/myapp.log')
    assert os.path.exists(myappLog) == True

def test_requests_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    requestsLog = os.path.join(root, '../app/logs/requests.log')
    assert os.path.exists(requestsLog) == True

def test_sqlalchemy_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    sqlalchemyLog = os.path.join(root, '../app/logs/sqlalchemy.log')
    assert os.path.exists(sqlalchemyLog) == True

def test_werkzeug_logfiles():
    root = os.path.dirname(os.path.abspath(__file__))
    werkzeugLog = os.path.join(root, '../app/logs/werkzeug.log')
    assert os.path.exists(werkzeugLog) == True
