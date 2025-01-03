# Define the provider
provider "aws" {
  region = var.region
}

module "mlflow" {
  source = "./MLflow"
  region = var.region
  mlflow_bucket_name = var.mlflow_bucket_name
  ecr_repo_for_mlflow_model = var.ecr_repo_for_mlflow_model
}
