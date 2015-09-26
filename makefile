start:
	echo `grep "http-socket" uwsgi-conf.ini`
	uwsgi --ini uwsgi-conf.ini

reload:
	kill -HUP `cat uwsgi.pid`
	uwsgi --reload uwsgi.pid

stop:
	uwsgi --stop uwsgi.pid
