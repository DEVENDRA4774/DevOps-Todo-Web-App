# Terraform configuration for local development with VirtualBox
# Note: This is a placeholder for actual cloud provider configuration (e.g., OCI)

terraform {
  required_providers {
    virtualbox = {
      source = "terra-farm/virtualbox"
      version = "0.2.2-alpha.1"
    }
  }
}

# Example resource (commented out as it requires the provider to be installed)
# resource "virtualbox_vm" "node" {
#   name      = "devops-todo-vm"
#   image     = "https://app.vagrantup.com/ubuntu/boxes/bionic64/versions/20180426.0.0/providers/virtualbox.box"
#   cpus      = 1
#   memory    = "512mib"
#
#   network_adapter {
#     type = "nat"
#   }
# }

output "message" {
  value = "Terraform configuration initialized. In a real scenario, this would provision a VM on Oracle Cloud or locally."
}
