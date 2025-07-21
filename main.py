import tkinter as tk
from tkinter import messagebox
try:
    import customtkinter as ctk
except ImportError:
    messagebox.showerror("Error de Librería", "La librería 'customtkinter' no está instalada.\nPor favor, instálela usando: pip install install customtkinter")
    exit()

from calculos import CalculadoraFinanciera # Import the calculator logic

class FinancialCalculatorCustomGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora Financiera Avanzada")
        self.master.geometry("1000x700")
        self.master.resizable(True, True)

        # Set default appearance mode (can be "System", "Dark", "Light")
        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("green") # Changed to green theme

        self.calculator = CalculadoraFinanciera()

        # Main frame divided into sidebar and content
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        # Sidebar frame
        self.sidebar_frame = ctk.CTkFrame(self.master, width=200, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(8, weight=1)

        # Sidebar title
        ctk.CTkLabel(self.sidebar_frame, text="Menú", font=ctk.CTkFont(size=20, weight="bold")).grid(row=0, column=0, padx=20, pady=20)

        # Sidebar buttons
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Interés Simple/Compuesto", command=lambda: self.select_frame_by_name("interest"))
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Conversión de Tasas", command=lambda: self.select_frame_by_name("rate_conversion"))
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="Préstamos y Amortización", command=lambda: self.select_frame_by_name("loan_amortization"))
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_4 = ctk.CTkButton(self.sidebar_frame, text="Valor Presente/Futuro (Monto Único)", command=lambda: self.select_frame_by_name("pv_fv_single"))
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_5 = ctk.CTkButton(self.sidebar_frame, text="Anualidades y Pagos (PMT, NPER, PV, FV, RATE)", command=lambda: self.select_frame_by_name("annuities"))
        self.sidebar_button_5.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        self.sidebar_button_6 = ctk.CTkButton(self.sidebar_frame, text="Depreciación Lineal", command=lambda: self.select_frame_by_name("depreciation"))
        self.sidebar_button_6.grid(row=6, column=0, padx=20, pady=10, sticky="ew")

        # Theme Switch
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Tema:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0), sticky="sw")
        self.appearance_mode_switch = ctk.CTkSwitch(self.sidebar_frame, text="Oscuro/Claro", command=self.change_appearance_mode_event)
        self.appearance_mode_switch.grid(row=8, column=0, padx=20, pady=(0, 20), sticky="nw")
        # Set initial state of switch based on current mode
        if ctk.get_appearance_mode() == "Dark":
            self.appearance_mode_switch.select()
        else:
            self.appearance_mode_switch.deselect()

        # Create content frames (hidden initially)
        self.interest_frame = ctk.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.rate_conversion_frame = ctk.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.loan_amortization_frame = ctk.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.pv_fv_single_frame = ctk.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.annuities_frame = ctk.CTkFrame(self.master, corner_radius=0, fg_color="transparent")
        self.depreciation_frame = ctk.CTkFrame(self.master, corner_radius=0, fg_color="transparent")

        # Initialize content for each frame
        self.create_interest_content(self.interest_frame)
        self.create_rate_conversion_content(self.rate_conversion_frame)
        self.create_loan_amort_content(self.loan_amortization_frame)
        self.create_pv_fv_single_content(self.pv_fv_single_frame)
        self.create_annuities_content(self.annuities_frame)
        self.create_depreciation_content(self.depreciation_frame)

        # Select initial frame
        self.select_frame_by_name("interest")

    def change_appearance_mode_event(self):
        if self.appearance_mode_switch.get() == 1: # Switch is ON -> Dark mode
            ctk.set_appearance_mode("Dark")
        else: # Switch is OFF -> Light mode
            ctk.set_appearance_mode("Light")

    def select_frame_by_name(self, name):
        # Set button color for selected button
        self.sidebar_button_1.configure(fg_color=("gray75", "gray25") if name == "interest" else "transparent")
        self.sidebar_button_2.configure(fg_color=("gray75", "gray25") if name == "rate_conversion" else "transparent")
        self.sidebar_button_3.configure(fg_color=("gray75", "gray25") if name == "loan_amortization" else "transparent")
        self.sidebar_button_4.configure(fg_color=("gray75", "gray25") if name == "pv_fv_single" else "transparent")
        self.sidebar_button_5.configure(fg_color=("gray75", "gray25") if name == "annuities" else "transparent")
        self.sidebar_button_6.configure(fg_color=("gray75", "gray25") if name == "depreciation" else "transparent")

        # Show selected frame, hide others
        if name == "interest":
            self.interest_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        else:
            self.interest_frame.grid_forget()
        if name == "rate_conversion":
            self.rate_conversion_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        else:
            self.rate_conversion_frame.grid_forget()
        if name == "loan_amortization":
            self.loan_amortization_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        else:
            self.loan_amortization_frame.grid_forget()
        if name == "pv_fv_single":
            self.pv_fv_single_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        else:
            self.pv_fv_single_frame.grid_forget()
        if name == "annuities":
            self.annuities_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        else:
            self.annuities_frame.grid_forget()
        if name == "depreciation":
            self.depreciation_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
        else:
            self.depreciation_frame.grid_forget()


    def create_interest_content(self, frame):
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1) # Allow result frame to expand

        ctk.CTkLabel(frame, text="Calculadora de Interés Simple y Compuesto", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(0, 20), sticky="ew")

        # Input Frame
        input_frame = ctk.CTkFrame(frame, corner_radius=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_frame, text="Capital Inicial:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.capital_entry = ctk.CTkEntry(input_frame)
        self.capital_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Tasa Anual (%):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.rate_entry = ctk.CTkEntry(input_frame)
        self.rate_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Tiempo (Años):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.time_entry = ctk.CTkEntry(input_frame)
        self.time_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Frecuencia (Compuesto, ej. 12 mensual):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.frequency_entry = ctk.CTkEntry(input_frame)
        self.frequency_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.frequency_entry.insert(0, "1")

        # Buttons Frame
        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        button_frame.grid_columnconfigure((0,1,2), weight=1)

        ctk.CTkButton(button_frame, text="Calcular Interés Simple", command=self.calculate_simple_interest).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Calcular Interés Compuesto", command=self.calculate_compound_interest).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Graficar Comparación", command=self.plot_interest_comparison).grid(row=0, column=2, padx=5, pady=5, sticky="ew")

        # Results display
        results_frame = ctk.CTkFrame(frame, corner_radius=10)
        results_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(results_frame, text="Resultados:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        self.result_text = ctk.CTkTextbox(results_frame, height=100, state="disabled", wrap="word")
        self.result_text.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")


    def create_rate_conversion_content(self, frame):
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(frame, text="Conversión de Tasas", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(0, 20), sticky="ew")

        # Input Frame
        input_frame = ctk.CTkFrame(frame, corner_radius=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_frame, text="Tasa a Convertir (%):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.rc_rate_entry = ctk.CTkEntry(input_frame)
        self.rc_rate_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Periodicidad Origen:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.rc_origin_var = ctk.StringVar()
        self.rc_origin_combo = ctk.CTkComboBox(input_frame, variable=self.rc_origin_var,
                                               values=["anual", "semestral", "trimestral", "mensual", "diaria"])
        self.rc_origin_combo.grid(row=1, column=1, padx=10, pady=5, sticky="ew")
        self.rc_origin_combo.set("anual")

        ctk.CTkLabel(input_frame, text="Periodicidad Destino:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.rc_destination_var = ctk.StringVar()
        self.rc_destination_combo = ctk.CTkComboBox(input_frame, variable=self.rc_destination_var,
                                                    values=["anual", "semestral", "trimestral", "mensual", "diaria"])
        self.rc_destination_combo.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.rc_destination_combo.set("mensual")

        ctk.CTkButton(input_frame, text="Convertir Tasa", command=self.convert_rate).grid(row=3, column=0, columnspan=2, pady=10)

        # Results display
        results_frame = ctk.CTkFrame(frame, corner_radius=10)
        results_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(results_frame, text="Resultados:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        self.rc_result_text = ctk.CTkTextbox(results_frame, height=70, state="disabled", wrap="word")
        self.rc_result_text.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")


    def create_loan_amort_content(self, frame):
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(frame, text="Préstamos y Amortización", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(0, 20), sticky="ew")

        # Input Frame
        input_frame = ctk.CTkFrame(frame, corner_radius=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_frame, text="Monto del Préstamo:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.loan_amount_entry = ctk.CTkEntry(input_frame)
        self.loan_amount_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Tasa Mensual (%):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.loan_rate_entry = ctk.CTkEntry(input_frame)
        self.loan_rate_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Número de Cuotas (Meses):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.loan_months_entry = ctk.CTkEntry(input_frame)
        self.loan_months_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Buttons Frame
        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        button_frame.grid_columnconfigure((0,1), weight=1)

        ctk.CTkButton(button_frame, text="Calcular Cuota Amortización", command=self.calculate_amortization_payment).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Graficar Amortización", command=self.plot_amortization).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Results display
        results_frame = ctk.CTkFrame(frame, corner_radius=10)
        results_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(results_frame, text="Resultados:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        self.loan_result_text = ctk.CTkTextbox(results_frame, height=70, state="disabled", wrap="word")
        self.loan_result_text.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")

    def create_pv_fv_single_content(self, frame):
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(frame, text="Valor Presente/Futuro (Monto Único)", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(0, 20), sticky="ew")

        # Input Frame
        input_frame = ctk.CTkFrame(frame, corner_radius=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_frame, text="Valor Presente/Futuro:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.pv_fv_amount_entry = ctk.CTkEntry(input_frame)
        self.pv_fv_amount_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Tasa Anual (%):").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.pv_fv_rate_entry = ctk.CTkEntry(input_frame)
        self.pv_fv_rate_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Tiempo (Años):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.pv_fv_time_entry = ctk.CTkEntry(input_frame)
        self.pv_fv_time_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Frecuencia de Capitalización (ej. 12 mensual):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.pv_fv_frequency_entry = ctk.CTkEntry(input_frame)
        self.pv_fv_frequency_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.pv_fv_frequency_entry.insert(0, "1")

        # Buttons Frame
        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        button_frame.grid_columnconfigure((0,1), weight=1)

        ctk.CTkButton(button_frame, text="Calcular Valor Presente", command=self.calculate_pv_single).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Calcular Valor Futuro", command=self.calculate_fv_single).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        
        # Results display
        results_frame = ctk.CTkFrame(frame, corner_radius=10)
        results_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(results_frame, text="Resultados:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        self.pv_fv_single_result_text = ctk.CTkTextbox(results_frame, height=70, state="disabled", wrap="word")
        self.pv_fv_single_result_text.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")


    def create_annuities_content(self, frame):
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(frame, text="Anualidades y Cálculos Financieros (PMT, NPER, PV, FV, RATE)", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(0, 20), sticky="ew")

        # Input Frame
        input_frame = ctk.CTkFrame(frame, corner_radius=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_frame, text="Tasa Periódica (ej. 0.005 para 0.5% mensual):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.ann_rate_entry = ctk.CTkEntry(input_frame)
        self.ann_rate_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Número de Períodos:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.ann_nper_entry = ctk.CTkEntry(input_frame)
        self.ann_nper_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Pago Periódico (PMT):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.ann_pmt_entry = ctk.CTkEntry(input_frame)
        self.ann_pmt_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")
        self.ann_pmt_entry.insert(0, "0")

        ctk.CTkLabel(input_frame, text="Valor Presente (PV):").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.ann_pv_entry = ctk.CTkEntry(input_frame)
        self.ann_pv_entry.grid(row=3, column=1, padx=10, pady=5, sticky="ew")
        self.ann_pv_entry.insert(0, "0")

        ctk.CTkLabel(input_frame, text="Valor Futuro (FV):").grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.ann_fv_entry = ctk.CTkEntry(input_frame)
        self.ann_fv_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")
        self.ann_fv_entry.insert(0, "0")

        ctk.CTkLabel(input_frame, text="Tipo de Pago (0=Fin, 1=Inicio):").grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.ann_type_entry = ctk.CTkEntry(input_frame)
        self.ann_type_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")
        self.ann_type_entry.insert(0, "0")

        ctk.CTkLabel(input_frame, text="Estimación de Tasa (para RATE, ej. 0.1):").grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.ann_rate_estimate_entry = ctk.CTkEntry(input_frame)
        self.ann_rate_estimate_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")
        self.ann_rate_estimate_entry.insert(0, "0.1")

        # Buttons Frame
        button_frame = ctk.CTkFrame(frame, fg_color="transparent")
        button_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
        button_frame.grid_columnconfigure((0,1,2,3,4), weight=1)

        ctk.CTkButton(button_frame, text="Calcular PMT", command=self.calculate_pmt).grid(row=0, column=0, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Calcular NPER", command=self.calculate_nper).grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Calcular PV", command=self.calculate_pv_annuity).grid(row=0, column=2, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Calcular FV", command=self.calculate_fv_annuity).grid(row=0, column=3, padx=5, pady=5, sticky="ew")
        ctk.CTkButton(button_frame, text="Calcular RATE", command=self.calculate_rate).grid(row=0, column=4, padx=5, pady=5, sticky="ew")

        # Results display
        results_frame = ctk.CTkFrame(frame, corner_radius=10)
        results_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(results_frame, text="Resultados:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        self.ann_result_text = ctk.CTkTextbox(results_frame, height=100, state="disabled", wrap="word")
        self.ann_result_text.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")

    def create_depreciation_content(self, frame):
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)

        ctk.CTkLabel(frame, text="Depreciación Lineal", font=ctk.CTkFont(size=18, weight="bold")).grid(row=0, column=0, pady=(0, 20), sticky="ew")

        # Input Frame
        input_frame = ctk.CTkFrame(frame, corner_radius=10)
        input_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        input_frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(input_frame, text="Valor Inicial del Activo:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.dep_initial_value_entry = ctk.CTkEntry(input_frame)
        self.dep_initial_value_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Valor Residual:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.dep_residual_value_entry = ctk.CTkEntry(input_frame)
        self.dep_residual_value_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkLabel(input_frame, text="Vida Útil (Años):").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.dep_useful_life_entry = ctk.CTkEntry(input_frame)
        self.dep_useful_life_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        ctk.CTkButton(input_frame, text="Calcular Depreciación Lineal", command=self.calculate_depreciation).grid(row=3, column=0, columnspan=2, pady=10)

        # Results display
        results_frame = ctk.CTkFrame(frame, corner_radius=10)
        results_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        results_frame.grid_columnconfigure(0, weight=1)
        results_frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(results_frame, text="Resultados:", font=ctk.CTkFont(weight="bold")).grid(row=0, column=0, padx=10, pady=(10,5), sticky="w")
        self.dep_result_text = ctk.CTkTextbox(results_frame, height=70, state="disabled", wrap="word")
        self.dep_result_text.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")


    def update_result_text(self, text_widget, message):
        text_widget.configure(state="normal")
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", message)
        text_widget.configure(state="disabled")

    def get_float_input(self, entry_widget, field_name, result_widget):
        try:
            return float(entry_widget.get())
        except ValueError:
            self.update_result_text(result_widget, f"Error: '{field_name}' debe ser un número válido.")
            return None

    def get_int_input(self, entry_widget, field_name, result_widget):
        try:
            return int(entry_widget.get())
        except ValueError:
            self.update_result_text(result_widget, f"Error: '{field_name}' debe ser un número entero válido.")
            return None

    # --- Interest & PV/FV Single Amount ---
    def calculate_simple_interest(self):
        capital = self.get_float_input(self.capital_entry, "Capital Inicial", self.result_text)
        tasa = self.get_float_input(self.rate_entry, "Tasa Anual", self.result_text)
        tiempo = self.get_float_input(self.time_entry, "Tiempo", self.result_text)

        if all(v is not None for v in [capital, tasa, tiempo]):
            interes, monto_final = self.calculator.interesSimple(capital, tasa, tiempo)
            if interes is not None:
                message = f"Interés Simple: ${interes:,.2f}\nMonto Final: ${monto_final:,.2f}"
            else:
                message = "Error en el cálculo del interés simple."
            self.update_result_text(self.result_text, message)

    def calculate_compound_interest(self):
        capital = self.get_float_input(self.capital_entry, "Capital Inicial", self.result_text)
        tasa = self.get_float_input(self.rate_entry, "Tasa Anual", self.result_text)
        tiempo = self.get_float_input(self.time_entry, "Tiempo", self.result_text)
        frecuencia = self.get_int_input(self.frequency_entry, "Frecuencia", self.result_text)

        if all(v is not None for v in [capital, tasa, tiempo, frecuencia]):
            interes, monto_final = self.calculator.interesCompuesto(capital, tasa, tiempo, frecuencia)
            if interes is not None:
                message = f"Interés Compuesto: ${interes:,.2f}\nMonto Final: ${monto_final:,.2f}"
            else:
                message = "Error en el cálculo del interés compuesto."
            self.update_result_text(self.result_text, message)

    def plot_interest_comparison(self):
        try:
            capital = float(self.capital_entry.get())
            tasa = float(self.rate_entry.get())
            tiempo = int(self.time_entry.get())
            frecuencia = int(self.frequency_entry.get())
            
            messagebox.showinfo("Generando Gráfico", "Se está generando el gráfico de comparación de interés. Esto puede tardar unos segundos y aparecerá en una ventana separada.")
            self.calculator.graficarInteresSimpleVsCompuesto(capital, tasa, tiempo, frecuencia)
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese valores numéricos válidos para Capital, Tasa, Tiempo y Frecuencia.")
        except Exception as e:
            messagebox.showerror("Error al Graficar", f"Ocurrió un error al intentar graficar: {e}")

    # --- Rate Conversion ---
    def convert_rate(self):
        rate = self.get_float_input(self.rc_rate_entry, "Tasa a Convertir", self.rc_result_text)
        origin = self.rc_origin_var.get()
        destination = self.rc_destination_var.get()

        if rate is not None:
            converted_rate = self.calculator.conversionTasas(rate, origin, destination)
            if converted_rate is not None:
                message = f"Tasa convertida de {origin} a {destination}: {converted_rate:,.4f}%"
            else:
                message = "Error en la conversión de tasas. Verifique las periodicidades."
            self.update_result_text(self.rc_result_text, message)

    # --- Loan & Amortization ---
    def calculate_amortization_payment(self):
        capital = self.get_float_input(self.loan_amount_entry, "Monto del Préstamo", self.loan_result_text)
        tasa_mensual = self.get_float_input(self.loan_rate_entry, "Tasa Mensual", self.loan_result_text)
        meses = self.get_int_input(self.loan_months_entry, "Número de Cuotas", self.loan_result_text)

        if all(v is not None for v in [capital, tasa_mensual, meses]):
            cuota = self.calculator.pagoAmortizacion(capital, tasa_mensual, meses)
            if cuota is not None:
                message = f"Cuota Mensual Fija: ${cuota:,.2f}"
            else:
                message = "Error en el cálculo de la cuota de amortización."
            self.update_result_text(self.loan_result_text, message)

    def plot_amortization(self):
        try:
            capital = float(self.loan_amount_entry.get())
            tasa_mensual = float(self.loan_rate_entry.get())
            meses = int(self.loan_months_entry.get())

            messagebox.showinfo("Generando Gráfico", "Se está generando el gráfico de amortización. Esto puede tardar unos segundos y aparecerá en una ventana separada.")
            self.calculator.graficarAmortizacion(capital, tasa_mensual, meses)
        except ValueError:
            messagebox.showerror("Error de Entrada", "Por favor, ingrese valores numéricos válidos para Monto del Préstamo, Tasa Mensual y Número de Cuotas.")
        except Exception as e:
            messagebox.showerror("Error al Graficar", f"Ocurrió un error al intentar graficar: {e}")

    # --- PV/FV Single Amount Tab Functions ---
    def calculate_pv_single(self):
        futuro = self.get_float_input(self.pv_fv_amount_entry, "Valor Futuro", self.pv_fv_single_result_text)
        tasa = self.get_float_input(self.pv_fv_rate_entry, "Tasa Anual", self.pv_fv_single_result_text)
        tiempo = self.get_float_input(self.pv_fv_time_entry, "Tiempo", self.pv_fv_single_result_text)
        frecuencia = self.get_int_input(self.pv_fv_frequency_entry, "Frecuencia", self.pv_fv_single_result_text)

        if all(v is not None for v in [futuro, tasa, tiempo, frecuencia]):
            pv = self.calculator.valorPresenteMontoUnico(futuro, tasa, tiempo, frecuencia)
            if pv is not None:
                message = f"Valor Presente: ${pv:,.2f}"
            else:
                message = "Error en el cálculo del Valor Presente."
            self.update_result_text(self.pv_fv_single_result_text, message)

    def calculate_fv_single(self):
        presente = self.get_float_input(self.pv_fv_amount_entry, "Valor Presente", self.pv_fv_single_result_text)
        tasa = self.get_float_input(self.pv_fv_rate_entry, "Tasa Anual", self.pv_fv_single_result_text)
        tiempo = self.get_float_input(self.pv_fv_time_entry, "Tiempo", self.pv_fv_single_result_text)
        frecuencia = self.get_int_input(self.pv_fv_frequency_entry, "Frecuencia", self.pv_fv_single_result_text)

        if all(v is not None for v in [presente, tasa, tiempo, frecuencia]):
            fv = self.calculator.valorFuturoMontoUnico(presente, tasa, tiempo, frecuencia)
            if fv is not None:
                message = f"Valor Futuro: ${fv:,.2f}"
            else:
                message = "Error en el cálculo del Valor Futuro."
            self.update_result_text(self.pv_fv_single_result_text, message)

    # --- Annuities Tab Functions ---
    def calculate_pmt(self):
        rate_per = self.get_float_input(self.ann_rate_entry, "Tasa Periódica", self.ann_result_text)
        nper = self.get_float_input(self.ann_nper_entry, "Número de Períodos", self.ann_result_text)
        pv = self.get_float_input(self.ann_pv_entry, "Valor Presente (PV)", self.ann_result_text)
        fv = self.get_float_input(self.ann_fv_entry, "Valor Futuro (FV)", self.ann_result_text)
        payment_type = self.get_int_input(self.ann_type_entry, "Tipo de Pago", self.ann_result_text)

        if all(v is not None for v in [rate_per, nper, pv, fv, payment_type]):
            pmt = self.calculator.calcularPmt(rate_per, nper, pv, fv, payment_type)
            if pmt is not None:
                message = f"Pago Periódico (PMT): ${pmt:,.2f}"
            else:
                message = "Error en el cálculo de PMT."
            self.update_result_text(self.ann_result_text, message)

    def calculate_nper(self):
        rate_per = self.get_float_input(self.ann_rate_entry, "Tasa Periódica", self.ann_result_text)
        pmt = self.get_float_input(self.ann_pmt_entry, "Pago Periódico (PMT)", self.ann_result_text)
        pv = self.get_float_input(self.ann_pv_entry, "Valor Presente (PV)", self.ann_result_text)
        fv = self.get_float_input(self.ann_fv_entry, "Valor Futuro (FV)", self.ann_result_text)
        payment_type = self.get_int_input(self.ann_type_entry, "Tipo de Pago", self.ann_result_text)

        if all(v is not None for v in [rate_per, pmt, pv, fv, payment_type]):
            nper = self.calculator.calcularNper(rate_per, pmt, pv, fv, payment_type)
            if nper is not None:
                message = f"Número de Períodos (NPER): {nper:,.2f}"
            else:
                message = "Error en el cálculo de NPER."
            self.update_result_text(self.ann_result_text, message)

    def calculate_pv_annuity(self):
        rate_per = self.get_float_input(self.ann_rate_entry, "Tasa Periódica", self.ann_result_text)
        nper = self.get_float_input(self.ann_nper_entry, "Número de Períodos", self.ann_result_text)
        pmt = self.get_float_input(self.ann_pmt_entry, "Pago Periódico (PMT)", self.ann_result_text)
        fv = self.get_float_input(self.ann_fv_entry, "Valor Futuro (FV)", self.ann_result_text)
        payment_type = self.get_int_input(self.ann_type_entry, "Tipo de Pago", self.ann_result_text)

        if all(v is not None for v in [rate_per, nper, pmt, fv, payment_type]):
            pv = self.calculator.calcularPv(rate_per, nper, pmt, fv, payment_type)
            if pv is not None:
                message = f"Valor Presente (PV): ${pv:,.2f}"
            else:
                message = "Error en el cálculo de PV."
            self.update_result_text(self.ann_result_text, message)

    def calculate_fv_annuity(self):
        rate_per = self.get_float_input(self.ann_rate_entry, "Tasa Periódica", self.ann_result_text)
        nper = self.get_float_input(self.ann_nper_entry, "Número de Períodos", self.ann_result_text)
        pmt = self.get_float_input(self.ann_pmt_entry, "Pago Periódico (PMT)", self.ann_result_text)
        pv = self.get_float_input(self.ann_pv_entry, "Valor Presente (PV)", self.ann_result_text)
        payment_type = self.get_int_input(self.ann_type_entry, "Tipo de Pago", self.ann_result_text)

        if all(v is not None for v in [rate_per, nper, pmt, pv, payment_type]):
            fv = self.calculator.calcularFv(rate_per, nper, pmt, pv, payment_type)
            if fv is not None:
                message = f"Valor Futuro (FV): ${fv:,.2f}"
            else:
                message = "Error en el cálculo de FV."
            self.update_result_text(self.ann_result_text, message)

    def calculate_rate(self):
        nper = self.get_float_input(self.ann_nper_entry, "Número de Períodos", self.ann_result_text)
        pmt = self.get_float_input(self.ann_pmt_entry, "Pago Periódico (PMT)", self.ann_result_text)
        pv = self.get_float_input(self.ann_pv_entry, "Valor Presente (PV)", self.ann_result_text)
        fv = self.get_float_input(self.ann_fv_entry, "Valor Futuro (FV)", self.ann_result_text)
        payment_type = self.get_int_input(self.ann_type_entry, "Tipo de Pago", self.ann_result_text)
        estimacion = self.get_float_input(self.ann_rate_estimate_entry, "Estimación de Tasa", self.ann_result_text)


        if all(v is not None for v in [nper, pmt, pv, fv, payment_type, estimacion]):
            rate = self.calculator.calcularRate(nper, pmt, pv, fv, payment_type, estimacion)
            if rate is not None:
                message = f"Tasa por Período (RATE): {rate * 100:,.4f}%"
            else:
                message = "Error en el cálculo de RATE o no se encontró convergencia."
            self.update_result_text(self.ann_result_text, message)

    # --- Depreciation Tab Functions ---
    def calculate_depreciation(self):
        valor_inicial = self.get_float_input(self.dep_initial_value_entry, "Valor Inicial", self.dep_result_text)
        valor_residual = self.get_float_input(self.dep_residual_value_entry, "Valor Residual", self.dep_result_text)
        vida_util = self.get_float_input(self.dep_useful_life_entry, "Vida Útil", self.dep_result_text)

        if all(v is not None for v in [valor_inicial, valor_residual, vida_util]):
            depreciacion = self.calculator.depreciacionLineal(valor_inicial, valor_residual, vida_util)
            if depreciacion is not None:
                message = f"Depreciación Anual Lineal: ${depreciacion:,.2f}"
            else:
                message = "Error en el cálculo de la depreciación lineal."
            self.update_result_text(self.dep_result_text, message)


if __name__ == "__main__":
    root = ctk.CTk()
    app = FinancialCalculatorCustomGUI(root)
    root.mainloop()