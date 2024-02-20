variable "gcp_region" {
  description = "The region where the Cloud Run service will be deployed."
  type        = string
}


variable "network_id" {
  description = "The ID of the VPC network."
  type        = string
}

variable "subnetwork_id" {
  description = "The ID of the subnetwork."
  type        = string
}

variable "gcp_db_instance_ip_address" {
  description = "The private IP address of the Cloud SQL instance."
  type        = string
}


variable "gcp_project_id" {
  description = "Project ID"
  type        = string
}

variable "github_token" {
  description = "GitHub Access Token"
  type        = string
}
