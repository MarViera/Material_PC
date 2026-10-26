"""
BannerGrab.py — Banner grabbing sobre múltiples puertos
Tema: Sockets, reconocimiento de servicios
Uso:  python BannerGrab.py
"""
import socket
import argparse


PUERTOS_COMUNES = {21: "FTP", 22: "SSH", 25: "SMTP", 80: "HTTP",
                   110: "POP3"}


def get_banner(sock: socket.socket, target: str) -> bytes:
    """Envía una petición HTTP GET y regresa la respuesta cruda."""
    peticion = (
        f"GET / HTTP/1.1\r\n"
        f"Host: {target}\r\n"
        "User-Agent: python-banner-grabber/1.0\r\n"
        "Accept: */*\r\n"
        "Connection: close\r\n\r\n"
    )
    sock.send(peticion.encode())
    return sock.recv(2048)


def grab_banner(ip: str, puerto: int, timeout: float = 3.0) -> None:
    """Conecta al puerto indicado y muestra el banner del servicio."""
    servicio = PUERTOS_COMUNES.get(puerto, "Desconocido")
    print(f"\n[*] Puerto {puerto}/{servicio}")
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            # ← evita colgarse indefinidamente
            s.connect((ip, puerto))
            banner = get_banner(s, ip)
            print(banner.decode(errors="replace")[:500])
    except socket.timeout:
        print("    Tiempo de espera agotado.")
    except ConnectionRefusedError:
        print("    Puerto cerrado o sin servicio.")
    except Exception as e:
        print(f"    Error: {e}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Banner Grabber — reconocimiento de servicios")
    parser.add_argument("-t", "--target", required=True, help="IP o nombre de host objetivo")
    parser.add_argument("-p", "--puertos", default="21,22,25,80,110",
                        help="Puertos separados por coma (default: 21,22,25,80,110)")
    parser.add_argument("--timeout", type=float, default=3.0,
                        help="Segundos de espera por puerto (default: 3)")
    args = parser.parse_args()

    puertos = [int(p.strip()) for p in args.puertos.split(",")]
    print(f"[+] Objetivo: {args.target}")
    print(f"[+] Puertos:  {puertos}")
    for puerto in puertos:
        grab_banner(args.target, puerto, args.timeout)


if __name__ == "__main__":
    main()
