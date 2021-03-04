data "aws_ami" "amazon_linux_2" {
  owners      = ["amazon"]
  most_recent = true

  filter {
    name   = "description"
    values = ["Amazon Linux 2 * HVM *"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  filter {
    name   = "root-device-type"
    values = ["ebs"]
  }
}


resource "aws_security_group" "webserver" {
  name        = "${local.name_prefix}-webserver"
  description = "Allow HTTP and SSH from everywhere"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description = "HTTP from everywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "SSH from everywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = local.tags
}


data "template_file" "webserver_init" {
  template = file("${path.module}/webserver_init.tpl")
  vars = {
    project = var.project
  }
}



resource "aws_instance" "webserver" {
  count                  = var.webserver_count
  ami                    = data.aws_ami.amazon_linux_2.id
  instance_type          = var.webserver_instance_type
  key_name               = var.key_name
  vpc_security_group_ids = [aws_security_group.webserver.id]
  subnet_id              = module.vpc.public_subnets[0]
  user_data              = data.template_file.webserver_init.rendered

  tags = merge(
    local.tags,
    {
      Name = "${local.name_prefix}-webserver-${count.index + 1}"
    }
  )
}