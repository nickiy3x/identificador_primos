import streamlit as st


def es_primo(numero: int) -> bool:
    """Devuelve True si numero es primo."""
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True


st.set_page_config(page_title="Verificador de números primos", page_icon="🔢")
st.title("🔢 Verificador de números primos")
st.write("Escribe un número entero y descubre si es primo.")

numero = st.number_input(
    "Número entero",
    min_value=-(10**15),
    max_value=10**15,
    value=2,
    step=1,
)

if st.button("Comprobar", type="primary"):
    if es_primo(int(numero)):
        st.success(f"{int(numero)} es un número primo.")
    else:
        st.info(f"{int(numero)} no es un número primo.")
