import requests

r = requests.post("http://localhost:8000/",json={"id":4,"name":"AnotherTest","age":40})
result = r.json()
print(result)