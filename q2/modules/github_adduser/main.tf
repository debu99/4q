provider "github" {
  token        = "${var.github_token}"
  organization = "${var.github_organization}"
}

data "external" "parse" {
  program = ["python", "${path.module}/parse.py"]

  query = {
    path     = "${path.root}"
    filename = "${var.filename}"
  }
}

locals {
  teams   = "${split(",", data.external.parse.result.teams)}"
  members = "${split(",", data.external.parse.result.members)}"
}

resource "github_team" "teams" {
  count = "${length(local.teams)}"
  name  = "${local.teams[count.index]}"
}

resource "github_team_membership" "members" {
  count    = "${length(local.members)}"
  team_id  = "${element(split("|",element(local.members,count.index)),0)}"
  username = "${element(split("|",element(local.members,count.index)),1)}"
  role     = "${element(split("|",element(local.members,count.index)),2)}"
}
