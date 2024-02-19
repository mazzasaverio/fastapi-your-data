output "instance_ip_address" {
  value = google_sql_database_instance.instance.private_ip_address
}
