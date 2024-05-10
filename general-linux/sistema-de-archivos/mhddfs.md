# MHDDFS

![Header](../../img/ima-mhddfs-header-01.png)

[MHDDFS (Multi-HDD filesystem)](https://romanrm.net/mhddfs) es un sistema de archivos que permite combinar múltiples dispositivos de almacenamiento en uno solo. Es especialmente útil en situaciones donde tienes varios discos duros o particiones y deseas agruparlos en un único punto de montaje para simplificar la gestión del almacenamiento.

## Ventajas
* **Agrupación de almacenamiento:** MHDDFS te permite combinar varios discos duros, particiones o carpetas en un solo punto de montaje, lo que facilita la gestión del almacenamiento.
* **Espacio total disponible:** Al combinar los dispositivos de almacenamiento, obtienes acceso a todo el espacio disponible en ellos como si fuera un único volumen.
* **Balanceo de carga:** MHDDFS puede distribuir los archivos entre los diferentes dispositivos de almacenamiento para mejorar el rendimiento y el equilibrio de carga.
* **Compatibilidad con diferentes tamaños de disco:** No es necesario que los dispositivos de almacenamiento tengan el mismo tamaño o tipo. MHDDFS puede trabajar con dispositivos de diferentes capacidades y velocidades.
* **Disponibilidad independiente:** A pesar de estar montados en una ubicación única, los discos siguen estando disponibles de forma independiente, lo que facilita el acceso y la gestión individual de cada uno.

## Inconvenientes
* **Rendimiento limitado:** Dependiendo de la configuración y la carga de trabajo, el rendimiento de MHDDFS puede ser inferior al de un disco duro único, especialmente en comparación con RAID.
* **Ausencia de redundancia:** MHDDFS no proporciona redundancia de datos. Si uno de los discos falla, podrías perder los datos almacenados en él.
* **Complejidad de configuración:** La configuración inicial de MHDDFS puede ser un poco compleja, especialmente para usuarios principiantes.
* **No es adecuado para todos los casos de uso:** Aunque MHDDFS es útil para la agrupación de almacenamiento, puede no ser la mejor opción para aplicaciones que requieren alta disponibilidad o rendimiento extremo.

## Conclusión
MHDDFS es una herramienta útil para combinar varios dispositivos de almacenamiento en uno solo, lo que simplifica la gestión del almacenamiento y proporciona acceso a un espacio total disponible. Sin embargo, es importante considerar sus limitaciones en términos de rendimiento y redundancia antes de implementarlo en entornos de producción, aunque su capacidad para mantener la disponibilidad independiente de los discos puede suponer una ventaja significativa en entornos caseros.

[Inicio de sección](#mhddfs) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
1. [Instalación](#instalación)
2. [Ejemplos de uso](#ejemplos-de-uso)

[<< Página principal >>](../../README.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#mhddfs)
<br><br>

# Instalación
La instalación en Debian y derivados es bastante sencilla, solo hay que usar el gestor de paquetes.

```bash
sudo apt-get update -y
sudo apt-get install -y mhddfs
```

[Inicio de sección](#instalación) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#mhddfs)
<br><br>

# Ejemplos de uso
## Supuesto 1: ¿Cómo unir unidades de distinta capacidad?
Tenemos tres discos conectados al equipo, con sus respectivos puntos de montaje en ```/media``` o en ```/mnt```

```bash
df -h

# Que nos devuelve como resultado:
Filesystem            Size  Used Avail Use% Mounted on
...
/dev/sda1              80G   50G   30G  63% /media/sda1
/dev/sdb1              40G   35G    5G  88% /media/sdb1
/dev/sdc1              60G   10G   50G  17% /media/sdc1
```
Creamos un directorio que será el nuevo punto de montaje del arreglo mhddfs.

```bash
mkdir -p /media/join

# La opción '-o allow_other' permite hacer visible el nuevo punto de montaje a todos los usuarios
mhddfs /media/sda1,/media/sdb1,/media/sdc1 /media/join -o allow_other

# Que nos devuelve como resultado:
option: allow_other (1)
mhddfs: directory '/media/sda1' added to list
mhddfs: directory '/media/sdb1' added to list
mhddfs: directory '/media/sdc1' added to list
mhddfs: move size limit 4294967296 bytes
mhddfs: mount point '/media/join'
```

Después de ejecutar ```mhddfs``` podermos observar la nueva disposición.
```bash
df -h

# Que nos devuelve como resultado:
Filesystem            Size  Used Avail Use% Mounted on
...
/dev/sda1              80G   50G   30G  63% /media/sda1
/dev/sdb1              40G   35G    5G  88% /media/sdb1
/dev/sdc1              60G   10G   50G  17% /media/sdc1
mhddfs                180G   95G   85G  53% /media/join
```

Se puede observar que el nuevo punto de montaje combina el espacio de todos los discos (en este ejemplo 180 GB). 

En este caso el funcionamiento de ```mhddfs``` es similar al de un RAID pero dejando la opción de poder trabajar con cada unidad de manera independiente.

## Supuesto 2: ¿Cómo unir unidades de distinto origen?
En este caso vamos a trabajar un el siguiente escenario.

```bash
# Configuración inicial
Disco rígido            --> /media/sda1
Disco temporal (tmpfs)  --> /media/temp1
Conexión NFS            --> /media/nfs1
```

Después de ejecutar ```mhddfs``` podermos observar la nueva disposición.
```bash
mkdir -p /media/join

# La opción '-o allow_other' permite hacer visible el nuevo punto de montaje a todos los usuarios
mhddfs /media/sda1,/media/temp1,/media/nfs1 /media/join -o allow_other

# Que nos devuelve como resultado:
option: allow_other (1)
mhddfs: directory '/media/sda1' added to list
mhddfs: directory '/media/temp1' added to list
mhddfs: directory '/media/nfs1' added to list
mhddfs: move size limit xxxxxxxxxxxx bytes
mhddfs: mount point '/media/join'
```

## Supuesto 3: Montar automáticamente las unidades, durante el arranque
Sólo debemos escribir al final del archivo ```/etc/fstab``` los parámetros del punto de montaje correspondiente. 

¡¡OJO!! Hay que tener en cuenta que todas las unidades deben estar montadas antes que mhddfs.

```bash
mhddfs /media/sda1,/media/temp1,/media/nfs1 /media/join fuse defaults,noatime,allow_other 0 0
```

Para finalizar una vez que tenemos el punto de montaje operativo podemos exportarlo mediante NFS o Samba, lo cual nos permite compartir la información de una forma rápida y sencilla.


[Inicio de sección](#ejemplos-de-uso) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#mhddfs)
<br><br>