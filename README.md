# Proyecto ywnlmt (Letter Application)
Ingenieria del proyecto ' Eva Parcial 1

# 1.- Ingenieria DevOps - Evaluacion Parcial 1

Este repositorio contiene el microservicio base ywnlmt, una aplicación de escritorio desarrollada en Python orientada a la gestión de interfaces multimedia.
El proyecto sirve como la base técnica para la implementación de un pipeline de despliegue continuo (CI/CD) que se desarrollará durante el semestre.

# 2. Guía de Buenas Prácticas (Estrategia DevOps)
Para cumplir con los estándares de control de versiones y asegurar la trazabilidad del código, hemos definido las siguientes convenciones:

Estrategia de Ramificación (Branching):

main: Rama protegida que contiene el código estable y listo para producción.

feature/*: Ramas utilizadas para el desarrollo de nuevas funcionalidades (ej. feature/implementacion-musica).

hotfix/*: Ramas para correcciones rápidas de errores o ajustes de configuración (ej. hotfix/fuente-texto).

Convención de Commits:

Utilizamos el estándar de Conventional Commits para facilitar la lectura del historial: feat: para nuevas características, fix: para correcciones y chore: para tareas de mantenimiento.

Control de Versiones:

Toda integración a main se realiza mediante Pull Requests (PR), los cuales requieren la revisión y aprobación del otro integrante del equipo para asegurar la calidad del código.

# 3. Estructura del Repositorio
La organización de carpetas sigue un patrón de separación de responsabilidades para facilitar la automatización:

/src: Contiene el código fuente de la aplicación (main.py, utilidades.py).

/assets: Recursos multimedia divididos en /audio e /images.

requirements.txt: Archivo de configuración de dependencias para asegurar la portabilidad del entorno.

.gitignore: Configuración para evitar el rastreo de entornos virtuales (venv) y archivos basura del sistema operativo.

# 4. Instalación y Configuración
Para ejecutar este microservicio en un entorno local, siga estos pasos:

Clonar el repositorio:

Bash
git clone https://github.com/skt-t/DevOpsPipeline.git

Crear y activar entorno virtual:

PowerShell
python -m venv venv
.\venv\Scripts\activate

Instalar dependencias (Dentro del entorno virtual):

PowerShell
pip install -r ywnlmt/requirements.txt

# 5. Ejecución
Para iniciar la aplicación, ejecute el script principal desde la raíz:

PowerShell
python ywnlmt/src/main.py

