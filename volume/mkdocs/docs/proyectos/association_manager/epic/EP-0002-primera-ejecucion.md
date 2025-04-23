---
title: "Primera Ejecución del Programa"
authors:
  - Carmelo Molero Castillo
date: 2025-04-13
version: 1.0.0
tags: [épica, configuración inicial]
---

# 🏗 EP-0002 - Primera Ejecución del Programa

---

[🔙 Volver al índice del proyecto](../index.md) 

---

## 📖 Descripción   
Esta épica cubre el comportamiento y configuración del sistema durante su primer arranque, justo después de una instalación exitosa. Aquí se valida la licencia, se activa el sistema, se recopila información básica de la asociación y se inicializa el entorno de trabajo.

---

## 🎯 Objetivo  
Permitir al usuario activar el sistema, ingresar datos esenciales y dejarlo listo para comenzar la operación diaria.

---

## 🧱 Dependencias Técnicas  
- La aplicación debe haber sido instalada (ver [EP-0001](./EP-0001-instalacion.md))
- Debe existir una licencia válida en la carpeta correspondiente

---

## 🏗 Historias de usuario relacionadas  
- [HU-0005 - Verificar archivo de licencia](../hu/HU-0005.md)  
- [HU-0006 - Activar la licencia del programa](../hu/HU-0006.md)  
- [HU-0007 - Confirmar activación exitosa de la licencia](../hu/HU-0007.md)  
- [HU-0008 - Iniciar la aplicación](../hu/HU-0008.md)

---

## ✅ Criterios de finalización  
- Se verifica la presencia y validez de una licencia
- El sistema se activa correctamente y guarda estado
- Se muestra un primer mensaje de bienvenida o configuración inicial
- El sistema queda listo para registrar los primeros datos (ver [EP-0003](./EP-0003.md))

---

[🔙 Volver al índice del proyecto](../index.md) 
