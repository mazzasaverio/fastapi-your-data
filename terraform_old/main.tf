terraform {
  required_providers {
    google = {
      source = "hashicorp/google"

    }
    google-beta = {
      source = "hashicorp/google-beta"

    }
  }
}

provider "google" {
  credentials = file(var.gcp_credentials_file)
  project     = var.gcp_project_id
  region      = var.gcp_region
  zone        = var.gcp_zone
}

provider "google-beta" {
  credentials = file(var.gcp_credentials_file)
  project     = var.gcp_project_id
  region      = var.gcp_region
  zone        = var.gcp_zone
}

# Fetch existing service account
data "google_service_account" "existing_service_account" {
  account_id = var.gcp_service_account_name
}

# Activate Google services
resource "google_project_service" "enabled_services" {
  for_each           = toset(var.gcp_services)
  service            = "${each.key}.googleapis.com"
  disable_on_destroy = false
}



# IAM role assignments for an existing service account
resource "google_project_iam_member" "existing_service_account_iam_roles" {
  for_each = toset(var.gcp_existing_service_account_roles)
  project  = var.gcp_project_id
  role     = "roles/${each.value}"
  member   = "serviceAccount:${data.google_service_account.existing_service_account.email}"
}

# IAM role assignments for Cloud Build service account with specific roles
resource "google_project_iam_member" "cloud_build_service_account_iam_roles" {
  for_each = toset(var.gcp_cloud_build_service_account_roles)
  project  = var.gcp_project_id
  role     = "roles/${each.value}"
  member   = "serviceAccount:${var.gcp_project_number}@cloudbuild.gserviceaccount.com"
}



/* -------------------------------------------------------------------------- */
/*                                   Modules                                  */
/* -------------------------------------------------------------------------- */

module "secret_manager" {
  source                  = "./modules/secret_manager"
  gcp_db_user             = var.gcp_db_user
  gcp_db_password         = var.gcp_db_password
  gcp_db_name             = var.gcp_db_name
  gcp_db_port             = var.gcp_db_port
  instance_ssh_public_key = var.instance_ssh_public_key
}


module "compute_instance" {
  source = "./modules/compute_instance"

  gcp_project_id            = var.gcp_project_id
  gcp_instance_name         = var.gcp_instance_name
  gcp_instance_type         = var.gcp_instance_type
  gcp_instance_zone         = var.gcp_zone
  gcp_instance_image        = var.gcp_instance_image
  gcp_instance_tags         = var.gcp_instance_tags
  gcp_service_account_email = data.google_service_account.existing_service_account.email
  gcp_db_user               = var.gcp_db_user
  gcp_db_password           = var.gcp_db_password
  gcp_db_name               = var.gcp_db_name
  network_id                = var.gcp_network_name
  # db_instance_ip_address    = module.cloud_sql.instance_ip_address
  instance_ssh_public_key = var.instance_ssh_public_key



  depends_on = [

    module.secret_manager
  ]
}
