from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]
def recibop():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t\t{fecha_recibo}'+ '\n')
    texto_recibo.insert(END, F'*'* 63+ '\n')
    texto_recibo.insert(END, 'Items\t\tCant. \tCosto items\n')
    texto_recibo.insert(END, F'-'* 75+ '\n') 
    
    x = 0 
    for com in textoc:
        if com.get() != "0":
            texto_recibo.insert(END, F'{list_comidas[x]}\t\t{com.get()}\t'
                                f'${int(com.get()) * precios_comida[x]}\n')
        x += 1     
    x = 0                
    for beb in textob:
        if beb.get() != "0":
            texto_recibo.insert(END, F'{list_bebidas[x]}\t\t{beb.get()}\t'
                                f'${int(beb.get()) * precios_bebida[x]}\n')
        x += 1   
    x = 0                  
    for pos in textop:
        if pos.get() != "0":
            texto_recibo.insert(END, F'{list_postres[x]}\t\t{pos.get()}\t'
                                f'${int(pos.get()) * precios_postres[x]}\n')
        x += 1  
    texto_recibo.insert(END, F'-'* 75+ '\n') 
    texto_recibo.insert(END, F'Costo de la comida: \t\t\t{var_costo_comida.get()}\n')  
    texto_recibo.insert(END, F'costo de la bebida: \t\t\t{var_costo_bebida.get()}\n')     
    texto_recibo.insert(END, F'costo de los postres: \t\t\t{var_costo_postre.get()}\n')    
    texto_recibo.insert(END, F'-'* 75+ '\n')      
    texto_recibo.insert(END, F'Subtotal: \t\t\t{var_subtotal.get()}\n') 
    texto_recibo.insert(END, F'Impuestos: \t\t\t{var_impuesto.get()}\n')    
    texto_recibo.insert(END, F'Total: \t\t\t{var_total.get()}\n')     
    texto_recibo.insert(END, F'*'* 63+ '\n')          
    texto_recibo.insert(END, 'Lo esperamos pronto!')     
def totalp():
    subtotal_comida = 0
    p = 0
    for cant in textoc:
        subtotal_comida = subtotal_comida + (float(cant.get()) * precios_comida[p])
        p += 1
    subtotal_bebida = 0
    p = 0
    for cant in textob:
        subtotal_bebida = subtotal_bebida + (float(cant.get()) * precios_bebida[p])
        p += 1
    subtotal_postre = 0
    p = 0
    for cant in textop:
        subtotal_postre = subtotal_postre + (float(cant.get()) * precios_postres[p])
        p += 1 
    
    sub_total = subtotal_comida + subtotal_bebida + subtotal_postre
    impuestop = sub_total * 0.07
    totalp = sub_total + impuestop
    
    var_costo_comida.set(f"${round(subtotal_comida,2)}")
    var_costo_bebida.set(f"${round(subtotal_bebida,2)}")
    var_costo_postre.set(f"${round(subtotal_postre,2)}")
    var_subtotal.set(f"${round(sub_total,2)}")
    var_impuesto.set(f"${round(impuestop,2)}")
    var_total.set(f"${round(totalp,2)}")

def click_boton(numero):
    global operador
    
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0,END)
    
def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0, resultado) 
    operador = ""

def revisar_check():
    x = 0
    for c in cuadrosc:
        if variables[x].get() == 1:
            cuadrosc[x].config(state = NORMAL)
            if cuadrosc[x].get() == 0:
                cuadrosc[x].delete(0,END)
            cuadrosc[x].focus()
        else:  
            cuadrosc[x].config(state = DISABLED)
            textoc[x].set("0")
        x += 1
    
    x = 0
    for b in cuadrosb:
        if variablesb[x].get() == 1:
            cuadrosb[x].config(state = NORMAL)
            if cuadrosb[x].get() == 0:
                cuadrosb[x].delete(0,END)
            cuadrosb[x].focus()
        else:  
            cuadrosb[x].config(state = DISABLED)
            textob[x].set("0")
        x += 1
    
    x = 0
    for p in cuadrosp:
        if variablesp[x].get() == 1:
            cuadrosp[x].config(state = NORMAL)
            if cuadrosp[x].get() == 0:
                cuadrosp[x].delete(0,END)
            cuadrosp[x].focus()
        else:  
            cuadrosp[x].config(state = DISABLED)
            textop[x].set("0")
        x += 1

