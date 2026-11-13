# CASTIGO 2 — SEMANA 5: 25 EJERCICIOS INTEGRADORES

**Curso:** Fundamentos de programación
**Tipo:** Sanción por faltas de disciplina en clase · **forma parte de la calificación de la Actividad 4**
**Valor:** 20 de los 100 puntos de la Actividad 4
**Modalidad:** Individual
**Fecha límite:** viernes 13 de noviembre de 2026, 23:59 h (sin prórroga)
**Entrega:** `semana5/castigo2_ejercicios.ipynb` en **tu mismo repositorio del curso**

---

## 1. Qué tienes que hacer

Resuelve los **25 problemas** de este documento en un solo notebook. Ninguno es de un solo tema: en cada uno combinas lo de esta semana (tuplas, diccionarios, excepciones y strings) con lo que ya sabes (variables, `if`, ciclos, listas, matrices y funciones).

No son difíciles, pero sí llevan tiempo. Avanza de 5 en 5 y haz commit cada vez que termines un bloque.

### Reglas
1. **Un par de celdas por ejercicio:** una Markdown con el título (`## Ejercicio 7 — Boleta del grupo`) y una de código con tu solución.
2. **Usa los datos tal cual** vienen en cada enunciado y, en los que piden `input()`, escribe **las entradas de prueba** que se indican, en ese orden.
3. Tu salida debe coincidir con la **salida esperada** (el texto puede variar un poco; los números no).
4. Respeta la línea **"Usa:"**: indica lo que tu solución debe incluir sí o sí.
5. El notebook debe estar **ejecutado**: en GitHub se deben ver todas las salidas.
6. Las soluciones idénticas entre alumnos valen 0. Puedo pedirte que expliques cualquiera en clase.

> 💡 **Herramientas nuevas que puedes usar** (vienen con su pista en el ejercicio): `" ".join(lista)`, `texto[::-1]`, `caracter.isdigit()`, `caracter.isupper()`.

---

## 2. Los 25 problemas

### BLOQUE 1 · La rodada (tuplas + listas + ciclos + funciones)

#### Ejercicio 1 — Bitácora de la semana
```python
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
km = (120, 85, 0, 210, 95, 0, 150)
```
Crea la función `resumen(km)` que **regrese una tupla** con: total de km, cuántos días sí se rodó (km > 0), el promedio de km **solo de los días rodados** (redondeado a 1 decimal) y el **índice** del día más largo. Desempaca el resultado y muéstralo.
**Usa:** función con `return` de una tupla, `for`, `if`, desempaquetar.
**Salida esperada:**
```
Total: 660 km
Días con rodada: 5
Promedio por día rodado: 132.0 km
Día más largo: Jueves (210 km)
```

#### Ejercicio 2 — La votación del festival
```python
votos = [("Metallica", 48), ("Slayer", 22), ("Megadeth", 35), ("Anthrax", 15), ("Iron Maiden", 40)]
```
Encuentra la banda ganadora **sin usar `sort()` ni `max()`**. Crea `promedio_votos(lista)` con `return` y muestra las bandas que quedaron por encima del promedio.
**Usa:** lista de tuplas, función con `return`, `for` desempaquetando.
**Salida esperada:**
```
Ganador: Metallica con 48 votos
Promedio: 32.0
Arriba del promedio:
- Metallica (48)
- Megadeth (35)
- Iron Maiden (40)
```

#### Ejercicio 3 — Tramos de la ruta a la Sierra
```python
paradas = (("Querétaro", 0), ("San Juan del Río", 52), ("Tequisquiapan", 74), ("Bernal", 125), ("Jalpan", 260))
```
El número es el kilómetro donde está cada parada, contado desde la salida. Muestra la distancia de cada tramo (de una parada a la siguiente) y cuál es el tramo más largo.
**Usa:** tupla de tuplas, `for` con `range(len(...) - 1)`, comparación.
**Salida esperada:**
```
Querétaro → San Juan del Río: 52 km
San Juan del Río → Tequisquiapan: 22 km
Tequisquiapan → Bernal: 51 km
Bernal → Jalpan: 135 km
Tramo más largo: Bernal → Jalpan (135 km)
```

#### Ejercicio 4 — ¿Con chamarra o sin chamarra?
```python
temps = (8, 14, 22, 27, 31, 19, 11)
```
Crea `clasificar(t)` que regrese `"frío"` (menos de 12), `"templado"` (de 12 a 24) o `"calor"` (25 o más). Arma una **lista** con la etiqueta de cada día y un **diccionario** contador, y di cuál predomina.
**Usa:** función con `return`, `if/elif/else`, lista con `append()`, diccionario contador.
**Salida esperada:**
```
['frío', 'templado', 'templado', 'calor', 'calor', 'templado', 'frío']
{'frío': 2, 'templado': 3, 'calor': 2}
Predomina: templado
```

