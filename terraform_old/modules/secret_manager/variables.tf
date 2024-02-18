
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


variable "instance_ssh_user" {
  description = "The username to use for SSH access to the instance"
  type        = string
  default     = "ubuntu"
}

variable "instance_ssh_public_key" {
  description = "The public key to use for SSH access to the instance"
  type        = string
}


