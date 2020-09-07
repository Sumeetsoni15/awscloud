import sys
sys.path.insert(0, '/var/www/ProjectBook/')
from book import app as application
application.debug = True
