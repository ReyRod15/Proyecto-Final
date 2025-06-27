def alerta_min(inventario):
    for nombre, datos in inventario.items():
        if datos["cantidad"] < datos["minimo"]:
            print(f"\n⚠️ Alerta: {nombre} está por debajo del mínimo ({datos['cantidad']}/{datos['minimo']})")

