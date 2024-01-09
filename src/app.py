import streamlit as st

st.title("Suma tres números")

st.write("## Usando `number_input`")

n1 = st.number_input("Primer sumando:")
n2 = st.number_input("Segundo sumando:")
n3 = st.number_input("Tercer sumando:")

st.write("La suma de los tres números es", n1 + n2 + n3)

st.divider()

st.write("## Usando `slider`")

p1 = st.slider("Primer sumando:")
p2 = st.slider("Segundo sumando:")
p3 = st.slider("Tercer sumando:")

st.write("La suma de los tres números es", p1 + p2 + p3)