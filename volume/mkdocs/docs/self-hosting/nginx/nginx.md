---
title: "NGINX"
authors:
  - Carmelo Molero Castillo
date: 2025-04-05
version: 1.0.0
---

# NGINX

![NGINX](img/img-nginx-header-01.png)

**NGINX** es un servidor web de alto rendimiento, también utilizado como proxy inverso, equilibrador de carga y caché HTTP. Es conocido por su eficiencia, bajo consumo de recursos y su capacidad para manejar miles de conexiones simultáneas.

### 🚀 **¿Por qué usar NGINX?**  
✅ **Servidor web ligero y rápido**.  
✅ **Ideal para servir contenido estático**.  
✅ **Soporte de proxy inverso y balanceo de carga**.  
✅ **Amplia comunidad y documentación**.  
✅ **Integración sencilla con Docker**.  
✅ **Configuración flexible y modular**.  

🔹 **Página oficial**: [https://nginx.org](https://nginx.org)  

---

## Instalación

Organizaremos los archivos de NGINX dentro del directorio `~/docker/nginx` para mantener una estructura clara y ordenada.

### Paso 1: Crear estructura de directorios

```bash
mkdir -p ~/docker/nginx/volume/{conf.d,html,logs}
```

### Paso 2: Crear el archivo `docker-compose.yml`

```bash
vim ~/docker/nginx/docker-compose.yml
```

### Paso 3: Estructura de directorios esperada

Antes de iniciar el contenedor, la estructura del sistema de ficheros debería quedar organizada de la siguiente manera:

```bash
$ tree ~

~/docker/nginx
├── docker-compose.yml
└── volume
    ├── conf.d
    ├── html
    └── logs
```

---

## Despliegue de `docker-compose.yml`

Para desplegar el contenedor de **NGINX**, puedes hacerlo tanto desde **Portainer** como desde la línea de comandos usando Docker Compose. Si optas por la segunda opción, ejecuta el siguiente comando para levantar el contenedor:

```bash
$ docker-compose up -d

# Puedes 'bajar' el contenedor mediante
$ docker-compose down

# Puedes ver la salida de log usando
$ docker logs -f <ID_CONTENEDOR>
```

### Contenido del archivo `docker-compose.yml`

Este es el contenido del archivo `docker-compose.yml` que necesitas para configurar tu contenedor de **NGINX**: 

```yaml
services:

  # ================== NGINX
  nginx:
    image: nginx:alpine
    container_name: nginx
    restart: unless-stopped

    ports:
      - 80:80                           # Puerto HTTP
      - 443:443                         # Puerto HTTPS (si se configura)
    
    volumes:
      - html:/usr/share/nginx/html      # Contenido web estático
      - conf:/etc/nginx/conf.d          # Archivos de configuración extra
      - logs:/var/log/nginx             # Archivos de logs

volumes:
  html:
    driver_opts:
      type: none
      device: ~/docker/nginx/volume/html
      o: bind
  conf:
    driver_opts:
      type: none
      device: ~/docker/nginx/volume/conf.d
      o: bind
  logs:
    driver_opts:
      type: none
      device: ~/docker/nginx/volume/logs
      o: bind
```

---

## Configuración adicional

### Archivo de configuración personalizado

Puedes colocar archivos `.conf` dentro de `~/docker/nginx/volume/conf.d`. Por ejemplo, crea uno básico:

```bash
vim ~/docker/nginx/volume/conf.d/default.conf
```

Contenido de ejemplo:

```nginx
server {
    listen 80;
    server_name localhost;

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ =404;
    }
}
```

### Añadir una página web estática

Crea un archivo HTML dentro de `~/docker/nginx/volume/html`:

```bash
echo "<h1>¡Hola desde NGINX en Docker!</h1>" > ~/docker/nginx/volume/html/index.html
```

---

## Acceso

Una vez desplegado, podrás acceder al servidor web introduciendo en tu navegador:

```
http://ip-servidor
```

Sustituye `ip-servidor` por la IP o dominio de tu máquina.

---
