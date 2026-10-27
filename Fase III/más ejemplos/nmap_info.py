"""
nmap_info.py — Información detallada de un puerto con python-nmap
Instalar: pip install python-nmap
E instalar nmap: https://nmap.org/download.html#windows
Uso:  python nmap_info.py -t 148.234.5.222 -p 80
"""
import nmap
import argparse


def escanear_puerto(target: str, port: int) -> None:
    scanner = nmap.PortScanner()
    scanner.scan(target, str(port))

    print(f"Comando ejecutado : {scanner.command_line()}")
    print(f"Información       : {scanner.scaninfo()}")

    for ip in scanner.all_hosts():
        print(f"\nHost : {ip}  ({scanner[ip].hostname()})")
        print(f"Estado : {scanner[ip].state()}")
        print(f"Protocolos : {scanner[ip].all_protocols()}")

        # Mostrar rango de puertos alrededor del objetivo
        for p in range(port - 2, port + 3):
            if p <= 0:
                continue
            if scanner[ip].has_tcp(p):
                estado = scanner[ip]["tcp"][p]["state"]
            else:
                estado = "cerrado/filtrado"
            print(f"  Puerto {p}: {estado}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Información de puerto con nmap")
    parser.add_argument("-t", "--target", required=True, help="IP o host objetivo")
    parser.add_argument("-p", "--port",   type=int, default=80, help="Puerto a analizar")
    args = parser.parse_args()

    escanear_puerto(args.target, args.port)


if __name__ == "__main__":
    main()
