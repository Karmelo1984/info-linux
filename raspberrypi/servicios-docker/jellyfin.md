# Jellyfin

![Header](../../img/ima-raspberrypi-servicios-jellyfin-header-01.png)

`Jellyfin` es un sistema de medios de código abierto que te permite gestionar y transmitir tu contenido multimedia. Es una alternativa a los sistemas propietarios como Emby y Plex, y permite distribuir medios desde un servidor dedicado a dispositivos finales a través de varias aplicaciones. 

Jellyfin se basa en la versión 3.5.2 de Emby y ha sido adaptado al framework .NET Core para ofrecer soporte multiplataforma completo. No requiere licencias premium ni características ocultas: es un proyecto colaborativo que busca mejorar y avanzar en conjunto. 


&nbsp; &nbsp; [- Web oficial de Jellyfin](https://jellyfin.org/docs/)


[Inicio de sección](#jellyfin) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [Jellyfin](#jellyfin)
- [Índice](#índice)
- [Definir ruta de instalación](#definir-ruta-de-instalación)
- [Variables de entorno necesarias](#variables-de-entorno-necesarias)
- [Despliegue `docker-compose.yml`](#despliegue-docker-composeyml)
- [Acceso](#acceso)
- [Configuración de la biblioteca](#configuración-de-la-biblioteca)

[<< Raspberry Pi >>](../raspberrypi.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#jellyfin)
<br><br>

# Definir ruta de instalación
Todas los ficheros relacionados con nuestra instalación se alojarán dentro de un directorio ubicado en `~/docker`, a fin de tener organizado nuestro sistema de ficheros.

```bash
mkdir -p ~/docker/jellyfin/volume/{cache,config}
mkdir -p /mnt/server                 # Usar como punto de montaje 'mhddfs' posteriormente.
vim ~/docker/jellyfin/docker-compose.yml

# Esta es la estructura que debe quedar (antes de iniciar el contenedor)
tree ~

HOME/docker/jellyfin
├── docker-compose.yml
└── volume
    ├── cache
    └── config

/
├── ...
├── mnt
│   └── server
└── ...
```


[Inicio de sección](#definir-ruta-de-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#jellyfin)
<br><br>

# Variables de entorno necesarias
Esta son las variables de entorno que tenemos que definir para poder levantar nuestro contenedor.

```.env
# NO hay variables 'extras' definidas, solo se usan las própias del SO.
```

[Inicio de sección](#variables-de-entorno-necesarias) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#jellyfin)
<br><br>

# Despliegue `docker-compose.yml`
El despliegue se puede hacer tanto desde `portainer` como desde docker compose con el comando `docker-compose up -d`.

```yaml
version: '3.7'

services:

  # ================== Jellyfin
  jellyfin:
    image: lscr.io/linuxserver/jellyfin:latest
    container_name: jellyfin      # Nombre del contenedor
    restart: unless-stopped       # Política de reinicio del contenedor

    environment:
      PUID: 1000                  # ID de usuario en el host
      PGID: 1000                  # ID de grupo en el host
      TZ: Europe/Madrid           # Zona horaria
      #JELLYFIN_PublishedServerUrl: 192.168.0.5  # Dirección IP opcional

    volumes:
      - config:/config            # Volumen para la configuración de Jellyfin
      - data:/data                # Volumen para los datos

    ports:
      - "8096:8096"               # Puerto para la interfaz web
      - "8920:8920"               # Puerto opcional para HTTPS
      - "7359:7359/udp"           # Puerto opcional para auto-detección
      - "1900:1900/udp"           # Puerto opcional para DLNA

    extra_hosts:
      - 'host.docker.internal:host-gateway'  # Host adicional para la red interna del contenedor

volumes:
  config:                         # Volumen para la configuración de Jellyfin
    driver_opts:
      type: none
      device: $HOME/docker/jellyfin/volume/config
      o: bind

  data:                       # Volumen para los datos
    driver_opts:
      type: none
      device: /mnt/server
      o: bind

```

[Inicio de sección](#despliegue-docker-composeyml) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#jellyfin)
<br><br>

# Acceso
El aceso se hace mediante navegador web a través de la URL http://ip-raspberry:8096

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#jellyfin)
<br><br>

# Configuración de la biblioteca
Puedes ver la configuración de medios en la [documentación oficial](https://jellyfin.org/docs/general/server/devices). Aunque aquí muestro la estructura base que debes tener en los HDD's para que sea reconocible.


```bash
/mnt/server
    ├── Books
    │   ├── Audiobooks
    │   │   ├── Author
    │   │   │   ├── Book1.flac
    │   │   │   └── Book2.flac
    │   │   └── Book
    │   │       ├── Chapter1.flac
    │   │       └── Chapter2.flac
    │   └── Books
    │       └── Author
    │           ├── Book1.epub
    │           ├── Book2.epub
    │           ├── Book
    │           │   ├── Book1.epub
    │           │   ├── cover.ext
    │           │   └── metadata.opf
    │           └── Book3.mp3
    ├── Comics
    │   ├── Plastic Man #002 (1944).cbz
    │   ├── Attack on Titan #001 (2012).cbz
    │   └── Comic (2008)
    │       ├── ComicInfo.xml
    │       └── Comic #001 (2008).cbr
    ├── Movies
    │   ├── Film (1990).mp4
    │   ├── Film (1994).mp4
    │   ├── Film (2008)
    │   │   └── Film.mkv
    │   └── Film (2010)
    │   │   ├── Film-cd1.avi
    │   │   └── Film-cd2.avi
    │   ├── Best_Movie_Ever (2019)
    │   │   ├── Best_Movie_Ever (2019) - 1080P.mp4
    │   │   ├── Best_Movie_Ever (2019) - 720P.mp4
    │   │   └── Best_Movie_Ever (2019) - Directors Cut.mp4
    │   └── Movie (2021) [imdbid-tt12801262]
    │       ├── Movie (2021) [imdbid-tt12801262] - 2160p.mp4
    │       ├── Movie (2021) [imdbid-tt12801262] - 1080p.mp4
    │       └── Movie (2021) [imdbid-tt12801262] - Directors Cut.mp4
    ├── Music
    │   ├── Some Artist
    │   │   ├── Album A
    │   │   │   ├── Song 1.flac
    │   │   │   ├── Song 2.flac
    │   │   │   └── Song 3.flac
    │   │   └── Album B
    │   │       ├── Track 1.m4a
    │   │       ├── Track 2.m4a
    │   │       └── Track 3.m4a
    │   └── Album X
    │       ├── Disc 1 Track 1.ogg
    │       ├── Disc 1 Track 2.ogg
    │       ├── Disc 2 Track 1.ogg
    │       ├── Disc 3 Track 1.ogg
    │       ├── Disc 3 Track 2.ogg
    │       └── Disc 3 Track 3.ogg
    └── Shows
        ├── Series Name A (2010)
        │   ├── Season 00
        │   │   ├── Some Special.mkv
        │   │   ├── Series Name A S00E01.mkv
        │   │   └── Series Name A S00E02.mkv
        │   ├── Season 01
        │   │   ├── Series Name A S01E01-E02.mkv
        │   │   ├── Series Name A S01E03.mkv
        │   │   └── Series Name A S01E04.mkv
        │   └── Season 02
        │       ├── Series Name A S02E01.mkv
        │       ├── Series Name A S02E02.mkv
        │       ├── Series Name A S02E03 Part 1.mkv
        │       └── Series Name A S02E03 Part 2.mkv
        └── Series Name B (2018)
            ├── Season 01
            │   ├── Series Name B S01E01.mkv
            │   └── Series Name B S01E02.mkv
            └── Season 02
                ├── Series Name B S02E01-E02.mkv
                └── Series Name B S02E03.mkv
```

[Inicio de sección](#acceso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#jellyfin)
<br><br>