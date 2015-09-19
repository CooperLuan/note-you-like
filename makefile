start:
	uwsgi --ini uwsgi-conf.ini

reload:
	kill -HUP `cat uwsgi.pid`
	uwsgi --reload uwsgi.pid

stop:
	uwsgi --stop uwsgi.pid
