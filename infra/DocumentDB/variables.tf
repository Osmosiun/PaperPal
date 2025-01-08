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