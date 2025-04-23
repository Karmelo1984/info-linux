---
title: "Instalación de la Aplicación"
authors:
  - Carmelo Molero Castillo
date: 2025-04-13
version: 1.0.0
tags: [épica, instalación]
---

# 🏗 EP-0001 - Instalación de la Aplicación

---

[🔙 Volver al índice del proyecto](../index.md) 

---

## 📖 Descripción  
Esta épica cubre todo el proceso de instalación del sistema de gestión para asociaciones. El objetivo es asegurar que, una vez completada, el entorno base esté listo para ejecutar la aplicación por primera vez: estructura de carpetas creada, base de datos inicializada, licencia incluida y ejecutable funcional.

---

## 🎯 Objetivo  
Proporcionar un entorno funcional donde se pueda ejecutar correctamente el software de gestión, con todos los archivos y dependencias preparados.

---

## 🧱 Dependencias Técnicas  
- Python y sus dependencias
- Herramientas de creación de ejecutables (como `PyInstaller`)
- Sistema operativo compatible (Windows/Linux)

---

## 🏗 Historias de usuario relacionadas  
- [HU-0001 - Ejecutar el instalador](../hu/HU-0001-ejecutar-instalador.md)  
- [HU-0002 - Seguir los pasos de instalación](../hu/HU-0002-seguir-pasos-instalacion.md)  
- [HU-0003 - Confirmar instalación exitosa](../hu/HU-0003-confirmar-instalacion-exitosa.md)  
- [HU-0004 - Desinstalar la aplicación](../hu/HU-0004-desinstalar-aplicacion.md)

---

## ✅ Criterios de finalización  
- Se genera la estructura de carpetas básica (`data`, `logs`, `resources`, `license`, etc.)
- Se copia el ejecutable (`dist/`) y los recursos estáticos
- Se incluye una licencia funcional en `license/`
- La base de datos SQLite se crea en `data/db/`
- El usuario puede lanzar el ejecutable correctamente

---

[🔙 Volver al índice del proyecto](../index.md) 
