provider "azurerm" {}

terraform {
  backend "azurerm" {
    storage_account_name = "tstate14401"
    container_name       = "tstate"
    key                  = "terraform.tfstate"
  }
}
