# Duplicati

![Header](../../img/ima-raspberrypi-servicios-duplicati-header-01.jpg)


[Inicio de sección](#duplicati) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Duplicati](#duplicati)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso y configuración](#acceso-y-configuración)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#duplicati)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/duplicati/volume/config
sudo mkdir -p /mnt/backups
vim ~/docker/duplicati/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/duplicati
├── docker-compose.yml
└── volume
    └── config

/
├── ...
├── mnt
│   └── backups
└── ...
```

[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#duplicati)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#duplicati)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  #================== duplicati
  duplicati:
    image: lscr.io/linuxserver/duplicati:latest
    container_name: duplicati
    restart: unless-stopped

    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Madrid                  # Zona horaria
      # - CLI_ARGS= #optional

    ports:
      - 8001:8200

    volumes:
      - config:/config
      - backups:/backups
      - source:/source

# Definición de volúmenes
volumes:

  config:
    driver_opts:
      type: none
      device: $HOME/docker/duplicati/volume/config
      o: bind
      
  backups: 
    driver_opts:
      type: none
      device: /mnt/backups 
      o: bind
      
  source: 
    driver_opts:
      type: none
      device: $HOME/docker
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#duplicati)
<br><br>

# Acceso y configuración
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry:8200

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#acceso-y-configuración) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#duplicati)
<br><br>