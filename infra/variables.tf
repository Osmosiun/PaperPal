variable "region" {
  description = "AWS region"
  type        = string
}

variable "mlflow_bucket_name" {
  description = "Name of the S3 bucket to create for the MLflow experimentations"
  type        = string
}

variable "backend_bucket_name" {
  description = "Name of the backend S3 bucket for Terraform state"
  type        = string
}

variable "ecr_repo_for_mlflow_model" {
  description = "Name of the ECR repository which will be used to store mlflow models docker image so that they can be used for deployment in either sagemaker or eks"
  type        = string
}