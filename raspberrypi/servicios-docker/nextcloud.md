# Nextcloud

![Header](../../img/ima-example-header-01.png)




&nbsp; &nbsp; [- Web oficial de ]()


[Inicio de sección](#header) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Nextcloud](#nextcloud)
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
mkdir -p ~/docker/nextcloud/volume/{config,data}
vim ~/docker/nextcloud/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/nextcloud
├── docker-compose.yml
└── volume
    ├── config
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

  # ================== Nextcloud
  nextcloud:
    image: lscr.io/linuxserver/nextcloud:latest
    container_name: nextcloud              # Nombre del contenedor
    restart: unless-stopped                # Política de reinicio del contenedor
    
    environment:
      PUID: 1000                           # ID de usuario
      PGID: 1000                           # ID de grupo
      TZ: Europe/Madrid                    # Zona horaria

    ports:
      - 443:443                            # Puerto para HTTPS
    
    volumes:
      - config:/config                     # Volumen para la configuración de Nextcloud
      - data:/data                         # Volumen para los datos de Nextcloud
    
volumes:
  config:                                  # Volumen para la configuración de Nextcloud
    driver_opts:
      type: none
      device: $HOME/docker/nextcloud/volume/config
      o: bind
  data:                                    # Volumen para los datos de Nextcloud
    driver_opts:
      type: none
      device: $HOME/docker/nextcloud/volume/data
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL https://ip-raspberry:443

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#header)
<br><br>