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



variable "documentdb_cluster_identifier" {
  description = "Cluster identifier for the DocumentDB cluster"
  type        = string
  default     = "document_querying_rag_cluster"
}

variable "documentdb_master_username" {
  description = "Master username for the DocumentDB cluster"
  type        = string
  default     = "admin"
}

variable "documentdb_master_password" {
  description = "Master password for the DocumentDB cluster"
  type        = string
  default     = "admin123"
}

variable "documentdb_instance_class" {
  description = "Instance class for the DocumentDB instance"
  type        = string
  default     = "db.t3.medium"
}

variable "ami_of_ec2_for_docdb" {
  description = "AMI of ec2 instance created for docdb"
  type        = string
  default     = "ami-005fc0f236362e99f"
}

variable "instance_type_of_ec2_for_docdb" {
  description = "Instance type of ec2 instance created for docdb"
  type        = string
  default     = "t2.micro"
}

variable "key_pair_name_for_ec2" {
  description = "Name of Key-Pair being created which will be used for the ec2 instance"
  type        = string
  default     = "paperpal"
}