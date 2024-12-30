variable "region" {
  description = "AWS region"
  type        = string
}

variable "mlflow_bucket_name" {
  description = "Name of the S3 bucket to create for the MLflow experimentations"
  type        = string
}