# Homarr

![Header](../../img/ima-raspberrypi-servicios-homarr-header-01.png)
Homarr es un panel de control versátil y potente para gestionar tu servidor en casa o como la mejor página de inicio para tu navegador favorito. Con Homarr, simplificarás la gestión de tu servidor gracias a su diseño elegante y moderno, que pone todas tus aplicaciones y servicios al alcance de tu mano. Además, cuenta con una comunidad activa de desarrolladores y usuarios, y puedes encontrar más información sobre el proyecto en Github.

Con Homarr, accederás y controlarás todo desde una ubicación conveniente, ya que se integra perfectamente con las aplicaciones que has añadido, proporcionándote información valiosa y un control total. La instalación es sencilla y admite una amplia gama de métodos de despliegue, como su despliegue en Deepin usando Docker, lo que facilita la gestión y escalabilidad de tu servidor.

Implementar Homarr como contenedor Docker proporciona varias ventajas, como la portabilidad, la fácil instalación y la gestión de dependencias. Además, Docker ofrece aislamiento y seguridad para tus aplicaciones, así como la posibilidad de desplegar y actualizar Homarr de forma rápida y eficiente.

[Inicio de sección](#homarr) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Homarr](#homarr)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso](#acceso)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#homarr)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/homarr/volume/{config,icons}
vim ~/docker/homarr/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/homarr
├── docker-compose.yml
└── volume
    ├── config
    └── icons
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#homarr)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#homarr)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  # ================== Homarr
  homarr:
    image: ghcr.io/ajnart/homarr:latest
    container_name: homarr                    # Nombre del contenedor
    restart: unless-stopped                     # Política de reinicio del contenedor

    ports:
      - '7575:7575'

    volumes:
      - config:/app/data/configs
      - icons:/app/public/icons

volumes:
  config:
    driver_opts:
      type: none
      device: ${HOME}/docker/homarr/volume/config
      o: bind
  icons:
    driver_opts:
      type: none
      device: ${HOME}/docker/homarr/volume/icons
      o: bind
```

[Inicio de sección](#despliegue-pihole-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#homarr)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry:7575

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#samba)
<br><br>