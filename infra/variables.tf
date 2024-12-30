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