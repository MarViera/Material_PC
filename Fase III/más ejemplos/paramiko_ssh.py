"""
paramiko_ssh.py — Conexión SSH básica con Paramiko
Módulo: paramiko  |  pip install paramiko

Uso:
    python paramiko_ssh.py --host 192.168.1.10 --usuario admin
    python paramiko_ssh.py --host 192.168.1.10 --usuario admin --puerto 2222 --comando "ls -la"
"""

import sys
import argparse
import getpass
import paramiko


# ─── Funciones ────────────────────────────────────────────────────────────────

def conectar(host: str, usuario: str, contrasena: str, puerto: int) -> paramiko.SSHClient:
    """Establece conexión SSH y retorna el cliente."""
    cliente = paramiko.SSHClient()
    # Acepta automáticamente el fingerprint del servidor (⚠ solo para laboratorio)
    cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    cliente.connect(
        hostname=host,
        port=puerto,
        username=usuario,
        password=contrasena,
        timeout=10
    )
    return cliente


def ejecutar_comando(cliente: paramiko.SSHClient, comando: str) -> tuple[str, str]:
    """Ejecuta un comando remoto y retorna (stdout, stderr)."""
    _, stdout, stderr = cliente.exec_command(comando)
    return stdout.read().decode(), stderr.read().decode()


# ─── Programa principal ───────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Conexión SSH básica con Paramiko",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--host",    required=True,          help="IP o hostname del servidor")
    parser.add_argument("--usuario", required=True,          help="Usuario SSH")
    parser.add_argument("--puerto",  type=int, default=22,   help="Puerto SSH")
    parser.add_argument("--comando", default="uname -a",     help="Comando a ejecutar remotamente")
    args = parser.parse_args()

    contrasena = getpass.getpass(f"Contraseña para {args.usuario}@{args.host}: ")

    try:
        print(f"[*] Conectando a {args.host}:{args.puerto}...")
        cliente = conectar(args.host, args.usuario, contrasena, args.puerto)
        print(f"[+] Conexión establecida\n")

        salida, error = ejecutar_comando(cliente, args.comando)

        if salida:
            print(f"--- Salida ---\n{salida.strip()}")
        if error:
            print(f"--- Error ---\n{error.strip()}", file=sys.stderr)

        cliente.close()
        print("\n[*] Conexión cerrada")

    except paramiko.AuthenticationException:
        print("[-] Autenticación fallida: usuario o contraseña incorrectos")
        sys.exit(1)
    except paramiko.NoValidConnectionsError:
        print(f"[-] No se pudo conectar a {args.host}:{args.puerto} — ¿está el servidor activo?")
        sys.exit(1)
    except TimeoutError:
        print(f"[-] Tiempo de espera agotado al conectar a {args.host}")
        sys.exit(1)
    except Exception as e:
        print(f"[-] Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
