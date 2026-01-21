variable "aws_ec2_root_storage_device" {
  default = 8
  type = number
  description = "The size of the root storage device for the EC2 instance in GiB."  
}

variable "aws_ec2_storage_type" {
  default = "gp3"
  type = string
  description = "The storage type for the root storage device of the EC2 instance."  
}

variable "aws_ec2_instance_type" {
  default = "t2.micro"
  type = string
  description = "The type of the EC2 instance."
}

variable "aws_ec2_ami" {
  default = "ami-0c55b159cbfafe1f0" # Example AMI ID for Amazon Linux 2 in us-east-1
  type = string
  description = "The AMI ID for the EC2 instance."
}

variable "aws_ec2_key_name" {
  default = "id_ed25519"
  type = string
  description = "The name of the key pair to use for the EC2 instance."
}

