# Define the provider
provider "aws" {
  region = var.region
}

# Create the main S3 bucket
resource "aws_s3_bucket" "mlflow_bucket" {
  bucket = var.mlflow_bucket_name
}