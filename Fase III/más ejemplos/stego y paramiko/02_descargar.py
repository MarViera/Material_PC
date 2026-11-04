# 02_descargar.py — Alumno: conectarse al equipo y bajar la imagen
# pip install paramiko

import paramiko


def descargar_imagen(ip, usuario, contrasena, archivo_remoto, archivo_local):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username=usuario, password=contrasena)

    sftp = ssh.open_sftp()
    sftp.get(archivo_remoto, archivo_local)
    sftp.close()
    ssh.close()

    print(f"Imagen descargada: {archivo_local}")


# --- Llenar con los datos que da la maestra ---
IP             = "192.168.0.1" #cambiar
USUARIO        = "kali"
CONTRASENA     = "kali"
ARCHIVO_REMOTO = "/home/kali/img/imagen_secreta.png"
ARCHIVO_LOCAL  = "imagen_secreta.png"

descargar_imagen(IP, USUARIO, CONTRASENA, ARCHIVO_REMOTO, ARCHIVO_LOCAL)
