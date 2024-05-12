# Raspberry Pi

![Header](../img/ima-raspberrypi-header-01.png)

Raspberry Pi es una serie de computadoras de placa única (SBC, por sus siglas en inglés) desarrolladas por la Raspberry Pi Foundation en el Reino Unido. Estas computadoras ofrecen un bajo costo, bajo consumo de energía y un tamaño compacto, lo que las hace ideales para una variedad de proyectos de electrónica y programación.

## Características Principales:

* ***Tamaño Pequeño:*** El tamaño de una tarjeta de crédito, las Raspberry Pi son increíblemente compactas.
* ***Bajo Costo:*** La Raspberry Pi inicialmente se diseñó con el objetivo de proporcionar una computadora de bajo costo para promover la educación en informática y la programación.
* ***Puertos y Conectividad:*** Las Raspberry Pi están equipadas con una variedad de puertos, incluidos puertos USB, HDMI, Ethernet y GPIO (General Purpose Input/Output), lo que las hace versátiles y fácilmente integrables en proyectos electrónicos.
* ***Flexibilidad:*** Se pueden utilizar con una variedad de sistemas operativos, incluyendo Raspbian (una distribución de Linux optimizada para Raspberry Pi), Ubuntu, y otros sistemas operativos basados en Linux, así como versiones especiales de Windows 10.

## Usos Comunes:

* ***Educación:*** Raspberry Pi se utiliza ampliamente en entornos educativos para enseñar conceptos de informática y programación. Se han desarrollado numerosos recursos educativos y proyectos para apoyar este objetivo.
* ***Proyectos de Electrónica y Robótica:*** Raspberry Pi es popular entre los aficionados y estudiantes de electrónica y robótica. Se utiliza para crear robots, sistemas de automatización del hogar, sistemas de vigilancia, entre otros.
* ***Servidores y Aplicaciones Web:*** Debido a su bajo costo y consumo de energía, algunas personas utilizan Raspberry Pi como servidores web ligeros o para alojar aplicaciones web simples.
* ***Media Center:*** Raspberry Pi puede convertirse fácilmente en un centro multimedia utilizando software como Kodi, permitiendo la reproducción de películas, música y otros medios.

## Conclusión:

Raspberry Pi es una plataforma versátil y asequible que ha ganado popularidad en la comunidad de la electrónica y la programación. Su tamaño compacto, bajo costo y amplia gama de usos lo hacen ideal tanto para proyectos educativos como para aplicaciones prácticas en el hogar y en la industria.

