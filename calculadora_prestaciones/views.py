from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def calculadora_prestaciones(request):
    if request.method == 'POST':
        print(request.POST)
        salario = float(request.POST.get('salario', 0))

        TECHO_ISSS = 1000.00
        PORCENTAJE_ISSS_LABORAL = 0.03
        PORCENTAJE_ISSS_PATRONAL = 0.075

        # Porcentajes
        afp_laboral_porcentaje = 7.25 / 100
        afp_patronal_porcentaje = 7.75 / 100

        # Deducciones laborales
        afp_laboral = round(salario * afp_laboral_porcentaje, 2)
        isss_laboral = round(min(salario, TECHO_ISSS) * PORCENTAJE_ISSS_LABORAL, 2)
        deduccionTotalLaboral = round(afp_laboral + isss_laboral, 2)

        # Salario líquido para el ISR
        salario_liquido_para_isr = round(salario - deduccionTotalLaboral, 2)

        # Cálculo de ISR según tramos
        if salario_liquido_para_isr <= 472.00:
            isr = 0
        elif salario_liquido_para_isr <= 895.24:
            isr = (salario_liquido_para_isr - 472.00) * 0.10 + 17.67
        elif salario_liquido_para_isr <= 2038.10:
            isr = (salario_liquido_para_isr - 895.24) * 0.20 + 60.00
        else:
            isr = (salario_liquido_para_isr - 2038.10) * 0.30 + 288.57

        # Salario Neto
        salario_neto = round(salario_liquido_para_isr - isr, 2)

        # Cálculos AFP e ISSS patronales
        afp_patronal = round(salario * afp_patronal_porcentaje, 2)
        isss_patronal = round(min(salario, TECHO_ISSS) * PORCENTAJE_ISSS_PATRONAL, 2)

        # Total de deducciones
        descuento_total = round(afp_laboral + isss_laboral + isr, 2)

        # Resultado
        resultado = {
            'salario': round(salario, 2),
            'afp_laboral': afp_laboral,
            'isss_laboral': isss_laboral,
            'deduccion_total_laboral': deduccionTotalLaboral,
            'salario_menos_afp': round(salario - afp_laboral, 2),
            'salario_liquido_para_isr': salario_liquido_para_isr,
            'isr': round(isr, 2),
            'descuento_total': descuento_total,
            'salario_neto': salario_neto,
            'afp_patronal': afp_patronal,
            'isss_patronal': isss_patronal,
        }
        print(resultado)
        return render(request, 'index.html', resultado)

    return render(request, 'index.html')
