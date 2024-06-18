# Plex

![Header](../../img/ima-raspberrypi-servicios-plex-header-01.png)

Plex es una plataforma de gestión y reproducción de contenido multimedia que te permite organizar, almacenar y acceder a tus películas, programas de televisión, música y fotos desde cualquier dispositivo. 

Utilizando un contenedor Docker, Plex ofrece una forma flexible y escalable de implementar su servidor, lo que facilita su instalación, actualización y mantenimiento. Además, Docker proporciona a Plex un entorno aislado, lo que garantiza una mayor seguridad y estabilidad del sistema, y permite una fácil migración entre diferentes sistemas operativos y plataformas de hardware sin afectar la configuración.

En resumen, Plex simplifica la forma en que consumes tu entretenimiento digital al centralizar y organizar tu contenido multimedia en un solo lugar, permitiéndote acceder a él de manera fácil y conveniente desde una amplia variedad de dispositivos. Y al utilizar contenedores Docker, obtienes ventajas adicionales como una instalación y mantenimiento simplificados, mayor seguridad y flexibilidad en la implementación.


[Inicio de sección](#plex) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Plex](#plex)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso](#acceso)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#plex)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/plex/volume/config
mkdir -p /mnt/server                 # Usar como punto de montaje 'mhddfs' posteriormente.
vim ~/docker/plex/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/plex
├── docker-compose.yml
└── volume
    └── config

/
├── ...
├── mnt
│   └── server
└── ...
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#plex)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#plex)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

Antes de continuar, debes visitar [https://www.plex.tv/claim/](https://www.plex.tv/claim/) y obtener un `Claim Code`.

```yaml
version: '3.7'

services:

  #================== Plex
  plex:
    image: greensheep/plex-server-docker-rpi:latest
    container_name: plex              # Nombre del contenedor
    restart: unless-stopped           # Política de reinicio del contenedor

    ports:
      - "32400:32400"
      
    volumes:
      - config:/config
      - data:/data

# Definición de volúmenes
volumes:
  config:                        # Volumen para la configuración Plex
    driver_opts:
      type: none
      device: ${HOME}/docker/plex/volume/config
      o: bind
  data:                              # Volumen para contenido multimedia
    driver_opts:
      type: none
      device: /mnt/server              # Montar con mhddfs toda la biblioteca multimedia
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#plex)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry:32400/web


[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#plex)
<br><br>