################
## Network vars
################

variable "location" {
  default = {
    dev = "West US"
  }
}

variable "resource_group_name" {
  default = {
    dev = "map-rg"
  }
}

variable "address_space" {
  default = {
    dev = "10.0.0.0/22"
  }
}
