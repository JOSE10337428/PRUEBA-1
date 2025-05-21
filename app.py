import streamlit as st

# Explicación básica
st.title("Aprende Python: while, if, for")
st.write("""
### 🤔 ¿Cómo funcionan estas estructuras?
- **if**: ejecuta un bloque si se cumple una condición.
- **while**: repite un bloque mientras se cumpla una condición.
- **for**: repite un bloque un número específico de veces o sobre una secuencia.
""")

# Preguntas y respuestas
preguntas = [
    {
        "pregunta": "¿Qué hace un bucle 'while'?",
        "opciones": ["Ejecuta una vez", "Repite mientras una condición sea verdadera", "Repite un número fijo de veces"],
        "respuesta": "Repite mientras una condición sea verdadera"
    },
    {
        "pregunta": "¿Qué evalúa una sentencia 'if'?",
        "opciones": ["El tipo de una variable", "Una condición booleana", "El tamaño de una lista"],
        "respuesta": "Una condición booleana"
    },
    {
        "pregunta": "¿Qué estructura usarías para recorrer una lista?",
        "opciones": ["if", "while", "for"],
        "respuesta": "for"
    },
    {
        "pregunta": "¿Qué imprime este código?\n\nfor i in range(3): print(i)",
        "opciones": ["1 2 3", "0 1 2", "0 1 2 3"],
        "respuesta": "0 1 2"
    },
    {
        "pregunta": "¿Qué ocurre si la condición de un 'while' nunca es falsa?",
        "opciones": ["El programa se detiene", "Se imprime un error", "Bucle infinito"],
        "respuesta": "Bucle infinito"
    },
    {
        "pregunta": "¿Qué operador se usa para comparar en una condición 'if'?",
        "opciones": ["=", "==", "==="],
        "respuesta": "=="
    },
    {
        "pregunta": "¿Qué hace 'break' en un bucle?",
        "opciones": ["Continúa con la siguiente iteración", "Finaliza el bucle", "Reinicia el bucle"],
        "respuesta": "Finaliza el bucle"
    },
    {
        "pregunta": "¿Qué hace 'continue' en un bucle?",
        "opciones": ["Finaliza el bucle", "Salta al final del bucle", "Salta a la siguiente iteración"],
        "respuesta": "Salta a la siguiente iteración"
    },
    {
        "pregunta": "¿Qué devuelve range(5)?",
        "opciones": ["1 a 5", "0 a 4", "1 a 4"],
        "respuesta": "0 a 4"
    },
    {
        "pregunta": "¿Se puede usar 'if' dentro de un 'for'?",
        "opciones": ["Sí", "No", "Solo en funciones"],
        "respuesta": "Sí"
    }
]

respuestas_usuario = []
puntos = 0

st.write("## 📝 Responde las preguntas:")

# Mostrar las preguntas
for idx, item in enumerate(preguntas):
    seleccion = st.radio(f"{idx+1}. {item['pregunta']}", item['opciones'], key=idx)
    respuestas_usuario.append(seleccion)

# Botón para puntuar
if st.button("Calcular Puntaje"):
    puntos = sum([respuestas_usuario[i] == preguntas[i]["respuesta"] for i in range(len(preguntas))])
    st.success(f"Tu puntaje: {puntos} / 10")

    # Mostrar globos si obtiene 10
    if puntos == 10:
        st.balloons()
    elif puntos >= 7:
        st.info("¡Buen trabajo! Puedes seguir mejorando.")
    else:
        st.warning("Revisa las respuestas y vuelve a intentarlo.")
