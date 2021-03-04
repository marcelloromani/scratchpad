terraform {
  backend "s3" {
    bucket = "marcelloromani-scratchpad-terraform-eu-west-2"
    region = "eu-west-2"
    key = "aws_alb/terraform.tfstate"
  }

  required_version = ">= 0.14.7"
}

provider "aws" {
  region = "eu-west-2"
}
