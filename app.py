from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
    <body>

    <h1>Welcome to Kubernetes Applicaton !</h1>

    <p>
        This application is running successfully using
        <b>Kubernetes</b>, <b>Docker</b>, and a
        <b>CI/CD Pipeline</b> powered by <b>GitHub Actions</b>.
    </p>

    <p><b>Pod Name:</b> {os.environ.get('HOSTNAME')}</p>

    <hr>

    <h2>Most Frequently Used Kubernetes Commands</h2>

    <table border="1" cellpadding="10">
        <tr>
            <th>S.No</th>
            <th>Command</th>
            <th>Description</th>
        </tr>

        <tr>
            <td>1</td>
            <td>minikube start</td>
            <td>Starts the Minikube Kubernetes cluster.</td>
        </tr>

        <tr>
            <td>2</td>
            <td>kubectl get nodes</td>
            <td>Displays all nodes available in the cluster.</td>
        </tr>

        <tr>
            <td>3</td>
            <td>kubectl describe nodes</td>
            <td>Provides detailed information about cluster nodes.</td>
        </tr>

        <tr>
            <td>4</td>
            <td>kubectl get namespace (or) kubectl get ns</td>
            <td>Lists all namespaces in the Kubernetes cluster.</td>
        </tr>

        <tr>
            <td>5</td>
            <td>kubectl create ns test</td>
            <td>Creates a namespace named "test".</td>
        </tr>

        <tr>
            <td>6</td>
            <td>kubectl delete ns test</td>
            <td>Deletes the "test" namespace and its resources.</td>
        </tr>

        <tr>
            <td>7</td>
            <td>kubectl get pods -n test</td>
            <td>Displays all pods in the test namespace.</td>
        </tr>

        <tr>
            <td>8</td>
            <td>kubectl apply -f deployment.yaml</td>
            <td>Creates or updates resources from deployment.yaml.</td>
        </tr>

        <tr>
            <td>9</td>
            <td>kubectl get deployment -n test</td>
            <td>Lists all deployments in the test namespace.</td>
        </tr>

        <tr>
            <td>10</td>
            <td>kubectl apply -f service.yaml</td>
            <td>Creates or updates resources from service.yaml.</td>
        </tr>

        <tr>
            <td>11</td>
            <td>kubectl get svc -n test</td>
            <td>Displays all services in the test namespace.</td>
        </tr>

        <tr>
            <td>12</td>
            <td>minikube ip</td>
            <td>Retrieves the IP address of the Minikube cluster.</td>
        </tr>

        <tr>
            <td>13</td>
            <td>minikube service list</td>
            <td>Lists all services exposed by Minikube.</td>
        </tr>

        <tr>
            <td>14</td>
            <td>minikube service web-app-service -n test</td>
            <td>Opens the web-app-service running in the test namespace.</td>
        </tr>

    </table>

    <hr>

    <p>
        These are the most commonly used Kubernetes commands for managing
        clusters, namespaces, deployments, services, and applications in a
        Kubernetes environment.
    </p>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
