from model import Deployment


def delete(deployment: Deployment):
    print(f"Deployment {deployment.name} has been deleted")


def create(deployment: Deployment):
    print(f"Deployment {deployment.name} has been created with {deployment.spec.replica} replicas")

    print(f"Here is the json representation: {deployment.model_dump_json()}")


def apply_manifest(manifest: dict) -> None:
    """using kubernetes api apply"""
    print(f"Applied to the kubernetes: {manifest}")