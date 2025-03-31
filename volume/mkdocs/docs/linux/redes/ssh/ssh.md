---
title: "Guía de SSH"
authors:
  - Carmelo Molero Castillo
date: 2025-03-21
version: 1.0.0
---

# Guía de SSH

![Header](img/img-ssh-header-01.png)

**Descripción**:  
SSH (Secure Shell) es un protocolo de red que permite a los usuarios acceder de forma segura a una computadora remota a través de una conexión encriptada. Proporciona un canal seguro sobre una red no segura, como Internet, para realizar tareas como ejecutar comandos, transferir archivos y gestionar sistemas de forma remota.

SSH es una herramienta fundamental para la administración remota de sistemas y la transferencia segura de archivos en redes no seguras. Proporciona una capa adicional de seguridad al encriptar las comunicaciones entre el cliente y el servidor, lo que protege los datos sensibles de posibles ataques.

**Características principales**:  
- ✅ **Acceso Remoto** - Permite administrar servidores y solucionar problemas en sistemas remotos.  
- ✅ **Transferencia de Archivos** - Usa SCP y SFTP para transferir archivos de forma segura.  
- ✅ **Túneles Seguros** - Cifra el tráfico entre dos puntos en una red para acceso seguro.  
- ✅ **Automatización de Tareas** - Se integra en scripts para ejecución de comandos remotos.  

---

## Instalación

Antes de usar SSH, asegúrate de cumplir con los **requisitos previos**:

### Requisitos previos
- 📌 **Sistema operativo compatible**: Linux, macOS y Windows (con OpenSSH).  
- 📌 **Dependencias**: OpenSSH instalado tanto en cliente como en servidor.  
- 📌 **Acceso**: Se requieren permisos de administrador para la configuración del servidor SSH.  

### Instalación en Linux / macOS

```bash
# Instalar OpenSSH en Debian/Ubuntu
sudo apt update && sudo apt install openssh-server -y

# Verificar estado del servicio
sudo systemctl status ssh
```

### Instalación en Windows

Si usas Windows, puedes habilitar OpenSSH desde PowerShell:

```powershell
# Habilitar OpenSSH
Get-WindowsFeature -Name OpenSSH* | Install-WindowsFeature
```

📌 *Nota*: En Windows, también puedes usar herramientas como PuTTY para conectar vía SSH.

---

## Uso de SSH

### Conectarse a un servidor remoto

```bash
ssh usuario@servidor
```

Si el puerto SSH ha sido cambiado:

```bash
ssh -p PUERTO usuario@servidor
```

---

## Configurar SSH para el acceso a servidor mediante clave pública

SSH permite autenticarse sin contraseña mediante claves públicas. Para configurarlo:

```bash
# Paso 1: Generar un par de claves SSH
ssh-keygen -t rsa

# Paso 2: Copiar la clave pública al servidor remoto
ssh-copy-id usuario@servidor

# Paso 3: Acceder al servidor sin contraseña
ssh usuario@servidor
```

📌 *Nota*: Si `ssh-copy-id` no está disponible, puedes copiar manualmente la clave:

```bash
cat ~/.ssh/id_rsa.pub | ssh usuario@servidor "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys"
```

---

## Configuración Avanzada

Para mejorar la seguridad, puedes modificar la configuración de SSH editando:

```bash
sudo nano /etc/ssh/sshd_config
```

Recomendaciones:  
- 🔒 **Cambiar el puerto predeterminado** (`Port 2222` en lugar de `22`).  
- 🔒 **Deshabilitar login como root** (`PermitRootLogin no`).  
- 🔒 **Permitir solo autenticación con clave** (`PasswordAuthentication no`).  

Reinicia SSH para aplicar cambios:

```bash
sudo systemctl restart ssh
```

---

## Solución de Problemas

**Error: "Connection refused"**  
🔹 Solución: Verifica que el servicio SSH esté activo con:

```bash
sudo systemctl status ssh
```

**Error: "Permission denied (publickey)"**  
🔹 Solución: Asegúrate de que la clave pública esté en `~/.ssh/authorized_keys` en el servidor.

---

## **Aplicaciones Prácticas de SSH**  

SSH permite muchas aplicaciones avanzadas más allá del acceso remoto. Aquí te mostramos algunos ejemplos útiles:  

### **Montar una carpeta remota con SSHFS**  
Si necesitas acceder a archivos de un servidor como si fueran locales, puedes usar **SSHFS**.  

#### **Ejemplo: Acceder a una base de datos SQLite con DBeaver**  

1. **Instala SSHFS en tu máquina local:**  
   ```bash
   sudo apt install sshfs
   ```  
2. **Monta la carpeta remota en tu máquina local:**  
   ```bash
   mkdir ~/jellyfin_db
   sshfs mediauser@192.168.1.140:/home/mediauser/docker/jellyfin/volume/config/data ~/jellyfin_db
   ```  
3. **Abre DBeaver y selecciona el archivo:**  
   - Ve a `~/jellyfin_db/jellyfin.db` y ábrelo como base de datos SQLite.  
4. **Desmontar la carpeta cuando termines:**  
   ```bash
   fusermount -u ~/jellyfin_db
   ```  
   