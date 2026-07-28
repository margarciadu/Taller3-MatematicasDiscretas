# Taller 3

**Materia:** Matematicas Discretas I
**Universidad Nacional de Colombia**
**Profesor:** Jhoan Sebastian Tenjo Garcia

## Integrantes
* Mariana Garcia Dussan

## Lenguaje y Requisitos
* **Lenguaje:** Python 3.9+
* **Librerias externas:** Ninguna. El proyecto usa unicamente la libreria
  estandar de Python (`math`, `random`, `heapq`, `itertools`, `collections`).

## Descripcion del Proyecto
Este repositorio contiene la implementacion en Python de los 10 ejercicios del Taller 3, abordando los conceptos del tercer corte:
1. **Criptografia clasica y moderna:** Cifrado Cesar, RSA de juguete y Computacion Multipartita Segura (MPC).
2. **Teoria de grafos:** Algoritmo de Dijkstra, evaluacion del impacto por cierre de nodos y coloreo voraz de grafos.
3. **Algebra de Boole, Shannon y cuantica:** Tablas de verdad, simplificacion de minterminos, entropia de la informacion y simulacion basica de un qubit.

---

## Estructura del Repositorio
```text
.
├── README.md               # Instrucciones del proyecto e informacion general
├── requirements.txt        # Librerias necesarias (ninguna externa)
├── docs/                   # Explicacion matematica de las soluciones (PDF)
├── src/                    # Codigo fuente del proyecto
│   ├── crypto/             # Bloque A: Cifrado Cesar, RSA y MPC
│   ├── graphs/             # Bloque B: Dijkstra, cierre de estaciones y coloreo
│   ├── boole/              # Bloque C: Tablas de verdad y simplificador
│   └── quantum/            # Bloque C: Entropia de Shannon y simulador de qubit
└── tests/                  # Pruebas para verificacion de resultados
```

---

## Como ejecutar

Clonar el repositorio y ubicarse en la raiz del proyecto.

### Ejecutar todas las pruebas de una vez
```bash
python3 -m tests.run_all_test
```

### Ejecutar un ejercicio individual
Cada modulo puede correrse por separado usando el flag `-m` desde la raiz
del repositorio (necesario porque los modulos usan imports internos del
paquete `src`):

```bash
python3 -m src.crypto.caesar
python3 -m src.crypto.rsa_toy
python3 -m src.crypto.mpc_sum
python3 -m src.graphs.dijkstra
python3 -m src.graphs.station_closure
python3 -m src.graphs.graph_coloring
python3 -m src.boole.truth_tables
python3 -m src.boole.boolean_minimizer
python3 -m src.quantum.shannon_entropy
python3 -m src.quantum.qubit_simulator
```

## Ejercicios desarrollados
1. Cifrado Cesar (`src/crypto/caesar.py`)
2. RSA de juguete (`src/crypto/rsa_toy.py`)
3. MPC - suma secreta (`src/crypto/mpc_sum.py`)
4. Ruta mas corta - Dijkstra (`src/graphs/dijkstra.py`)
5. Cierre de estacion / impacto en la red (`src/graphs/station_closure.py`)
6. Coloreo de grafos (`src/graphs/graph_coloring.py`)
7. Tablas de verdad (`src/boole/truth_tables.py`)
8. Simplificacion booleana (`src/boole/boolean_minimizer.py`)
9. Entropia de Shannon (`src/quantum/shannon_entropy.py`)
10. Simulador cuantico de un qubit (`src/quantum/qubit_simulator.py`)

## Pruebas
La carpeta `tests/` contiene `run_all_test.py`, que verifica los 10 puntos
con los casos de prueba obligatorios indicados en la guia del taller
