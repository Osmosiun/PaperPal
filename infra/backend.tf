terraform {
  backend "s3" {
    bucket         = "terraform-backend-663"
    key            = "terraform.tfstate"
    region         = "us-east-1"
  }
}