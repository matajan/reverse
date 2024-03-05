# Proposed solution
The solution uses Digital Ocean as the public cloud provider. It is not a free tier, due to GCP's credit card verification issues.
<br> <br>

## Application
The application is very simple and is developed in python 3.9. It uses an embedded sqlite3 database with a table with 2 columns, time to store the request time and r_ip to store the ip of the request in reverse format.
<br> <br>

## Dockerfile
Use alpine as a base image because it is small and light. It exposes port 8000 which is where the application listens.
<br> <br>

## Helm chart
The helm chart is also extremely basic, it only uses a LoadBalancer and a Deployment. 
<br> <br>
Note: Due to time constraints, the solution does not use RBAC, Network Policies, Service Account, digital certificates, or any other security measures.
<br> <br>

## Workflows
The workflow is also very simple, perform the docker build, push the generated container to the GitHub registry, install doctl to retrieve the kube config file with the cluster data and deploy the helm chart.
<br> <br>

## Public IP
The port used is port **80** and this is the public IP address of the proposed solution: **1**
<br> <br>
