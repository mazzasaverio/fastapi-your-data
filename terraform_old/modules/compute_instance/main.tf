

resource "google_compute_instance" "app_instance" {
  name         = var.gcp_instance_name
  machine_type = var.gcp_instance_type
  zone         = var.gcp_instance_zone

  boot_disk {
    auto_delete = true

    initialize_params {
      image = var.gcp_instance_image
      size  = 60
      type  = "pd-ssd"
    }
  }


  network_interface {
    network = var.network_id
    # subnetwork = var.subnetwork_id
    access_config {}
  }



  metadata = {
    # db-host    = var.db_instance_ip_address
    project-id = var.gcp_project_id


  }

  metadata_startup_script = file("${path.module}/startup-script.sh")

  service_account {
    email  = var.gcp_service_account_email
    scopes = ["cloud-platform"]
  }

  tags = var.gcp_instance_tags

  allow_stopping_for_update = true
}
