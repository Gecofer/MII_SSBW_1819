#!/bin/bash

# Creación del grupo de recursos con localización en el este de EE.UU.
echo " ------ Creación del grupo de recursos ------ "
az group create --name myResourceGroup-eastus --location eastus

# Creación de una red virtual llamada myVnet y una subred llamada mySubnet
echo " ------ Creación de la red virtual ------ "
az network vnet create  --resource-group myResourceGroup-eastus --name myVnet --address-prefix 10.0.0.0/16 --subnet-name mySubnet --subnet-prefix 10.0.1.0/24


# Creación de la máquina virtual - Obtenemos la IP
echo " ------ Creación de la máquina virtual ------ "
IP=$(az vm create  --resource-group myResourceGroup-eastus --name MV --image UbuntuLTS --admin-username gemazure --generate-ssh-keys --storage-sku Standard_LRS --public-ip-address-allocation static --vnet-name MyVnet --subnet mySubnet | jq -r '.publicIpAddress')

# Cambiamos el tamaño a la máquina virtual
echo " ------ Cambiando el tamaño a la máquina virtual ------ "
az vm resize --resource-group myResourceGroup-eastus --name MV --size Standard_B1s

# Abrimos el puerto 80
echo " ------ Abrimos el puerto 80 ------ "
az vm open-port --port 80 --resource-group myResourceGroup-eastus --name MV --priority 300
az vm open-port --port 8000 --resource-group myResourceGroup-eastus --name MV --priority 400
az vm open-port --port 8081 --resource-group myResourceGroup-eastus --name MV --priority 500
az vm open-port --port 443 --resource-group myResourceGroup-eastus --name MV --priority 600

# Una vez creada la máquina virtual, mostramos su nombre y su dirección IP
echo " ------ Datos de la máquina virtual creada ------ "
echo -name: MV
echo -ip: $IP

# Conectarnos a la máquina virtual - 40.121.70.119
# ssh gemazure@$IP

# Instalar docker
# sudo apt install docker.io

# Instalar docker-compose
# https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-16-04
# sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
# sudo chmod +x /usr/local/bin/docker-compose
# docker-compose --version

# Descargar el repo de Github
# git clone https://github.com/Gecofer/MII_SSBW_1819.git

# Ponerlo en funcionamiento
# cd MII_SSBW_1819/codigo/
# sudo docker-compose up --build

