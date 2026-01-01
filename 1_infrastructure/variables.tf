variable "devopsassessment1" {
  description = "Project name prefix"
  type        = string
  default     = "devops-assessment"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "nat_az_index" {
  description = "Availability zone index for NAT Gateway"
  type        = number
  default     = 1
}

variable "aws_region" {
  description = "AWS region"
  type        = string
}

