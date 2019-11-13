resource "azurerm_resource_group" "main" {
  name     = "map-${terraform.workspace}-rg"
  location = "${var.location}"
}
