resource "aws_alb" "webserver" {
  name = "${local.name_prefix}-webserver"
  internal = false
  load_balancer_type = "application"
  subnets = module.vpc.public_subnets
  security_groups = [ aws_security_group.webserver.id ]

  tags = local.tags
}

resource "aws_alb_target_group" "webserver" {
  health_check {
    interval            = 10
    path                = "/"
    protocol            = "HTTP"
    timeout             = 5
    healthy_threshold   = 5
    unhealthy_threshold = 2
  }

  name        = "${local.name_prefix}-webserver"
  port        = 80
  protocol    = "HTTP"
  target_type = "instance"
  vpc_id = module.vpc.vpc_id

  tags = local.tags
}


resource "aws_alb_target_group_attachment" "webserver" {
  target_id = aws_instance.webserver[0].id
  target_group_arn = aws_alb_target_group.webserver.arn
}

resource "aws_alb_listener" "webserver" {
  load_balancer_arn = aws_alb.webserver.arn
  port = 80
  protocol = "HTTP"
  default_action {
    type = "forward"
    target_group_arn = aws_alb_target_group.webserver.arn
  }
}
