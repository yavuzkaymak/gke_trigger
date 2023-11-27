from dataclasses import dataclass, field
import yaml
from typing import Optional
from IScaler import Scaler


@dataclass
class KedaPubSub(Scaler):
    name: str
    scaled_target: str = field(repr=False)
    authenticationRef: str = field(repr=False)
    subscriptionName: str = field(repr=False)
    maxReplicaCount: Optional[int] = field(repr=False, default=3)

    def __post_init__(self):
        self.template = f"""

        apiVersion: keda.sh/v1alpha1
        kind: ScaledObject
        metadata:
          name: {self.name}
        spec:
          pollingInterval: 10                              
          cooldownPeriod: 180                             
          minReplicaCount: 1                                
          maxReplicaCount: {self.maxReplicaCount}             
          idleReplicaCount: 0
          scaleTargetRef:
            name: {self.scaled_target}
          triggers:
            - type: gcp-pubsub
              authenticationRef:
                name: keda-auth
              metadata:
                subscriptionName : {self.subscriptionName}
          advanced: 
            horizontalPodAutoscalerConfig: 
              behavior:
                scaleUp:
                  stabilizationWindowSeconds: 20
                  policies:
                    - type: Pods
                      value: 1
                      periodSeconds: 40
                scaleDown:
                  stabilizationWindowSeconds: 180
                  policies:
                    - type: Pods
                      value: 5
                      periodSeconds: 60

        """

    @property
    def manifest(self):
        return yaml.safe_load(self.template)
