import multiprocessing

bind = "0.0.0.0:5000"
workers = max(2, multiprocessing.cpu_count() // 2)
worker_class = "gthread"
threads = 4
timeout = 120
keepalive = 5
accesslog = "-"
errorlog = "-"
loglevel = "info"
