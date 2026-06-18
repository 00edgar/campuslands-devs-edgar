# Ejercicio 03 — Backend básico para torneo battle royale

**Nombre:** Edgar Sanchez
## Solución

Estructura de carpetas creada (proyecto simulado en `proyecto-battle-royale/`):

```
proyecto-battle-royale/
├── README.md
└── src/
    ├── controllers/
    │   └── .gitkeep
    ├── services/
    │   └── .gitkeep
    ├── models/
    │   └── .gitkeep
    └── routes/
    │   └── .gitkeep
```

### Responsabilidad de cada carpeta

- **src/controllers** → capa de entrada HTTP. Recibe `req`, hace validación básica, llama al service y devuelve `res`. No tiene lógica de negocio.
- **src/services** → lógica de negocio del torneo: crear partidas, registrar equipos, calcular ganadores.
- **src/models** → definición de los datos (`Partida`, `Equipo`): qué campos existen y qué valores son válidos.
- **src/routes** → mapa de URLs de la API; conecta cada endpoint con su controller.

## Evidencia de validación

- **Caso normal:** el árbol contiene las 4 carpetas pedidas dentro de `src/` y un README en la raíz del proyecto simulado. ✔
- **Caso límite:** ninguna carpeta queda vacía (cada una tiene al menos un archivo de ejemplo), y el controller valida el caso de datos vacíos (para casos de carpetas vacias cada una tiene un archivo `.gitkeep`)