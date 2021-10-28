import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("si-datos.csv")

df.set_index('heuristicas', inplace=True)

df[['nodos']].plot(kind="bar", legend=True)


plt.ylabel("Heurísticas")
plt.suptitle("Comparativa entre heurísticas")

# plt.show()
plt.savefig("result.png")
