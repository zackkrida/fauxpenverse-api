bind = ["0.0.0.0:8002"]
capture_output = True
chdir = "./ingestion_server/"
timeout = 120
reload = True
loglevel = "debug"
wsgi_app = "indexer_worker:api"
accesslog = "-"
errorlog = "-"
