terraform{
   required_providers {
    aws ={
       source = "hashicorp/aws"
       version = "~> 5.0"
       }
    }
  }
  provider "aws"{
    region = var.region
    }
  resource "aws_instance" "app" {
    ami            = "ami-0c55b159cbfafe1f0"
    instance_type  = var.instance_type
  tags ={
    Name ="deploypilot-ai"
    }
  }  
