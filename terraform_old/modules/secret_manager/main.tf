


/* -------------------------------- Cloud SQL ------------------------------- */

# DB_USER Secret
resource "google_secret_manager_secret" "db_user_secret" {
  secret_id = "DB_USER"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "db_user_secret_version" {
  secret      = google_secret_manager_secret.db_user_secret.id
  secret_data = var.gcp_db_user
}

# DB_PASS Secret
resource "google_secret_manager_secret" "db_pass_secret" {
  secret_id = "DB_PASS"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "db_pass_secret_version" {
  secret      = google_secret_manager_secret.db_pass_secret.id
  secret_data = var.gcp_db_password
}




# DB_NAME Secret
resource "google_secret_manager_secret" "db_name_secret" {
  secret_id = "DB_NAME"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "db_name_secret_version" {
  secret      = google_secret_manager_secret.db_name_secret.id
  secret_data = var.gcp_db_name
}

# DB_PORT Secret
resource "google_secret_manager_secret" "db_port" {
  secret_id = "DB_PORT"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "db_port_secret_version" {
  secret      = google_secret_manager_secret.db_port.id
  secret_data = var.gcp_db_port
}



/* ------------------------- Compute Engine Istance ------------------------- */


# INSTANCE_USER Secret
resource "google_secret_manager_secret" "instance_user_secret" {
  secret_id = "INSTANCE_USER"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "instance_user_secret_version" {
  secret      = google_secret_manager_secret.instance_user_secret.id
  secret_data = var.instance_ssh_user
}


# SSH_PUBLIC_KEY Secret
resource "google_secret_manager_secret" "ssh_public_key_secret" {
  secret_id = "SSH_PUBLIC_KEY"
  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "ssh_public_key_secret_version" {
  secret      = google_secret_manager_secret.ssh_public_key_secret.id
  secret_data = var.instance_ssh_public_key
}


