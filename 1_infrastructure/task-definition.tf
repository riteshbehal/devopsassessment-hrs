resource "aws_cloudwatch_log_group" "ecs" {
  name              = "/ecs/${var.devopsassessment1}"
  retention_in_days = 7
}

resource "aws_ecs_task_definition" "nginx_app" {
  family                   = "${var.devopsassessment1}-nginx-task"
  network_mode             = "awsvpc"
  requires_compatibilities = ["FARGATE"]
  cpu                      = "256"
  memory                   = "512"

  execution_role_arn = aws_iam_role.ecs_task_execution_role.arn

  container_definitions = jsonencode([
    {
      name      = "java-application"
      image     = "amazoncorretto:17"
      essential = true

      portMappings = [
        {
          containerPort = 8080
          protocol      = "tcp"
        }
      ]

      environment = [
        {
          name  = "APP_NAME"
          value = var.devopsassessment1
        }
      ]

      command = [
        "java",
        "-jar",
        "/app/app.jar"
      ]

      logConfiguration = {
        logDriver = "awslogs"
        options = {
          awslogs-group         = aws_cloudwatch_log_group.ecs.name
          awslogs-region        = var.aws_region
          awslogs-stream-prefix = "ecs"
        }
      }
    }
  ])
}