from redis import Redis
from rq import Queue, Callback
from tasks import calculate_square
import time

#Tell RQ what Redis connection to use
redis_conn = Redis(
  host='redis-10273.c56.east-us.azure.cloud.redislabs.com',
  port=10273,
  password='JLhFXEBm3flmz0ubo1NXSwtoJazgL31t')

#Create a queue using the default queue name
# by default the name of the queu is 'default'
queue = Queue(connection=redis_conn)

def report_success(job, connection, result):
    print(result)

#Enqueue the calculate_square task with argument 5
job = queue.enqueue(calculate_square,5,on_success=Callback(report_success))
print(f"Task enqueued. Job ID:{job.id}")
#result = job.latest_result()  #  returns Result(id=uid, type=SUCCESSFUL)
#if result == result.Type.SUCCESSFUL: 
#print(job.result)
#time.sleep(2)
#print(job.result)


#else: 
#print(result.exc_string)
