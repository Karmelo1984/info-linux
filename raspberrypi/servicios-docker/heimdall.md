# Heimdall

![Header](../../img/ima-raspberrypi-servicios-heimdall-header-01.png)

Heimdall es un tablero de control web que te permite acceder rápidamente a tus aplicaciones y servicios favoritos desde un único lugar. Es perfecto para organizar y acceder de manera conveniente a tus aplicaciones web, como servidores de medios, herramientas de productividad, foros, y más.

Instalando Heimdall en tu Raspberry Pi, puedes tener un acceso rápido y centralizado a todas tus aplicaciones y servicios, lo que mejora la eficiencia y la comodidad en la gestión de tus servicios en la red local.


[Inicio de sección](#heimdall) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Heimdall](#heimdall)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-pihole-docker-composeyml)
- [Acceso](#acceso)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#heimdall)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/heimdall/volume/config
vim ~/docker/heimdall/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/heimdall
├── docker-compose.yml
└── volume
    └── config
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#heimdall)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#heimdall)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  # ================== Heimdall
  heimdall:
    image: ¿?
    container_name: heimdall                    # Nombre del contenedor
    restart: unless-stopped                     # Política de reinicio del contenedor

    ports:
      - 8500:80                                 # Puerto para la interfaz web (HTTP)
      - 6443:443                                # Puerto para la interfaz web (HTTPS)

    environment:
      - PUID=1000
      - PGID=1000
      - TZ=Europe/Madrid                        # Zona horaria

    volumes:
      - config:/config

volumes:
  config:
    driver_opts:
      type: none
      device: ${HOME}/docker/heimdall/volume/config
      o: bind
```

[Inicio de sección](#despliegue-pihole-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#heimdall)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#heimdall)
<br><br>