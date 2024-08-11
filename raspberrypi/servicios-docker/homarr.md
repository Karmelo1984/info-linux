# Homarr

![Header](../../img/ima-raspberrypi-servicios-homarr-header-01.png)

***Un panel de control sencillo pero poderoso para tu servidor.***

Simplifica la gestión de tu servidor con **Homarr**: un panel de control moderno y elegante que pone todas tus aplicaciones y servicios al alcance de tu mano. Con **Homarr**, puedes acceder y controlar todo desde un solo lugar conveniente. **Homarr** se integra perfectamente con las aplicaciones que has añadido, proporcionándote información valiosa y dándote control total. La instalación es muy fácil, y **Homarr** admite una amplia variedad de métodos de implementación.

&nbsp; &nbsp; [- Web oficial de Homarr](https://homarr.dev/)

[Inicio de sección](#homarr) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Homarr](#homarr)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso y configuración](#acceso-y-configuración)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#homarr)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/homarr/volume/{config,data,icons}
vim ~/docker/homarr/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/homarr
├── docker-compose.yml
└── volume
    ├── config
    ├── data
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
    container_name: homarr
    restart: unless-stopped

    ports:
      - '8002:7575'

    volumes:
      - /var/run/docker.sock:/var/run/docker.sock # Optional, only if you want docker integration
      - config:/app/data/configs
      - data:/data
      - icons:/app/public/icons

volumes:
  config:
    driver_opts:
      type: none
      device: $HOME/docker/homarr/volume/config
      o: bind
  data:
    driver_opts:
      type: none
      device: $HOME/docker/homarr/volume/data
      o: bind
  icons:
    driver_opts:
      type: none
      device: $HOME/docker/homarr/volume/icons
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#homarr)
<br><br>

# Acceso y configuración
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry:7575

Revisa el siguiente [link](https://homarr.dev/docs/getting-started/after-the-installation) (necesitas conexión a internet).

[Inicio de sección](#acceso-y-configuración) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#homarr)
<br><br>