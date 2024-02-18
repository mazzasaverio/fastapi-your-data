#!/bin/bash

LOG_FILE="/var/log/startup-script.log"
PROJECT_ID=$(curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/project-id" -H "Metadata-Flavor: Google")

echo "Using Project ID: ${PROJECT_ID}" >> $LOG_FILE

# Updating and installing required packages
echo "Starting system update and package installation" >> $LOG_FILE
apt-get update >> $LOG_FILE 2>&1
apt-get install -y postgresql-client postgresql-client-common >> $LOG_FILE 2>&1

# Installing Zsh and Oh My Zsh
echo "Installing Zsh" >> $LOG_FILE
apt-get install -y zsh >> $LOG_FILE 2>&1

echo "Installing Oh My Zsh" >> $LOG_FILE
sh -c "$(wget https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh -O -)" >> $LOG_FILE 2>&1


# Setting up environment variables from Secret Manager
echo "Fetching environment variables from Secret Manager" >> $LOG_FILE
DB_USER=$(gcloud secrets versions access latest --secret="DB_USER" --project="${PROJECT_ID}" 2>&1) || { echo "Failed to fetch DB_USER" >> $LOG_FILE; exit 1; }
DB_PASS=$(gcloud secrets versions access latest --secret="DB_PASS" --project="${PROJECT_ID}" 2>&1) || { echo "Failed to fetch DB_PASS" >> $LOG_FILE; exit 1; }
DB_NAME=$(gcloud secrets versions access latest --secret="DB_NAME" --project="${PROJECT_ID}" 2>&1)
DB_HOST=$(curl http://metadata.google.internal/computeMetadata/v1/instance/attributes/db-host -H "Metadata-Flavor: Google")
DB_PORT=$(gcloud secrets versions access latest --secret="DB_PORT" --project="${PROJECT_ID}" 2>&1 || echo '5432')


# Exporting environment variables for all users
echo "Exporting environment variables" >> $LOG_FILE
echo "export DB_NAME='${DB_NAME}'" >> /etc/profile
echo "export DB_USER='${DB_USER}'" >> /etc/profile
echo "export DB_PASS='${DB_PASS}'" >> /etc/profile
echo "export DB_HOST='${DB_HOST}'" >> /etc/profile
echo "export DB_PORT='${DB_PORT}'" >> /etc/profile
echo "export API_KEY='12345'" >> /etc/profile

# Fetching instance user and SSH public key
INSTANCE_USER=$(gcloud secrets versions access latest --secret="INSTANCE_USER" --project="${PROJECT_ID}" 2>&1)
SSH_PUBLIC_KEY=$(gcloud secrets versions access latest --secret="SSH_PUBLIC_KEY" --project="${PROJECT_ID}" 2>&1) >> $LOG_FILE

# Check if user exists, if not create the user and set up SSH access
if ! id "${INSTANCE_USER}" &>/dev/null; then
    echo "Creating user ${INSTANCE_USER}" >> $LOG_FILE
    useradd -m -s /bin/bash "${INSTANCE_USER}"
fi

echo "Setting up SSH access for ${INSTANCE_USER}" >> $LOG_FILE
SSH_DIR="/home/${INSTANCE_USER}/.ssh"
mkdir -p "${SSH_DIR}"
echo "${SSH_PUBLIC_KEY}" | tee -a "${SSH_DIR}/authorized_keys" > /dev/null
chmod 700 "${SSH_DIR}"
chmod 600 "${SSH_DIR}/authorized_keys"
chown -R "${INSTANCE_USER}:${INSTANCE_USER}" "${SSH_DIR}"

# Ensuring permissions are correct for the user's home directory
chmod 755 "/home/${INSTANCE_USER}"

# Installing Docker
echo "Installing Docker and starting Docker service" >> $LOG_FILE
sudo apt-get update >> $LOG_FILE 2>&1
sudo apt-get install -y docker.io >> $LOG_FILE 2>&1
sudo systemctl start docker >> $LOG_FILE 2>&1
sudo systemctl enable docker >> $LOG_FILE 2>&1

# Add instance user to the Docker group
echo "Adding ${INSTANCE_USER} to the Docker group" >> $LOG_FILE
sudo usermod -aG docker "${INSTANCE_USER}"

# Refresh group memberships for the instance user
echo "Refreshing group memberships for ${INSTANCE_USER}" >> $LOG_FILE
if pgrep -u "${INSTANCE_USER}"; then
    sudo -u "${INSTANCE_USER}" newgrp docker
else
    echo "User ${INSTANCE_USER} not logged in, skipping group refresh" >> $LOG_FILE
fi

# Installing Docker Compose
echo "Installing Docker Compose" >> $LOG_FILE
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose >> $LOG_FILE 2>&1
sudo chmod +x /usr/local/bin/docker-compose >> $LOG_FILE 2>&1
