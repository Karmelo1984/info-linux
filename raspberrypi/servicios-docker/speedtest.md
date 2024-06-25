# Header

![Header](../../img/ima-example-header-01.png)


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
mkdir -p ~/docker/speedtest-tracker/volume/{keys,data}
vim ~/docker/speedtest-tracker/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/speedtest-tracker
├── docker-compose.yml
└── volume
    ├── data
    └── keys
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

  # ================== SpeedTest Tracker
    speedtest-tracker:
        image: lscr.io/linuxserver/speedtest-tracker:latest
        container_name: speedtest-tracker
        restart: unless-stopped

        environment:
            - PUID=1000
            - PGID=1000
            - DB_CONNECTION=sqlite
            # - APP_KEY=
            # - SPEEDTEST_SCHEDULE=
            # - SPEEDTEST_SERVERS=
            # - PRUNE_RESULTS_OLDER_THAN=
            # - CHART_DATETIME_FORMAT= 
            # - DATETIME_FORMAT=
            # - APP_TIMEZONE=
            # - TELEGRAM_BOT_TOKEN=
        
        ports:
            - 9080:80
            - 9443:443

        volumes:
            - data:/config
            - keys:/config/keys
    
volumes:
  data:                                  # Volumen para configuración de Pi-hole
    driver_opts:
      type: none
      device: ${HOME}/docker/speedtest-tracker/volume/data
      o: bind
  keys:                              # Volumen para configuración de dnsmasq
    driver_opts:
      type: none
      device: ${HOME}/docker/speedtest-tracker/volume/keys
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#samba)
<br><br>