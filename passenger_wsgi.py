import os, sys
sys.path.insert(0, '/home/b/bcrhf2xx/bcrhf2xx.beget.tech/coolsite')
sys.path.insert(1, 'home/b/bcrhf2xx/bcrhf2xx.beget.tech/djangodev/lib/python3.11/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'coolsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()