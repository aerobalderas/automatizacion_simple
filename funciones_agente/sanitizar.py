def sanitizar(name):

    # Prefijos
    prefixies = ["la", "el", "las", "los", "de", "precio de", "clima en", "clima de"]

    # Entrada en Minúsculas
    name = name.lower()

    # Eliminar prefijos

    changed = True
    while changed:
        changed = False
        for p in prefixies:
            if name.startswith(p):
                name = name[len(p):].strip()
                changed = True
    
    return name