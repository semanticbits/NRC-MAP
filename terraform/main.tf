module "resource_group" {
  source   = "./modules/resource_group"
  location = "${lookup(var.location, terraform.workspace)}"
}

module "networking" {
  source        = "./modules/networking"
  address_space = "${var.address_space[terraform.workspace]}"
  location      = "${lookup(var.location, terraform.workspace)}"
  rg_name       = "${module.resource_group.rg_name}"
}


# module "tableau" {
#   source      = "./modules/tableau"
#   rg_name     = "${module.resource_group.rg_name}"
#   rg_location = "${module.resource_group.rg_location}"
# }
