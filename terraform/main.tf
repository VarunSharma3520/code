
# demo is native name to terraform
# 
# resource "aws_s3_bucket" "storage" { 
#   bucket = "cybro-terraform-demo-12345"

# }

# resource "aws_vpc" "server_vpc" {
#   cidr_block           = "10.10.0.0/16"
#   enable_dns_hostnames = true
#   enable_dns_support   = true
#   tags = {
#     Name = "cybro-terraform-demo-vpc"
#     Test = "Demo"
#   }
# }

# resource "aws_security_group" "ssh" {
#   name = "allow-ssh-http"

#   ingress {
#     from_port   = 22
#     to_port     = 22
#     protocol    = "tcp"
#     cidr_blocks = ["172.19.0.1/32"]
#   }

#   ingress {
#     from_port   = 80
#     to_port     = 80
#     protocol    = "tcp"
#     cidr_blocks = ["0.0.0.0/0"]
#   }

#   egress {
#     from_port   = 0
#     to_port     = 0
#     protocol    = "-1"
#     cidr_blocks = ["0.0.0.0/0"]
#   }
# }

data "aws_ami" "ubuntu" {
  most_recent = true

  owners = ["0997201 09477"] 

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}



resource "aws_instance" "api_server" {
  ami                         = data.aws_ami.ubuntu.id
  instance_type               = "t2.micro"
  associate_public_ip_address = true

  vpc_security_group_ids = [
    aws_security_group.ssh.id
 ]

  user_data = file("nginx.tpl")

  tags = {
    Name = "testinghi"
  }
}
