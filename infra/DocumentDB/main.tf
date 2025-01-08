resource "aws_security_group" "docdb_sg" {
  name_prefix = "docdb-sg"

  ingress {
    from_port   = 27017
    to_port     = 27017
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Restrict to your IP range for security
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_docdb_subnet_group" "document_querying_rag_subnet" {
  name       = "docdb-subnet-group"
  subnet_ids = ["subnet-0d5e70cd5b7a51efc", "subnet-05d4a80f0438997d9"] # Replace with your subnet IDs
}

resource "aws_docdb_cluster" "document_querying_rag" {
  cluster_identifier      = var.documentdb_cluster_identifier
  engine                  = "docdb"
  master_username         = var.documentdb_master_username
  master_password         = var.documentdb_master_password
  backup_retention_period = 5
  db_subnet_group_name = aws_docdb_subnet_group.document_querying_rag_subnet.name 
  vpc_security_group_ids = [aws_security_group.docdb_sg.id]
}

resource "aws_docdb_cluster_instance" "document_querying_rag_instance" {
  cluster_identifier = aws_docdb_cluster.document_querying_rag.id
  instance_class     = var.documentdb_instance_class
}

resource "aws_security_group" "allow_all" {
  name        = "allow-all-traffic"
  description = "Allow all inbound and outbound traffic"

  # Allow all inbound traffic
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allow from all IPv4 addresses
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"] # Allow to all IPv4 addresses
  }
}

resource "aws_instance" "ec2_for_docdb" {
  ami           = var.ami_of_ec2_for_docdb
  instance_type = var.instance_type_of_ec2_for_docdb
  key_name = var.key_pair_name_for_ec2
  security_groups = [aws_security_group.allow_all.name]
  tags = {
    Name = "MyEC2InstanceForDocDB"
  }
}

