export AWS_REGION='us-east-1'
export AWS_ACCOUNT='253490781721'

# Get ECR login token
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com

# Pull the MLflow image
docker pull ghcr.io/mlflow/mlflow:v2.17.2

# Tag the image for your ECR
docker tag ghcr.io/mlflow/mlflow:v2.17.2 $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/paperpal-mlflow-models:latest

# Push to ECR
docker push $AWS_ACCOUNT.dkr.ecr.$AWS_REGION.amazonaws.com/paperpal-mlflow-models:latest