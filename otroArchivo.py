from puntajes import agregar_jugador, mostrar_datos, eliminar_todos_los_jugadores
from jugador import Jugador

# Crear instancias de jugadores falsos
jugador_falso1 = Jugador(nombre="Paloma", puntos=300, tiempo=300)
jugador_falso2 = Jugador(nombre="Azul", puntos=450, tiempo=350)
jugador_falso3 = Jugador(nombre="Miguel", puntos=150, tiempo=400)

# Agregar los jugadores a la base de datos
agregar_jugador(jugador_falso1)
agregar_jugador(jugador_falso2)
agregar_jugador(jugador_falso3)

# Mostrar los datos para verificar
print(mostrar_datos())

# eliminar_todos_los_jugadores()