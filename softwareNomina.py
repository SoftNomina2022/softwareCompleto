from re import A
from tkinter import *
from typing_extensions import Self
from fpdf import FPDF
import random
from tkinter import messagebox


class Bill_App(FPDF):
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#fafafa")
        self.root.title("Calculadora pago de nómina")
        title = Label(self.root, text="Sistema de pago de Nómina", bd=12, relief=RIDGE, font=(
            "Arial Black", 20), bg="#1e3c68", fg="white").pack(fill=X)
        # ===================================variables=======================================================================================
        self.diasLaborales = IntVar() #Dias que laboró el empleado durante el mes
        self.salarioDia = IntVar() #Calcular el día
        
        self.canthrn = IntVar()  #Cantidad de horas con recargo nocturno
        self.canthed = IntVar()  #Cantidad de horas extras diurnas
        self.canthen = IntVar()  #Cantidad de horas extras nocturnas
        self.canthrfd = IntVar() #Cantidad de horas con recargo festivo diurno
        self.canthrfn = IntVar() #Cantidad de horas con recargo festivo nocturno
        self.canthdfe = IntVar() #Cantidad de horas diurnas festivas extras
        self.canthnfe = IntVar() #Cantidad de horas nocturnas festivas extras
        
        self.c_name = StringVar() #Nombre del empleado

        self.bill_no = StringVar()          #Numero aleatorio para el comprobante
        x = random.randint(1000, 9999)      #Numero aleatorio para el comprobante
        self.bill_no.set(str(x))            #Numero aleatorio para el comprobante

        self.salario = IntVar()     #Salario mensual
        self.dias = StringVar()     #Reset dias laborales
        self.setsd = StringVar()    #Envio salario diario
        self.setsb = StringVar()    #Envio salario basico
        self.sethl = StringVar()    #Envio hora laboral
        self.setatd = StringVar()   #Envio auxilio de transporte diario
        self.setatp = StringVar()   #Envio auxilio de transporte a pagar
        self.settsba = StringVar()  #Envio total salario basico + auxilio de transporte
        self.setther = StringVar()  #Envio total horas extras y recargos
        self.settap = StringVar()   #Envio total a pagar
        # ==========================================Detalles del Empleado=================================================
        details = LabelFrame(self.root, text="Detalles del Empleado", font=(
            "Arial Black", 12), bg="#3891c8", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Nombre del Empleado", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=0, padx=15)

        cust_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.c_name).grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="Salario básico mensual", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=2, padx=10)

        contact_entry = Entry(details, borderwidth=4, width=30,
                              textvariable=self.salario).grid(row=0, column=3, padx=8)
        

        bill_name = Label(details, text="No de pago", font=(
            "Arial Black", 14), bg="#3891c8", fg="white").grid(row=0, column=4, padx=10)

        bill_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.bill_no).grid(row=0, column=5, padx=8)
        # =======================================Calculo x Día=================================================================
        snacks = LabelFrame(self.root, text="Calculo x Día", font=(
            "Arial Black", 12), bg="#3891c8", fg="#ffffff", relief=GROOVE, bd=10)
        snacks.place(x=5, y=180, height=380, width=325)

        item1 = Label(snacks, text="Dias laborados", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item1_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.diasLaborales).grid(row=0, column=1, padx=10)

        item2 = Label(snacks, text="Valor día laboral", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item2_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.setsd).grid(row=1, column=1, padx=10)

        item3 = Label(snacks, text="Valor Hora laboral", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item3_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.sethl).grid(row=2, column=1, padx=10)

        item4 = Label(snacks, text="Valor del día", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)

        item5 = Label(snacks, text="Auxilio de transporte", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item5_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.setatd).grid(row=4, column=1, padx=10)

        item6 = Label(snacks, text="Valor a pagar", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        

        item7 = Label(snacks, text="Auxilio de transporte", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item7_entry = Entry(snacks, borderwidth=2, width=15,
                            textvariable=self.setatp).grid(row=6, column=1, padx=10)
        # ===================================Horas Extras y Recargos Columna 1=====================================================================================
        grocery = LabelFrame(self.root, text="Horas Extras y Recargos", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        grocery.place(x=340, y=180, height=380, width=325)

        item8 = Label(grocery, text="Hora Extra Diurna", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.canthed).grid(row=1, column=1, padx=10)
        
        item9 = Label(grocery, text="Hora con recargo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=2, column=0, pady=11)
        item10 = Label(grocery, text="festivo diurno", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.canthrfd).grid(row=3, column=1, padx=10)

        item11 = Label(grocery, text="Hora con recargo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=4, column=0, pady=11)
        item12 = Label(grocery, text="festivo nocturno", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.canthrfn).grid(row=5, column=1, padx=10)

        item13 = Label(grocery, text="Hora Diurna ", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item14 = Label(grocery, text="Festiva Extra", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=7, column=0, pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.canthdfe).grid(row=7, column=1, padx=10)
        # ========================================Horas Extras y Recargos Columna 2===============================================================================
        hygine = LabelFrame(self.root, text="Horas Extras y Recargos", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="#ffffff")
        hygine.place(x=677, y=180, height=380, width=325)

        item15 = Label(hygine, text="Hora con Recargo", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=0, column=0, pady=11)
        item16 = Label(hygine, text="Nocturno Ordinario", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=1, column=0, pady=11)
        item16_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.canthrn).grid(row=1, column=1, padx=10)

        item18 = Label(hygine, text="Hora Extra Nocturna", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=3, column=0, pady=11)
        item18_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.canthen).grid(row=3, column=1, padx=10)


        item20 = Label(hygine, text="Hora Nocturna", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=5, column=0, pady=11)
     

        item21 = Label(hygine, text="Festiva Extra", font=(
            "Arial Black", 11), bg="#3891c8", fg="#ffffff").grid(row=6, column=0, pady=11)
        item21_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.canthnfe).grid(row=6, column=1, padx=10)
        # =====================================================Área de Impresión==============================================================================
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#3891c8")
        billarea.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(billarea, text="Área de Impresión", font=(
            "Arial Black", 17), bd=7, relief=GROOVE, bg="#3891c8", fg="#ffffff").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # =================================================Resumen de pago de nómina=========================================================================================
        billing_menu = LabelFrame(self.root, text="Resumen de pago de nómina", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#3891c8", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_snacks = Label(billing_menu, text="Salario devengado", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=0)
        total_snacks_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.setsb).grid(row=0, column=1, padx=10, pady=7)

        total_grocery = Label(billing_menu, text="Aux. transporte", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=1, column=0)
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2,
                                    textvariable=self.setatp).grid(row=1, column=1, padx=10, pady=7)

        total_hygine = Label(billing_menu, text="Total Salario + Aux.", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=0)
        total_hygine_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.settsba).grid(row=2, column=1, padx=10, pady=7)

        tax_snacks = Label(billing_menu, text="Total HE y Recargos", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=0, column=2)
        tax_snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.setther).grid(
            row=0, column=3, padx=10, pady=7)

        tax_hygine = Label(billing_menu, text="Total a pagar", font=(
            "Arial Black", 11), bg="#3891c8", fg="white").grid(row=2, column=2)
        tax_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.settap).grid(
            row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#fafafa")
        button_frame.place(x=830, width=500, height=95)

        button_total = Button(button_frame, text="Calcular Pago", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="Resetear", font=("Arial Black", 15), pady=10,
                              bg="#3891c8", fg="#ffffff", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(button_frame, text="Imprimir", font=("Arial Black", 15), pady=10, bg="#3891c8",
                             fg="#ffffff", width=8, command=lambda: imprimir()).grid(row=0, column=2, padx=10, pady=6)
        intro(self)



def total(self):
    if (self.c_name.get == "" or self.salario.get() == ""):
        messagebox.showerror("Error", "Complete los datos del Empleado!!")
    if (self.salario.get() < 1000000):
        messagebox.showerror("Error", "El salario debe ser mayor o igual a un salario minimo que es 1.000.000")
    if (self.diasLaborales.get() < 1 or self.diasLaborales.get() > 30):
        messagebox.showerror("Error", "Por favor ingresar dias laborales de 1 a 30 dias!!")
    if (self.salario.get() > 2000000 ):
        messagebox.showinfo("Salario superior a 2 SMMLV", "Tenga en cuenta que: este empleado no tiene derecho a auxilio de transporte!!")
    if (self.salario.get() <= 2000000 ):
        self.atm = 117172
    else:
        self.atm = 0

    self.dl = self.diasLaborales.get()
    self.sd = self.salario.get()/30
    self.hl = self.sd/8
    self.sb = round(self.sd*self.dl)
    self.atd = self.atm/30
    self.atp = round(self.atd*self.dl)
    self.tsba = round(self.sb+self.atp)

    self.phrn = self.hl*(0.35)
    self.phed = self.hl*(1.25)
    self.phen = self.hl*(1.75)
    self.phrfd = self.hl*(1.75)
    self.phrfn = self.hl*(2.1)
    self.phdfe = self.hl*(2)
    self.phnfe = self.hl*(2.5)

    self.chrn = self.canthrn.get()
    self.ched = self.canthed.get()
    self.chen = self.canthen.get()
    self.chrfd = self.canthrfd.get()
    self.chrfn = self.canthrfn.get()
    self.chdfe = self.canthdfe.get()
    self.chnfe = self.canthnfe.get()

    self.vhrn = self.phrn*self.chrn
    self.vhed = self.phed*self.ched
    self.vhen = self.phen*self.chen
    self.vhrfd = self.phrfd*self.chrfd
    self.vhrfn = self.phrfn*self.chrfn
    self.vhdfe = self.phdfe*self.chdfe
    self.vhnfe = self.phnfe*self.chnfe
    
    self.setsd.set(str(round(self.sd)))
    self.setsb.set(str(self.sb)+" COP")
    self.sethl.set(str(round(self.hl)))
    self.setatd.set(str(round(self.atd)))
    self.setatp.set(str(self.atp)+" COP")
    self.settsba.set(str(self.tsba) + " COP")

    self.ther = self.vhrn + self.vhed + self.vhen + self.vhrfd + self.vhrfn + self.vhdfe + self.vhnfe
    self.setther.set(str(round(self.ther))+" COP")
    self.tap = self.tsba + self.ther
    self.settap.set(str(round(self.tap))+" COP")

    PDF.datosImprimir(self)
    
    intro(self)


    


    

def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(
        END, "\tBienvenid@ al \n\tSistema pago de Nómina \n\tNit 8888888888-1")
    self.txtarea.insert(END, f"\n\nNúmero de Pago : {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nNombre Empleado : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nSalario Mensual : {self.salario.get()}")
    self.txtarea.insert(END, f"\nDias Laborados : {self.diasLaborales.get()}")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nValor día Laboral : \t{round(self.sd)}")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nValor Hora Laboral : \t{round(self.hl)}")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nSalario devengado : \t{self.sb}")
    
    self.txtarea.insert(END, "\n====================================\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nAuxilio de transporte \nmensual : \t{self.atm}")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nAuxilio de \ntransporte x dia : \t{round(self.atd)}")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nValor a pagar \nAuxilio de transporte : \t{self.atp}")
    self.txtarea.insert(END, "\n====================================\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nTotal salario básico + \nAuxilio de transporte : \t{self.tsba}")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, f"\nHoras Extras y Recargos Nocturnos\n\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nHoras con recargo nocturno ordinario,\n porcentaje: 0.35\n Cantidad :\t{self.chrn} \n Total : \t{round(self.vhrn)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nHoras Extras Diurnas,\n porcentaje: 1.25\n Cantidad :\t{self.ched} \n Total : \t{round(self.vhed)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nHoras Extras Nocturna,\n porcentaje: 1.75\n Cantidad :\t{self.chen} \n Total : \t{round(self.vhen)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nHoras con recargo Festivos Diurno,\n porcentaje: 1.75\n Cantidad :\t{self.chrfd} \n Total : \t{round(self.vhrfd)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nHoras con recargo Festivos Nocturno,\n porcentaje: 2.1\n Cantidad :\t{self.chrfn} \n Total : \t{round(self.vhrfn)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nHoras Diurnas Festivas Extras,\n porcentaje: 2.00\n Cantidad :\t{self.chdfe} \n Total : \t{round(self.vhdfe)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nHoras Nocturnas Festivas Extras,\n porcentaje: 2.5\n Cantidad :\t{self.chnfe} \n Total : \t{round(self.vhnfe)}\n")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, f"\nTotal a pagar al empleado\n\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nTotal devengado + Auxilio\n de Transporte : \t{round(self.tsba)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\nTotal Horas Extras \n y Recargos : \t{round(self.ther)}\n")
    if self.diasLaborales.get() != 0:
        self.txtarea.insert(
            END, f"\n\nTotal a Pagar : \t{round(self.tap)}\n") 

