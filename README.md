# Una Introducción (Muy algoritmica) a la Teoría de grafos

Este proyecto utiliza [**Manim Community Edition**](https://www.manim.community/) para la exposición sobre la temática grafos en el semillero de Neuroco.

---

## Requisitos

- Python 3.9 o superior  
- [Manim Community Edition](https://docs.manim.community/en/stable/installation.html)  

---

## Cómo ejecutar las animaciones

### 1. Crear y activar el entorno virtual (Windows PowerShell o CMD):

   ```bash

   python -m venv manim-env

   .\manim-env\Scripts\activate

   pip install -r requirements.txt
   ```

### 2. Ejecutar una animación de forma rápida:

   ```bash
   manim -pql archivo.py NombreClase
   ```   

Donde:

- archivo.py → tu script de Manim

- NombreClase → la clase dentro del archivo que define tu animación

### 3. Opciones de ejecución útiles

| Comando        | Descripción                                     |
|----------------|-------------------------------------------------|
| `-p`           | Abre el video automáticamente al terminar       |
| `-ql`          | Render rápido en baja calidad (preview)         |
| `-qm`          | Render en calidad media                         |
| `-qh`          | Render en alta calidad (HD)                     |
| `--format=mp4` | Exporta en formato MP4                          |
| `--format=gif` | Exporta en formato GIF                          |
| `--fps 60`     | Define los frames por segundo (ej: 60 fps)      |
| `-r 1920,1080` | Cambia la resolución de salida (ej: Full HD)    |

### 4. Ejemplo de ejecución en alta calidad, Full HD y 60 fps:

   ```bash
manim -pqh -r 1920,1080 --fps 60 archivo.py NombreClase
   ```