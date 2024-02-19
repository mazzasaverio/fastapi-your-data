variable "gcp_project_id" {
  description = "The GCP project ID."
  type        = string
}

variable "gcp_network_name" {
  description = "The name of the VPC network."
  type        = string
}

variable "gcp_region" {
  description = "The region where the resources will be created."
  type        = string
}
