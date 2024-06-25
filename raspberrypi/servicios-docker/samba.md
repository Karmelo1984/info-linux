# Samba

![Header](../../img/ima-raspberrypi-servicios-samba-header-01.png)

**Samba** en contenedores Docker simplifica el compartir archivos en tu red local, permitiendo el acceso desde cualquier dispositivo. Al implementarlo en tu Raspberry Pi, obtienes un servidor de archivos centralizado y fácil de mantener. Con Samba, puedes compartir archivos entre sistemas operativos diferentes de manera eficiente y segura, sin la necesidad de configuraciones complicadas. Además, al usar Docker, puedes actualizar y escalar tu entorno de Samba de manera sencilla, asegurando un funcionamiento estable y seguro de tus servicios de compartición de archivos.

[Inicio de sección](#samba) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Samba](#samba)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso](#acceso)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#samba)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/samba/volume/config
mkdir -p /mnt/server                 # Usar como punto de montaje 'mhddfs' posteriormente.
vim ~/docker/samba/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/samba
├── docker-compose.yml
└── volume
    └── config

/
├── ...
├── mnt
│   └── server
└── ...
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#samba)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#samba)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  # ================== Samba
  samba:
    image: dockurr/samba:latest
    container_name: samba       # Nombre del contenedor
    restart: unless-stopped     # Política de reinicio del contenedor

    environment:
      USER: "samba"
      PASS: "secret"

    volumes:
      - config:/etc/samba
      - data:/storage        # Ruta carpeta compartida

    ports:
      - "137:137"               # Puerto protocolo NetBios
      - "138:138"               # Puerto protocolo NetBios
      - "139:139"               # Puerto protocolo SMB
      - "445:445"               # Puerto protocolo SMB

volumes:
  config:                        # Volumen para la configuracion Samba
    driver_opts:
      type: none
      device: ${HOME}/docker/samba/volume/config
      o: bind
  data:                              # Volumen para las series de TV
    driver_opts:
      type: none
      device: /mnt/server              # Montar con mhddfs toda la biblioteca multimedia
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#samba)
<br><br>

# Acceso
El aceso se hace a través de la configuración de equipos de red del equipo desde donde queremos conectarnos.

Con esta configuración se tiene acceso a todos los dipositivos montados en `/media`.

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#samba)
<br><br>