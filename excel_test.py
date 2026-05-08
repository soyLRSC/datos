import xlwings as xw
import pandas as pd 
import matplotlib.pyplot as plt

wb = xw.Book(r"D:\analisis de datos\excel avanzado.xlsx")
sheet = wb.sheets[0]
sht = wb.sheets.add(name="Graficos")

data = {
     "Mes": ["Enero", "Febrero", "Marzo", "Abril"],
    "Ventas": [120, 150, 90, 200]
}

df = pd.DataFrame(data)

# Escribir el DataFrame en Excel (a partir de la celda A2)
sheet.range("a2").value = df

#generar grafico con matplotlib
plt.figure(figsize=(8,5))
plt.bar(df["Mes"], df["Ventas"], color='green')
plt.xlabel("Mes")
plt.ylabel("Ventas")
plt.title("Ventas por mes")

#insertar grafico en el excel 
sht.pictures.add(plt.gcf(), name="Grafico de ventas", update=True, left=300, top=50)

#GUARDAR
wb.save()

