# Define the provider
provider "aws" {
  region = var.region
}

module "mlflow" {
  source = "./MLflow"
  region = var.region
  mlflow_bucket_name = var.mlflow_bucket_name
}
