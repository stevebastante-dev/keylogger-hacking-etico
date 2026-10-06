# Keylogger - Trabajo Parcial Hacking Etico

**Curso:** 1CCB0001 - Hacking Etico  
**Semestre:** 2026-10  
**Docente:** Gianpaul Custodio

## ⚠️ Advertencia
Este software es **unicamente con fines educativos**. Su uso sin consentimiento es **ilegal** y viola la privacidad. El autor no se responsabiliza por el mal uso.

## 📋 Descripcion
Keylogger desarrollado en Python que captura las pulsaciones del teclado, las almacena en un archivo de log con timestamp, e implementa persistencia en el sistema.

## ⚙️ Funcionalidades
- Captura de teclas normales y especiales.
- Almacenamiento en `log.txt` con fecha y hora.
- **Persistencia**: se copia al inicio automatico de Windows (funcionalidad adicional).
- Detencion con la tecla ESC.

## 🛠️ Requisitos
- Python 3.x
- pynput

## 🚀 Instalacion y uso
```bash
pip install -r requirements.txt
python keylogger.py
```