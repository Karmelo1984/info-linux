# Instalar Docker y Docker compose en "Raspberry Pi"

![Header](../img/ima-raspberrypi-docker-header-01.png)

Docker y Docker Compose son herramientas populares en el mundo del desarrollo y la administración de sistemas. Permiten la creación, gestión y despliegue de aplicaciones en contenedores de manera eficiente. Su combinación es especialmente útil en entornos como Raspberry Pi, proporcionando ventajas significativas en términos de portabilidad, escalabilidad y gestión de aplicaciones.

## Características principales:

* **Docker:** Permite encapsular aplicaciones y sus dependencias en contenedores ligeros y portátiles, asegurando la consistencia del entorno de ejecución.
* **Docker Compose:** Facilita la gestión de múltiples contenedores como una aplicación única, definiendo sus servicios, redes y volúmenes en un archivo YAML.

## Ventajas

* **Portabilidad:** Los contenedores Docker son independientes de la infraestructura subyacente, lo que facilita el despliegue en diferentes entornos, incluyendo Raspberry Pi.
* **Facilidad de uso:** Docker Compose simplifica la gestión de múltiples contenedores, permitiendo definir la configuración de la aplicación en un solo archivo.
* **Eficiencia:** Los contenedores son más ligeros que las máquinas virtuales, lo que reduce el uso de recursos y permite ejecutar más aplicaciones en el mismo hardware.

## Inconvenientes

* **Recursos:** Aunque más ligeros que las máquinas virtuales, los contenedores todavía necesitan recursos como CPU y RAM.
* **Curva de aprendizaje:** Puede requerir tiempo para familiarizarse con Docker y Docker Compose, especialmente para usuarios nuevos en la virtualización y el despliegue de aplicaciones.

## Conclusión

Docker y Docker Compose son herramientas poderosas para desarrolladores y administradores que desean gestionar aplicaciones de manera eficiente y escalable, especialmente en entornos como Raspberry Pi donde se valora la portabilidad y la optimización de recursos.

[Inicio de sección](#instalar-docker-y-docker-compose-en-raspberry-pi) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
1. [Documentación `Docker`](../docker/docker.md)
2. [Instalación](#instalación)
   

[<< Raspberry Pi >>](./raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#instalar-docker-y-docker-compose-en-raspberry-pi)
<br><br>

# Instalación
Para instalar `Docker` y `Docker Compose` en `Raspberry Pi`, primero actualiza el sistema con sudo apt-get update && sudo apt-get upgrade. Luego, instala las dependencias necesarias y agrega los repositorios de Docker.

```bash
# Paso 1: Actualizar el sistema
sudo apt-get -y update && sudo apt-get -y upgrade

# Paso 2: Instalar dependencias
sudo apt-get -y install apt-transport-https ca-certificates software-properties-common

# Paso 3: Agregar la clave GPG oficial de Docker
curl -fsSL https://download.docker.com/linux/raspbian/gpg | sudo apt-key add -

# Paso 4: Agregar el repositorio de Docker a las fuentes de APT
echo "deb [arch=armhf] https://download.docker.com/linux/raspbian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

# Paso 5: Actualizar el índice de paquetes de APT
sudo apt-get -y update

# Paso 6: Instalar Docker
sudo apt-get -y install docker-ce

# Paso 7: Instalar Docker Compose
sudo apt-get -y install docker-compose

# Paso 8: Verificar la instalación de Docker y Docker Compose
docker --version
docker-compose --version

# Paso 9: Agregar tu usuario al grupo Docker
sudo usermod -aG docker ${USER}

# Paso 10: Cerrar sesión y volver a iniciar sesión para aplicar los cambios de grupo
sudo reboot
```

[Inicio de sección](#instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#instalar-docker-y-docker-compose-en-raspberry-pi)
<br><br>
