data "google_secret_manager_secret_version" "db_user" {
  secret  = "DB_USER"
  project = var.gcp_project_id
  version = "latest"
}

data "google_secret_manager_secret_version" "db_pass" {
  secret  = "DB_PASS"
  project = var.gcp_project_id
  version = "latest"
}

data "google_secret_manager_secret_version" "db_name" {
  secret  = "DB_NAME"
  project = var.gcp_project_id

  version = "latest"
}



resource "google_cloud_run_v2_service" "default" {
  name         = "cloudrun-service"
  location     = "us-central1"
  launch_stage = "BETA"
  ingress      = "INGRESS_TRAFFIC_ALL"

  template {
    containers {
      image = "gcr.io/${var.gcp_project_id}/fastapi-your-data:latest"
      resources {
        limits = {
          cpu    = "2"
          memory = "1024Mi"
        }
      }

      env {
        name  = "DB_USER"
        value = data.google_secret_manager_secret_version.db_user.secret_data
      }
      env {
        name  = "DB_PASS"
        value = data.google_secret_manager_secret_version.db_pass.secret_data
      }
      env {
        name  = "DB_NAME"
        value = data.google_secret_manager_secret_version.db_name.secret_data
      }
      env {
        name  = "DB_HOST"
        value = var.gcp_db_instance_ip_address
      }
      env {
        name  = "DB_PORT"
        value = "5432"
      }
    }
    vpc_access {
      egress = "ALL_TRAFFIC"
      #egress = "PRIVATE_RANGES_ONLY"
      network_interfaces {
        network    = var.network_id
        subnetwork = var.subnetwork_id
        tags       = ["cloud-run-service"]
      }
    }
  }
  traffic {
    type    = "TRAFFIC_TARGET_ALLOCATION_TYPE_LATEST"
    percent = 100
  }

}

resource "google_cloud_run_service_iam_member" "public_invoker" {
  location = "us-central1"
  service  = google_cloud_run_v2_service.default.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
