from typing import Dict, Any

def evaluar_estado(inputs: Dict[str, float]) -> str:
    """
    inputs espera un dict con al menos estas claves:
    - 'valor_a' : float  (ej. temperatura normalizada 0-1 o puntaje)
    - 'valor_b' : float  (ej. frecuencia cardiaca normalizada)
    - 'valor_c' : float  (ej. puntaje de sintomas 0-10)

    Retorna uno de:
    - "NO ENFERMO"
    - "ENFERMEDAD LEVE"
    - "ENFERMEDAD AGUDA"
    - "ENFERMEDAD CRÓNICA"

    La lógica es intencionalmente simple y determinista (reglas).
    """

    a = float(inputs.get("valor_a", 0.0))
    b = float(inputs.get("valor_b", 0.0))
    c = float(inputs.get("valor_c", 0.0))

    # Ejemplo de normalización/interpretación:
    # a: 0..1 (0 = normal, 1 = muy alto)
    # b: ritmo relativo (por ejemplo 0..200 mapeado a 0..1), aqui se asume 0..1
    # c: sintomas 0..10 (0 = nada, 10 = grave)

    # Regla 1: NO ENFERMO (todo cercano a 0)
    if a <= 0.2 and b <= 0.2 and c <= 1.0:
        return "NO ENFERMO"

    # Regla 2: ENFERMEDAD LEVE (sintomas bajos o 1 indicador moderado)
    if (a <= 0.5 and b <= 0.5 and c <= 3.0) or (c <= 2.0 and (a > 0.2 or b > 0.2)):
        return "ENFERMEDAD LEVE"

    # Regla 3: ENFERMEDAD CRÓNICA (indicador persistente: b alto con c moderado, o a moderada y c moderado)
    if b >= 0.7 and c >= 3.0 and a <= 0.7:
        return "ENFERMEDAD CRÓNICA"

    # Regla 4: ENFERMEDAD AGUDA (valores altos, síntomas severos)
    if a > 0.7 or b > 0.8 or c >= 6.0:
        return "ENFERMEDAD AGUDA"

    # Caso por defecto (si no cae en anteriores)
    # Puede que caiga en un rango intermedio: devolver LEVE por defecto
    return "ENFERMEDAD LEVE"
