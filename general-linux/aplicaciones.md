

vim
ranger
neofetch
tree
locale


### Grabar vídeo GIF con Peek
Permite algunas opciones como:
- Modificar el atajo de teclado para iniciar y detener la grabación
- Seleccionar el formato de salida entre GIF, MP4 y WebM.
- Definir el retraso en segundos desde que pulsas el botón de grabar o el atajo de teclado, hasta que empieza la grabación. Esto nos da un pequeño margen de tiempo, para preparar todo antes de la grabación.
- El número de fotogramas por segundo.
- La disminución de la resolución.
- Si queremos captarar el ratón.

```bash
sudo add-apt-repository ppa:peek-developers/stable
sudo apt-get update
sudo apt install peek
```


### Encontrar y Eliminar Archivos Duplicados en Linux Usando Fdupes
```bash
sudo apt-get update
sudo apt install fdupes
```

Después de la instalación, podrás utilizar fdupes para encontrar archivos duplicados.

Ejecuta el siguiente comando con la ruta de tu directorio para encontrar archivos duplicados. Este comando solo busca archivos duplicados en la carpeta actual. No realiza búsquedas en subcarpetas ni en otros directorios similares.

fdupes <ruta del directorio>

Ejecute el comando fdupes con la opción -r para encontrar duplicados en toda la carpeta y subcarpetas. La salida muestra que la opción "-r" realiza una búsqueda más exhaustiva de archivos duplicados en las carpetas y subcarpetas.

fdupes -r <ruta del directorio>

También puedes buscar archivos duplicados que no estén vacíos. Te permitirá concentrarte en la tarea y evitar tener que lidiar con archivos vacíos. Utiliza el siguiente comando para habilitar esta opción.

fdupes -n <ruta del directorio>

Traduce las siguientes frases al ESPAÑOL utilizando un tono de voz serio y las reglas gramaticales correctas: -m opción.

fdupes -n <ruta del directorio>

También puede introducir este comando fdupes con la opción -S para obtener información sobre el tamaño de los archivos duplicados.

fdupes -S <ruta del directorio>

Para guardar los resultados del comando fdupes, ejecute el siguiente comando.

fdupes <ruta del directorio> > output.txt

Eliminar archivos duplicados en Linux con fdupes.
Una vez reducidos los duplicados del directorio, utilice el comando fdupes con la opción -d para eliminarlos.

fdupes <ruta del directorio>