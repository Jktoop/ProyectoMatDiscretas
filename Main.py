import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from ciudades import CIUDADES, CONEXIONES, POSICIONES
from dijkstra import construir_grafo, dijkstra, obtener_ruta

# variables globales de la interfaz
combo_origen  = None
combo_destino = None
texto_resultado = None
lienzo = None
fig = None
ax = None
grafo = None   # diccionario con la estructura del grafo


# dibujar el grafo usando matplotlib directamente 
def dibujar_grafo(ruta_optima=None):

    ax.clear()
    ax.set_facecolor("#181825")
    fig.patch.set_facecolor("#181825")

    # Construir un set con las aristas de la ruta para busqueda rapida
    aristas_ruta = set()
    if ruta_optima and len(ruta_optima) > 1:
        for i in range(len(ruta_optima) - 1):
            a = ruta_optima[i]
            b = ruta_optima[i + 1]
            aristas_ruta.add((a, b))
            aristas_ruta.add((b, a))

    # dibujar todas las aristas
    for origen, destino, peso in CONEXIONES:
        x1, y1 = POSICIONES[origen]
        x2, y2 = POSICIONES[destino]

        if (origen, destino) in aristas_ruta:
            # arista de la ruta optima roja y gruesa
            ax.plot([x1, x2], [y1, y2],
                    color="#f38ba8", linewidth=3.0, zorder=1)
            # mostrar el peso sobre la arista
            mx, my = (x1 + x2) / 2, (y1 + y2) / 2
            ax.text(mx, my, f"{peso} km",
                    fontsize=6.5, color="#f9e2af", ha="center", va="center",
                    bbox=dict(boxstyle="round,pad=0.2", fc="#313244", ec="none", alpha=0.85),
                    zorder=3)
        else:
            # arista normal gris
            ax.plot([x1, x2], [y1, y2],
                    color="#45475a", linewidth=1.0, zorder=1)

    # dibujar los nodos
    origen_sel  = combo_origen.get()
    destino_sel = combo_destino.get()

    for ciudad in CIUDADES:
        x, y = POSICIONES[ciudad]

        if ciudad == origen_sel:
            color = "#a6e3a1"   # verde = origen
            tamanio = 120
        elif ciudad == destino_sel:
            color = "#f9e2af"   # amarillo = destino
            tamanio = 120
        elif ruta_optima and ciudad in ruta_optima:
            color = "#f38ba8"   # rosa = en la ruta
            tamanio = 100
        else:
            color = "#89b4fa"   # azul = resto
            tamanio = 80

        ax.scatter(x, y, s=tamanio, color=color, zorder=4)
        ax.text(x, y + 0.5, ciudad,
                fontsize=7.5, color="#cdd6f4", ha="center", va="bottom",
                fontweight="bold", zorder=5)

    # leyenda
    leyenda = [
        mlines.Line2D([], [], color="#a6e3a1", marker="o", linestyle="None",
                      markersize=7, label="Origen"),
        mlines.Line2D([], [], color="#f9e2af", marker="o", linestyle="None",
                      markersize=7, label="Destino"),
        mlines.Line2D([], [], color="#f38ba8", linewidth=2.5,
                      label="Ruta optima"),
        mlines.Line2D([], [], color="#45475a", linewidth=1.0,
                      label="Otras conexiones"),
    ]
    ax.legend(handles=leyenda, loc="lower left",
              facecolor="#313244", edgecolor="none",
              labelcolor="#cdd6f4", fontsize=8)

    ax.set_title("Red de ciudades europeas", color="#cdd6f4", fontsize=11, pad=10)
    ax.axis("off")
    fig.tight_layout()
    lienzo.draw()

    # mostrar el resultado en el cuadro de texto

def mostrar_resultado(origen, destino, ruta, costo):
    texto_resultado.config(state=tk.NORMAL)
    texto_resultado.delete("1.0", tk.END)

    lineas = [
        f"Origen  : {origen}",
        f"Destino : {destino}",
        "-" * 28,
        "Ruta optima:",
    ]
    for i, ciudad in enumerate(ruta):
        flecha = "  →" if i < len(ruta) - 1 else ""
        lineas.append(f"  {ciudad}{flecha}")

    lineas += [
        "-" * 28,
        f"Costo total : {costo} km",
        f"Tramos      : {len(ruta) - 1}",
    ]

    texto_resultado.insert(tk.END, "\n".join(lineas))
    texto_resultado.config(state=tk.DISABLED)

