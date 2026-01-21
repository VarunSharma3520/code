# key pair to be used for EC2 instance access
resource "aws_key_pair" "deployer" {
  key_name   = var.aws_ec2_key_name
  public_key = file("~/.ssh/id_ed25519.pub")
}

# EC2 instance resource
resource "aws_instance" "web_server" {
  count                  = 1
  ami                    = "ami-0b6c6ebed2801a5cb" # Ubuntu Server 24.04 LTS in us-east-1
  instance_type          = "t2.micro"
  subnet_id              = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.web_sg.id]
  user_data              = file("install_docker.sh") # to install docker on launch
  key_name               = aws_key_pair.deployer.key_name
  root_block_device {
    volume_size           = var.aws_ec2_root_storage_device
    delete_on_termination = true
    volume_type           = var.aws_ec2_storage_type
  }
  instance_initiated_shutdown_behavior = "terminate"
  tags = {
    Name = "web-server"
  }
}
