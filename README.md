# Proposed solution

## Application
The application is very simple and is developed in python 3.9. It uses an embedded sqlite3 database with a table with 2 columns, time to store the request time and r_ip to store the ip of the request in reverse format.
<br> <br>

## Dockerfile
Use alpine as a base image because it is small and light. It exposes port 8000 which is where the application listens.
<br> <br>

## Helm chart
The helm chart is also extremely basic, it only uses a LoadBalancer and a Deployment. 
<br>
Note: Due to time constraints, the solution does not use RBAC, Network Policies, Service Account, digital certificates, or any other security measures.
<br> <br>

## Workflows

<br> <br>


## Public IP

