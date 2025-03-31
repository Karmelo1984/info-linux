---
title: "Actores del Sistema"
authors:
  - Carmelo Molero Castillo
date: 2025-03-21
version: 1.0.0
tags: [actores, roles]
---

# 👥 Actores del Sistema  

En esta sección se describen los actores que interactúan con la aplicación.

---

[🔙 Volver al índice del proyecto](./index.md) 

---

## 👤 **Administrador**
El administrador del sistema (en este caso, el propietario del software) tiene acceso completo a todas las funcionalidades del sistema de licencias. Sus principales responsabilidades son:

- **Generar licencias**: Crear nuevas licencias asociadas a empresas y generar los archivos JSON encriptados correspondientes.
- **Gestionar licencias**: Ver, modificar y eliminar licencias existentes.
- **Renovar licencias**: Modificar la fecha de expiración y otros parámetros de una licencia según las necesidades de la empresa.
- **Gestionar empresas**: Añadir, editar o eliminar empresas asociadas a las licencias generadas.
- **Gestionar características**: Asignar o eliminar funcionalidades de las licencias disponibles para cada empresa.

## 👤 **Sistema de Licencias**

El sistema actúa de manera autónoma y se encarga de realizar ciertas acciones automáticas, como la encriptación y desencriptación de las licencias generadas. El sistema realiza las siguientes funciones:

- **Encriptar licencias**: Genera archivos JSON con la información de la licencia y los encripta utilizando un sistema de claves públicas y privadas.
- **Desencriptar licencias**: Permite al administrador visualizar la información de una licencia en su formato legible desencriptando el archivo JSON.
- **Almacenar información**: Guarda las licencias generadas, las empresas y las características asociadas en la base de datos SQLite.

---

[🔙 Volver al índice del proyecto](./index.md) 

---
