"""
scanner_red.py — Descubrimiento de hosts en una red con python-nmap
Reemplaza la opción deprecada -sP por -sn (ping scan).
Instalar: pip install python-nmap
Uso:  python scanner_red.py -r 10.0.110.0/24
"""
import nmap
import argparse


def descubrir_red(red: str) -> None:
    scanner = nmap.PortScanner()

    print(f"[*] Descubriendo hosts en {red}...")
    scanner.scan(hosts=red, arguments="-sn")  # -sn reemplaza al deprecado -sP

    hosts_activos = [h for h in scanner.all_hosts() if scanner[h].state() == "up"]

    print(f"[+] Hosts activos encontrados: {len(hosts_activos)}\n")
    for ip in hosts_activos:
        hostname = scanner[ip].hostname() or "sin nombre"
        print(f"  {ip:20s}  ({hostname})")


def main() -> None:
    parser = argparse.ArgumentParser(description="Descubrimiento de hosts (ping scan)")
    parser.add_argument("-r", "--red", required=True,
                        help="Rango de red en notación CIDR, ej: 192.168.1.0/24")
    args = parser.parse_args()

    descubrir_red(args.red)


if __name__ == "__main__":
    main()
