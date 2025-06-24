terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
      version = "5.86.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = var.region
}

resource "aws_instance" "myserver" {
  ami = "ami-00bb6a80f01f03502"
  instance_type = "t2.micro"

  tags = {
    Name = "SampleServer"
  }
}