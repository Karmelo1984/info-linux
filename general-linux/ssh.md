# SSH

![Header](../img/ima-ssh-header-01.png)

SSH (Secure Shell) es un protocolo de red que permite a los usuarios acceder de forma segura a una computadora remota a través de una conexión encriptada. Proporciona un canal seguro sobre una red no segura, como Internet, para realizar tareas como ejecutar comandos, transferir archivos y gestionar sistemas de forma remota.

## ¿Para qué sirve SSH?

* **Acceso Remoto:** Permite acceder a una computadora remota como si estuvieras físicamente frente a ella, lo que facilita la administración de servidores y la resolución de problemas en sistemas remotos.
* **Transferencia de Archivos:** SSH incluye herramientas como SCP (Secure Copy Protocol) y SFTP (SSH File Transfer Protocol), que permiten transferir archivos de manera segura entre sistemas locales y remotos.
* **Túneles Seguros:** SSH puede crear túneles seguros que cifran el tráfico entre dos puntos en una red, lo que es útil para acceder a servicios en una red interna de forma segura desde el exterior.
* **Tareas Automatizadas:** Se puede utilizar en scripts y tareas automatizadas para realizar operaciones en sistemas remotos de manera segura y sin intervención manual.

## Principios Básicos de SSH:

* **Autenticación:** SSH utiliza un sistema de autenticación de clave pública/privada o de contraseña para verificar la identidad del usuario. La autenticación por clave pública/privada es más segura y se recomienda para entornos de producción.
* **Cifrado:** SSH utiliza técnicas de cifrado para proteger la confidencialidad y la integridad de los datos transmitidos entre el cliente y el servidor. Esto garantiza que incluso si los datos son interceptados, no puedan ser leídos por terceros.
* **Puerto Predeterminado:** El puerto TCP estándar para SSH es el 22. Sin embargo, se puede cambiar si es necesario por razones de seguridad o para evitar conflictos con otros servicios en el servidor.
* **Configuración del Servidor:** Para permitir conexiones SSH, el servidor debe tener un servidor SSH instalado y configurado. Normalmente, esto se hace instalando el paquete SSH y ajustando la configuración según sea necesario.

## Conclusión:

SSH es una herramienta fundamental para la administración remota de sistemas y la transferencia segura de archivos en redes no seguras. Proporciona una capa adicional de seguridad al encriptar las comunicaciones entre el cliente y el servidor, lo que protege los datos sensibles de posibles ataques.

[Inicio de sección](#ssh) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
- [SSH](#ssh)
  - [¿Para qué sirve SSH?](#para-qué-sirve-ssh)
  - [Principios Básicos de SSH:](#principios-básicos-de-ssh)
  - [Conclusión:](#conclusión)
- [Índice](#índice)
- [Configurar SSH para el acceso a servidor mediante clave pública](#configurar-ssh-para-el-acceso-a-servidor-mediante-clave-pública)
- [Sección 1](#sección-1)

[<< Página principal >>](../README.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#ssh)
<br><br>

# Configurar SSH para el acceso a servidor mediante clave pública

La configuración de SSH para el acceso mediante clave pública implica generar un par de claves pública y privada en el cliente, y luego configurar el servidor para que acepte la clave pública del cliente como método de autenticación. 

```bash
# Paso 1: Generar un par de claves SSH (Clave pública y privada en ~/.ssh/id_rsa y ~/.ssh/id_rsa.pub.)
ssh-keygen -t rsa

# Paso 2: Copiar la clave pública al servidor remoto
    ## Opción 1 (recomendado):
    ssh-copy-id usuario@servidor
    ## Opción 2:
    cat ~/.ssh/id_rsa.pub | ssh usuario@servidor "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"

# Paso 3: Acceder al servidor remoto sin contraseña
ssh usuario@servidor

```

[Inicio de sección](#configurar-ssh-para-el-acceso-a-servidor-mediante-clave-pública) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#ssh)
<br><br>

# Sección 1



[Inicio de sección](#sección-1) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#ssh)
<br><br>