[Inicio de sección](#raspberry-pi ) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
1. [Crear un servidor NAS - OpenMedia Vault](./servidorNAS.md)
2. [Instalar Docker y Docker compose en "Raspberry Pi"](./docker.md)
3. [Utilidades varias](./utilidadespi.md)
4. [Configuración Personalizada de la Instalación](#configuración-personalizada-de-la-instalación)
   
[<< Página principal >>](../README.md)<br>
[Índice](#índice ) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#raspberry-pi)
<br><br>

# Configuración Personalizada de la Instalación
Se optó por configurar dos equipos por dos razones:
1. **Equipo 1:** se centra solo en los servicios DNS y DHCP.
2. **Equipo 2:** se centra en dar servicio como DNS secundario en caso de que el primero falle. Además de alojar el resto de servicios, incluyendo Plex y Samba, para compartir archivos. Realmente funciona como un servidor NAS, pero sin tener instalado ningún software específico de NAS.

## Equipo 1: Raspberry Pi 3 Model B Rev 1.2 

### Características del sistema
```bash
neofetch

  `.::///+:/-.        --///+//-:``    pi@raspberrypi 
 `+oooooooooooo:   `+oooooooooooo:    -------------- 
  /oooo++//ooooo:  ooooo+//+ooooo.    OS: Raspbian GNU/Linux 12 (bookworm) armv7l 
  `+ooooooo:-:oo-  +o+::/ooooooo:     Host: Raspberry Pi 3 Model B Rev 1.2 
   `:oooooooo+``    `.oooooooo+-      Kernel: 6.6.28+rpt-rpi-v7 
     `:++ooo/.        :+ooo+/.`       Uptime: xx hours 
        ...`  `.----.` ``..           Packages: yyy (dpkg) 
     .::::-``:::::::::.`-:::-`        Shell: bash 5.2.15 
    -:::-`   .:::::::-`  `-:::-       Terminal: /dev/pts/0 
   `::.  `.--.`  `` `.---.``.::`      CPU: BCM2835 (4) @ 1.200GHz 
       .::::::::`  -::::::::` `       Memory: 267MiB / 920MiB 
 .::` .:::::::::- `::::::::::``::.      
-:::` ::::::::::.  ::::::::::.`:::-   MicroSD: 8GB                        
::::  -::::::::.   `-::::::::  ::::                           
-::-   .-:::-.``....``.-::-.   -::-
 .. ``       .::::::::.     `..`..
   -:::-`   -::::::::::`  .:::::`
   :::::::` -::::::::::` :::::::.
   .:::::::  -::::::::. ::::::::
    `-:::::`   ..--.`   ::::::.
      `...`  `...--..`  `...`
            .::::::::::
             `.-::::-`
```

### Método para hacer backup
Como se tiene un sistema DNS redundante con `DNS primario` y `DNS secundario` se puede apagar el **equipo 1** el tiempo necesario para hacer una imagen `img` de la tarjeta MicroSD. Además se podrá optimizar el tamaño de la imagen resultante haciendo uso de [`pishrink`](./utilidadespi.md#reducir-imagen-de-microsd).

### Elementos instalados
Este equipo actúa exclusivamente como DNS primario y está conectado directamente al router mediante cable Ethernet.

1. Paquetes importantes instalados:
   * `Docker:` Plataforma de contenedores que permite empaquetar, distribuir y ejecutar aplicaciones de manera eficiente. [`Configuración`](./docker.md).
2. Contenedores docker:
   * `PiHole:` Servidor de DNS que bloquea anuncios y rastreadores en toda la red. [`Configuración`](./servicios-docker/pihole.md).


## Equipo 2: Raspberry Pi 4 Model B Rev 1.4 

### Características del sistema
```bash
neofetch

       _,met$$$$$gg.          naspicar@naspicar 
    ,g$$$$$$$$$$$$$$$P.       ----------------- 
  ,g$$P"     """Y$$.".        OS: Debian GNU/Linux 12 (bookworm) aarch64 
 ,$$P'              `$$$.     Host: Raspberry Pi 4 Model B Rev 1.4 
',$$P       ,ggs.     `$$b:   Kernel: 6.6.28+rpt-rpi-v8 
`d$$'     ,$P"'   .    $$$    Uptime: xxx mins 
 $$P      d$'     ,    $$P    Packages: yyy (dpkg) 
 $$:      $$.   -    ,d$$'    Shell: bash 5.2.15 
 $$;      Y$b._   _,d$P'      Terminal: /dev/pts/0 
 Y$$.    `.`"Y$$$$P"'         CPU: (4) @ 1.800GHz 
 `$$b      "-.__              Memory: 358MiB / 1846MiB
  `Y$$                        
   `Y$$.                      MicroSD: 32GB ó 64GB                        
     `$$b.                                            
       `Y$$b.
          `"Y$b._
              `"""

```

### Método para hacer backup
Como se tiene un sistema DNS redundante con `DNS primario` y `DNS secundario` se puede apagar el **equipo 2** el tiempo necesario para hacer una imagen `img` de la tarjeta MicroSD. Además se podrá optimizar el tamaño de la imagen resultante haciendo uso de [`pishrink`](./utilidadespi.md#reducir-imagen-de-microsd).

Durante el tiempo que el sistema esté apagado, no estarán operativos el resto de servicios, ya que no cuentan con redundancia.

### Elementos instalados
Este equipo actúa como DNS secundario y está conectado al router a través de wifi. En él, se configuran todos los servicios que interesen implementar.

1. Paquetes importantes instalados:
   * `Docker:` Plataforma de contenedores que permite empaquetar, distribuir y ejecutar aplicaciones de manera eficiente. [`Configuración`](./docker.md).
2. Contenedores docker:
   * `Homarr:` Panel de inicio que permite acceder fácilmente a aplicaciones web y servicios en un solo lugar. [`Configuración`](./servicios-docker/homarr.md).
   * `Homebridge:` Puente de software para acceder a dispositivos de hogar inteligente desde la plataforma Apple HomeKit. [`Configuración`](./servicios-docker/homebridge.md).
   * `PiHole:` Servidor de DNS que bloquea anuncios y rastreadores en toda la red. [`Configuración`](./servicios-docker/pihole.md).
   * `Plex:` Servidor de medios que permite organizar, transmitir y acceder a contenido multimedia. [`Configuración`](./servicios-docker/plex.md).
   * `Portainer:` Herramienta de gestión de contenedores Docker con una interfaz web fácil de usar. [`Configuración`](./servicios-docker/portainer.md).
   * `Samba:` Implementación de protocolos de archivos compartidos de Windows para sistemas no Windows. [`Configuración`](./servicios-docker/samba.md).
   * `Watchtower:` Servicio que actualiza automáticamente contenedores Docker con las últimas versiones disponibles [`Configuración`](./servicios-docker/wathtower.md).
   * `Wireguard:` Protocolo VPN de código abierto y de alto rendimiento. [`Configuración`](./servicios-docker/wireguard.md).


[Configuración Personalizada de la Instalación](#configuración-personalizada-de-la-instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice ) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#raspberry-pi)
<br><br>

# Sección 1



[Inicio de sección](#sección-1 ) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice ) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#raspberry-pi)
<br><br>




