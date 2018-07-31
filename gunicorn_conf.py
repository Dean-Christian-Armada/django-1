bind = '0.0.0.0:8000'
loglevel = 'debug'
errorlog = '-'
accesslog = '-'
# the formula is based on the assumption that for a given core, one worker
# will be reading or writing from the socket while the other worker is
# processing a request.
workers = 2
preload = True
reload = True
worker_class = 'gevent'  # async type worker, so the app can handle a stream of requests in parallel
