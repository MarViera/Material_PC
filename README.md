# Retos de Programación para Ciberseguridad — AD2026

Repositorio público con los retos (actividades prácticas) de la materia **Programación para Ciberseguridad**, Facultad de Ciencias Físico Matemáticas, UANL.

**Profesora:** Dra. Perla Marlene Viera González
**Semestre:** Agosto–Diciembre 2026 (AD2026)

> Este repositorio contiene únicamente los **PDF de los retos** (enunciado + guía paso a paso). Las evidencias de ejecución (capturas de pantalla) se entregan por separado en Microsoft Teams — aquí no se sube evidencia personal de ningún estudiante.

---

## 🗂 Estructura del repositorio

Un folder por fase del curso. Dentro de cada folder, todos los PDF de los retos de esa fase:

```
/
├── README.md
├── Fase-I-PowerShell/
│   ├── R3_PC.pdf
│   ├── R4_PC.pdf
│   ├── Reto-05-excepciones-transcript.pdf
│   ├── Reto-06-virtualbox-kali.pdf
│   ├── Reto-07-inventarios-acl-eventid.pdf
│   ├── Reto-08-csv-json-normalizacion.pdf
│   ├── Reto-09-blue-team-cookbook.pdf
│   └── Reto-10-tryhackme-windows-cmd.pdf
├── Fase-II-Bash/
│   ├── Reto-11-permisos-grep-awk-sed.pdf
│   ├── Reto-12-tryhackme-linux-fundamentals-1.pdf
│   ├── Reto-13-htb-meow.pdf
│   ├── Reto-14-reconocimiento-red.pdf
│   ├── Reto-15-tryhackme-linux-fundamentals-2.pdf
│   ├── Reto-16-htb-fawn.pdf
│   ├── Reto-17-tryhackme-linux-fundamentals-3.pdf
│   ├── Reto-18-logs-a-json.pdf
│   ├── Reto-19-classroom50-bash-autoevaluable.pdf
│   └── Reto-20-htb-dancing.pdf
└── ...
```

- Cada PDF contiene el enunciado y la guía paso a paso del reto correspondiente.
- Los archivos se nombran como `Reto-NN-nombre-corto.pdf`, en minúsculas y con guiones (sin espacios ni acentos), para que el orden numérico se mantenga visualmente en GitHub.
- La numeración de retos es continua entre fases (no reinicia en 1 en cada fase) — así el número de reto identifica de forma única la actividad en todo el curso.

---

## 📋 Retos — Fase I: PowerShell (Semanas 1–4)

| # | Reto | Tema | Estado |
|---|------|------|--------|
| 03 | Funciones de auditoría con parámetros | `function`, `param()`, `Parameter[]`, buenas prácticas de nomenclatura | ✅ Publicado |
| 04 | Módulos propios y módulos de la Gallery | `.psm1`, `.psd1`, `New-ModuleManifest`, PowerShell Gallery | ✅ Publicado |
| 05 | Excepciones y script de cierre con Transcript | `try`/`catch`/`finally`, `throw`, `Start-Transcript` | ✅ Publicado |
| 06 | Tu primer laboratorio: VirtualBox y Kali Linux | Hipervisores, máquinas virtuales, snapshots | ✅ Publicado |
| 07 | Inventarios, ACLs/GPO y Event IDs | `Get-CimInstance`, `Get-Acl`, `gpresult`, `Get-WinEvent` | ✅ Publicado |
| 08 | Exportación a CSV/JSON y Normalización de datos | `Export-Csv`, `ConvertTo-Json` | ✅ Publicado |
| 09 | Tu propio Blue Team Cookbook | Módulo defensivo integrador (cierre de Fase I) | ✅ Publicado |
| 10 | TryHackMe — Windows Command Line | Reconocimiento de sistema vía CMD | ✅ Publicado |

> Los retos 01–03 corresponden a las primeras semanas de la fase (fundamentos de shell, primeros scripts, funciones) — sus PDFs se agregan conforme se formalicen en este formato.

## 📋 Retos — Fase II: Bash, Administración y Forense en Linux (Semanas 5–7)

| # | Reto | Plataforma | Estado |
|---|------|------------|--------|
| 11 | Auditoría de permisos + pipeline `grep`\|`awk`\|`sed` | Guiado, en clase | 🔜 Planeado |
| 12 | *Linux Fundamentals Part 1* | TryHackMe | 🔜 Planeado |
| 13 | **Meow** (Tier 0) | HTB Starting Point | 🔜 Planeado |
| 14 | Reconocimiento de red (`ss`/`tcpdump`/`ip`) | Guiado, en clase | 🔜 Planeado |
| 15 | *Linux Fundamentals Part 2* | TryHackMe | 🔜 Planeado |
| 16 | **Fawn** (Tier 0) | HTB Starting Point | 🔜 Planeado |
| 17 | *Linux Fundamentals Part 3* | TryHackMe | 🔜 Planeado |
| 18 | Script integrador: `auth.log` → JSON (cierre de fase) | Guiado, en clase | 🔜 Planeado |
| 19 | Reto de scripting Bash con pruebas automáticas | Classroom 50 | 🔜 Planeado |
| 20 | **Dancing** (Tier 0) | HTB Starting Point | 🔜 Planeado |

> Los checkpoints teóricos de Fase II (Kahoots en vivo, HTB Academy) **no** se consideran retos y no se documentan en este repositorio — se evalúan por otro medio.

---

## 🚀 Cómo usar este repositorio (para estudiantes)

1. Entra al folder de la fase correspondiente.
2. Descarga o abre el PDF del reto que te fue asignado.
3. Sigue la guía paso a paso dentro del propio documento.
4. Ejecuta el código resultante en tu propio entorno de práctica (máquina virtual o entorno aislado autorizado) — nunca en sistemas de producción o de terceros sin autorización.
5. Si el reto es una máquina de TryHackMe o Hack The Box, conéctate únicamente a través de la VPN oficial de la plataforma — nunca ataques hosts fuera del laboratorio designado.

---

## ⚖️ Uso y licencia

Este material se comparte con fines **educativos**. Puedes consultarlo y usarlo como referencia para aprender, pero no está autorizado su uso para fines comerciales sin permiso de la autora.

Todo el código aquí publicado sigue el principio visto en clase: **la misma herramienta que sirve para auditar puede usarse mal — el contexto, la autorización y la intención son lo que determina su uso correcto.** Úsalo de forma responsable.

---

## 📬 Contacto

Dra. Perla Marlene Viera González
perla.vieragn@uanl.edu.mx
Facultad de Ciencias Físico Matemáticas, UANL