#### Ejercicio 5 — ¿Cuánto dura el show?
```python
setlist = (("Intro", 95), ("Riff asesino", 245), ("Balada", 302), ("Solo", 128), ("Encore", 409))
```
Los números son segundos. Crea `formato(seg)` que regrese el texto `"m:ss"` (con dos dígitos en los segundos). Muestra cada canción y la duración total.
**Usa:** función con `return`, `//` y `%`, `if`, f-string.
💡 Pista: `245 // 60` da los minutos (4) y `245 % 60` los segundos (5); si los segundos son menos de 10, agrega un `0` antes.
**Salida esperada:**
```
Intro: 1:35
Riff asesino: 4:05
Balada: 5:02
Solo: 2:08
Encore: 6:49
Duración total: 19:39
```

---

### BLOQUE 2 · El taller y la tienda (diccionarios + listas + funciones)

#### Ejercicio 6 — Pedidos del taller
```python
inventario = {"bujía": 10, "cadena": 2, "balata": 6, "filtro": 4}
pedidos = [("bujía", 3), ("cadena", 5), ("espejo", 1), ("balata", 6), ("filtro", 1)]
```
Procesa cada pedido: si la pieza no existe, avisa; si no alcanza, avisa cuántas hay; si alcanza, réstala del inventario. Al final muestra el inventario y la lista de piezas agotadas (en 0).
**Usa:** diccionario, `in`, `if/elif/else`, lista de tuplas, `items()`.
**Salida esperada:**
```
bujía: surtido (3)
cadena: stock insuficiente (hay 2)
espejo: no existe en el taller
balata: surtido (6)
filtro: surtido (1)
{'bujía': 7, 'cadena': 2, 'balata': 0, 'filtro': 3}
Agotados: ['balata']
```

#### Ejercicio 7 — Boleta del grupo
```python
notas = {"Ana": [90, 85, 78], "Luis": [60, 72, 65], "Mía": [100, 95, 98], "Beto": [70, 68, 74]}
```
Crea `promedio(lista)` que sume con un `for` y regrese el promedio redondeado a 1 decimal. Guarda los promedios en un **diccionario nuevo**, muestra si cada alumno aprueba (70 o más) y quién tiene el mejor promedio.
**Usa:** diccionario con listas como valores, función con `return`, `round()`, `items()`.
**Salida esperada:**
```
Ana: 84.3 - Aprobado
Luis: 65.7 - Reprobado
Mía: 97.7 - Aprobado
Beto: 70.7 - Aprobado
Mejor promedio: Mía
```

#### Ejercicio 8 — Agenda por inicial
```python
nombres = ["Ana", "Alberto", "Beto", "Carla", "Brenda", "Andrea", "Ceci", "Diego"]
```
Agrupa los nombres en un diccionario cuya clave es la **inicial** y cuyo valor es una **lista** de nombres. Muestra cada grupo con cuántos nombres tiene.
**Usa:** índice de string (`nombre[0]`), diccionario con listas, `in`, `append()`.
**Salida esperada:**
```
A (3): ['Ana', 'Alberto', 'Andrea']
B (2): ['Beto', 'Brenda']
C (2): ['Carla', 'Ceci']
D (1): ['Diego']
```

#### Ejercicio 9 — El ticket del merch
```python
precios = {"playera": 350, "gorra": 220, "parche": 80, "sudadera": 650}
carrito = ["playera", "gorra", "playera", "parche", "parche", "parche"]
```
El carrito es una lista con repetidos. Cuenta cuántas piezas hay de cada producto con un diccionario, calcula el importe de cada renglón y el subtotal. Si el subtotal pasa de $800, aplica 10 % de descuento.
**Usa:** diccionario contador, segundo diccionario de precios, `items()`, `if`.
**Salida esperada:**
```
2 x playera = $700
1 x gorra = $220
3 x parche = $240
Subtotal: $1160
Descuento: $116.0
Total: $1044.0
```

