# WatchTower

![Header](../../img/ima-raspberrypi-servicios-watchtower-header-01.png)

Con **Watchtower** puedes actualizar la versión en ejecución de tu aplicación contenerizada simplemente subiendo una nueva imagen a Docker Hub o tu propio registro de imágenes. Watchtower descargará tu nueva imagen, apagará tu contenedor existente de manera controlada y lo reiniciará con las mismas opciones que se usaron cuando fue desplegado inicialmente.


&nbsp; &nbsp; [- Web oficial de WatchTower](https://containrrr.dev/watchtower/)


[Inicio de sección](#watchtower) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [WatchTower](#watchtower)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso y configuración](#acceso-y-configuración)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#watchtower)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/watchtower/volume
vim ~/docker/watchtower/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/watchtower
├── docker-compose.yml
└── volume
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#watchtower)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#watchtower)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  #================== watchtower  
  watchtower:
    image: containrrr/watchtower:latest
    container_name: watchtower        # Nombre del contenedor
    restart: unless-stopped           # Política de reinicio del contenedor
    
    environment:
      - TZ=Europe/Madrid                 # Zona horaria
      - WATCHTOWER_CLEANUP=true          # Remove old images after updetes
      - WATCHTOWER_REMOVE_VOLUMES=true   # Removes anonymous volumes after updating
      - WATCHTOWER_LOG_FORMAT=Pretty     # Sets what logging format to use for console output.
      - WATCHTOWER_POLL_INTERVAL=86400   # Tiempo en seg. (revisa cada día)
      - WATCHTOWER_MONITOR_ONLY=true     # Modo monitor, solo informa

    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#watchtower)
<br><br>

# Acceso y configuración
Está configurado como modo 'Monitor' por lo que no hará ningún cambio. Para  revisar si hay algún contenedor que actualizar, hay que revisar los logs del contenedor de 'watchtower', y en él vendrá la información.

Ejemplo de ejecución:

```bash
time="2024-05-05T18:35:26+02:00" level=info msg="Watchtower 1.7.1"
time="2024-05-05T18:35:26+02:00" level=info msg="Using no notifications"
time="2024-05-05T18:35:26+02:00" level=info msg="Checking all containers (except explicitly disabled with label)"
time="2024-05-05T18:35:26+02:00" level=info msg="Scheduling first run: 2024-05-05 18:35:36 +0200 CEST"
time="2024-05-05T18:35:26+02:00" level=info msg="Note that the first check will be performed in 9 seconds"
time="2024-05-05T18:35:39+02:00" level=info msg="Session done" Failed=0 Scanned=4 Updated=0 notify=no
time="2024-05-05T18:35:49+02:00" level=info msg="Session done" Failed=0 Scanned=4 Updated=0 notify=no
time="2024-05-05T18:35:59+02:00" level=info msg="Session done" Failed=0 Scanned=4 Updated=0 notify=no
```

[Inicio de sección](#acceso-y-configuración) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#watchtower)
<br><br>