def clear(self):
    self.txtarea.delete(1.0, END)
    self.diasLaborales.set(0)
    
    self.canthrn.set(0)
    self.canthed.set(0)
    self.canthen.set(0)
    self.canthrfd.set(0)
    self.canthrfn.set(0)
    self.canthdfe.set(0)
    self.canthnfe.set(0)
    x = random.randint(1000, 9999)  
    self.bill_no.set(str(x))
    self.c_name.set(0)
    self.salario.set(0)
    self.dias.set(0)
    self.salarioDia.set(0)
    self.setsd.set(0)
    self.setsb.set(0)
    self.sethl.set(0)
    self.setatd.set(0)
    self.setatp.set(0)
    self.settsba.set(0)
    self.setther.set(0)
    self.settap.set(0)


title = 'Sistema pago de Nómina'



class PDF(FPDF):
    def datosImprimir(self):
        global nomEmpleado
        nomEmpleado = str(self.c_name.get())

        global numCompPago
        numCompPago = str(self.bill_no.get())

        global salMensual
        salMensual = str(self.salario.get())
        txtsMes= "{:_}"
        global txtsalMensual
        txtsalMensual = txtsMes.format(int(salMensual)).replace("_",".")

        global diasLabor
        diasLabor = str(self.diasLaborales.get())

        global valorDia
        valorDia = str(round(self.sd))
        txtvDia= "{:_}"
        global txtvalorDia
        txtvalorDia = txtvDia.format(int(valorDia)).replace("_",".")

        global valorHora
        valorHora = str(round(self.hl))
        txtvHora= "{:_}"
        global txtvalorHora
        txtvalorHora = txtvHora.format(int(valorHora)).replace("_",".")

        global salDevengado
        salDevengado = str(self.sb)
        txtsDev= "{:_}"
        global txtsalDevengado
        txtsalDevengado = txtsDev.format(int(salDevengado)).replace("_",".")

        global auxTransMensual
        auxTransMensual = str(self.atm)
        txtaTMes= "{:_}"
        global txtauxTransMensual
        txtauxTransMensual = txtaTMes.format(int(auxTransMensual)).replace("_",".")

        global auxTransDia
        auxTransDia = str(round(self.atd))
        txtaTDiar= "{:_}"
        global txtauxTransDia
        txtauxTransDia = txtaTDiar.format(int(auxTransDia)).replace("_",".")

        global auxTransPagar
        auxTransPagar = str(self.atp)
        txtaTPagar= "{:_}"
        global txtauxTransPagar
        txtauxTransPagar = txtaTPagar.format(int(auxTransPagar)).replace("_",".")

        global cantHorasRNO
        cantHorasRNO = str(self.chrn)

        global valHorasRNO
        valHorasRNO = str(round(self.vhrn))
        txtvHorasRNO= "{:_}"
        global txtvalHorasRNO
        txtvalHorasRNO = txtvHorasRNO.format(int(valHorasRNO)).replace("_",".")

        global cantHorasED
        cantHorasED = str(self.ched)

        global valHorasED
        valHorasED = str(round(self.vhed))
        txtvHorasED= "{:_}"
        global txtvalHorasED
        txtvalHorasED = txtvHorasED.format(int(valHorasED)).replace("_",".")

        global cantHorasEN
        cantHorasEN = str(self.chen)

        global valHorasEN
        valHorasEN = str(round(self.vhen))
        txtvHorasEN= "{:_}"
        global txtvalHorasEN
        txtvalHorasEN = txtvHorasEN.format(int(valHorasEN)).replace("_",".")

        global cantHorasRFD
        cantHorasRFD = str(self.chrfd)

        global valHorasRFD
        valHorasRFD = str(round(self.vhrfd))
        txtvHorasRFD= "{:_}"
        global txtvalHorasRFD
        txtvalHorasRFD = txtvHorasRFD.format(int(valHorasRFD)).replace("_",".")

        global cantHorasRFN
        cantHorasRFN = str(self.chrfn)

        global valHorasRFN
        valHorasRFN = str(round(self.vhrfn))
        txtvHorasRFN= "{:_}"
        global txtvalHorasRFN
        txtvalHorasRFN = txtvHorasRFN.format(int(valHorasRFN)).replace("_",".")

        global cantHorasDFE
        cantHorasDFE = str(self.chdfe)

        global valHorasDFE
        valHorasDFE = str(round(self.vhdfe))
        txtvHorasDFE = "{:_}"
        global txtvalHorasDFE
        txtvalHorasDFE = txtvHorasDFE.format(int(valHorasDFE)).replace("_",".")
        
        global cantHorasNFE
        cantHorasNFE = str(self.chnfe)

        global valHorasNFE
        valHorasNFE = str(round(self.vhnfe))
        txtvHorasNFE = "{:_}"
        global txtvalHorasNFE
        txtvalHorasNFE = txtvHorasNFE.format(int(valHorasNFE)).replace("_",".")

        global totalSalAux
        totalSalAux = str(round(self.tsba))
        txttSalAux = "{:_}"
        global txttotalSalAux
        txttotalSalAux = txttSalAux.format(int(totalSalAux)).replace("_",".")

        global totalHEyR
        totalHEyR = str(round(self.ther))
        txttHEyR = "{:_}"
        global txttotalHEyR
        txttotalHEyR = txttHEyR.format(int(totalHEyR)).replace("_",".")

        global totalPagar
        totalPagar = str(round(self.tap))
        txttap = "{:_}"
        global txttotalPagar
        txttotalPagar = txttap.format(int(totalPagar)).replace("_",".")
                



    def header(self):
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Calcular ancho del texto (title) y establecer posición
        w = self.get_string_width(title) + 6
        self.set_x((210 - w) / 2)
        # Colores del marco, fondo y texto
        self.set_fill_color(255, 255, 255)
        self.set_text_color(220, 50, 50)
        # Grosor del marco (1 mm)
        self.set_line_width(1)
        # Titulo
        self.cell(w, 9, title, 1, 1, 'C', 1)
        # Salto de línea
        self.ln(10)

        

    def footer(self):
        # Posición a 1.5 cm desde abajo
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Color de texto en gris
        self.set_text_color(128)
        # Numero de pagina
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_title(self, num, label):
        # Arial 12
        self.set_font('Arial', '', 12)
        # Color de fondo
        self.set_fill_color(200, 220, 255)
        # Titulo
        self.cell(0, 6, '%d : %s' % (num,label), 0, 1, 'L', 1)
        # Salto de línea
        self.ln()
    
    
    def chapter_body(self, name):
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Número, comprobante de pago : '  + numCompPago, 0, 1, 'L', 1)     
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Nombre del empleado : '  + nomEmpleado, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Salario mensual del empleado : '  + txtsalMensual, 0, 1, 'L', 1)

        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6,'2 : Salario acorde a los días laborados durante el mes', 0, 1, 'L', 1)
        self.ln()

        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Días laborados en el mes : '  + diasLabor, 0, 1, 'L', 1)     
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Valor día laboral : '  + txtvalorDia, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Valor hora laboral : '  + txtvalorHora, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Salario acorde a los días laborados : '  + txtsalDevengado, 0, 1, 'L', 1)

        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6,'3 : Auxilio de transporte acorde a los días laborados durante el mes', 0, 1, 'L', 1)
        self.ln()

        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Auxilio de transporte mensual : '  + txtauxTransMensual, 0, 1, 'L', 1)     
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Valor auxilio de transporte por día : '  + txtauxTransDia, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Valor a pagar auxilio de transporte acorde a los días laborados : '  + txtauxTransPagar, 0, 1, 'L', 1)

        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6,'4 : Horas extras y recargos', 0, 1, 'L', 1)
        self.ln()

        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Horas con recargo nocturno ordinario : ', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      porcentaje: 0.35'  , 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Cantidad: '  + cantHorasRNO, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Total: '  + txtvalHorasRNO, 0, 1, 'L', 1)
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Horas Extras Diurnas : ', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      porcentaje: 1.25', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Cantidad: '  + cantHorasED, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Total: '  + txtvalHorasED, 0, 1, 'L', 1)
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Horas Extras Nocturna : ', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      porcentaje: 1.75', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Cantidad: '  + cantHorasEN, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Total: '  + txtvalHorasEN, 0, 1, 'L', 1)
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Horas con recargo Festivos Diurno : ', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      porcentaje: 1.75', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Cantidad: '  + cantHorasRFD, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Total: '  + txtvalHorasRFD, 0, 1, 'L', 1)
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Horas con recargo Festivos Nocturno : ', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      porcentaje: 2.1', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Cantidad: '  + cantHorasRFN, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Total: '  + txtvalHorasRFN, 0, 1, 'L', 1)
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Horas Diurnas Festivas Extras : ', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      porcentaje: 2.00', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Cantidad: '  + cantHorasDFE, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Total: '  + txtvalHorasDFE, 0, 1, 'L', 1)
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(240, 240, 240)
        self.cell(0, 6,'   Horas Nocturnas Festivas Extras : ', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      porcentaje: 2.5', 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Cantidad: '  + cantHorasNFE, 0, 1, 'L', 1)
        self.set_font('Times', '', 14)
        self.set_fill_color(248, 248, 248)
        self.cell(0, 6,'      Total: '  + txtvalHorasNFE, 0, 1, 'L', 1)
        self.ln()

        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 6,'5 : Total a pagar al Empleado : ' + nomEmpleado, 0, 1, 'L', 1)
        self.ln()

        self.set_font('Times', '', 14)
        self.set_fill_color(245, 245, 248)
        self.cell(0, 6,'      Total salario devengado + auxilio de transporte: '  + txttotalSalAux, 0, 1, 'L', 1)
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(245, 245, 245)
        self.cell(0, 6,'      Total Horas extras y recargos: '  + txttotalHEyR, 0, 1, 'L', 1)
        self.ln()
        self.ln()
        self.set_font('Times', '', 14)
        self.set_fill_color(195, 225, 194)
        self.cell(0, 6,'      Total a pagar: '  + txttotalPagar, 0, 1, 'L', 1)



    def print_chapter(self, num, title, name):
        self.add_page()
        self.chapter_title(num, title)
        self.chapter_body(name)

# Instantiation of inherited class
def imprimir():
    pdf = PDF()
    pdf.set_title(title)
    pdf.set_author('Jules Verne')
    pdf.print_chapter(1, 'Datos del empleado', '20k_c1.txt')
    pdf.output('Sistema_Pago_de_Nomina_N_'+numCompPago+'.pdf', 'F')


root = Tk()
obj = Bill_App(root)
root.mainloop()
