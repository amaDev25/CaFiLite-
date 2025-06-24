import os
import sys
import time
from logica.utils import *
from colorama import init, Fore, Style, Back
from logica.calculos import CalculadoraFinanciera

# --- Función Principal del Menú ---
def menu():
    """
    Función que contiene el menú interactivo para la calculadora financiera.
    """
    try:
        calc = CalculadoraFinanciera() # Se crea una instancia de la calculadora
        
        # Inicializa Colorama al principio de tu script
        init(autoreset=True) # `autoreset=True` es clave para que los colores se reseteen automáticamente después de cada `print`
        
        while True:
            limpiarPantalla()
            print(f"{Fore.BLUE}{Style.BRIGHT}╔════════════════════════════════════════════════╗{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Style.BRIGHT}║          {Fore.GREEN}📊 CALCULADORA FINANCIERA COMPLETA 📊{Fore.BLUE}          ║{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Style.BRIGHT}╠════════════════════════════════════════════════╣{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{Style.BRIGHT}║          CÁLCULOS PRINCIPALES (TVM)            ║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ 1. Calcular Pago Periódico (PMT)                 ║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ 2. Calcular Número de Períodos (NPER)            ║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ 3. Calcular Valor Presente (PV) de Anualidad     ║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ 4. Calcular Valor Futuro (FV) de Anualidad       ║{Style.RESET_ALL}")
            print(f"{Fore.CYAN}║ 5. Calcular Tasa de Interés (RATE)               ║{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Style.BRIGHT}╠════════════════════════════════════════════════╣{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{Style.BRIGHT}║          CÁLCULOS BÁSICOS Y CONVERSIONES         ║{Style.RESET_ALL}")
            print(f"{Fore.GREEN}║ 6. Interés Simple                                ║{Style.RESET_ALL}")
            print(f"{Fore.GREEN}║ 7. Interés Compuesto                             ║{Style.RESET_ALL}")
            print(f"{Fore.GREEN}║ 8. Valor Presente (Monto Único)                  ║{Style.RESET_ALL}")
            print(f"{Fore.GREEN}║ 9. Valor Futuro (Monto Único)                    ║{Style.RESET_ALL}")
            print(f"{Fore.GREEN}║ 10. Tasa Nominal a Efectiva Anual                ║{Style.RESET_ALL}")
            print(f"{Fore.GREEN}║ 11. Tasa Efectiva Anual a Nominal                ║{Style.RESET_ALL}")
            print(f"{Fore.GREEN}║ 12. Conversión entre Tasas Efectivas             ║{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Style.BRIGHT}╠════════════════════════════════════════════════╣{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{Style.BRIGHT}║          OTROS CÁLCULOS ADICIONALES              ║{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}║ 13. Pago de Amortización (Sistema Francés)       ║{Style.RESET_ALL}")
            print(f"{Fore.MAGENTA}║ 14. Depreciación Lineal                          ║{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Style.BRIGHT}╠════════════════════════════════════════════════╣{Style.RESET_ALL}")
            print(f"{Fore.YELLOW}{Style.BRIGHT}║          VISUALIZACIÓN DE DATOS                  ║{Style.RESET_ALL}")
            print(f"{Fore.WHITE}║ 15. Graficar Interés Simple vs. Compuesto        ║{Style.RESET_ALL}")
            print(f"{Fore.WHITE}║ 16. Graficar Tabla de Amortización               ║{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Style.BRIGHT}╠════════════════════════════════════════════════╣{Style.RESET_ALL}")
            print(f"{Fore.RED}║ 0. Salir de la Aplicación                        ║{Style.RESET_ALL}")
            print(f"{Fore.BLUE}{Style.BRIGHT}╚════════════════════════════════════════════════╝{Style.RESET_ALL}")
        
            opcion = int(input(f"\n{Fore.YELLOW}{Style.BRIGHT}👉 Digite su opción: {Style.RESET_ALL}"))
            
            if opcion == 0:
                limpiarPantalla()
                print(f"{Fore.GREEN}{Style.BRIGHT}👋 ¡Gracias por usar la calculadora financiera! ¡Hasta pronto! 👋{Style.RESET_ALL}")
                time.sleep(2)
                sys.exit()
            
            # --- CÁLCULOS PRINCIPALES (TVM) ---
            elif opcion == 1: # PMT
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║      {Fore.GREEN}CALCULAR PAGO PERIÓDICO (PMT){Fore.BLUE}       ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}💡 {Style.BRIGHT}**IMPORTANTE:**{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - Dinero que {Fore.GREEN}RECIBE{Style.RESET_ALL}{Fore.YELLOW} (ej. préstamo)  ➡️ {Fore.GREEN}POSITIVO (+){Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - Dinero que {Fore.RED}PAGA{Style.RESET_ALL}{Fore.YELLOW} (ej. cuota, inversión) ➡️ {Fore.RED}NEGATIVO (-){Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - Tasas Anuales: Ej. '5' para 5%, '4.5' para 4.5%.{Style.RESET_ALL}")
                
                try:
                    pv = float(input(f"{Fore.CYAN}   💲 Valor Presente (PV): {Style.RESET_ALL}"))
                    tasa_anual_input = float(input(f"{Fore.CYAN}   📈 Tasa Anual (%): {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de Capitalización/Pagos por Año (ej. 12 para mensual): {Style.RESET_ALL}"))
                    nper_anios = float(input(f"{Fore.CYAN}   ⏳ Plazo en Años: {Style.RESET_ALL}"))
                    fv = float(input(f"{Fore.CYAN}   🎯 Valor Futuro deseado (0 si se amortiza completamente): {Style.RESET_ALL}"))
                    tipo_pago = int(input(f"{Fore.CYAN}   ⏰ Tipo de Pago (0=Fin de período, 1=Principio de período): {Style.RESET_ALL}"))
                    
                    tasa_periodica = (tasa_anual_input / 100) / frecuencia
                    nper_total = nper_anios * frecuencia
                    
                    calculo_pago = calc.calcularPmt(tasa_periodica, nper_total, pv, fv, tipo_pago)
                    
                    if calculo_pago is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   El {Fore.WHITE}{Style.BRIGHT}Pago Periódico (PMT){Fore.GREEN} es: ${abs(round(calculo_pago, 2)):,.2f}   ✨{Style.RESET_ALL}") 
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar el cálculo PMT. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                except ZeroDivisionError:
                    print(f"{Fore.RED}\n❗ Error: No se puede dividir por cero. Revise la tasa o NPER. ❗{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}\n🚫 Ocurrió un error inesperado al calcular PMT: {e} 🚫{Style.RESET_ALL}")
                pausar()

            elif opcion == 2: # NPER
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║    {Fore.GREEN}CALCULAR NÚMERO DE PERÍODOS (NPER){Fore.BLUE}    ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}💡 {Style.BRIGHT}**CONVENCIÓN DE SIGNOS:**{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - PV:  (+) si dinero {Fore.GREEN}recibido{Style.RESET_ALL}{Fore.YELLOW} (préstamo), (-) si {Fore.RED}inversión inicial{Style.RESET_ALL}{Fore.YELLOW}.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - PMT: (-) si {Fore.RED}pago/contribución{Style.RESET_ALL}{Fore.YELLOW} (dinero que sale), (+) si {Fore.GREEN}ingreso{Style.RESET_ALL}{Fore.YELLOW}.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - FV:  (+) si {Fore.GREEN}objetivo de ahorro{Style.RESET_ALL}{Fore.YELLOW}, (-) si {Fore.RED}deuda remanente{Style.RESET_ALL}{Fore.YELLOW} (si aplica).{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - Tasas Anuales: Ej. '5' para 5%, '4.5' para 4.5%.{Style.RESET_ALL}")

                try:
                    tasa_anual_input = float(input(f"{Fore.CYAN}   📈 Tasa Anual (%): {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de Capitalización/Pagos por Año (ej. 12 para mensual): {Style.RESET_ALL}"))
                    pmt = float(input(f"{Fore.CYAN}   💲 Pago Periódico (PMT): {Style.RESET_ALL}"))
                    pv = float(input(f"{Fore.CYAN}   💲 Valor Presente (PV): {Style.RESET_ALL}"))
                    fv = float(input(f"{Fore.CYAN}   🎯 Valor Futuro deseado (0 si se amortiza completamente): {Style.RESET_ALL}"))
                    tipo_pago = int(input(f"{Fore.CYAN}   ⏰ Tipo de Pago (0=Fin de período, 1=Principio de período): {Style.RESET_ALL}"))

                    tasa_periodica = (tasa_anual_input / 100) / frecuencia
                    
                    calculo_nper = calc.calcularNper(tasa_periodica, pmt, pv, fv, tipo_pago)
                    
                    if calculo_nper is not None:
                        nper_anios = calculo_nper / frecuencia
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   El {Fore.WHITE}{Style.BRIGHT}Número de Períodos (NPER){Fore.GREEN} es: {round(calculo_nper, 2)} ({round(nper_anios, 2)} años)   ✨{Style.RESET_ALL}") 
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar el cálculo NPER. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}\n🚫 Ocurrió un error inesperado al calcular NPER: {e} 🚫{Style.RESET_ALL}")
                pausar()

            elif opcion == 3: # PV
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║      {Fore.GREEN}CALCULAR VALOR PRESENTE (PV){Fore.BLUE}        ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}💡 {Style.BRIGHT}**CONVENCIÓN DE SIGNOS:**{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - PMT: (-) si {Fore.RED}pago/contribución{Style.RESET_ALL}{Fore.YELLOW} (salida), (+) si {Fore.GREEN}ingreso{Style.RESET_ALL}{Fore.YELLOW}.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - FV:  (+) si {Fore.GREEN}objetivo de ahorro{Style.RESET_ALL}{Fore.YELLOW}, (-) si {Fore.RED}deuda remanente{Style.RESET_ALL}{Fore.YELLOW} (si aplica).{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - Tasas Anuales: Ej. '5' para 5%, '4.5' para 4.5%.{Style.RESET_ALL}")

                try:
                    tasa_anual_input = float(input(f"{Fore.CYAN}   📈 Tasa Anual (%): {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de Capitalización/Pagos por Año (ej. 12 para mensual): {Style.RESET_ALL}"))
                    nper_anios = float(input(f"{Fore.CYAN}   ⏳ Plazo en Años: {Style.RESET_ALL}"))
                    pmt = float(input(f"{Fore.CYAN}   💲 Pago Periódico (PMT): {Style.RESET_ALL}"))
                    fv = float(input(f"{Fore.CYAN}   🎯 Valor Futuro deseado (0 si se amortiza completamente): {Style.RESET_ALL}"))
                    tipo_pago = int(input(f"{Fore.CYAN}   ⏰ Tipo de Pago (0=Fin de período, 1=Principio de período): {Style.RESET_ALL}"))
                    
                    tasa_periodica = (tasa_anual_input / 100) / frecuencia
                    nper_total = nper_anios * frecuencia
                    
                    calculo_pv = calc.calcularPv(tasa_periodica, nper_total, pmt, fv, tipo_pago)
                    
                    if calculo_pv is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   El {Fore.WHITE}{Style.BRIGHT}Valor Presente (PV){Fore.GREEN} es: ${round(calculo_pv, 2):,.2f}   ✨{Style.RESET_ALL}") 
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar el cálculo PV. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}\n🚫 Ocurrió un error inesperado al calcular PV: {e} 🚫{Style.RESET_ALL}")
                pausar()

            elif opcion == 4: # FV
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║       {Fore.GREEN}CALCULAR VALOR FUTURO (FV){Fore.BLUE}         ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}💡 {Style.BRIGHT}**CONVENCIÓN DE SIGNOS:**{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - PV:  (-) si {Fore.RED}inversión inicial{Style.RESET_ALL}{Fore.YELLOW}, (+) si {Fore.GREEN}préstamo{Style.RESET_ALL}{Fore.YELLOW}.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - PMT: (-) si {Fore.RED}pago/contribución{Style.RESET_ALL}{Fore.YELLOW} (salida), (+) si {Fore.GREEN}ingreso{Style.RESET_ALL}{Fore.YELLOW}.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - Tasas Anuales: Ej. '5' para 5%, '4.5' para 4.5%.{Style.RESET_ALL}")

                try:
                    tasa_anual_input = float(input(f"{Fore.CYAN}   📈 Tasa Anual (%): {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de Capitalización/Pagos por Año (ej. 12 para mensual): {Style.RESET_ALL}"))
                    nper_anios = float(input(f"{Fore.CYAN}   ⏳ Plazo en Años: {Style.RESET_ALL}"))
                    pmt = float(input(f"{Fore.CYAN}   💲 Pago Periódico (PMT): {Style.RESET_ALL}"))
                    pv = float(input(f"{Fore.CYAN}   💲 Valor Presente (PV): {Style.RESET_ALL}"))
                    tipo_pago = int(input(f"{Fore.CYAN}   ⏰ Tipo de Pago (0=Fin de período, 1=Principio de período): {Style.RESET_ALL}"))
                    
                    tasa_periodica = (tasa_anual_input / 100) / frecuencia
                    nper_total = nper_anios * frecuencia
                    
                    calculo_fv = calc.calcularFv(tasa_periodica, nper_total, pmt, pv, tipo_pago)
                    
                    if calculo_fv is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   El {Fore.WHITE}{Style.BRIGHT}Valor Futuro (FV){Fore.GREEN} es: ${round(calculo_fv, 2):,.2f}   ✨{Style.RESET_ALL}") 
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar el cálculo FV. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}\n🚫 Ocurrió un error inesperado al calcular FV: {e} 🚫{Style.RESET_ALL}")
                pausar()

            elif opcion == 5: # RATE
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║      {Fore.GREEN}CALCULAR TASA DE INTERÉS (RATE){Fore.BLUE}     ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}💡 {Style.BRIGHT}**CONVENCIÓN DE SIGNOS:**{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - PV:  (+) si dinero {Fore.GREEN}recibido{Style.RESET_ALL}{Fore.YELLOW} (préstamo), (-) si {Fore.RED}inversión inicial{Style.RESET_ALL}{Fore.YELLOW}.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - PMT: (-) si {Fore.RED}pago/contribución{Style.RESET_ALL}{Fore.YELLOW} (salida), (+) si {Fore.GREEN}ingreso{Style.RESET_ALL}{Fore.YELLOW}.{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - FV:  (+) si {Fore.GREEN}objetivo de ahorro{Style.RESET_ALL}{Fore.YELLOW}, (-) si {Fore.RED}deuda remanente{Style.RESET_ALL}{Fore.YELLOW} (si aplica).{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}   - Resultado en % anual.{Style.RESET_ALL}")

                try:
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de Capitalización/Pagos por Año (ej. 12 para mensual): {Style.RESET_ALL}"))
                    nper_anios = float(input(f"{Fore.CYAN}   ⏳ Plazo en Años: {Style.RESET_ALL}"))
                    pmt = float(input(f"{Fore.CYAN}   💲 Pago Periódico (PMT): {Style.RESET_ALL}"))
                    pv = float(input(f"{Fore.CYAN}   💲 Valor Presente (PV): {Style.RESET_ALL}"))
                    fv = float(input(f"{Fore.CYAN}   🎯 Valor Futuro deseado (0 si se amortiza completamente): {Style.RESET_ALL}"))
                    tipo_pago = int(input(f"{Fore.CYAN}   ⏰ Tipo de Pago (0=Fin de período, 1=Principio de período): {Style.RESET_ALL}"))
                    
                    nper_total = nper_anios * frecuencia
                    
                    calculo_rate = calc.calcularRate(nper_total, pmt, pv, fv, tipo_pago)
                    
                    if calculo_rate is not None:
                        tasa_anual_resultante = calculo_rate * frecuencia * 100
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   La {Fore.WHITE}{Style.BRIGHT}Tasa Anual (RATE){Fore.GREEN} es: {round(tasa_anual_resultante, 4)}%   ✨{Style.RESET_ALL}") 
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar el cálculo RATE. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                except Exception as e:
                    print(f"{Fore.RED}\n🚫 Ocurrió un error inesperado al calcular RATE: {e} 🚫{Style.RESET_ALL}")
                pausar()
            
            # --- CÁLCULOS BÁSICOS Y CONVERSIONES ---
            elif opcion == 6: # Interés Simple
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║         {Fore.GREEN}CALCULAR INTERÉS SIMPLE{Fore.BLUE}           ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    capital = float(input(f"{Fore.CYAN}   💲 Capital inicial: {Style.RESET_ALL}"))
                    tasa = float(input(f"{Fore.CYAN}   📈 Tasa de interés anual (%): {Style.RESET_ALL}"))
                    tiempo = float(input(f"{Fore.CYAN}   ⏳ Tiempo en años: {Style.RESET_ALL}"))
                    
                    interes, monto_final = calc.interesSimple(capital, tasa, tiempo)
                    if interes is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Interés Simple: ${round(interes, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Monto Final: ${round(monto_final, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo calcular el interés simple. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            elif opcion == 7: # Interés Compuesto
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║         {Fore.GREEN}CALCULAR INTERÉS COMPUESTO{Fore.BLUE}        ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    capital = float(input(f"{Fore.CYAN}   💲 Capital inicial: {Style.RESET_ALL}"))
                    tasa = float(input(f"{Fore.CYAN}   📈 Tasa de interés anual (%): {Style.RESET_ALL}"))
                    tiempo = float(input(f"{Fore.CYAN}   ⏳ Tiempo en años: {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de capitalización por año (ej. 1 para anual, 12 para mensual): {Style.RESET_ALL}"))
                    
                    interes, monto_final = calc.interesCompuesto(capital, tasa, tiempo, frecuencia)
                    if interes is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Interés Compuesto: ${round(interes, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Monto Final: ${round(monto_final, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo calcular el interés compuesto. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            elif opcion == 8: # Valor Presente (Monto Único)
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║     {Fore.GREEN}CALCULAR VALOR PRESENTE (MONTO ÚNICO){Fore.BLUE}    ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    futuro = float(input(f"{Fore.CYAN}   💲 Valor Futuro: {Style.RESET_ALL}"))
                    tasa = float(input(f"{Fore.CYAN}   📈 Tasa de interés anual (%): {Style.RESET_ALL}"))
                    tiempo = float(input(f"{Fore.CYAN}   ⏳ Tiempo en años: {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de capitalización por año: {Style.RESET_ALL}"))
                    
                    vp = calc.valorPresenteMontoUnico(futuro, tasa, tiempo, frecuencia)
                    if vp is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Valor Presente: ${round(vp, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo calcular el valor presente. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            elif opcion == 9: # Valor Futuro (Monto Único)
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║      {Fore.GREEN}CALCULAR VALOR FUTURO (MONTO ÚNICO){Fore.BLUE}     ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    presente = float(input(f"{Fore.CYAN}   💲 Capital inicial: {Style.RESET_ALL}"))
                    tasa = float(input(f"{Fore.CYAN}   📈 Tasa de interés anual (%): {Style.RESET_ALL}"))
                    tiempo = float(input(f"{Fore.CYAN}   ⏳ Tiempo en años: {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de capitalización por año: {Style.RESET_ALL}"))
                    
                    vf = calc.valorFuturoMontoUnico(presente, tasa, tiempo, frecuencia)
                    if vf is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Valor Futuro: ${round(vf, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo calcular el valor futuro. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            elif opcion == 10: # Tasa Nominal a Efectiva
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║   {Fore.GREEN}CONVERTIR TASA NOMINAL A EFECTIVA ANUAL{Fore.BLUE}  ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    tasa_nominal = float(input(f"{Fore.CYAN}   📈 Tasa Nominal Anual (%): {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de Capitalización por Año: {Style.RESET_ALL}"))
                    
                    tea = calc.tasaNominalAEfectiva(tasa_nominal, frecuencia)
                    if tea is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Tasa Efectiva Anual (TEA): {round(tea, 4)}%   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar la conversión. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            elif opcion == 11: # Tasa Efectiva a Nominal
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║   {Fore.GREEN}CONVERTIR TASA EFECTIVA ANUAL A NOMINAL{Fore.BLUE}  ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    tasa_efectiva = float(input(f"{Fore.CYAN}   📈 Tasa Efectiva Anual (%): {Style.RESET_ALL}"))
                    frecuencia = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de Capitalización por Año (ej. 12 para mensual): {Style.RESET_ALL}"))
                    
                    nominal = calc.tasaEfectivaANominal(tasa_efectiva, frecuencia)
                    if nominal is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Tasa Nominal Anual: {round(nominal, 4)}%   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar la conversión. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            elif opcion == 12: # Conversión entre Tasas Efectivas
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║   {Fore.GREEN}CONVERSIÓN ENTRE TASAS EFECTIVAS{Fore.BLUE}     ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                print(f"{Fore.YELLOW}Periodicidades disponibles: anual, semestral, trimestral, mensual, diaria{Style.RESET_ALL}")
                try:
                    tasa_conocida = float(input(f"{Fore.CYAN}   📈 Tasa Efectiva de Origen (%): {Style.RESET_ALL}"))
                    origen = input(f"{Fore.CYAN}   🗒️ Periodicidad de Origen (ej. mensual): {Style.RESET_ALL}").lower()
                    destino = input(f"{Fore.CYAN}   ➡️ Periodicidad de Destino (ej. anual): {Style.RESET_ALL}").lower()
                    
                    tasa_convertida = calc.conversionTasas(tasa_conocida, origen, destino)
                    if tasa_convertida is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Tasa Convertida ({destino}): {round(tasa_convertida, 4)}%   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo realizar la conversión de tasas. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar valores válidos. ❌{Style.RESET_ALL}")
                pausar()

            # --- OTROS CÁLCULOS ADICIONALES ---
            elif opcion == 13: # Pago de Amortización
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║   {Fore.GREEN}CALCULAR PAGO DE AMORTIZACIÓN{Fore.BLUE}      ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    capital = float(input(f"{Fore.CYAN}   💲 Monto del préstamo: {Style.RESET_ALL}"))
                    tasa_mensual = float(input(f"{Fore.CYAN}   📈 Tasa de interés mensual (%): {Style.RESET_ALL}"))
                    meses = int(input(f"{Fore.CYAN}   ⏳ Número de meses: {Style.RESET_ALL}"))
                    
                    cuota_mensual = calc.pagoAmortizacion(capital, tasa_mensual, meses)
                    if cuota_mensual is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Cuota Mensual: ${round(cuota_mensual, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo calcular el pago de amortización. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            elif opcion == 14: # Depreciación Lineal
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║      {Fore.GREEN}CALCULAR DEPRECIACIÓN LINEAL{Fore.BLUE}        ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    valor_inicial = float(input(f"{Fore.CYAN}   💲 Valor inicial del activo: {Style.RESET_ALL}"))
                    valor_residual = float(input(f"{Fore.CYAN}   💲 Valor residual del activo: {Style.RESET_ALL}"))
                    vida_util = float(input(f"{Fore.CYAN}   ⏳ Vida útil en años: {Style.RESET_ALL}"))
                    
                    depreciacion = calc.depreciacionLineal(valor_inicial, valor_residual, vida_util)
                    if depreciacion is not None:
                        print(f"{Fore.GREEN}{Style.BRIGHT}\n✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨   Depreciación Anual: ${round(depreciacion, 2):,.2f}   ✨{Style.RESET_ALL}")
                        print(f"{Fore.GREEN}{Style.BRIGHT}✨═════════════════════════════════════════✨{Style.RESET_ALL}")
                    else:
                        print(f"{Fore.YELLOW}\n⚠️ No se pudo calcular la depreciación lineal. Verifique sus entradas. ⚠️{Style.RESET_ALL}")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                pausar()

            # --- FUNCIONES DE VISUALIZACIÓN ---
            elif opcion == 15: # Graficar Interés Simple vs. Compuesto
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║   {Fore.GREEN}GRAFICAR INTERÉS SIMPLE VS. COMPUESTO{Fore.BLUE}  ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    capital = float(input(f"{Fore.CYAN}   💲 Capital inicial: {Style.RESET_ALL}"))
                    tasa = float(input(f"{Fore.CYAN}   📈 Tasa de interés anual (%): {Style.RESET_ALL}"))
                    tiempo = int(input(f"{Fore.CYAN}   ⏳ Tiempo en años (para el gráfico): {Style.RESET_ALL}"))
                    frecuencia_compuesto = int(input(f"{Fore.CYAN}   🗓️ Frecuencia de capitalización compuesto (ej. 1 para anual, 12 para mensual): {Style.RESET_ALL}"))
                    
                    calc.graficarInteresSimpleVsCompuesto(capital, tasa, tiempo, frecuencia_compuesto)
                    pausar("Gráfico generado. Presione Enter para volver al menú...")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                    pausar()
                except Exception as e:
                    print(f"{Fore.RED}\n🚫 Ocurrió un error al generar el gráfico: {e} 🚫{Style.RESET_ALL}")
                    pausar()

            elif opcion == 16: # Graficar Tabla de Amortización
                limpiarPantalla()
                print(f"{Fore.BLUE}{Style.BRIGHT}╔═════════════════════════════════════════╗{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}║      {Fore.GREEN}GRAFICAR TABLA DE AMORTIZACIÓN{Fore.BLUE}      ║{Style.RESET_ALL}")
                print(f"{Fore.BLUE}{Style.BRIGHT}╚═════════════════════════════════════════╝{Style.RESET_ALL}")
                try:
                    capital = float(input(f"{Fore.CYAN}   💲 Monto del préstamo: {Style.RESET_ALL}"))
                    tasa_mensual = float(input(f"{Fore.CYAN}   📈 Tasa de interés mensual (%): {Style.RESET_ALL}"))
                    meses = int(input(f"{Fore.CYAN}   ⏳ Número de meses: {Style.RESET_ALL}"))
                    
                    calc.graficarAmortizacion(capital, tasa_mensual, meses)
                    pausar("Gráficos generados. Presione Enter para volver al menú...")
                except ValueError:
                    print(f"{Fore.RED}\n❌ Entrada inválida. Asegúrese de ingresar números válidos. ❌{Style.RESET_ALL}")
                    pausar()
                except Exception as e:
                    print(f"{Fore.RED}\n🚫 Ocurrió un error al generar el gráfico: {e} 🚫{Style.RESET_ALL}")
                    pausar()

            else:
                print(f"{Fore.YELLOW}\n⚠️ Opción no válida. Por favor, intente de nuevo. ⚠️{Style.RESET_ALL}")
                pausar()
    except KeyboardInterrupt:
        print("\nl programa fue detendio por teclado")
        pausar()
        limpiarPantalla()
        sys.exit()
    except ValueError:
        print(f"{Fore.RED}\n❌ Entrada inválida. Por favor, digite un número para seleccionar una opción. ❌{Style.RESET_ALL}")
        pausar()
    except Exception as e:
        print(f"{Fore.RED}\n🚫 Ocurrió un error inesperado en el menú principal: {e} 🚫{Style.RESET_ALL}")
        pausar()