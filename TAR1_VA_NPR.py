import matplotlib.pyplot as plt
import numpy as np


def g(x):
  y = (2500 - 25*x) / 250
  return y


# Mínimo de campañas
min = 0
# Maximo de campañas de Social Media
max_x = 2500 / 36
# Maximo de campañas de TV
max_y = 2500 / 200

# Generar puntos para la gráfica
x = np.linspace(min, max_x, 100)


# Grafica de funcion
plt.plot(x, g(x), color = "darkorange", linewidth=5)


# Detalles de la gráfica
plt.xlabel('Campañas de Social Media')
plt.ylabel('Campañas de TV')
plt.title("Grafica de inversión en campañas")


plt.show()