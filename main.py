from fastapi import FastAPI, status
from model import Deployment
from service.kubernetes import Deployment_Service


app = FastAPI(title="GKE Trigger", summary="GKE Trigger")


@app.post(path="/deployment/", status_code=status.HTTP_201_CREATED, tags=["Kubernetes Deployment"], summary="creates k8 deployment")
async def create(deployment: Deployment):
    Deployment_Service.create(deployment)
    return "Done!"

@app.delete(path="/deployment/", status_code=status.HTTP_201_CREATED, tags=["Kubernetes Deployment"], summary="deletes k8 deployment")
async def delete(deployment: Deployment):
    Deployment_Service.delete(deployment)
    return "Done!"
