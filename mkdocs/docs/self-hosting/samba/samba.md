---
title: "Samba"
authors:
  - Carmelo Molero Castillo
date: 2025-03-21
version: 1.0.0
---

# Samba

![Samba](img/img-samba-header-01.png)

**Samba** es un software de código abierto que permite compartir archivos e impresoras en una red entre sistemas **Linux, Windows y macOS**. Funciona implementando el protocolo **SMB (Server Message Block)**, que es el estándar en redes Windows.  

**Samba** en contenedores Docker simplifica el compartir archivos en tu red local, permitiendo el acceso desde cualquier dispositivo. 

### 🎯 **¿Para qué sirve Samba?**  
✅ **Comparte archivos y carpetas** en una red local.  
✅ **Permite que Windows acceda a recursos en servidores Linux**.  
✅ **Actúa como controlador de dominio** en redes empresariales.  
✅ **Facilita la autenticación y gestión de usuarios en red**.  
✅ **Comparte impresoras entre diferentes sistemas operativos**.  

🔹 **Página oficial**: [https://www.samba.org](https://www.samba.org)  
🔹 **Documentación**: [https://wiki.samba.org](https://wiki.samba.org)

---

## Instalación

Todos los ficheros relacionados con nuestra instalación de **Samba** se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

### Paso 1: Crear la estructura de directorios

Para comenzar, crea la estructura de directorios necesaria en tu sistema:

```bash
mkdir -p ~/docker/samba/volume/config
$ sudo mkdir -p /mnt/server
$ sudo chown $(whoami):$(whoami) /mnt/server 
```

### Paso 2: Crear el archivo `docker-compose.yml`

Luego, crea y edita el archivo `docker-compose.yml` en el directorio correspondiente:

```bash
vim ~/docker/samba/docker-compose.yml
```

### Paso 3: Estructura de directorios esperada

Antes de iniciar el contenedor, la estructura del sistema de ficheros debería quedar organizada de la siguiente manera:

```bash
$ tree ~

~/docker/samba
├── docker-compose.yml
└── volume
    └── config

/
├── ...
├── mnt
│   └── server
└── ...
```

---

## Despliegue de `docker-compose.yml`

Para desplegar el contenedor de **Samba**, puedes hacerlo tanto desde **Portainer** como desde la línea de comandos usando Docker Compose. Si optas por la segunda opción, ejecuta el siguiente comando para levantar el contenedor:

```bash
$ docker-compose up -d

# Puedes 'bajar' el contenedor mediante
$ docker-compose down

# Puedes ver la salida de log usando
$ docker logs -f <ID_CONTENEDOR>
```

### Contenido del archivo `docker-compose.yml`

Este es el contenido del archivo `docker-compose.yml` que necesitas para configurar tu contenedor de **Samba**:

```yaml
services:

  # ================== Samba
  samba:
    image: dockurr/samba:latest
    container_name: samba       # Nombre del contenedor
    restart: unless-stopped     # Política de reinicio del contenedor

    environment:
      USER: usuario
      PASS: contraseña

    volumes:
      - config:/etc/samba
      - data:/storage           # Ruta carpeta compartida

    ports:
      - "137:137"               # Puerto protocolo NetBios
      - "138:138"               # Puerto protocolo NetBios
      - "139:139"               # Puerto protocolo SMB
      - "445:445"               # Puerto protocolo SMB

volumes:
  config:                       # Volumen para la configuracion Samba
    driver_opts:
      type: none
      device: ~/docker/samba/volume/config
      o: bind

  data:                         # Volumen para la biblioteca multimedia
    driver_opts:
      type: none
      device: /mnt/server       # Montar con mhddfs toda la biblioteca multimedia
      o: bind
```

---

## Acceso

El aceso se hace a través de la configuración de equipos de red del equipo desde donde queremos conectarnos.

Con esta configuración se tiene acceso a todos los dipositivos montados en `/mnt/server`.