"""
nmap_scan.py — Escaneo de rango de puertos con python-nmap + exportación CSV
(Combina nmap_test.py y nmap_test2.py)
Instalar: pip install python-nmap
Uso:  python nmap_scan.py -t 192.168.1.100 -i 20 -f 25 -o resultado.csv
"""
import nmap
import argparse
import csv
import sys


def escanear_rango(target: str, inicio: int, fin: int, archivo_csv: str) -> None:
    scanner = nmap.PortScanner()
    filas = []

    for puerto in range(inicio, fin + 1):
        print(f"[*] Escaneando puerto {puerto}...", end=" ", flush=True)
        try:
            scanner.scan(target, str(puerto))
            estado = scanner[target]["tcp"][puerto]["state"]
        except KeyError:
            estado = "cerrado/filtrado"
        except Exception as e:
            estado = f"error: {e}"

        print(estado)
        filas.append({"host": target, "puerto": puerto, "estado": estado})

    # Guardar CSV
    with open(archivo_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["host", "puerto", "estado"])
        writer.writeheader()
        writer.writerows(filas)

    print(f"\n[+] Resultados guardados en: {archivo_csv}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Escaneo de puertos con nmap")
    parser.add_argument("-t", "--target", required=True, help="IP objetivo")
    parser.add_argument("-i", "--inicio", type=int, default=20, help="Puerto inicial")
    parser.add_argument("-f", "--fin",    type=int, default=25, help="Puerto final")
    parser.add_argument("-o", "--output", default="resultado.csv", help="Archivo de salida CSV")
    args = parser.parse_args()

    if args.inicio > args.fin:
        print("Error: el puerto inicial debe ser menor al final.")
        sys.exit(1)

    escanear_rango(args.target, args.inicio, args.fin, args.output)


if __name__ == "__main__":
    main()
