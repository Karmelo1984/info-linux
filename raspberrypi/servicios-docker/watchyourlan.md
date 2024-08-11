# Header

![Header](../../img/ima-example-header-01.png)




&nbsp; &nbsp; [- Web oficial de ](https://github.com/aceberg/WatchYourLAN)


[Inicio de sección](#header) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Header](#header)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso](#acceso)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/watchyourlan/volume/data
vim ~/docker/watchyourlan/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/watchyourlan
├── docker-compose.yml
└── volume
    └── data
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  #================== watch your lan
  watchyourlan:
    image: aceberg/watchyourlan:latest
    container_name: watchyourlan
    restart: unless-stopped

    environment:
      TZ: Europe/Madrid                 # Zona horaria
      IFACE: "eth0"                     # required: 1 or more interface !!! OJO poner la del equipo donde se monta el contenedor
      DBPATH: "/data/db.sqlite"         # optional, default: /data/db.sqlite
      GUIPORT: "8004"                   # optional, default: 8840
      TIMEOUT: "120"                    # optional, time in seconds, default: 60

    network_mode: "host"  

    volumes:
    - data:/data

# Definición de volúmenes
volumes:
  data:
    driver_opts:
      type: none
      device: $HOME/docker/watchyourlan/volume/data
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry:8004

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>