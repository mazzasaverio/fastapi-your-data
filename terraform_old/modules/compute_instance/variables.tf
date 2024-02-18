variable "gcp_project_id" {
  description = "The ID of the project in which the resource belongs. If it is not provided, the provider project is used."
  type        = string
}

variable "gcp_instance_name" {
  description = "The name of the instance"
  type        = string
}

variable "gcp_instance_type" {
  description = "The machine type of the instance"
  type        = string
  default     = "e2-medium"
}

variable "gcp_instance_zone" {
  description = "The zone to host the instance in"
  type        = string
}

variable "gcp_instance_image" {
  description = "The image to use for the instance"
  type        = string
  default     = "ubuntu-os-cloud/ubuntu-2004-lts"
}

variable "gcp_instance_tags" {
  description = "A list of network tags to attach to the instance"
  type        = list(string)
  default     = []
}

variable "gcp_service_account_email" {
  description = "The email of the service account to grant access to the Cloud SQL instance."
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

variable "network_id" {
  description = "The ID of the VPC network."
  type        = string
}

# variable "subnetwork_id" {
#   description = "The ID of the subnetwork."
#   type        = string
# }

# variable "db_instance_ip_address" {
#   description = "The private IP address of the Cloud SQL instance."
#   type        = string
# }

variable "instance_ssh_user" {
  description = "The username to use for SSH access to the instance"
  type        = string
  default     = "ubuntu"
}

variable "instance_ssh_public_key" {
  description = "The public key to use for SSH access to the instance"
  type        = string
}


