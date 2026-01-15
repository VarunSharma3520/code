terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "~> 5.0" # Or your desired version
    }
  }
}

provider "aws" {
  region = locals.region
}

