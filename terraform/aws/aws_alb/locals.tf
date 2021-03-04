locals {
  name_prefix = var.project

  tags = {
    ManagedBy = "terraform"
    TerraformVersion = "0.14.7"
    Project = var.project
  }
}