# acción del boton calcular

def calcular_ruta():
    origen  = combo_origen.get()
    destino = combo_destino.get()

    if origen == destino:
        messagebox.showwarning("Advertencia",
                               "El origen y el destino deben ser ciudades distintas.")
        return

    distancias, anteriores = dijkstra(grafo, origen)
    ruta  = obtener_ruta(anteriores, origen, destino)
    costo = distancias[destino]

    if not ruta or costo == float('inf'):
        messagebox.showerror("Error", "No existe ruta entre esas ciudades.")
        return

    mostrar_resultado(origen, destino, ruta, costo)
    dibujar_grafo(ruta_optima=ruta)
    
    # Construir ventana prinicpal
def crear_ventana():
    global combo_origen, combo_destino, texto_resultado
    global lienzo, fig, ax, grafo
    
    grafo = construir_grafo(CIUDADES, CONEXIONES)
    
    ventana = tk.Tk()
    ventana.title("Ruta optimas entre Ciudades Europeas")
    ventana.geometry("1100x680")
    ventana.configure(bg="#1e1e2e")
    
    # panel izquierda (controles)
    panel_izq = tk.Frame(ventana, bg="#1e1e2e", width=250)
    panel_izq.pack(side=tk.LEFT, fill=tk.Y, padx=16, pady=16)
    panel_izq.pack_propagate(False)
    
    tk.Label(panel_izq, text="Rutas Optimas",
             font=("Helvetica", 15, "bold"),
             bg="#1e1e2e", fg="#cdd6f4").pack(padx=(0, 2))
    
    tk.Label(panel_izq, text="Ciudades Europeas | Dijkstra",
             font=("Helvetica", 9),
             bg="#1e1e2e", fg="#6c7086").pack(pady=(0,18))
    
    # Origen
    tk.Label(panel_izq, text="Ciudad de Origen",
             font=("Helvetica", 10, "bold"),
             bg="#1e1e2e", fg="#89b4fa").pack(anchor="w")
    
    combo_origen = ttk.Combobox(panel_izq,
                                values=sorted(CIUDADES),
                                state="readonly",
                                font=("Helvetica", 10))
    combo_origen.set("Madrid")
    combo_origen.pack(fill=tk.X, pady=(4, 12))
    
    # Destino
    tk.Label(panel_izq, text="Ciudad de Destino",
             font=("Helvetica", 10, "bold"),
             bg="#1e1e2e", fg="#a6e3a1").pack(anchor="w")
    
    combo_destino = ttk.Combobox(panel_izq,
                                 values=sorted(CIUDADES),
                                 state="readonly",
                                 font=("Helvetica", 10))
    
    combo_destino.set("Berlin")
    combo_destino.pack(fill=tk.X, pady=(4, 18))
    
    # Boton calcular
    tk.Button(panel_izq,
              text="Calcular Ruta Optima",
              font=("Helvetica", 11, "bold"),
              bg="#89b4fa", fg="#1e1e2e",
              activebackground="#74c7ec",
              relief=tk.FLAT, cursor="hand2",
              command=calcular_ruta).pack(fill=tk.X, pady=(0, 18))
    
    # Cuadro de resultado
    tk.Label(panel_izq, text="Resultado",
             font=("Helvetica", 10, "bold"),
             bg="#1e1e2e", fg="#cdd6f4").pack(anchor="w")
    texto_resultado = tk.Text(panel_izq,
                              height=14,
                              font=("Courier", 9),
                              bg="#313244", fg="#cdd6f4",
                              relief=tk.FLAT,
                              wrap=tk.WORD,
                              state=tk.DISABLED,
                              padx=8, pady=8)
    texto_resultado.pack(fill=tk.BOTH, expand=True)

    # ---- Panel derecho (grafico) ----
    panel_der = tk.Frame(ventana, bg="#181825")
    panel_der.pack(side=tk.LEFT, fill=tk.BOTH, expand=True,
                   padx=(0, 16), pady=16)

    fig, ax = plt.subplots(figsize=(9, 7))
    lienzo = FigureCanvasTkAgg(fig, master=panel_der)
    lienzo.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Dibujar el grafo inicial (sin ruta)
    dibujar_grafo(ruta_optima=None)

    ventana.mainloop()



# Punto de entrada
if __name__ == "__main__":
    crear_ventana()
