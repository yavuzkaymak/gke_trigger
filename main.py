from fastapi import FastAPI, status, Body
from model import Deployment
from service.kubernetes import Deployment_Service
from rule import RuleFactory

app = FastAPI(title="GKE Trigger", summary="GKE Trigger")


@app.post(path="/deployment/", status_code=status.HTTP_201_CREATED, tags=["Kubernetes deployment"], summary="creates k8 deployment")
async def create(deployment: Deployment) -> str:
    Deployment_Service.create(deployment)
    return "Done!"

@app.delete(path="/deployment/", status_code=status.HTTP_201_CREATED, tags=["Kubernetes deployment"], summary="deletes k8 deployment")
async def delete(deployment: Deployment) -> str:
    Deployment_Service.delete(deployment)
    return "Done!"

@app.post(path="/deploy/")
async def rule_deployer(rule: RuleFactory):
    rule = rule.getRule()
    rule.deploy_dataflow()
    Deployment_Service.apply_manifest(rule.scaler.manifest)

