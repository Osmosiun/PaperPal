# Output variables
output "mlflow_bucket_name" {
  description = "The name of the MLflow S3 bucket"
  value       = aws_s3_bucket.mlflow_bucket.bucket
}