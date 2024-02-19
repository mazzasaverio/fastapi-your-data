



/* ------------------------------ GCP Foundation----------------------------- */

variable "gcp_project_id" {
  description = "The GCP project ID."
  type        = string
}
variable "gcp_project_number" {
  description = "The GCP project number."
  type        = string
}

variable "gcp_service_account_name" {
  description = "The name of the service account."
  type        = string
}

variable "gcp_credentials_file" {
  description = "The path to the Google Cloud Service Account credentials file."
  type        = string
}

variable "gcp_services" {
  description = "The list of services to enable."
  type        = list(string)
}

variable "gcp_existing_service_account_roles" {
  description = "List of roles to be assigned to the existing service account"
  type        = list(string)
  default     = ["secretmanager.secretAccessor", "cloudsql.client"]
}

variable "gcp_cloud_build_service_account_roles" {
  description = "List of roles to be assigned to the Cloud Build service account"
  type        = list(string)
  default     = ["secretmanager.secretAccessor", "compute.admin", "run.admin"]
}

variable "gcp_network_name" {
  description = "The name of the VPC network."
  type        = string
}


variable "gcp_region" {
  description = "The region where the resources will be created."
  type        = string
}

variable "gcp_zone" {
  description = "The zone where the resources will be created."
  type        = string
}


/* ----------------------------- Secret Manager ----------------------------- */


variable "repo_name" {
  description = "The name of the repository to create the trigger for the Cloud Build."
  type        = string
}

variable "branch" {
  description = "The branch of the repository to create the trigger for the Cloud Build."
  type        = string
}

variable "github_token" {
  description = "The GitHub personal access token."
  type        = string
}


variable "github_gcp_installation_id" {
  description = "The GitHub App installation ID."
  type        = string
}

variable "github_remote_uri" {
  description = "The GitHub remote URI."
  type        = string
}

/* -------------------------- network and firewall -------------------------- */

variable "internal_traffic_source_range" {
  description = "Source IP range for internal traffic."
  type        = string

}

variable "internet_access_source_ranges" {
  description = "Source IP ranges for internet access."
  type        = list(string)

}

/* ----------------------------- Cloud SQL ----------------------------- */

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


variable "cloud_sql_proxy_source_range" {
  description = "Source IP range for Cloud SQL proxy."
  type        = string
}


variable "gcp_db_version" {
  description = "The database version to use."

}


variable "gcp_db_instance_name" {
  description = "The name of the db instance."
  type        = string
}
