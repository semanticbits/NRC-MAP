resource "azurerm_virtual_network" "main" {
  name                = "map-${terraform.workspace}-network"
  resource_group_name = "map-${terraform.workspace}-rg"
  location            = "${var.location}"
  address_space       = "${var.address_space}"
}
