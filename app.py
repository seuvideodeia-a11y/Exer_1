import streamlit as st

# Configuração da página para um visual limpo e moderno
st.set_page_config(
    page_title="Calculadora Simples",
    page_icon="🧮",
    layout="centered"
)

# 1. Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write("Bem-vindo ao seu primeiro projeto em Streamlit! Insira os valores e escolha a operação abaixo.")

# Criando um layout em colunas para organizar os campos de entrada
col1, col2 = st.columns(2)

# 2. Dois campos de entrada numérica com valores padrão definidos como 0.0
with col1:
    num1 = st.number_input("Digite o primeiro número:", value=0.0, format="%.2f")

with col2:
    num2 = st.number_input("Digite o segundo número:", value=0.0, format="%.2f")

# 3. Componente de seleção para escolher a operação
operacao = st.radio(
    "Escolha a operação desejada:",
    ("Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"),
    horizontal=True
)

st.markdown("---")

# 4. Botão de ação com o texto "Calcular"
if st.button("Calcular", type="primary", use_container_width=True):
    # 5. Lógica de cálculo e tratamento de erros
    if operacao == "Soma (+)":
        resultado = num1 + num2
        st.metric(label="Resultado da Soma", value=f"{resultado:.2f}")
        st.success("Cálculo realizado com sucesso! 🎉")
        
    elif operacao == "Subtração (-)":
        resultado = num1 - num2
        st.metric(label="Resultado da Subtração", value=f"{resultado:.2f}")
        st.success("Cálculo realizado com sucesso! 🎉")
        
    elif operacao == "Multiplicação (*)":
        resultado = num1 * num2
        st.metric(label="Resultado da Multiplicação", value=f"{resultado:.2f}")
        st.success("Cálculo realizado com sucesso! 🎉")
        
    elif operacao == "Divisão (/)":
        if num2 == 0.0:
            # Tratamento amigável para divisão por zero
            st.error("⚠️ Ops! Não é possível realizar uma divisão por zero. Tente alterar o segundo número.")
        else:
            resultado = num1 / num2
            st.metric(label="Resultado da Divisão", value=f"{resultado:.2f}")
            st.success("Cálculo realizado com sucesso! 🎉")
