---
title: "Guía de Git"
authors:
  - Carmelo Molero Castillo
date: 2025-03-30
version: 1.0.0
---

# Guía de Git

![Git Header](img/img-git-header-01.png)

**Descripción**:  
Git es un sistema de control de versiones distribuido que permite gestionar el historial de cambios en un proyecto de software. Facilita la colaboración entre desarrolladores, permitiendo realizar seguimientos, fusionar cambios y revertir versiones si es necesario.

---

## Instalación

Antes de usar Git, asegúrate de cumplir con los **requisitos previos**.

### Requisitos previos
- 📌 **Sistema operativo compatible**: Linux, macOS y Windows.  
- 📌 **Acceso a terminal o consola de comandos**.  
- 📌 **Conexión a Internet** (para operaciones remotas).  

### Instalación en Linux
```bash
# En distribuciones basadas en Debian/Ubuntu
sudo apt update && sudo apt install git -y

# En distribuciones basadas en Red Hat/Fedora
sudo dnf install git -y
```

### Instalación en macOS
```bash
brew install git
```

### Instalación en Windows
Descarga el instalador desde [git-scm.com](https://git-scm.com/) y sigue las instrucciones.

---

## Uso de Git

### Configurar Git
Tras instalar Git, es importante configurarlo con tu identidad:

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tuemail@example.com"
```

Verifica la configuración:
```bash
git config --list
```

### Inicializar un repositorio
```bash
git init
```

### Clonar un repositorio existente
```bash
git clone URL_DEL_REPO
```

### Ver estado del repositorio
```bash
git status
```

### Agregar cambios al área de preparación (staging)
```bash
git add archivo.txt  # Agregar un archivo

git add .  # Agregar todos los archivos modificados
```

### Confirmar cambios (commit)
```bash
git commit -m "Mensaje del commit"
```

### Ver historial de commits
```bash
git log --oneline --graph
```

### Enviar cambios al repositorio remoto
```bash
git push origin main  # Enviar cambios a la rama principal
```

### Obtener cambios del repositorio remoto
```bash
git pull origin main
```

---

## Configuración Básica

Para mejorar el uso de Git, puedes definir alias para comandos frecuentes:

```bash
git config --global alias.st "status"
git config --global alias.co "checkout"
git config --global alias.br "branch"
git config --global alias.cm "commit -m"
```

---

## Configuración Avanzada

### Trabajar con ramas

Crear una nueva rama:
```bash
git branch nueva-rama
```

Cambiar a otra rama:
```bash
git checkout nueva-rama
```

Fusionar ramas:
```bash
git merge otra-rama
```

Eliminar una rama:
```bash
git branch -d nombre-rama
```

#### Crear una rama basada en `main` sin cambiarte de rama
Si estás trabajando en otra rama y necesitas crear una nueva rama a partir de `main`, puedes hacerlo así:

```bash
git fetch origin main
git branch nueva-rama origin/main
```

Esto crea una nueva rama local `nueva-rama` basada en el estado remoto actual de `main` sin necesidad de salir de tu rama actual.

#### Crear una etiqueta (tag) del estado actual de `main`
Para marcar el estado actual de la rama `main` con una etiqueta, por ejemplo `v1.0.0`:

```bash
git tag v1.0.0 origin/main
git push origin v1.0.0
```

Esto es útil para versionar hitos importantes en el proyecto.

### Restablecer cambios
Revertir cambios no confirmados:
```bash
git checkout -- archivo.txt
```

Deshacer un commit:
```bash
git reset --soft HEAD~1  # Mantiene cambios en staging

git reset --hard HEAD~1  # Borra cambios por completo
```

---

## Estándar de Commits
Para mantener un historial de cambios claro, es recomendable seguir el estándar **Conventional Commits**:

### **Estructura de un Commit**
```plaintext
<tipo>(<área>): <breve descripción>

[opcional] Descripción más detallada en párrafos adicionales.

[opcional] Closes #[número de issue] | Relates to #[número de issue]
```

### **Tipos de Commit**
| Tipo       | Descripción |
|------------|------------|
| `feat`     | Nueva funcionalidad |
| `fix`      | Corrección de error |
| `docs`     | Cambios en la documentación |
| `style`    | Cambios de formato (sin afectar código funcional) |
| `refactor` | Refactorización del código (sin cambios en funcionalidad) |
| `test`     | Agregar o modificar pruebas |
| `chore`    | Tareas de mantenimiento (sin afectar código fuente) |
| `perf`     | Mejoras de rendimiento |
| `ci`       | Cambios en configuración de integración continua |
| `build`    | Cambios en el sistema de compilación o dependencias |
| `revert`   | Revertir un commit previo |

Ejemplo de commit correcto:
```plaintext
feat(auth): agregar autenticación con JWT
fix(api): corregir error en la validación de usuarios
docs(readme): añadir instrucciones para configuración local
```

---

## Solución de Problemas

**Error: "fatal: Not a git repository"**  
🔹 Solución: Asegúrate de estar dentro de un repositorio Git o ejecuta `git init` si deseas inicializar uno.

**Error: "failed to push some refs"**  
🔹 Solución: Tu rama local está desactualizada. Ejecuta `git pull origin main` antes de hacer `git push`.

**Error: "conflict in merge"**  
🔹 Solución: Edita los archivos conflictivos, resuelve los conflictos y ejecuta:
```bash
git add archivo_resuelto.txt
git commit -m "Resolver conflicto de merge"
```

---

## Flujos de trabajo con GIT

### 1. **Flujo de trabajo centralizado (Centralized Workflow)**
Este es un flujo básico, donde todos los desarrolladores trabajan en una sola rama, generalmente `master` o `main`. Los cambios se suben al repositorio central de forma secuencial.

#### **Cómo aplicarlo:**
1. Clonar el repositorio central.
2. Trabajar directamente en la rama principal (`master` o `main`).
3. Realizar los commits localmente.
4. Subir los cambios al repositorio central con `git push`.

#### **Ventajas:**
- **Simplicidad**: Fácil de entender y utilizar para pequeños equipos.
- **Rapidez**: No se requiere una gestión compleja de ramas, lo que acelera la integración.

#### **Inconvenientes:**
- **Confusión en equipos grandes**: Sin una separación clara de tareas y sin ramificación, puede ser difícil para varios desarrolladores trabajar en paralelo sin sobrescribir cambios.
- **Riesgo de errores**: Los desarrolladores pueden sobrescribir el trabajo de otros si no hay una gestión adecuada de los commits y las actualizaciones.

---

### 2. **Flujo de trabajo de características (Feature Branch Workflow)**
En este flujo, cada nueva funcionalidad se desarrolla en una rama separada (`feature/xxx`), que se fusiona de nuevo con la rama principal cuando se completa.

#### **Cómo aplicarlo:**
1. Crear una nueva rama para cada nueva funcionalidad:
   ```bash
   git checkout -b feature/nueva-funcionalidad
   ```
2. Trabajar en la rama `feature` hasta completar el trabajo.
3. Hacer commit y push de los cambios.
4. Realizar una **Pull Request** o una **Merge Request** cuando la funcionalidad esté lista, para integrarla en `main` o `develop`.

#### **Ventajas:**
- **Aislación de características**: Cada nueva funcionalidad se desarrolla de forma aislada, lo que facilita la integración sin interferir en el trabajo de otros.
- **Mejor control de versiones**: Puedes fácilmente revisar, probar y realizar revisiones de código antes de integrar el código en la rama principal.

#### **Inconvenientes:**
- **Riesgo de divergencia**: Si las ramas se mantienen demasiado tiempo sin integrarse, pueden volverse difíciles de fusionar debido a los conflictos.
- **Manejo de ramas**: Se necesita gestionar múltiples ramas activas, lo que puede ser un desafío si el número de desarrolladores es grande.

---

### 3. **Flujo de trabajo con Gitflow**
**Gitflow** es un flujo de trabajo que define roles específicos para las ramas, siendo una estrategia robusta para proyectos de largo plazo o equipos grandes. Se basa en las siguientes ramas:
- `master`: contiene el código en producción.
- `develop`: para integrar las nuevas características.
- `feature/*`: ramas para nuevas funcionalidades.
- `release/*`: ramas para preparar el lanzamiento.
- `hotfix/*`: ramas para corregir errores críticos en producción.

#### **Cómo aplicarlo:**
1. Crear ramas `feature` a partir de `develop`.
2. Una vez que la funcionalidad esté terminada, hacer merge de `feature` a `develop`.
3. Cuando el código en `develop` esté listo para una nueva versión, se crea una rama `release` para realizar pruebas y correcciones.
4. Una vez aprobado, la rama `release` se fusiona en `master` y `develop`.
5. Si se encuentra un error en producción, se crea una rama `hotfix` desde `master` para corregirlo rápidamente.

#### **Ventajas:**
- **Organización clara**: Cada tipo de trabajo tiene su propia rama, lo que permite a los equipos trabajar de manera ordenada.
- **Mejor control de versiones**: Permite lanzamientos controlados y mantenimiento de producción sin afectar el desarrollo de nuevas características.

#### **Inconvenientes:**
- **Complejidad**: Gitflow es bastante estructurado, lo que puede ser excesivo para proyectos pequeños o equipos pequeños.
- **Ciclos largos de desarrollo**: Las ramas pueden quedarse mucho tiempo sin fusionarse, lo que puede generar conflictos si no se gestionan bien.

---

### 4. **Flujo de trabajo de fork/pull request (Fork and Pull Request Workflow)**
Este flujo es comúnmente utilizado en proyectos de código abierto. En lugar de tener acceso directo al repositorio central, los desarrolladores hacen un fork del repositorio y luego envían una **pull request** para que se revise y se fusionen sus cambios.

#### **Cómo aplicarlo:**
1. Hacer un fork del repositorio principal.
2. Clonar el repositorio forkeado.
3. Crear una rama para el trabajo a realizar y realizar commits.
4. Enviar una pull request al repositorio principal para que los mantenedores revisen y fusionen los cambios.

#### **Ventajas:**
- **Control sobre el repositorio principal**: El equipo principal tiene control total sobre las contribuciones externas, ya que deben ser revisadas antes de fusionarse.
- **Ideal para proyectos de código abierto**: Permite contribuciones externas sin comprometer la estabilidad del proyecto principal.

#### **Inconvenientes:**
- **Proceso de integración más lento**: Cada contribución debe ser revisada antes de ser integrada, lo que puede ser más lento en proyectos grandes.
- **Más pasos para desarrolladores**: Los colaboradores externos deben aprender a trabajar con forks y pull requests, lo que puede ser un proceso algo complejo para principiantes.

---

### 5. **Flujo de trabajo de ramas de integración continua (CI Workflow)**
En este flujo, las ramas de desarrollo están configuradas para disparar procesos automáticos de **integración continua** (CI) cada vez que se realiza un commit o un merge.

#### **Cómo aplicarlo:**
1. Trabajar en ramas de características o `develop`.
2. Configurar una herramienta CI (como Jenkins, GitHub Actions, CircleCI, etc.) para ejecutar pruebas automáticas y validaciones con cada nuevo commit.
3. Los cambios se integran después de pasar por todas las pruebas automáticas.

#### **Ventajas:**
- **Automatización de pruebas**: Cada commit dispara pruebas automáticas, lo que asegura que el código se mantiene en un estado funcional en todo momento.
- **Integración más rápida**: Los problemas se detectan rápidamente gracias a la CI, lo que permite una integración continua más eficiente.

#### **Inconvenientes:**
- **Configuración de CI compleja**: Requiere tiempo y esfuerzo para configurar el entorno de CI correctamente.
- **Dependencia de herramientas externas**: El flujo depende de herramientas de CI, lo que puede agregar complejidad al proceso.

---

### Conclusión:  

| **Flujo de Trabajo**       | **Ventajas**        | **Inconvenientes**        | **Usos Recomendados**                    |
|----------------------------|---------------------|---------------------------|------------------------------------------|
| **Centralizado**           | - Fácil de entender y utilizar para equipos pequeños. | - Difícil de gestionar en equipos grandes.             | - Equipos pequeños con pocos desarrolladores. |
|                            | - Rápido para proyectos con pocos colaboradores.      | - Riesgo de sobrescribir cambios de otros sin control. | - Proyectos sencillos o temporales.           |
| **Feature Branch**         | - Aislación clara de cada funcionalidad.              | - Puede generar divergencias si no se integran las ramas rápidamente. | - Proyectos donde se desarrollan múltiples funcionalidades de manera simultánea.|
|                            | - Permite integraciones controladas (pull requests).  | - Necesita una buena gestión de ramas.                                | - Equipos medianos a grandes que necesitan dividir tareas.                      |
| **Gitflow**                | - Estructura clara y organizada para proyectos grandes. | - Es complejo de implementar y gestionar, especialmente en proyectos. | - Proyectos a largo plazo y equipos grandes que requieren un control riguroso.|
|                            | - Buen control sobre las versiones de producción y desarrollo. | - Puede generar ciclos largos de desarrollo. | - Proyectos con ciclos de lanzamiento definidos. |
| **Fork and Pull Request**  | - Control sobre el repositorio principal sin comprometerlo.    | - Proceso de integración más lento por las revisiones de código. | - Proyectos de código abierto o con colaboradores externos.|
|                            | - Facilita la colaboración de desarrolladores externos sin acceso directo.| - Necesita una gestión eficiente de pull requests. | - Proyectos con contribuciones de múltiples colaboradores externos.|
| **CI Workflow**            | - Automatización de pruebas, asegurando que el código está siempre funcional.| - Requiere herramientas de CI que deben configurarse correctamente.  | - Proyectos que necesitan integración continua y validaciones automáticas.|
|                            | - Facilita la integración continua con procesos automáticos. | - Depende de las herramientas de CI y puede añadir complejidad. | - Proyectos grandes con un flujo de trabajo que depende de pruebas automáticas. |

---

### **Conclusión**
- **Flujo Centralizado**: Ideal para equipos pequeños con necesidades simples.
- **Feature Branch**: Adecuado para equipos medianos a grandes que gestionan múltiples funcionalidades.
- **Gitflow**: Perfecto para proyectos grandes o a largo plazo con lanzamientos y mantenimiento bien definidos.
- **Fork and Pull Request**: La opción preferida para proyectos de código abierto o colaboraciones externas.
- **CI Workflow**: Esencial para proyectos que requieren automatización de pruebas y una integración continua constante.

