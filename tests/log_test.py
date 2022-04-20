import os

root = os.path.dirname(os.path.abspath(__file__))
logdir = os.path.join(root, '../app/logs')

def debug_log_test():
    assert os.path.exists(logdir) is True
    logfile = os.path.join(root, '../app/logs/debugs.log')
    assert os.path.exists(logfile) is True
