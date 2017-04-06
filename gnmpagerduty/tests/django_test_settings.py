import os
BASE_DIR = "/tmp"
SECRET_KEY = 'v7j%&)-4$(p&tn1izbm0&#owgxu@w#%!*xn&f^^)+o98jxprbe'
INSTALLED_APPS = ['gnmpagerduty','south']
ROOT_URLCONF = 'gnmpagerduty.urls'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'djangotestdb.sqlite3'),
    }
}

VIDISPINE_URL="http://localhost"
VIDISPINE_PORT=8080
VIDISPINE_USERNAME="fakeuser"
VIDISPINE_PASSWORD="fakepassword"

PAGERDUTY_KEY="blahblahblahblah"