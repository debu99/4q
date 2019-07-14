output "teams_id" {
  default = "The ID of the created team."
  value   = "${github_team.teams.*.id}"
}

output "length" {
  default = "The total number of the created members."
  value   = "${length(local.teams)}"
}

output "teams_name" {
  default = "The name of the created team."
  value   = "${local.teams}"
}