def guardar():  
    info_recibo = texto_recibo.get(1.0,END)  
    archivo = filedialog.asksaveasfile(mode = "w", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("información", "Su recibo ha sido guardado")

def resetear():
    texto_recibo.delete(0.1,END)
    for text in textoc:
        text.set("0")
    for text in textob:
        text.set("0")    
    for text in textop:
        text.set("0")    
    for cuadro in cuadrosc:
        cuadro.config(state = DISABLED)    
    for cuadro in cuadrosb:
        cuadro.config(state = DISABLED)    
    for cuadro in cuadrosp:
        cuadro.config(state = DISABLED)    
    for v in variables:
        v.set(0)
    for v in variablesb:
        v.set(0)
    for v in variablesp:
        v.set(0)
    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_postre.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")
#iniciar tkinter
app = Tk()

#tamaño
app.geometry("1200x630+0+0")

#evitar maximizar
app.resizable(0,0)

#titulo 
app.title("Gestor de restaurantes")

#icono
app.iconbitmap("C:\\Users\\Tomas\\Desktop\\Curso python\\curso python 2\\practica\\gestor de restaurantes\\restaurant.ico")

#color
app.config(bg="aquamarine1")

#panel superior
panel_sup = Frame(app, bd=1, relief=FLAT)
panel_sup.pack(side="top")

#titulo
titulo = Label(panel_sup, text = "Sistema de facturacion", fg = "cadet blue", font = ("Dosis",58),bg = "aquamarine1",width = 27)
titulo.grid(row = 0, column= 0)

#panel izquierdo
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side =LEFT)

#panel costos
costos =Frame(left_panel, bd=1, relief=FLAT, bg = "cadet blue",padx=50)
costos.pack(side=BOTTOM)

#panel comidas
comidas = LabelFrame(left_panel, text= "Comida", font = ("Dosis", 19,"bold"), bd=1, relief=FLAT, fg = "cadet blue")
comidas.pack(side=LEFT)

#panel bebidas
bebidas = LabelFrame(left_panel, text= "Bebidas", font = ("Dosis", 19,"bold"), bd=1, relief=FLAT, fg = "cadet blue")
bebidas.pack(side=LEFT)


