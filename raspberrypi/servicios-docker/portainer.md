# Portainer.io

![Header](../../img/ima-raspberrypi-servicios-portainer-header-01.png)

Portainer es una herramienta de gestión de contenedores basada en web que simplifica la administración de Docker. Con Portainer, puedes controlar y administrar fácilmente tus contenedores Docker desde una interfaz gráfica intuitiva.

Puedes instalar Portainer directamente en tu Raspberry Pi utilizando Docker, lo que facilita la gestión de tus contenedores desde cualquier lugar de tu red. Esta solución es ideal para usuarios que deseen una forma sencilla y eficiente de administrar sus contenedores Docker.


[Inicio de sección](#portainerio) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Portainer.io](#portainerio)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-pihole-docker-composeyml)
- [Acceso](#acceso)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#portainerio)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/portainer/volume/data
vim ~/docker/portainer/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/portainer
├── docker-compose.yml
└── volume
    └── data
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#portainerio)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#portainerio)
<br><br>

# Despliegue `docker-compose.yml`
Dado que el objetivo es instalar `portainer`, necesitamos deplegarlo obligatoriamente haciendo uso de `docker-compose up -d`.

```yaml
version: '3.7'

services:

  # ================== Portainer
  portainer:
    image: portainer/portainer-ce:latest
    container_name: portainer                           # Nombre del contenedor
    restart: unless-stopped                             # Política de reinicio del contenedor
    
    ports:
      - "9000:9000"
      - "9443:9443"
    
    volumes:
      - /etc/localtime:/etc/localtime:ro                # Volumen para sincronizar la zona horaria
      - /var/run/docker.sock:/var/run/docker.sock:ro    # Acceso al socket de Docker
      - data:/data

volumes:
  data:
    driver_opts:
      type: none
      device: ${HOME}/docker/portainer/volume/data
      o: bind

```

[Inicio de sección](#despliegue-pihole-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#portainerio)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry:9443

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#portainerio)
<br><br>