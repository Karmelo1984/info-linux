# 20 Comandos Docker que Debes Conocer

![Header](./img/ima-example-header-01.png)

Tu entorno Docker puede ser el Docker Engine de código abierto o la interfaz gráfica de usuario de Docker Desktop. La CLI será tu interfaz principal en un entorno Docker Engine, pero también tendrás acceso a la herramienta de línea de comandos si instalas Docker Desktop.

[Inicio de sección](#20-comandos-docker-que-debes-conocer) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice)
<br><br>

# Índice
1. [docker system]()
2. [docker context]()
3. [docker pause and unpause]()
4. [docker rm]()
5. [docker rmi]()
6. [docker volume]()
7. [docker search]()
8. [docker push]()
9. [docker pull]()
10. [docker ps]()
11. [docker tag]()
12. [docker rename]()
13. [docker commit]()
14. [docker network]()
15. [docker history]()
16. [docker update]()
17. [docker plugin install]()
18. [docker container]()
19. [docker logs]()
20. [docker swarm]()
   

[<< Docker >>](./docker.md)<br>
[Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#20-comandos-docker-que-debes-conocer)
<br><br>

https://kinsta.com/es/blog/comandos-docker/

# Sección 1



[Inicio de sección](#sección-1) &nbsp; &nbsp; - &nbsp; &nbsp; [Índice](#índice) &nbsp; &nbsp; - &nbsp; &nbsp;[Arriba](#20-comandos-docker-que-debes-conocer)
<br><br>





Para limpiar contenedores, imágenes y caché de Docker, puedes seguir estos pasos. Asegúrate de ejecutar estos comandos con cuidado, ya que eliminarán de forma permanente los elementos especificados.

### Limpiar Contenedores

Para eliminar todos los contenedores Docker detenidos, puedes usar el siguiente comando:

```bash
docker container prune
```

Este comando eliminará todos los contenedores detenidos.

Si también deseas eliminar los contenedores en ejecución, puedes usar:

```bash
docker container prune -f
```

### Limpiar Imágenes

Para eliminar imágenes Docker no utilizadas (sin contenedores asociados) y liberar espacio en disco, puedes ejecutar:

```bash
docker image prune
```

Este comando eliminará todas las imágenes no utilizadas.

Si deseas eliminar también las imágenes que están en uso (contenedores activos que dependen de ellas), puedes usar:

```bash
docker image prune -a
```

### Limpiar Caché

Para limpiar la caché de Docker, que incluye volúmenes no utilizados, redes no utilizadas y más, puedes ejecutar:

```bash
docker system prune
```

Este comando te preguntará qué elementos deseas eliminar (volúmenes, redes, etc.). Para forzar la eliminación sin preguntas, utiliza la opción `-f`:

```bash
docker system prune -f
```

### Eliminar Todo (Cuidado)

Si deseas eliminar todos los contenedores detenidos, todas las imágenes no utilizadas y toda la caché en un solo comando, puedes usar:

```bash
docker system prune -a --volumes
```

Este comando eliminará todos los contenedores (tanto detenidos como en ejecución), todas las imágenes no utilizadas y todos los volúmenes no utilizados.

### Verificar Espacio Ocupado y Limpiar Selectivamente

Puedes verificar cuánto espacio está ocupado por contenedores, imágenes y caché utilizando:

```bash
docker system df
```

Esto te mostrará una salida detallada del espacio utilizado por cada categoría.

Para eliminar elementos específicos (por ejemplo, contenedores detenidos pero no en ejecución), puedes usar los comandos de limpieza mencionados anteriormente de manera selectiva.

### Notas Importantes

- **Precaución**: Asegúrate de que realmente deseas eliminar los elementos antes de ejecutar estos comandos, ya que eliminarán los datos de forma permanente.
- **Backup**: Si hay datos importantes en contenedores o volúmenes, asegúrate de hacer un respaldo antes de limpiar.
- **Cuidado con `docker system prune -a --volumes`**: Este comando elimina todos los datos no utilizados, incluidos volúmenes. Utilízalo con precaución para evitar la pérdida de datos importantes.

Siguiendo estos pasos, podrás limpiar eficazmente los contenedores, imágenes y caché no utilizados en tu entorno Docker.