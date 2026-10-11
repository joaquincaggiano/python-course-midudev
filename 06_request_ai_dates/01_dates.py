# Trabajando con fechas y horas en Python

# Limpiar la terminal
import subprocess
_ = subprocess.run(["clear"], check=False)

# Módulo de fechas y horas
from datetime import datetime, timedelta
# Módulo de localización
import locale

# Configurar la localización para español
_ = locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')

# 1. Obtener la fecha y hora actual
print("\nFecha y hora actual:")
now = datetime.now()
print(now)

# 2. Crear una fecha y hora específica
print("\nFecha y hora específica:")
specific_date = datetime(2026, 10, 21, 10, 30, 0)
print(specific_date)

# 3. Formatear fechas: método strftime
# Docs: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print("\nFormatear fechas:")
formatted_date = now.strftime("%d/%m/%Y")
print(formatted_date)

# Formatear fecha con día y mes en español
print("\nFormatear fecha con día y mes en español:")
formatted_date = now.strftime("%d de %B de %Y")
print(formatted_date)

# 4. Operaciones con fechas (sumar/restar dias, minutos, horas, meses)
print("\nOperaciones con fechas:")
print(f"Hoy: {now}")
yesterday = now - timedelta(days=1)
print(f"Ayer: {yesterday}")
tomorrow = now + timedelta(days=1)
print(f"Mañana: {tomorrow}")
one_hour_later = now + timedelta(hours=1)
print(f"Una hora después: {one_hour_later}")

# 5. Obtener componentes individuales de una fecha
print("\nObtener componentes individuales de una fecha:")
print(f"Año: {now.year}")
print(f"Mes: {now.month}")
print(f"Día: {now.day}")
print(f"Hora: {now.hour}")
print(f"Minuto: {now.minute}")
print(f"Segundo: {now.second}")
print(f"Microsegundo: {now.microsecond}")

# 6. Calcular la diferencia entre dos fechas
print("\nCalcular la diferencia entre dos fechas:")
date1 = datetime.now()
date2 = datetime(2026, 10, 21)
difference = date2 - date1
print(f"Diferencia entre las fechas: {difference}")