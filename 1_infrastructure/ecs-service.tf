resource "aws_security_group" "ecs" {
  name        = "${var.devopsassessment1}-ecs-sg"
  description = "Security group for ECS tasks"
  vpc_id      = aws_vpc.this.id

  ingress {
    from_port       = 8080
    to_port         = 8080
    protocol        = "tcp"
    security_groups = [aws_security_group.alb.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.devopsassessment1}-ecs-sg"
  }
}

resource "aws_ecs_service" "nginx_app" {
  name            = "${var.devopsassessment1}-nginx-service"
  cluster         = aws_ecs_cluster.this.id
  task_definition = aws_ecs_task_definition.nginx_app.arn
  launch_type     = "FARGATE"
  desired_count   = 1

  network_configuration {
    subnets         = [
    aws_subnet.public[0].id,
    aws_subnet.public[1].id]
    security_groups = [aws_security_group.ecs_sg.id]
    assign_public_ip = true
  }
}
