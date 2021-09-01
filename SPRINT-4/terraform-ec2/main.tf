provider "aws" {
  region = "us-west-2"
}

resource "aws_security_group" "instance-sg" {
  name = "sebastian-terraform-sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "sebastian_terraform" {
  ami           = "ami-03d5c68bab01f3496"
  instance_type = "t3.micro"

  tags = {
    Name = "sebastian_terraform"
  }

  vpc_security_group_ids = [aws_security_group.instance-sg.id]
}
