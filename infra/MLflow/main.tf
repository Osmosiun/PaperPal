# Define the provider
provider "aws" {
  region = var.region
}

# Create the main S3 bucket
resource "aws_s3_bucket" "mlflow_bucket" {
  bucket = var.mlflow_bucket_name
}

resource "aws_ecr_repository" "ecr_repository_for_mlflow_model_deployment" {
  name                 = var.ecr_repo_for_mlflow_model
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}