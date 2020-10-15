import pandas as pd
import matplotlib.pyplot as plt

f= pd.read_csv("rendu.csv")
f.head()

plt.plot(f["x"], f["normal"]/10, label="normal")
plt.plot(f["x"], f["simple"], label="simple") 
plt.plot(f["x"], f["anneaux"], label="anneaux")
plt.plot(f["x"], f["hyper"], label="hyper")
leg = plt.legend(loc='best', ncol=2, mode="expand", shadow=True, fancybox=True)
plt.show()
