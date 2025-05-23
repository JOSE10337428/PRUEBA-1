import math

def calcular_sc(talla_cm, peso_kg):
    """Calcula la superficie corporal (SC) con la fórmula de Mosteller"""
    return math.sqrt((talla_cm * peso_kg) / 3600)

def calcular_crcl_urinaria(u_cr, volumen_orina_ml, p_cr, tiempo_min):
    """Calcula la depuración de creatinina usando orina"""
    return (u_cr * volumen_orina_ml) / (p_cr * tiempo_min)

def calcular_crcl_corregida(crcl, sc):
    """Corrige CrCl por superficie corporal estándar (1.73 m²)"""
    return crcl * (1.73 / sc)

def main():
    # Datos del paciente
    talla = float(input("Talla (cm): "))
    peso = float(input("Peso (kg): "))
    sc = calcular_sc(talla, peso)

    # Datos del laboratorio
    u_cr = float(input("Creatinina urinaria (mg/dL): "))
    volumen_orina = float(input("Volumen total de orina (mL): "))
    p_cr = float(input("Creatinina sérica (mg/dL): "))
    tiempo = float(input("Tiempo de recolección (minutos): "))  # normalmente 1440 min (24 h)

    # Cálculos
    crcl = calcular_crcl_urinaria(u_cr, volumen_orina, p_cr, tiempo)
    crcl_corregida = calcular_crcl_corregida(crcl, sc)

    # Resultados
    print(f"\nSuperficie corporal (SC): {sc:.2f} m²")
    print(f"Depuración de creatinina (no corregida): {crcl:.2f} mL/min")
    print(f"Depuración de creatinina corregida a 1.73 m²: {crcl_corregida:.2f} mL/min")

if __name__ == "__main__":
    main()
