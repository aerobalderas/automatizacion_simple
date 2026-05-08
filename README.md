
# Chatbot CLI

A simple command-line chatbot built in Python that answers two types of queries:

- **Stock prices** - powered by 'yfinance'
- **Weather by city** - powered by 'wttr.in'

## Requirements

```bash
pip install yfinance requests
```

## Usage

```bash
python main.py
```

### Example inputs

- `precio de Apple`
- `clima en Monterrey`
- `salir` - exits the chatbot

## Project Structure

```
automatizacion_simple/
├── main.py
└── funciones_agente/
    ├── sanitizar.py
    ├── obtener_clima.py
    └── obtener_precio_accion.py
```
