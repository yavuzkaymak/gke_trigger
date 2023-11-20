from model import Deployment

def delete(deployment: Deployment):
    print(f"Deployment {deployment.name} has been deleted")

def create(deployment: Deployment):
    print(f"Deployment {deployment.name} has been created with {deployment.spec.replica} replicas")


