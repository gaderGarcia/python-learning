from rq import Worker, Queue, Connection
from redis import Redis
#from tasks import calculate_square

redis_conn = Redis(
  host='redis-10273.c56.east-us.azure.cloud.redislabs.com',
  port=10273,
  password='JLhFXEBm3flmz0ubo1NXSwtoJazgL31t')

# Create a worker and connect it to the default queue
with Connection(redis_conn):
    worker = Worker(Queue('default'))
    #Run the worker
    worker.work()