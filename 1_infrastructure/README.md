. ├── 1_infrastructure/

│ ├── networking/

│ ├── security/

│ ├── compute/

│ ├── load-balancing/

│ └── variables.tf │ ├── application/

│ ├── Dockerfile

│ └── source-code/ │ ├── .gitignore

└── README.md

Deployment Lifecycle (Conceptual)

Infrastructure provisioning via Terraform
Container image built and referenced in ECS task definition
ECS service deployed and registered with ALB
Application exposed via ALB DNS endpoint
