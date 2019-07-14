variable "github_token" {
  description = "This is the GitHub personal access token."
  type        = "string"
}

variable "github_organization" {
  description = "This is the target GitHub organization to manage."
  type        = "string"
}

variable "filename" {
  description = "The filename of the csv."
  type        = "string"
}
