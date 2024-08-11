#!/bin/bash

# Definir el directorio base
path_base=~/docker

# Definir los servicios de docker y sus respectivos directorios
docker_stacks=(
    "duplicati config"
    "homarr {config,data,icons}"
    "homebridge config"
    "pihole {etc,dnsmasq,logs}"
    "portainer data"
    "samba config"
    "speedtest-tracker data"
    "watchtower"
    "watchyourlan data"
)

# Función para registrar mensajes de log
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

log "Inicio del proceso de creación de directorios y archivos docker-compose.yml."

# Crear directorios y archivos docker-compose.yml
for entry in "${docker_stacks[@]}"; do

    # Dividir la entrada en componentes de servicio y directorios
    service=$(echo "$entry" | awk '{print $1}')
    dirs=$(echo "$entry" | awk '{print $2}')

    # Generar los path
    path_service="$path_base/$service"
    path_service_volume="$path_service/volume"

    # Generar path de volumenes
    if [ -n "$dirs" ]; then
        path_service_volume="$path_service_volume/$dirs"
    fi

    # Crear los directorios
    mkdir -p "$path_service_volume"
    log "['$service'] Creado path 'Volumes': $path_service_volume"

    # Crear el archivo docker-compose.yml
    touch "$path_service/docker-compose.yml"
    log "['$service'] Creado 'fichero vacío' 'docker-compose.yml' en: $path_service/docker-compose.yml"

done

log "Todos los directorios y archivos se han creado correctamente."

