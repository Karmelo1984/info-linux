---
title: "Añadir un Disco Duro Externo a una Raspberry Pi"
authors:
  - Carmelo Molero Castillo
date: 2025-03-21
version: 1.0.0
---

# Añadir un Disco Duro Externo

**Descripción**:  
Esta guía explica cómo conectar y configurar un disco duro externo en una Raspberry Pi. Aprenderás a verificar el disco, formatearlo en `ext4` y montarlo de forma automática en cada arranque.

**Características principales**:  
- ✅ **Compatibilidad con distintos sistemas de archivos** - Se explican NTFS, FAT y `ext4`.  
- ✅ **Montaje automático** - Cómo hacer que el disco se monte cada vez que enciendas la Raspberry Pi.  
- ✅ **Configuración de permisos** - Asegura que los usuarios puedan leer y escribir en el disco.  

---

## Instalación

Antes de comenzar, verifica que tu Raspberry Pi tiene acceso al disco duro externo y que puedes ejecutar comandos de administración.

### Requisitos previos
- 📌 **Sistema operativo**: Raspberry Pi OS (o cualquier distribución basada en Linux).  
- 📌 **Acceso**: Se requieren permisos de `sudo`.  

### Comprobar la información del disco
Ejecuta el siguiente comando para verificar los dispositivos de almacenamiento conectados:

```bash
$ lsblk -fm
```
* `lsblk` informa sobre los dispositivos de almacenamiento.
* `-f` informa sobre los sistemas de archivos instalados.
* `-m` informa sobre quién es su propietario, su tamaño, etc.

Esto mostrará una lista de discos y particiones. Si el disco está montado, primero desmonta todas sus particiones:

```bash
$ sudo umount /dev/sdXu
```

---

## Uso

### Opción corta: Montar un disco temporalmente
Si solo necesitas acceder al disco sin configurarlo de forma permanente:

```bash
# Crear punto de montaje
$ sudo mkdir -p /media/backup

# Montar el disco
$ sudo mount /dev/sda1 /media/backup

# Comprobar que el montaje fue exitoso
$ lsblk -fm

# Desmontar antes de desconectarlo
$ sudo umount /mnt/sda
```

### Opción larga: Formatear y montar automáticamente
Si deseas integrar el disco a tu sistema de manera permanente:

#### Formatear en `ext4` (opcional)
Si el disco tiene datos y no quieres perderlos, salta este paso.

```bash
## ¡¡OJO!! Este procedimiento borra el contenido del disco
$ sudo mkfs.ext4 /dev/sdXu
```

#### Establecer un punto de montaje

```bash
# Paso 1: Crea la carpeta donde se montará el disco:
$ sudo mkdir -p /media/backup

# Paso 2: Obtener el UUID del disco
$ lsblk -fm

# Paso 3 (opcional): Añade el disco a `/etc/fstab` para montaje automático al arranque del SO:
$ sudo vim /etc/fstab

# Paso 3b: Añade esta línea (sustituyendo el UUID por el real de tu disco):
UUID=5acb11f9-a5e9-49c3-a225-a872fc688f22 /media/backup ext4 defaults 0 0

# Paso 3c: Reinicia la Raspberry Pi y verifica que el montaje funciona
$ sudo reboot
$ lsblk -fm
```

### Modificación de permisos
Para permitir que todos los usuarios accedan al disco:

```bash
sudo chmod 766 /media/backup
```

---

## Solución de problemas

**Error 1: El disco no se monta automáticamente**  

- Solución: Verifica que `/etc/fstab` está correctamente configurado y que el UUID es correcto.

**Error 2: No se tienen permisos para escribir en el disco**  

- Solución: Ajusta los permisos con `sudo chmod 766 /media/backup`.

---