def procesar_liga(equipos):
    for e in equipos:
        e["puntos"] = e["victorias"] * 3 + e["empates"]
        e["dg"] = e["golesFavor"] - e["golesContra"]

    equipos.sort(key=lambda x: (x["puntos"], x["dg"]), reverse=True)

    print(f"{'Pos':<4} | {'Equipo':<12} | {'Pts':<4} | {'DG':<4}")
    print("-" * 35)

    for i, e in enumerate(equipos, start=1):
        print(f"{i:<4} | {e['nombre']:<12} | {e['puntos']:<4} | {e['dg']:<4}")


datos = [
    {
        "nombre": "Titanes FC",
        "victorias": 3,
        "empates": 1,
        "derrotas": 1,
        "golesFavor": 12,
        "golesContra": 6,
    },
    {
        "nombre": "Rayo Futsal",
        "victorias": 3,
        "empates": 1,
        "derrotas": 1,
        "golesFavor": 10,
        "golesContra": 5,
    },
    {
        "nombre": "Guerreros",
        "victorias": 2,
        "empates": 0,
        "derrotas": 3,
        "golesFavor": 8,
        "golesContra": 9,
    },
]

procesar_liga(datos)