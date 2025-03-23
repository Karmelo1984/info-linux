---
title: "Instalación de Docker y Docker Compose en Raspberry Pi"
authors:
  - Carmelo Molero Castillo
date: 2025-03-21
version: 1.0.0
---

# Instalación de Docker y Docker Compose
![Header](img/img-raspberrypi-docker-header-01.png)

**Descripción**:  
Docker y Docker Compose son herramientas esenciales para la creación y gestión de aplicaciones en contenedores. Su uso en Raspberry Pi permite maximizar la eficiencia del sistema, mejorando la portabilidad y escalabilidad de los proyectos.

Su capacidad para encapsular aplicaciones en contenedores hace que la gestión sea más eficiente, permitiendo una mayor escalabilidad y portabilidad en entornos de bajo consumo.

**Características principales**:  
✅ **Docker** - Encapsula aplicaciones y dependencias en contenedores ligeros y portátiles.  
✅ **Docker Compose** - Facilita la gestión de aplicaciones compuestas por múltiples contenedores mediante un archivo YAML.

📌 *Referencias*:  
- [Documentación oficial de Docker](https://docs.docker.com/)  
- [Guía de Docker Compose](https://docs.docker.com/compose/)

---

## Instalación

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos previos:

### Requisitos previos
- 📌 **Sistema operativo compatible**: Raspberry Pi OS (basado en Debian) u otro sistema basado en Linux.
- 📌 **Dependencias**: apt-transport-https, ca-certificates, software-properties-common.
- 📌 **Acceso**: Se requieren permisos de superusuario (*sudo*).

### Instalación de Docker y Docker Compose

Ejecuta los siguientes comandos en la terminal de Raspberry Pi:

```bash
# Paso 1: Actualizar el sistema
$ sudo apt-get -y update && sudo apt-get -y upgrade

# Paso 2: Instalar dependencias
$ sudo apt-get -y install apt-transport-https ca-certificates software-properties-common

# Paso 3: Agregar la clave GPG oficial de Docker
$ curl -fsSL https://download.docker.com/linux/raspbian/gpg | sudo apt-key add -

# Paso 4: Agregar el repositorio de Docker a las fuentes de APT
$ echo "deb [arch=armhf] https://download.docker.com/linux/raspbian $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list

# Paso 5: Actualizar el índice de paquetes de APT
$ sudo apt-get -y update

# Paso 6: Instalar Docker
$ sudo apt-get -y install docker-ce

# Paso 7: Instalar Docker Compose
$ sudo apt-get -y install docker-compose

# Paso 8: Verificar la instalación de Docker y Docker Compose
$ docker --version
$ docker-compose --version

# Paso 9: Agregar tu usuario al grupo Docker
$ sudo usermod -aG docker ${USER}

# Paso 10: Cerrar sesión y volver a iniciar sesión para aplicar los cambios de grupo
$ sudo reboot
```

📌 *Nota*: Después del reinicio, puedes probar la instalación ejecutando `docker run hello-world`.

---

## Ventajas y Desventajas

### Ventajas
- **Portabilidad**: Los contenedores Docker pueden ejecutarse en distintos entornos sin modificaciones.
- **Facilidad de uso**: Docker Compose permite definir y gestionar aplicaciones complejas con un solo archivo YAML.
- **Eficiencia**: Los contenedores consumen menos recursos que las máquinas virtuales.

### Inconvenientes
- **Recursos**: Aunque ligeros, los contenedores requieren CPU y RAM, lo que puede ser limitante en Raspberry Pi.
- **Curva de aprendizaje**: Requiere conocimiento previo sobre virtualización y despliegue de aplicaciones.

---

## Uso básico

Una vez instalado Docker y Docker Compose, puedes probar su funcionamiento con los siguientes comandos:

```bash
# Probar Docker
$ sudo docker run hello-world

# Crear y ejecutar un contenedor simple
$ sudo docker run -d -p 8080:80 nginx

# Listar los contenedores en ejecución
$ docker ps

# Detener y eliminar un contenedor
$ docker stop <container_id>
$ docker rm <container_id>
```

Para proyectos más complejos, puedes usar Docker Compose con un archivo `docker-compose.yml`:

```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
```

Ejecuta:

```bash
$ docker-compose up -d
```

