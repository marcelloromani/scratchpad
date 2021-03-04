variable "project" {
  type    = string
  default = "scratchpad-alb"
}

variable "webserver_count" {
  description = "How many web servers (ec2 instances) to provision"
  type        = number
  default     = 1
}

variable "webserver_instance_type" {
  type    = string
  default = "t3.micro"
}

variable "key_name" {
  type    = string
  default = "aws_personal_london"
}