#### Ejercicio 10 — Traductor de mensajes de WhatsApp
```python
abrev = {"q": "que", "xq": "porque", "tmb": "también", "pq": "porque", "bn": "bien", "tqm": "te quiero mucho"}
```
Crea `expandir(mensaje)` que pase el mensaje a minúsculas, lo corte en palabras y cambie cada abreviatura por su significado (las palabras que no están se quedan igual). Debe **regresar** el mensaje traducido.
**Usa:** `lower()`, `split()`, `get()` con valor por defecto, lista, `return`.
💡 Pista: `" ".join(lista)` une una lista de palabras en un solo texto separado por espacios.
**Prueba con:** `"Q onda tmb voy al concierto xq tocan bn"` y `"tqm Mamá"`.
**Salida esperada:**
```
que onda también voy al concierto porque tocan bien
te quiero mucho mamá
```

---

### BLOQUE 3 · A prueba de usuarios (excepciones + validación)

#### Ejercicio 11 — Rendimiento de la moto
Crea `rendimiento()` que pida km recorridos y litros cargados (pueden tener decimales), calcule km/l redondeado a 1 decimal y lo **regrese**. Si escriben texto, avisa; si los litros son 0, avisa; en ambos casos vuelve a preguntar todo. Después clasifica: 20 o más "Excelente", 15 o más "Normal", menos "Revisa tu moto".
**Usa:** `while True`, `try`, `except ValueError`, `except ZeroDivisionError`, `float()`, función con `return`.
**Entradas de prueba:** `trescientos` · `300`, `0` · `300`, `16`
**Salida esperada:**
```
Escribe solo números
Los litros no pueden ser 0
Rendimiento: 18.8 km/l
Normal
```

#### Ejercicio 12 — Taquilla familiar
Pide la edad de **3 personas**. Cada edad se valida: si no es número, avisa; si está fuera de 0–120, avisa; en ambos casos vuelve a preguntar **por esa misma persona**. Crea `precio_boleto(edad)` con `return`: menores de 12 → $150, de 12 a 59 → $300, 60 o más → $180. Muestra cada boleto y el total.
**Usa:** `for` + `while True` + `try/except`, función con `return`, `if/elif/else`.
**Entradas de prueba:** `diez`, `10`, `-5`, `35`, `70`
**Salida esperada:**
```
Escribe la edad con número
Boleto: $150
Edad fuera de rango
Boleto: $300
Boleto: $180
Total a pagar: $630
```

#### Ejercicio 13 — Capturas sucias
```python
capturas = ["10", "7", "x", "", "9", "8.5", " 6 "]
```
Alguien capturó calificaciones a mano en un formulario. Convierte cada una a entero con `int()` dentro de un `try`: las válidas van a una lista y las inválidas se cuentan. Muestra el promedio de las válidas redondeado a 2 decimales.
**Usa:** `for`, `try/except ValueError`, lista con `append()`, contador.
**Salida esperada:**
```
Válidas: [10, 7, 9, 6]
Inválidas: 3
Promedio: 8.0
```
> En una celda Markdown explica en una línea por qué `" 6 "` sí se pudo convertir y `"8.5"` no.

#### Ejercicio 14 — Reserva tu asiento
```python
sala = [["X", "L", "L"], ["L", "X", "L"], ["X", "X", "L"]]
```
`X` = ocupado, `L` = libre. Crea `reservar(sala)` que pida fila y columna (índices desde 0) y **regrese** `True` si logró reservar o `False` si no. Atrapa texto (`ValueError`) y posiciones que no existen (`IndexError`); si el asiento está ocupado, avisa. Repite hasta lograr **una** reserva y muestra la sala sin corchetes.
**Usa:** matriz, función con `return`, `try` con dos `except`, `while`, `for` anidados con `end=" "`.
**Entradas de prueba:** `uno` · `0`, `5` · `0`, `0` · `1`, `2`
**Salida esperada:**
```
Escribe números
Ese asiento no existe
Ocupado, elige otro
¡Reservado!
X L L
L X X
X X L
```

#### Ejercicio 15 — Cupones de descuento
```python
cupones = {"METAL10": 10, "MOTO20": 20, "ROCK15": 15}
```
Crea `aplicar(total, codigo)` que limpie el código (`strip()` y `upper()`), busque el porcentaje en el diccionario y **regrese** el total con descuento. Si el cupón no existe, atrapa el `KeyError`, avisa y regresa el total sin cambios. Prueba con un total de $1200 y los códigos `"  moto20 "`, `"GRATIS"` y `"metal10"`.
**Usa:** `try/except KeyError`, métodos de string, función con `return`, `for` sobre una lista de códigos.
**Salida esperada:**
```
'  moto20 ' → $960.0
Cupón no válido
'GRATIS' → $1200
'metal10' → $1080.0
```

---

### BLOQUE 4 · El cartel (strings + todo lo demás)

