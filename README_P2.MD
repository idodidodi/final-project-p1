# Final Project - Phase 2 (Kubernetes)

This phase focuses on deploying the Flask application to a Kubernetes cluster using Minikube. It includes features like Horizontal Pod Autoscaling (HPA), Liveness/Readiness probes, and periodic tasks via CronJobs.

## 1. Prerequisites

Ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Minikube](https://minikube.sigs.k8s.io/docs/start/)

## 2. Start Kubernetes Cluster

Start Minikube and enable the metrics server, which is required for the Horizontal Pod Autoscaler (HPA):

```bash
minikube start
minikube addons enable metrics-server
```

## 3. Build Docker Image

To use the local Docker image inside Minikube, configure your shell to use Minikube's Docker daemon:

```bash
eval $(minikube docker-env)
docker-compose build
```

Switch back to local Docker after deployment:

```bash
eval $(minikube docker-env -u)
```

## 4. Apply Kubernetes Resources

Apply the configuration files to the cluster. Note that `flask-app.yaml` contains the Deployment, Service, ConfigMap, HPA, and CronJob definitions.

```bash
# Apply secrets first
kubectl apply -f secret.yaml

# Apply the main application resources
kubectl apply -f flask-app.yaml
```


## 5. Verify Deployment

Check the status of your pods and services:

```bash
kubectl get pods
kubectl get svc
```

## 6. Access the Application

Expose the service to access it from your browser:

```bash
minikube service flask-app-service
```

## 7. Test Horizontal Pod Autoscaler (HPA)

### Generate Load
In a separate terminal, run a loop to generate traffic:

```bash
while true; do wget -q -O- http://flask-app-service; done
```

### Watch Scaling
Monitor the HPA to see it scale the number of replicas:

```bash
kubectl get hpa -w
```

## 8. Test Probes (Health Checks)

The application provides health endpoints at:
- `/health/live`: Liveness probe
- `/health/ready`: Readiness probe

Monitor the pods to see how Kubernetes handles container health:

```bash
kubectl get pods -w
```

## 9. Test CronJob

Verify that the CronJob is creating jobs and pods as scheduled:

```bash
kubectl get pods -w
kubectl logs <cronjob-pod-name>
```

## 10. Cleanup

When finished, you can delete the Minikube cluster:

```bash
minikube delete
```