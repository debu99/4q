variable "github_token" {
  description = "This is the GitHub personal access token."
}

variable "github_organization" {
  description = "This is the target GitHub organization to manage."
}

variable "filename" {
  default = "test.csv"
}

module "github_adduser" {
  source              = "./modules/github_adduser"
  github_token        = "${var.github_token}"
  github_organization = "${var.github_organization}"
  filename            = "${var.filename}"
}