#### Ejercicio 16 — ¿Tu contraseña aguanta?
Crea `evaluar(pw)` que **regrese una lista** con las fallas encontradas: menos de 8 caracteres, sin ningún número, sin ninguna mayúscula o con espacios. Si la lista está vacía, la contraseña es segura. Prueba con `"metal"`, `"Harley2008"`, `"road glide 08"` y `"KLR650moto"`.
**Usa:** `len()`, `for` sobre un string, `in`, lista de fallas, función con `return`.
💡 Pista: `"7".isdigit()` da `True` y `"A".isupper()` da `True`.
**Salida esperada:**
```
metal: ['mínimo 8 caracteres', 'falta un número', 'falta una mayúscula']
Harley2008: segura
road glide 08: ['falta una mayúscula', 'sin espacios']
KLR650moto: segura
```

#### Ejercicio 17 — Se lee igual al revés
Crea `es_palindromo(texto)` que ignore mayúsculas y espacios y **regrese** `True` o `False`. Pruébala con una tupla de frases: `"Anita lava la tina"`, `"ABBA"`, `"Metallica"` y `"Oso"`.
**Usa:** `lower()`, `replace()`, tupla, `for`, función con `return`.
💡 Pista: `texto[::-1]` regresa el texto al revés.
**Salida esperada:**
```
Anita lava la tina: True
ABBA: True
Metallica: False
Oso: True
```

#### Ejercicio 18 — Contador de vocales
```python
frase = "el rock nunca va a morir en esta ciudad"
```
Crea `vocales(palabra)` que cuente sus vocales con un `for` y regrese el número. Construye un diccionario palabra → vocales y di cuál tiene más.
**Usa:** `split()`, `for` sobre un string, `in "aeiou"`, diccionario, función con `return`.
**Salida esperada:**
```
{'el': 1, 'rock': 1, 'nunca': 2, 'va': 1, 'a': 1, 'morir': 2, 'en': 1, 'esta': 2, 'ciudad': 3}
Más vocales: ciudad (3)
```

#### Ejercicio 19 — Usuarios del laboratorio
```python
alumnos = ["Bruce Dickinson", "Brian Dickinson", "Ana Lopez", "Andrea Lopez", "Angel Lopez"]
```
Crea `usuario(nombre)` que regrese la inicial del nombre más el apellido, todo en minúsculas (`"Bruce Dickinson"` → `"bdickinson"`). Si el usuario ya existe, agrégale un número empezando en 2 hasta que quede libre.
**Usa:** `lower()`, `split()`, índices de string, lista de usados, `while` con `in`, `str()`.
**Salida esperada:**
```
Bruce Dickinson → bdickinson
Brian Dickinson → bdickinson2
Ana Lopez → alopez
Andrea Lopez → alopez2
Angel Lopez → alopez3
```

#### Ejercicio 20 — El censor del salón
```python
prohibidas = ["tonto", "menso", "baboso"]
```
Crea `censurar(frase)` que cambie cada palabra prohibida (sin importar mayúsculas) por asteriscos del mismo largo y **regrese una tupla**: (frase censurada, cuántas censuró). Prueba con `"no seas menso y pásame el código"`, `"Tonto el que no haga commit"` y `"todo bien profe"`.
**Usa:** `split()`, `for` con `range(len(...))`, `lower()`, `in`, `"*" * len(...)`, `return` de una tupla, desempaquetar.
**Salida esperada:**
```
no seas ***** y pásame el código  (1 censuradas)
***** el que no haga commit  (1 censuradas)
todo bien profe  (0 censuradas)
```

---

### BLOQUE 5 · Integradores

#### Ejercicio 21 — Estacionamiento del foro
```python
autos = [("ABC123", 9, 11), ("XYZ789", 8, 15), ("MOT650", 10, 11), ("QRO001", 13, 13)]
```
Cada tupla es (placa, hora de entrada, hora de salida). Tarifa: $20 la primera hora (o fracción, incluso 0 horas) y $15 cada hora adicional. Crea `cobro(entrada, salida)` con `return`, guarda los cobros en un diccionario placa → cobro y muestra el total del día recorriendo `values()`.
**Usa:** lista de tuplas, desempaquetar, función con `return`, `if`, diccionario, `values()`.
**Salida esperada:**
```
ABC123: 2 h → $35
XYZ789: 7 h → $110
MOT650: 1 h → $20
QRO001: 0 h → $20
Total del día: $185
```

