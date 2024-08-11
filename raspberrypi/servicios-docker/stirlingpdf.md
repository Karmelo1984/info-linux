# Stirling-PDF

![Header](../../img/ima-example-header-01.png)




&nbsp; &nbsp; [- Web oficial de Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)


[Inicio de sección](#stirling-pdf) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Stirling-PDF](#stirling-pdf)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso](#acceso)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#stirling-pdf)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/stirlingpdf/volume/{tessdata,configs}
vim ~/docker/stirlingpdf/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/stirlingpdf
├── docker-compose.yml
└── volume
    ├── tessdata
    └── configs
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#stirling-pdf)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#stirling-pdf)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  #================== stirling-pdf
  stirling-pdf:
    image: frooodle/s-pdf:latest
    container_name: stirlingpdf
    restart: unless-stopped

    environment:
      - DOCKER_ENABLE_SECURITY=false
      - INSTALL_BOOK_AND_ADVANCED_HTML_OPS=false
      - LANGS=es_ES

    ports:
      - '8086:8080'

    volumes:
      - ./trainingData:/usr/share/tessdata #Required for extra OCR languages
      - ./extraConfigs:/configs
#      - ./customFiles:/customFiles/
#      - ./logs:/logs/

# Definición de volúmenes
volumes:
  tessdata:
    driver_opts:
      type: none
      device: $HOME/docker/stirlingpdf/volume/tessdata
      o: bind

  configs:
    driver_opts:
      type: none
      device: $HOME/docker/stirlingpdf/volume/configs
      o: bind
```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#stirling-pdf)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#stirling-pdf)
<br><br>