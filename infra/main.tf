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

module "documentdb_for_rag" {
  source = "./DocumentDB"
  documentdb_master_username = var.documentdb_master_username
  documentdb_master_password = var.documentdb_master_password
  documentdb_instance_class = var.documentdb_instance_class
  documentdb_cluster_identifier = var.documentdb_cluster_identifier
  ami_of_ec2_for_docdb = var.ami_of_ec2_for_docdb
  instance_type_of_ec2_for_docdb = var.instance_type_of_ec2_for_docdb
  key_pair_name_for_ec2 = var.key_pair_name_for_ec2
}