#### Ejercicio 22 — Tabla del torneo
```python
partidos = (("Pumas", "Tigres", 2, 1), ("América", "Pumas", 0, 0), ("Tigres", "América", 3, 2),
            ("Pumas", "América", 1, 2), ("Tigres", "Pumas", 1, 1))
```
Cada tupla es (local, visitante, goles local, goles visitante). Victoria = 3 puntos, empate = 1 para cada uno, derrota = 0. Arma un diccionario equipo → puntos (los equipos se agregan al aparecer) y di quién es el campeón.
**Usa:** tupla de tuplas, desempaquetar, `in`, diccionario, `if/elif/else`.
**Salida esperada:**
```
{'Pumas': 5, 'Tigres': 4, 'América': 4}
Campeón: Pumas con 5 puntos
```

#### Ejercicio 23 — Pulseras cashless del festival
```python
saldos = {"Ana": 500, "Luis": 200, "Mía": 300}
movs = ["Ana:-150", "Luis:-250", "Mía:+100", "Pedro:-50", "Ana:-cien", "Mía:-380", "Luis:-200"]
```
Cada movimiento es `"nombre:monto"`. Sepáralo con `split(":")` y convierte el monto con `int()`. Si el saldo quedaría negativo, rechaza el movimiento sin aplicarlo. Atrapa los montos inválidos (`ValueError`) y las personas sin pulsera (`KeyError`), y cuenta esos movimientos con error.
**Usa:** `split()`, `try` con dos `except`, diccionario, `if/else`, contador.
**Salida esperada:**
```
Luis: saldo insuficiente
Pedro no tiene pulsera
Monto inválido en 'Ana:-cien'
{'Ana': 350, 'Luis': 0, 'Mía': 20}
Movimientos con error: 2
```

#### Ejercicio 24 — Sábana de calificaciones
```python
nombres = ("Ana", "Luis", "Mía", "Beto")
cal = [[85, 90, 78, 92], [60, 75, 70, 68], [95, 98, 100, 97], [70, 65, 80, 75]]
```
Cada fila de la matriz son los 4 parciales de un alumno (en el mismo orden que la tupla de nombres). Crea `promedio(lista)` con `return` y úsala para el promedio de cada alumno (filas) **y** de cada parcial (columnas). Di quién es el mejor alumno.
**Usa:** tupla + matriz, `for` anidados, construir una lista por columna, función con `return` reutilizada.
**Salida esperada:**
```
Ana: 86.25
Luis: 68.25
Mía: 97.5
Beto: 72.5
Parcial 1: 77.5
Parcial 2: 82.0
Parcial 3: 82.0
Parcial 4: 83.0
Mejor alumno: Mía
```

#### Ejercicio 25 — La playlist del viaje
```python
playlist = ["Master of Puppets - Metallica - 8:35", "Holy Wars - Megadeth - 6:32",
            "Fade to Black - Metallica - 6:57", "The Trooper - Iron Maiden - 4:10",
            "Hangar 18 - Megadeth - 5:14", "Aces High - Iron Maiden - 4:31"]
```
Separa cada línea con `split(" - ")`. Crea `a_segundos("8:35")` que regrese 515 y reutiliza tu `formato(seg)` del ejercicio 5. Acumula en un diccionario los segundos por artista, muestra cada artista con su tiempo, el que más suena y la duración total.
**Usa:** `split()` dos veces, `int()`, dos funciones con `return`, diccionario acumulador, desempaquetar.
**Salida esperada:**
```
Metallica: 15:32
Megadeth: 11:46
Iron Maiden: 8:41
Más tiempo: Metallica
Total: 35:59
```

---

## 3. Evaluación (20 pts)

Cada ejercicio vale **0.8 pts**:

| Nivel | Pts | Condición |
| :--- | :---: | :--- |
| Completo | 0.8 | Corre, la salida coincide con la esperada y usa todo lo que pide su línea **"Usa:"**. |
| Parcial | 0.4 | Corre, pero la salida no coincide en algún dato **o** le falta algún elemento de "Usa:" (por ejemplo, no hizo la función). |
| Sin crédito | 0 | No está, no corre, la celda no está ejecutada o es idéntico al de otro alumno. |

**Total:** suma de los 25 ejercicios, redondeada al entero más cercano.

## 4. Checklist
- [ ] Están los 25 ejercicios, cada uno con su título en Markdown.
- [ ] Usé los datos y las entradas de prueba exactamente como vienen.
- [ ] Cada salida coincide con la esperada.
- [ ] Respeté la línea "Usa:" de cada ejercicio.
- [ ] El notebook está ejecutado y se ven las salidas en GitHub.
- [ ] Está en `semana5/castigo2_ejercicios.ipynb`, en mi mismo repositorio.
