# note-you-like

## uwsgi

```sh
uwsgi --ini uwsgi-conf.ini
```

restart uwsgi gracefully

```sh
# using kill to send the signal
kill -HUP `cat uwsgi.pid`
# or the convenience option --reload
uwsgi --reload uwsgi.pid
```

stop

```sh
uwsgi --stop uwsgi.pid
```
