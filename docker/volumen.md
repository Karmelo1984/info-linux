# Volúmenes Docker

![Encabezado](../img/ima-docker-header-volume-01.png)

Los volúmenes en Docker son un mecanismo para persistir datos generados por contenedores, permitiendo que estos datos sobrevivan a la terminación o eliminación de los contenedores que los crearon. Son una forma de compartir datos entre contenedores o entre el host y los contenedores de Docker.

## ¿Por qué usar volúmenes en Docker?
* ***Persistencia de Datos:*** Los volúmenes permiten que los datos persistan más allá del ciclo de vida de un contenedor. Esto es esencial para aplicaciones que necesitan almacenar datos de manera permanente, como bases de datos, archivos de configuración, o registros.
* ***Compartir Datos entre Contenedores:*** Los volúmenes facilitan el intercambio de datos entre múltiples contenedores. Esto es útil en entornos donde varios contenedores necesitan acceder a los mismos datos, como en aplicaciones distribuidas o microservicios.
* ***Aislamiento y Portabilidad:*** Los volúmenes permiten aislar los datos del contenedor, lo que facilita la migración de aplicaciones entre diferentes entornos de desarrollo, pruebas y producción.

## Tipos de Volúmenes en Docker
Docker ofrece varios tipos de volúmenes para satisfacer diferentes necesidades:
1. ***Volúmenes de Docker:*** Son directorios creados y gestionados por Docker. Se almacenan en la ubicación predeterminada del sistema de archivos del host.
2. ***Volúmenes de Host:*** Permiten montar un directorio o archivo del sistema de archivos del host directamente en un contenedor.
3. ***Volúmenes de Bind:*** Similar a los volúmenes de host, pero más flexibles. Permiten montar un directorio o archivo específico del sistema de archivos del host en un contenedor.

## Gestión de Volúmenes en Docker
La gestión de volúmenes en Docker se realiza a través de comandos CLI o mediante la definición de volúmenes en archivos de Docker Compose. Esto permite crear, listar, inspeccionar y eliminar volúmenes según sea necesario.

## Conclusión
Los volúmenes en Docker son una característica esencial para manejar datos persistentes y compartirlos entre contenedores y el host. Proporcionan flexibilidad, portabilidad y facilitan la gestión de datos en entornos de contenedores. Dominar el uso y la gestión de volúmenes es fundamental para desarrollar y desplegar aplicaciones Docker de manera efectiva.

[Inicio de sección](#volúmenes-docker ) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
1. [Backup de volúmenes docker](#backup-de-volúmenes-docker)
2. []()
3. []()

[<< Docker >>](docker.md)<br>
[Inicio de sección](#índice) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

## Backup de volúmenes docker
Apartado que explica como podemos generar un backup de un volumen, a fin de ponder guardarlo, transportarlo y restaurarlo, bien en el mismo equipo, bien en otro equipo para mantener la misma configuración.

### Elementos clave

- `Busybox:` Imagen minimalista que contiene utilidades de Unix necesarias para respaldar y restaurar.
- `docker run:` Comando para crear y ejecutar contenedores Docker.
- `--rm:` Opción para eliminar automáticamente el contenedor después de su uso.
- `-v <nombre_del_volumen>:/data:` Monta el volumen dentro del contenedor.
- `-v <ruta_destino_backup>:/backup:` Monta un directorio del host para almacenar el respaldo.
- `tar czf:` Comando para crear el archivo de respaldo del volumen.
- `tar xzf:` Comando para extraer el volumen desde el archivo de respaldo.
- `-C /:` Opción para especificar el directorio donde se extraerán los archivos.

#### Hacer backup
```bash
# Variables
nombre_del_volumen="<nombre_del_volumen>"
ruta_destino_backup="/ruta/destino/backup"

# 1. Detener los contenedores asociados
docker-compose stop

# 2. Crear un directorio para el backup si no existe
mkdir -p $ruta_destino_backup

# 3. Crear un archivo de respaldo del volumen
docker run --rm -v $nombre_del_volumen:/data -v $ruta_destino_backup:/backup busybox tar czf /backup/$nombre_del_volumen.tar.gz /data
```

#### Restaurar backup
```bash
# Variables
nombre_del_volumen="<nombre_del_volumen>"
ruta_origen_backup="/ruta/origen/backup"

# 1. Detener los contenedores asociados
docker-compose stop

# 2. Importar el volumen desde el archivo de respaldo
docker run --rm -v $nombre_del_volumen:/data -v $ruta_origen_backup:/backup busybox tar xzf /backup/$nombre_del_volumen.tar.gz -C /
```

[Inicio de sección](#backup-de-volúmenes-docker ) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#volúmenes-docker)
<br><br>