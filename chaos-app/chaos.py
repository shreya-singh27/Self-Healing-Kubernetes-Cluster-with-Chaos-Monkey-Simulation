import threading
import time
from flask import Flask
from kubernetes import client, config
import random
from prometheus_flask_exporter import PrometheusMetrics 

app = Flask(__name__)
metrics = PrometheusMetrics(app)  

def delete_pod_periodically():
    print(" Chaos Monkey thread started")
    config.load_incluster_config()
    v1 = client.CoreV1Api()

    while True:
        time.sleep(60)
        print(" Checking for flask-app pods...")
        pods = v1.list_namespaced_pod(namespace="default", label_selector="app=flask-app")
        if not pods.items:
            print("No flask-app pods found.")
            continue
        pod_to_delete = random.choice(pods.items)
        pod_name = pod_to_delete.metadata.name
        print(f" Deleting pod: {pod_name}")
        v1.delete_namespaced_pod(name=pod_name, namespace="default")
        print(f" Chaos Monkey deleted pod: {pod_name}")

@app.route("/")
def hello():
    return "Chaos Monkey Running"

if __name__ == "__main__":
    print(" Starting chaos-app")
    thread = threading.Thread(target=delete_pod_periodically, daemon=True)
    thread.start()
    app.run(host="0.0.0.0", port=5000)

