---
title: "Desinstalar la aplicación"
authors:
  - Carmelo Molero Castillo
date: 2025-02-09
version: 1.0.0
tags: [historia de usuario, feat, install]
---

# 📜 Desinstalar la aplicación

---

## 📖 Descripción  
**`COMO`** usuario que ya no necesita la aplicación
**`QUIERO`** poder desinstalarla fácilmente
**`PARA`** eliminar la aplicación del sistema sin complicaciones

---

## 🏗 **Épica Relacionada**  
**Parte de la épica:** [EP-0001 - Instalación de la Aplicación](../epic/EP-0001-instalacion.md)

---

## 🎯 **Criterios de Aceptación**  
```gherkin
Feature: Desinstalar la aplicación

  Scenario: La aplicación debe aparecer en la lista de programas instalados
    Given que el usuario accede al panel de control o gestor de aplicaciones
    When busca la aplicación en la lista de programas instalados
    Then debe poder encontrar la aplicación y seleccionar la opción de desinstalación

  Scenario: La aplicación debe ofrecer la opción de crear una copia de seguridad antes de desinstalar
    Given que el usuario ha iniciado el proceso de desinstalación
    When la aplicación detecta que hay datos guardados
    Then debe ofrecer la opción de crear una copia de seguridad antes de continuar con la desinstalación

  Scenario: El proceso de desinstalación debe completarse sin errores
    Given que el usuario ha iniciado la desinstalación
    When se ejecuta el proceso de eliminación de archivos y configuraciones
    Then la aplicación debe eliminarse correctamente sin mostrar errores

  Scenario: Debe mostrarse una confirmación de desinstalación exitosa
    Given que la aplicación ha sido eliminada correctamente
    When finaliza el proceso de desinstalación
    Then debe mostrarse un mensaje indicando que la aplicación ha sido desinstalada con éxito

  Scenario: No deben quedar archivos residuales en el sistema
    Given que la desinstalación se ha completado
    When el usuario revisa la carpeta de instalación
    Then no deben quedar archivos o configuraciones innecesarias en el sistema
```