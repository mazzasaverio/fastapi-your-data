

variable "github_token" {
  description = "The GitHub personal access token."
  type        = string
}



variable "gcp_db_user" {
  description = "The name of the db user."
  type        = string
}

variable "gcp_db_password" {
  description = "The password for the db user."
  type        = string

}


variable "gcp_db_name" {
  description = "The name of the db."
  type        = string
}

variable "gcp_db_port" {
  description = "The port of the db."
  type        = string
}


variable "openai_api_key" {
  description = "The OpenAI API key."
  type        = string
}
