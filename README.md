# devopsassessment-hrs

.
├── 1_infrastructure/
│   ├── networking/
│   ├── security/
│   ├── compute/
│   ├── load-balancing/
│   └── variables.tf
│
├── application/
│   ├── Dockerfile
│   └── source-code/
│
├── .gitignore
└── README.md

Deployment Lifecycle (Conceptual)

1. Infrastructure provisioning via Terraform
2. Container image built and referenced in ECS task definition
3. ECS service deployed and registered with ALB
4. Application exposed via ALB DNS endpoint

Assumptions & Constraints

1.  Single application environment (non-prod)
2.  HTTP-based application interface
3.  IAM roles and policies are scoped to ECS requirements
