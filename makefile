start:
	echo `grep "http-socket" uwsgi-conf.ini`
	export NYL_MONGO_URL=mongodb://127.1:27017/nyl
	export NYL_REDIS_URL=redis://:@127.1:6379/5
	uwsgi --ini uwsgi-conf.ini

reload:
	kill -HUP `cat uwsgi.pid`
	export NYL_MONGO_URL=mongodb://127.1:27017/nyl
	export NYL_REDIS_URL=redis://:@127.1:6379/5
	uwsgi --reload uwsgi.pid

stop:
	uwsgi --stop uwsgi.pid
