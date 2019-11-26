resource "azurerm_virtual_network" "main" {
  name                = "map-${terraform.workspace}-network"
  resource_group_name = "map-${terraform.workspace}-rg"
  location            = "${var.location}"
  address_space       = ["${var.address_space}"]
}

resource "azurerm_subnet" "external" {
  name                 = "map-${terraform.workspace}-external"
  resource_group_name  = "${var.rg_name}"
  virtual_network_name = "${azurerm_virtual_network.main.name}"
  address_prefix       = "${cidrsubnet(var.address_space, 4, 1)}"
}

resource "azurerm_subnet" "internal" {
  name                 = "map-${terraform.workspace}-internal"
  resource_group_name  = "${var.rg_name}"
  virtual_network_name = "${azurerm_virtual_network.main.name}"
  address_prefix       = "${cidrsubnet(var.address_space, 4, 2)}"
}
