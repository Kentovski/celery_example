CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'yaml']

CELERY_RESULT_BACKEND = 'amqp'
BROKER_URL = 'amqp://guest:guest@localhost:5672//'

AMQP_SERVER = "127.0.0.1"
AMQP_PORT = 5672
AMQP_USER = "guest"
AMQP_PASSWORD = "guest"
AMQP_VHOST = "/"

CELERY_INCLUDE = ('tasks',)
