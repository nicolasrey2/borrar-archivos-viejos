# Borrar Archivos Viejos

Este script en Python elimina archivos que superan un cierto número de días en un directorio específico.
Está diseñado para ser ejecutado manualmente o mediante un cron job en sistemas Linux/macOS.

---

## Requisitos

1. **Sistema operativo compatible:**

   * Linux (Ubuntu, Debian, CentOS, Fedora, etc.)
   * macOS
   * Windows (ejecutando desde PowerShell o CMD, pero el cron debe configurarse con el Programador de Tareas de Windows)

2. **Python 3**

   * El script utiliza solo librerías estándar: `os`, `time`, `argparse`.

---

## Instalación de Python 3

### En Ubuntu/Debian:

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip -y
```

### En CentOS/RHEL:

```bash
sudo yum install python3 -y
```

### En macOS (usando Homebrew):

```bash
brew install python
```

Verificar instalación:

```bash
python3 --version
```

---

## Instalación del script

1. Guardar el script como `borrar_viejos.py` o el nombre que prefieras.
2. Dar permisos de ejecución:

```bash
chmod +x borrar_viejos.py
```

3. (Opcional) Moverlo a un directorio en el PATH para ejecutarlo desde cualquier lugar:

```bash
sudo mv borrar_viejos.py /usr/local/bin/borrar_viejos
sudo chmod +x /usr/local/bin/borrar_viejos
```

---

## Uso

### Ejecutar manualmente

```bash
./borrar_viejos.py --dir /ruta/a/mi/directorio --dias 30
```

o si está en PATH:

```bash
borrar_viejos --dir /ruta/a/mi/directorio --dias 30
```

### Argumentos

* `--dir` o `-d`: Directorio donde se eliminarán los archivos.
* `--dias` o `-t`: Cantidad de días para conservar archivos (los archivos más antiguos se eliminarán).

---

## Automatización con Cron

Ejecutar automáticamente cada día a las 2 AM:

```bash
0 2 * * * /usr/local/bin/borrar_viejos --dir /ruta/a/mi/directorio --dias 30
```

---

## Notas

* Se requieren permisos de lectura/escritura sobre el directorio especificado.
* En caso de directorios protegidos, puede ser necesario ejecutar el script con `sudo`.
* El script solo elimina archivos, **no directorios**.