#panel postres
postres = LabelFrame(left_panel, text= "Postres", font = ("Dosis", 19,"bold"), bd=1, relief=FLAT, fg = "cadet blue")
postres.pack(side=LEFT)
#panel derecha
right_panel = Frame(app,bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

#panel calculadora
calculadora = Frame(right_panel,bd=1, relief=FLAT, bg= "aquamarine1")
calculadora.pack()

#panel recibo
recibo = Frame(right_panel,bd=1, relief=FLAT, bg= "aquamarine1")
recibo.pack()

#panel calculadora
botones = Frame(right_panel,bd=1, relief=FLAT, bg= "aquamarine1")
botones.pack()

#lista de productos
list_comidas = ["burger","pizza","salmon","ensalada","fideos","empanada","milanesa"]
list_bebidas = ["agua","gaseosa","cerveza","jugo","soda","vino","licuados","agua"]
list_postres = ["flan","budín","helado","torta","pie","fruta","durazno","budín"]
#genera items comida
variables = []
cuadrosc=[]
textoc = []
count = 0
for comida in list_comidas:
    #crear checkbutton
    variables.append("")
    variables[count]=IntVar()
    comida = Checkbutton(comidas, text= comida.title(), font=("Dosis", 19, "bold")
                         ,onvalue=1,offvalue=0, variable=variables[count],
                         command = revisar_check)
    comida.grid(row=count,column= 0, sticky=W)
    
    #cuadros de entrada
    cuadrosc.append("")
    textoc.append("")
    textoc[count] = StringVar()
    textoc[count].set("0")
    cuadrosc[count] = Entry(comidas, font=("Dosis",18,"bold"),
                            bd= 1, width=6,state=DISABLED,textvariable=textoc[count])
    cuadrosc[count].grid(row=count, column=1)
    count += 1

#genera items bebidas
variablesb = []
cuadrosb=[]
textob = []
count = 0
for bebida in list_bebidas:
    variablesb.append("")
    variablesb[count]=IntVar()
    bebida = Checkbutton(bebidas, text=bebida.title(), font=("Dosis", 19, "bold"),onvalue=1,offvalue=0, variable=variablesb[count]
                         ,
                         command = revisar_check)
    bebida.grid(row=count,column= 0, sticky=W)
    
     #cuadros de entrada
    cuadrosb.append("")
    textob.append("")
    textob[count] = StringVar()
    textob[count].set("0")
    cuadrosb[count] = Entry(bebidas, font=("Dosis",18,"bold"),
                            bd= 1, width=6,state=DISABLED,textvariable=textob[count])
    cuadrosb[count].grid(row=count, column=1)
    count += 1

#genera items postres
variablesp = []
cuadrosp=[]
textop = []
count = 0
for postre in list_postres:
    variablesp.append("")
    variablesp[count]=IntVar()
    postre = Checkbutton(postres, text= postre.title(), font=("Dosis", 19, "bold"),onvalue=1,offvalue=0, variable=variablesp[count]
                         ,
                         command = revisar_check)
    postre.grid(row=count,column= 0, sticky=W)
    
     #cuadros de entrada
    cuadrosp.append("")
    textop.append("")
    textop[count] = StringVar()
    textop[count].set("0")
    cuadrosp[count] = Entry(postres, font=("Dosis",18,"bold"),
                            bd= 1, width=6,state=DISABLED,textvariable=textop[count])
    cuadrosp[count].grid(row=count, column=1)
    count += 1
#variable
var_costo_comida= StringVar()
var_costo_bebida= StringVar()
var_costo_postre= StringVar()
var_subtotal= StringVar()
var_impuesto= StringVar()
var_total= StringVar()

#etiquetas de costo y campos de entrada
costo_comida = Label(costos, 
                     text="Costo comida",
                     font=("Dosis",12,"bold"),bg= "cadet blue",
                     fg = "white")
costo_comida.grid(row= 0, column= 0)
textocosto = Entry(costos,font=("Dosis",12,"bold"),bd=1, width=10, state="readonly",textvariable=var_costo_comida)
textocosto.grid(row= 0, column= 1, padx=41)




#etiquetas de costo y campos de entrada bebidas
costo_bebida = Label(costos, 
                     text="Costo bebida",
                     font=("Dosis",12,"bold"),bg= "cadet blue",
                     fg = "white")
costo_bebida.grid(row= 1, column= 0)
textocostob = Entry(costos,font=("Dosis",12,"bold"),bd=1, width=10, state="readonly",textvariable=var_costo_bebida)
textocostob.grid(row= 1, column= 1, padx=41)

#etiquetas de costo y campos de entrada postres
costo_postre= Label(costos, 
                     text="Costo postres",
                     font=("Dosis",12,"bold"),bg= "cadet blue",
                     fg = "white")
costo_postre.grid(row= 2, column= 0)
textocostop = Entry(costos,font=("Dosis",12,"bold"),bd=1, width=10, state="readonly",textvariable=var_costo_postre)
textocostop.grid(row= 2, column= 1, padx=41)

#etiquetas de subtotal
subtotal= Label(costos, 
                     text="subtotal",
                     font=("Dosis",12,"bold"),bg= "cadet blue",
                     fg = "white")
subtotal.grid(row= 0, column= 2)
textosubtotal = Entry(costos,font=("Dosis",12,"bold"),bd=1, width=10, state="readonly",textvariable=var_subtotal)
textosubtotal.grid(row= 0, column= 3, padx=41)

#etiquetas de impuesto
impuesto= Label(costos, 
                     text="impuesto",
                     font=("Dosis",12,"bold"),bg= "cadet blue",
                     fg = "white")
impuesto.grid(row= 1, column= 2)
textoimpuesto = Entry(costos,font=("Dosis",12,"bold"),bd=1, width=10, state="readonly",textvariable=var_impuesto)
textoimpuesto.grid(row= 1, column= 3, padx=41)

#etiquetas de total
total= Label(costos, 
                     text="total",
                     font=("Dosis",12,"bold"),bg= "cadet blue",
                     fg = "white")
total.grid(row= 2, column= 2)
textototal = Entry(costos,font=("Dosis",12,"bold"),bd=1, width=10, state="readonly",textvariable=var_total)
textototal.grid(row= 2, column= 3, padx=41)

#botones
boton = ["total", "recibo", "guardar","resetear"]
botones_creados =[]
columnas = 0
for bot in boton:
    bot =  Button(botones, text=bot.title(),
                  font = ("Dosis",12,"bold"),
                          fg= "white",
                          bg = "cadet blue",
                          bd= 1,
                          width = 9)
    botones_creados.append(bot)
    
    bot.grid(row=0, column = columnas)
    columnas +=1
botones_creados[0].config(command=totalp)   
botones_creados[1].config(command=recibop)  
botones_creados[2].config(command=guardar)  
botones_creados[3].config(command=resetear)  
#area de recibo
texto_recibo = Text(recibo,
                    font = ("Dosis",12,"bold"),
                    bd = 1,
                    width=42,
                    height=10)
texto_recibo.grid(row = 0, column= 0)

botones_guardados = []
#calculadora
visor_calculadora = Entry(calculadora, font = ("Dosis",16,"bold"),width = 32
                          , bd= 1)
visor_calculadora.grid(row = 0, column = 0,columnspan = 4)
botones_calcu = ["7","8","9","+","4","5","6","-","1","2","3","x","R","B","0","/"]
fila = 1
columna = 0
for but in botones_calcu:
    but = Button(calculadora, text = but.title(),
                 font= ("Dosis",16,"bold"),
                 fg = "white",
                 bg = "cadet blue",
                 bd = 1,
                 width = 8)
    botones_guardados.append(but)
    but.grid (row = fila, column= columna)
    if columna == 3:
        fila +=1
    
    columna += 1
    if columna == 4:
        columna = 0
botones_guardados[0].config(command=lambda :click_boton("7"))
botones_guardados[1].config(command=lambda :click_boton("8"))
botones_guardados[2].config(command=lambda :click_boton("9"))
botones_guardados[3].config(command=lambda :click_boton("+"))
botones_guardados[4].config(command=lambda :click_boton("4"))
botones_guardados[5].config(command=lambda :click_boton("5"))
botones_guardados[6].config(command=lambda :click_boton("6"))
botones_guardados[7].config(command=lambda :click_boton("-"))
botones_guardados[8].config(command=lambda :click_boton("1"))
botones_guardados[9].config(command=lambda :click_boton("2"))
botones_guardados[10].config(command=lambda :click_boton("3"))
botones_guardados[11].config(command=lambda :click_boton("*"))
botones_guardados[12].config(command=lambda :obtener_resultado())
botones_guardados[13].config(command=lambda :borrar())
botones_guardados[14].config(command=lambda :click_boton("0"))
botones_guardados[15].config(command=lambda :click_boton("/"))
#evitar que la pantalla se cierre
app.mainloop()