import math
import matplotlib.pyplot as plt

class CalculadoraFinanciera:
    def __init__(self):
        """
        Constructor de clase, de momento no recibe parametros
        """
        pass

    # --- FUNCIONES DE INTERÉS Y VALOR FUTURO/PRESENTE BÁSICAS (PARA MONTOS ÚNICOS) ---
    def interesSimple(self, capital, tasa, tiempo):
        """
        Calcula el interes simple.

        Parametros:
            capital (float): Capital a calcular el interes simple.
            tasa (float): Tasa de interes (en porcentaje, ej. 5 para 5%).
            tiempo (float): Tiempo en anios.

        Retorno:
            tuple: Una tupla con el interes simple y el monto final (capital + interes).
        """
        try:
            interes = capital * (tasa / 100) * tiempo
            return interes, capital + interes
        except (ValueError, TypeError):
            print(f"{Fore.RED}Error: Los valores de entrada para el cálculo de interés simple son inválidos.{Style.RESET_ALL}")
            return None, None

    def interesCompuesto(self, capital, tasa, tiempo, frecuencia=1):
        """
        Calcula el interes compuesto.

        Parametros:
            capital (float): Capital a calcular el interes simple.
            tasa (float): Tasa de interes (en porcentaje, ej. 5 para 5%).
            tiempo (float): Tiempo en anios.
            frecuencia (int): Veces que se aplica el interes al anio (por ejemplo, 12 para mensual).

        Retorno:
            tuple: Una tupla con el interes compuesto y el monto final (capital + interes).
        """
        try:
            if frecuencia <= 0:
                raise ValueError("La frecuencia de capitalización debe ser mayor que cero.")
            monto_final = capital * ((1 + (tasa / 100) / frecuencia) ** (frecuencia * tiempo))
            interes_compuesto = monto_final - capital
            return interes_compuesto, monto_final
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Error en el cálculo de interés compuesto: {e}{Style.RESET_ALL}")
            return None, None

    # Nota: `valorPresente` y `valorFuturo` aquí son para montos únicos,
    # no para anualidades (series de pagos). Las funciones PV y FV abajo sí manejan anualidades.
    def valorPresenteMontoUnico(self, futuro, tasa, tiempo, frecuencia=1):
        """
        Calcula el valor presente de un monto futuro (sin pagos periódicos).

        Parametros:
            futuro (float): Valor futuro.
            tasa (float): Tasa anual en % (ej. 5 para 5%).
            tiempo (float): Anios.
            frecuencia (int): Capitalizacion por anio.

        Retorno:
            float: Valor presente.
        """
        try:
            if frecuencia <= 0:
                raise ValueError("La frecuencia de capitalización debe ser mayor que cero.")
            valor_presente = futuro / ((1 + (tasa / 100) / frecuencia) ** (frecuencia * tiempo))
            return valor_presente
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Error en el cálculo del valor presente de monto único: {e}{Style.RESET_ALL}")
            return None

    def valorFuturoMontoUnico(self, presente, tasa, tiempo, frecuencia=1):
        """
        Calcula el valor futuro de un monto presente (sin pagos periódicos).

        Parametros:
            presente (float): Valor actual.
            tasa (float): Tasa anual en % (ej. 5 para 5%).
            tiempo (float): Anios.
            frecuencia (int): Capitalizacion por anio.

        Retorno:
            float: Retorna el valor futuro.
        """
        try:
            if frecuencia <= 0:
                raise ValueError("La frecuencia de capitalización debe ser mayor que cero.")
            valor_futuro = presente * ((1 + (tasa / 100) / frecuencia) ** (frecuencia * tiempo))
            return valor_futuro
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Error en el cálculo del valor futuro de monto único: {e}{Style.RESET_ALL}")
            return None

    # --- FUNCIONES DE CONVERSIÓN DE TASAS ---
    def tasaNominalAEfectiva(self, tasaNominal, frecuenciaCapitalizacion):
        """
        Convierte una tasa nominal anual a una tasa efectiva anual (TEA).

        Parametros:
            tasaNominal (float): La tasa nominal anual (en porcentaje, ej. 12 para 12%).
            frecuenciaCapitalizacion (int): El número de veces que la tasa se capitaliza por año.

        Retorno:
            float: La tasa efectiva anual (en porcentaje).
        """
        try:
            if frecuenciaCapitalizacion <= 0:
                raise ValueError("La frecuencia de capitalización debe ser mayor que cero.")
            # Convertir tasa nominal a decimal para el cálculo
            tasaNominalDecimal = tasaNominal / 100
            tea = ((1 + tasaNominalDecimal / frecuenciaCapitalizacion) ** frecuenciaCapitalizacion - 1) * 100
            return tea
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Error en la conversión de tasa nominal a efectiva: {e}{Style.RESET_ALL}")
            return None

    def tasaEfectivaANominal(self, tasaEfectivaAnual, frecuenciaCapitalizacion):
        """
        Convierte una tasa efectiva anual a una tasa nominal anual.

        Parametros:
            tasaEfectivaAnual (float): La tasa efectiva anual (en porcentaje, ej. 12.68 para 12.68%).
            frecuenciaCapitalizacion (int): El número de veces que la tasa se capitaliza por año.

        Retorno:
            float: La tasa nominal anual (en porcentaje).
        """
        try:
            if frecuenciaCapitalizacion <= 0:
                raise ValueError("La frecuencia de capitalización debe ser mayor que cero.")
            # Convertir tasa efectiva anual a decimal para el cálculo
            tasaEfectivaDecimal = tasaEfectivaAnual / 100
            tasaNominal = frecuenciaCapitalizacion * ((1 + tasaEfectivaDecimal)**(1/frecuenciaCapitalizacion) - 1) * 100
            return tasaNominal
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Error en la conversión de tasa efectiva a nominal: {e}{Style.RESET_ALL}")
            return None

    def tasaEfectivaAOtraEfectiva(self, tasaEfectivaConocida, periodosConocidosEnAnio, periodosDeseadosEnAnio):
        """
        Convierte una tasa efectiva de una periodicidad a otra periodicidad efectiva.

        Parametros:
            tasaEfectivaConocida (float): La tasa efectiva para el período conocido (en porcentaje, ej. 1 para 1%).
            periodosConocidosEnAnio (float): La cantidad de veces que el período conocido ocurre en un año (ej. 12 para mensual, 4 para trimestral).
            periodosDeseadosEnAnio (float): La cantidad de veces que el período deseado ocurre en un año (ej. 1 para anual, 12 para mensual).

        Retorno:
            float: La tasa efectiva para la nueva periodicidad (en porcentaje).
        """
        try:
            if periodosConocidosEnAnio <= 0 or periodosDeseadosEnAnio <= 0:
                raise ValueError("Los períodos de capitalización deben ser mayores que cero.")

            # Convertir tasa conocida a decimal
            tasaEfectivaDecimal = tasaEfectivaConocida / 100

            # Fórmula para convertir tasas efectivas entre diferentes periodicidades
            tasaConvertidaDecimal = (1 + tasaEfectivaDecimal)**(periodosConocidosEnAnio / periodosDeseadosEnAnio) - 1
            tasaConvertida = tasaConvertidaDecimal * 100
            return tasaConvertida
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Error en la conversión de tasa efectiva a otra efectiva: {e}{Style.RESET_ALL}")
            return None

    def conversionTasas(self, tasa, origen, destino):
        """
        Convierte entre tasas efectivas periódicas (por ejemplo: mensual -> anual, etc.).
        Esta función asume que las tasas de origen y destino son EFECTIVAS para sus respectivos períodos.

        Parametros:
            tasa (float): Valor de la tasa (en porcentaje).
            origen (str): Periodicidad de la tasa de origen ("anual", "semestral", "trimestral", "mensual", "diaria").
            destino (str): Periodicidad de la tasa de destino ("anual", "semestral", "trimestral", "mensual", "diaria").

        Retorno:
            float: Tasa convertida (en porcentaje).
        """
        try:
            equivalencias = {
                "anual": 1,
                "semestral": 2,
                "trimestral": 4,
                "mensual": 12,
                "diaria": 365
            }
            
            if origen not in equivalencias or destino not in equivalencias:
                raise ValueError("Origen o destino de periodicidad no válido. Opciones: anual, semestral, trimestral, mensual, diaria.")
            
            frecuenciaOrigen = equivalencias[origen]
            frecuenciaDestino = equivalencias[destino]

            # Reutiliza la función interna tasaEfectivaAOtraEfectiva
            # Aquí, la "tasaEfectivaConocida" es la tasa que entra, y los "periodosConocidos"
            # son los del origen, y los "periodosDeseados" son los del destino.
            tasaConvertida = self.tasaEfectivaAOtraEfectiva(tasa, frecuenciaOrigen, frecuenciaDestino)
            return tasaConvertida

        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Error en la conversión de tasas: {e}{Style.RESET_ALL}")
            return None
    
    # --- FUNCIONES FINANCIERAS PRINCIPALES (PMT, NPER, PV, FV, RATE) ---
    def calcularPmt(self, tasa_periodica, nper, pv, fv=0, tipo=0):
        """
        Calcula el pago periódico (PMT) de un préstamo o inversión.

        Parámetros:
            tasa_periodica (float): Tasa de interés por período (ej. 0.005 para 0.5% mensual).
            nper (float): Número total de períodos de pago.
            pv (float): Valor presente o principal del préstamo/inversión.
                            POSITIVO si es dinero que RECIBES (préstamo).
                            NEGATIVO si es dinero que INVIERTES/ENTREGAS (compra).
            fv (float): Valor futuro deseado (0 si se amortiza completamente).
            tipo (int): 0 = Pagos al final del período, 1 = Pagos al principio del período.

        Retorno:
            float: El valor del pago periódico. Negativo si es un desembolso.
        """
        try:
            if tasa_periodica == 0:
                if nper == 0:
                    raise ValueError("NPER no puede ser cero cuando la tasa es cero.")
                return -(pv + fv) / nper

            pow_factor = math.pow(1 + tasa_periodica, nper)
            
            # Numerador y denominador para la fórmula PMT
            # Adaptado para que PV sea positivo si es un préstamo (dinero que entra)
            # y PMT sea negativo (dinero que sale)
            # Si FV es 0 (amortización completa), se simplifica.
            
            # Fórmula estándar de PMT (basada en Excel/Numpy Financial)
            # PMT = (rate * (FV + PV * (1 + rate)^nper)) / ((1 + rate)^nper - 1)
            # Note the sign convention reversal for consistent output as a payment (negative)
            
            numerador = fv * tasa_periodica + pv * pow_factor * tasa_periodica
            denominador = pow_factor - 1

            if denominador == 0:
                raise ZeroDivisionError("El denominador de la fórmula PMT es cero.")

            pmt_valor = numerador / denominador

            if tipo == 1: # Ajuste para pagos anticipados
                if (1 + tasa_periodica) == 0:
                    raise ZeroDivisionError("(1 + tasa_periodica) es cero en anualidad anticipada.")
                pmt_valor /= (1 + tasa_periodica) # Aquí se divide para que el PMT sea menor ya que tienes un período extra para ganar interés.

            return -pmt_valor # Retornamos negativo para indicar que es un pago (salida de dinero)

        except (ValueError, ZeroDivisionError) as e:
            print(f"{Fore.RED}Error en el cálculo PMT: {e}{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}Ocurrió un error inesperado al calcular PMT: {e}{Style.RESET_ALL}")
            return None

    def calcularNper(self, tasa_periodica, pmt, pv, fv=0, tipo=0):
        """
        Calcula el número de períodos (NPER) requeridos para una inversión o préstamo.

        Parámetros:
            tasa_periodica (float): Tasa de interés por período (ej. 0.005 para 0.5% mensual).
            pmt (float): Pago periódico. NEGATIVO si es un pago (salida), POSITIVO si es un ingreso.
            pv (float): Valor presente. POSITIVO si es dinero que RECIBES (préstamo), NEGATIVO si es INVERSIÓN.
            fv (float): Valor futuro. POSITIVO si es un objetivo de ahorro, NEGATIVO si es una deuda remanente.
            tipo (int): 0 = Pagos al final del período, 1 = Pagos al principio del período.

        Retorno:
            float: El número total de períodos.
        """
        try:
            if tasa_periodica == 0:
                if pmt == 0:
                    if pv != -fv: # Si PMT es 0, PV debe ser igual a -FV para tener una solución real.
                        raise ValueError("PMT no puede ser cero si la tasa es cero y PV no es -FV.")
                    return 0.0 # No hay períodos si no hay flujo de efectivo o cambio en valor
                return -(pv + fv) / pmt # Fórmula simplificada para tasa cero

            # Ajuste PMT para anualidad anticipada
            pmt_adj = pmt * (1 + tasa_periodica) if tipo == 1 else pmt

            # Numerador y denominador para el logaritmo
            numerador_log = pmt_adj - fv * tasa_periodica
            denominador_log = pv * tasa_periodica + pmt_adj

            if denominador_log == 0:
                raise ZeroDivisionError("El denominador de la expresión del logaritmo para NPER es cero (situación indefinida).")

            argumento_log = numerador_log / denominador_log

            if argumento_log <= 0:
                raise ValueError("El argumento del logaritmo NPER debe ser positivo. Revise los signos de: PV, PMT, FV.")

            base_log = 1 + tasa_periodica
            if base_log <= 0:
                    raise ValueError("La base del logaritmo (1 + tasa_periodica) debe ser positiva.")

            valor_nper = math.log(argumento_log) / math.log(base_log)

            return valor_nper
        except (ValueError, ZeroDivisionError, TypeError) as e:
            print(f"{Fore.RED}Error al calcular el NPER: {e}{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}Ocurrió un error inesperado al calcular NPER: {e}{Style.RESET_ALL}")
            return None

    def calcularPv(self, tasa_periodica, nper, pmt, fv=0, tipo=0):
        """
        Calcula el Valor Presente (PV) de una inversión o préstamo.

        Parámetros:
            tasa_periodica (float): Tasa de interés por período (ej. 0.005 para 0.5% mensual).
            nper (float): Número total de períodos de pago.
            pmt (float): Pago periódico. NEGATIVO si es un pago (salida), POSITIVO si es un ingreso.
            fv (float): Valor futuro. POSITIVO si es un objetivo de ahorro, NEGATIVO si es una deuda remanente.
            tipo (int): 0 = Pagos al final del período, 1 = Pagos al principio del período.

        Retorno:
            float: El Valor Presente. NEGATIVO si es una inversión inicial (salida), POSITIVO si es un préstamo (entrada).
        """
        try:
            if tasa_periodica == 0:
                return -fv - (pmt * nper) # Simple sum for zero rate

            # (1 + r)^n
            pow_factor = math.pow(1 + tasa_periodica, nper)

            # Calculate PV components
            # PV_pmt_component = PMT * [1 - (1+r)^-n] / r
            # PV_fv_component = FV / (1+r)^n
            # Combined and adjusted for typical financial function output signs
            
            pv_value = (-fv - pmt * ((pow_factor - 1) / tasa_periodica)) / pow_factor

            if tipo == 1: # Adjustment for payments at the beginning of the period
                pv_value *= (1 + tasa_periodica) # Correctly MULTIPLY for beginning-of-period PV

            return pv_value

        except (ValueError, ZeroDivisionError) as e:
            print(f"{Fore.RED}Error en el cálculo PV: {e}{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}Ocurrió un error inesperado al calcular PV: {e}{Style.RESET_ALL}")
            return None

    def calcularFv(self, tasa_periodica, nper, pmt, pv=0, tipo=0):
        """
        Calcula el Valor Futuro (FV) de una inversión o préstamo.

        Parámetros:
            tasa_periodica (float): Tasa de interés por período (ej. 0.005 para 0.5% mensual).
            nper (float): Número total de períodos de pago.
            pmt (float): Pago periódico. NEGATIVO si es un pago (salida), POSITIVO si es un ingreso.
            pv (float): Valor presente. NEGATIVO si es una inversión inicial, POSITIVO si es un préstamo.
            tipo (int): 0 = Pagos al final del período, 1 = Pagos al principio del período.

        Retorno:
            float: El Valor Futuro. POSITIVO si es un valor acumulado, NEGATIVO si es una deuda remanente.
        """
        try:
            if tasa_periodica == 0:
                return -pv - (pmt * nper) # Simple sum for zero rate

            pow_factor = math.pow(1 + tasa_periodica, nper)
            
            # Standard FV formula, adjusted for typical financial function output signs
            # FV = -PV * (1+r)^n - PMT * [((1+r)^n - 1) / r]
            fv_value = -pv * pow_factor - pmt * ((pow_factor - 1) / tasa_periodica)
            
            if tipo == 1: # Adjustment for payments at the beginning of the period
                fv_value *= (1 + tasa_periodica) # Correctly MULTIPLY for beginning-of-period FV
            
            return fv_value

        except (ValueError, ZeroDivisionError) as e:
            print(f"{Fore.RED}Error en el cálculo FV: {e}{Style.RESET_ALL}")
            return None
        except Exception as e:
            print(f"{Fore.RED}Ocurrió un error inesperado al calcular FV: {e}{Style.RESET_ALL}")
            return None

    def calcularRate(self, nper, pmt, pv, fv=0, tipo=0, estimacion=0.1):
        """
        Calcula la tasa de interés (RATE) por período utilizando el método de Newton-Raphson.

        Parámetros:
            nper (float): Número total de períodos.
            pmt (float): Pago periódico. NEGATIVO si es un pago (salida), POSITIVO si es un ingreso.
            pv (float): Valor presente. POSITIVO si es dinero que RECIBES, NEGATIVO si es INVERSIÓN.
            fv (float): Valor futuro. POSITIVO si es un objetivo, NEGATIVO si es una deuda.
            tipo (int): 0 = Pagos al final del período, 1 = Pagos al principio del período.
            estimacion (float): Estimación inicial para la tasa (útil si hay problemas de convergencia).

        Retorno:
            float: La tasa de interés por período (en decimal).
        """
        tolerancia = 0.0000001
        max_iteraciones = 1000

        def ecuacionFv(tasa_local):
            """Función auxiliar que representa la ecuación de valor futuro."""
            if tasa_local == 0:
                return pv + pmt * nper + fv
            else:
                pmt_adj_local = pmt
                if tipo == 1:
                    pmt_adj_local = pmt * (1 + tasa_local)
                
                # FV formula rearranged to be F(rate) = 0 for Newton-Raphson
                return pv * math.pow(1 + tasa_local, nper) + pmt_adj_local * (math.pow(1 + tasa_local, nper) - 1) / tasa_local + fv

        try:
            tasa = estimacion
            for i in range(max_iteraciones):
                f_at_tasa = ecuacionFv(tasa)
                
                # Numerical derivative for F(rate)
                delta_tasa = 0.000001 # Small change for derivative
                derivada_f_at_tasa = (ecuacionFv(tasa + delta_tasa) - f_at_tasa) / delta_tasa

                if abs(derivada_f_at_tasa) < tolerancia: # Avoid division by near zero
                    break
                
                nueva_tasa = tasa - f_at_tasa / derivada_f_at_tasa

                if abs(nueva_tasa - tasa) < tolerancia: # Check for convergence
                    return nueva_tasa
                
                tasa = nueva_tasa
            
            raise ValueError(f"{Fore.RED}La tasa de interés no convergió después de {max_iteraciones} iteraciones. Revise los signos de PV, PMT, FV.{Style.RESET_ALL}")
        except (ValueError, ZeroDivisionError, TypeError) as e:
            print(f"{Fore.RED}Error en el cálculo RATE: {e}{Style.RESET_ALL}")
            return None
        except Exception as ex:
            print(f"{Fore.RED}Ocurrió un error inesperado al calcular RATE: {ex}{Style.RESET_ALL}")
            return None

    # --- OTRAS FUNCIONES FINANCIERAS ADICIONALES ---
    def pagoAmortizacion(self, capital, tasa_mensual, meses):
        """
        Calcula el pago mensual fijo del sistema francés de amortización (cuota constante).
        Es equivalente a la función PMT con FV=0 y tipo=0 para pagos mensuales.

        Parámetros:
            capital (float): Monto del préstamo.
            tasa_mensual (float): Tasa de interés mensual (en porcentaje, ej. 0.5 para 0.5%).
            meses (int): Número de cuotas en meses.

        Retorno:
            float: Cuota mensual calculada.
        """
        try:
            # Se convierte el porcentaje a decimal
            tasa_mensual_decimal = tasa_mensual / 100
            if tasa_mensual_decimal == 0:
                # Si no hay interés, es simplemente capital / meses
                return capital / meses 
            
            # Fórmula de la cuota fija (PMT)
            cuota = capital * (tasa_mensual_decimal * (1 + tasa_mensual_decimal) ** meses) / ((1 + tasa_mensual_decimal) ** meses - 1)
            return cuota
        except Exception as e:
            print(f"{Fore.RED}Ocurrió un error en el cálculo del pago de amortización: {e}{Style.RESET_ALL}")
            return None
            
    def depreciacionLineal(self, valor_inicial, valor_residual, vida_util):
        """
        Calcula la depreciación lineal anual.

        Parámetros:
            valor_inicial (float): Valor inicial del activo.
            valor_residual (float): Valor residual (o de salvamento) del activo al final de su vida útil.
            vida_util (float): Vida útil del activo en años.

        Retorno:
            float: Retorna la depreciación anual.
        """
        try:
            if vida_util <= 0:
                raise ValueError("La vida útil debe ser un número positivo.")
            depreciacion_lineal = (valor_inicial - valor_residual) / vida_util
            return depreciacion_lineal
        except (ValueError, TypeError) as e:
            print(f"{Fore.RED}Ocurrió un error en el cálculo de la depreciación lineal: {e}{Style.RESET_ALL}")
            return None

    # --- FUNCIONES DE GRAFICACIÓN INTEGRADAS ---
    def graficarInteresSimpleVsCompuesto(self, capital_inicial, tasa, tiempo, frecuencia_compuesto=1):
        """
        Grafica la evolución del capital con interés simple y compuesto a lo largo del tiempo.
        """
        try:
            intereses_simples = [capital_inicial * (tasa / 100) * t for t in range(tiempo + 1)]
            montos_simples = [capital_inicial + i for i in intereses_simples]

            montos_compuestos = [capital_inicial * ((1 + (tasa / 100) / frecuencia_compuesto) ** (frecuencia_compuesto * t)) for t in range(tiempo + 1)]

            plt.figure(figsize=(10, 6))
            plt.plot(range(tiempo + 1), montos_simples, label='Interés Simple', marker='o')
            plt.plot(range(tiempo + 1), montos_compuestos, label=f'Interés Compuesto (f={frecuencia_compuesto})', marker='x')
            plt.xlabel('Tiempo (años)')
            plt.ylabel('Monto Total')
            plt.title('Comparación Interés Simple vs. Compuesto')
            plt.legend()
            plt.grid(True)
            plt.show()
        except Exception as e:
            print(f"{Fore.RED}Error al generar el gráfico de Interés Simple vs. Compuesto: {e}{Style.RESET_ALL}")

    def graficarAmortizacion(self, capital, tasa_mensual, meses):
        """
        Genera y muestra un gráfico de la amortización de un préstamo.
        """
        try:
            cuota = self.pagoAmortizacion(capital, tasa_mensual, meses)
            if cuota is None:
                print(f"{Fore.RED}No se pudo calcular la cuota de amortización para la graficación.{Style.RESET_ALL}")
                return

            saldo = capital
            intereses_pagados = []
            capital_pagado = []
            saldos = []

            tasa_mensual_decimal = tasa_mensual / 100

            for _ in range(meses):
                interes = saldo * tasa_mensual_decimal
                principal = cuota - interes
                saldo -= principal

                intereses_pagados.append(interes)
                capital_pagado.append(principal)
                saldos.append(saldo)

            meses_lista = range(1, meses + 1)

            # Gráfico de líneas
            plt.figure(figsize=(12, 7))
            plt.plot(meses_lista, saldos, label='Saldo Pendiente', marker='o')
            plt.plot(meses_lista, intereses_pagados, label='Intereses Pagados', marker='x')
            plt.plot(meses_lista, capital_pagado, label='Capital Pagado', marker='+')
            plt.xlabel('Mes')
            plt.ylabel('Valor ($)')
            plt.title('Tabla de Amortización')
            plt.legend()
            plt.grid(True)
            plt.show()

            # Gráfico de barras apiladas
            plt.figure(figsize=(12, 7))
            plt.bar(meses_lista, capital_pagado, label='Capital Pagado', color='green')
            plt.bar(meses_lista, intereses_pagados, bottom=capital_pagado, label='Intereses Pagados', color='red')
            plt.xlabel('Mes')
            plt.ylabel('Valor ($)')
            plt.title('Composición del Pago Mensual')
            plt.legend()
            plt.grid(axis='y')
            plt.show()
        except Exception as e:
            print(f"{Fore.RED}Error al generar el gráfico de Amortización: {e}{Style.RESET_ALL}")