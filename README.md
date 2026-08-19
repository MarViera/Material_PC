# Retos de Programación para Ciberseguridad — AD2026

Repositorio público con los retos de código (actividades prácticas) de la materia **Programación para Ciberseguridad**, Facultad de Ciencias Físico Matemáticas, UANL.

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
│   ├── Reto-03-funciones-auditoria.pdf
│   └── ...
├── Fase-II-.../
│   ├── Reto-01-....pdf
│   └── ...
└── ...
```

- Cada PDF contiene el enunciado y la guía paso a paso del reto correspondiente.
- Los archivos se nombran como `Reto-NN-nombre-corto.pdf`, en minúsculas y con guiones (sin espacios ni acentos), para que el orden numérico se mantenga visualmente en GitHub.

---

## 📋 Retos publicados — Fase I (PowerShell)

| # | Reto | Tema | Estado |
|---|------|------|--------|
| 03 | Funciones de auditoría con parámetros | `function`, `param()`, `Parameter[]`, buenas prácticas de nomenclatura | ✅ Publicado |
| 04 | Módulo con manifiesto | `.psm1`, `.psd1`, `New-ModuleManifest`, `Import-Module` | 🔜 Próximamente |
| 05 | Módulos de PowerShell Gallery + `-ErrorAction` | `Find-Module`, `Install-Module`, PSScriptAnalyzer, `$Error` | 🔜 Próximamente |
| 06 | Excepciones con `try` / `catch` / `finally` | Manejo de errores robusto, `throw` | 🔜 Próximamente |
| 07 | Script integrador con Transcript | `Start-Transcript`, cierre de Fase I | 🔜 Próximamente |

> La numeración de esta tabla es una referencia inicial — ajústala si ya llevas un control distinto (por ejemplo, si el reto de funciones lo manejas internamente como otro número). Ve actualizando esta tabla cada vez que subas un reto nuevo.

---

## 🚀 Cómo usar este repositorio (para estudiantes)

1. Entra al folder de la fase correspondiente.
2. Descarga o abre el PDF del reto que te fue asignado.
3. Sigue la guía paso a paso dentro del propio documento.
4. Ejecuta el código resultante en tu propio entorno de práctica (máquina virtual o entorno aislado autorizado) — nunca en sistemas de producción o de terceros sin autorización.

---

## ⚖️ Uso y licencia

Este material se comparte con fines **educativos**. Puedes consultarlo y usarlo como referencia para aprender, pero no está autorizado su uso para fines comerciales sin permiso de la autora.

Todo el código aquí publicado sigue el principio visto en clase: **la misma herramienta que sirve para auditar puede usarse mal — el contexto, la autorización y la intención son lo que determina su uso correcto.** Úsalo de forma responsable.

---

## 📬 Contacto

Dra. Perla Marlene Viera González
perla.vieragn@uanl.edu.mx
Facultad de Ciencias Físico Matemáticas, UANL
