import os
from ruamel.yaml import YAML

def obtener_estructura_nav(base_path):
    """
    Genera la estructura 'nav' para el archivo YAML basado en la estructura de directorios.
    """
    nav = {}
    
    for root, dirs, files in os.walk(base_path):
        # Ignorar directorios no deseados (como .git, __pycache__, etc)
        if '.git' in root or '__pycache__' in root:
            continue
        
        # Eliminar la parte de la ruta base para crear las claves del 'nav'
        estructura_relativa = os.path.relpath(root, base_path)
        
        # Ignorar directorios vacíos
        if not dirs and not files:
            continue
        
        # Si la ruta no está vacía, establecer la clave para 'nav'
        if estructura_relativa == '.':
            # No agregar la raíz del proyecto como una clave
            continue
        else:
            # Generamos la clave para el directorio y la lista de archivos
            directorio_nombre = os.path.basename(estructura_relativa)
            archivos = [f'{estructura_relativa}/{file}' for file in files if file.endswith('.md')]
            
            if archivos:
                nav[directorio_nombre] = {os.path.splitext(file)[0]: archivo for file, archivo in zip(files, archivos)}

    return nav


def limpiar_mkdocs_yml(ruta_archivo, base_path):
    """
    Limpiar el archivo mkdocs.yml y actualizar la sección 'nav' con la estructura del proyecto.
    """
    yaml = YAML()
    yaml.preserve_quotes = True  # Conserva comillas si las hay
    yaml.default_flow_style = False  # Mantiene el formato de listas
    
    with open(ruta_archivo, 'r', encoding='utf-8') as file:
        data = yaml.load(file)

    # Obtener la estructura del directorio para la sección 'nav'
    data['nav'] = obtener_estructura_nav(base_path)

    # Guardar el archivo manteniendo el formato YAML
    with open(ruta_archivo, 'w', encoding='utf-8') as file:
        yaml.dump(data, file)

    print("El archivo mkdocs.yml ha sido actualizado correctamente con la jerarquía de archivos.")

# Especifica la ruta de tu archivo mkdocs.yml y la ruta base de tu proyecto
ruta_mkdocs = "mkdocs.yml"
base_path = "./"  # Cambia esta ruta al directorio raíz de tu proyecto

limpiar_mkdocs_yml(ruta_mkdocs, base_path)
