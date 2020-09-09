import sys
sys.path.insert(0, '/var/www/awscloud/')
from book import app as application
application.debug = True
