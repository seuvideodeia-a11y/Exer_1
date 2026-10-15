import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Calculadora Interativa", page_icon="🧮", layout="centered"
)

# Título principal com ícone amigável
st.title("🧮 Calculadora Interativa")
st.write(
    "Bem-vindo ao seu primeiro projeto em Streamlit! Insira os valores e escolha"
    " a operação abaixo."
)

# Layout em colunas para os números
col1, col2 = st.columns(2)

with col1:
    # format="%d" remove as casas decimais da exibição padrão
    num1 = st.number_input(
        "Digite o primeiro número:", value=0.0, format="%.0f"
    )

with col2:
    num2 = st.number_input(
        "Digite o segundo número:", value=0.0, format="%.0f"
    )

# Escolha da operação
operacao = st.radio(
    "Escolha a operação desejada:",
    ["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)"],
    horizontal=True,
)

st.markdown("---")

# Botão de ação
if st.button("Calcular", type="primary", use_container_width=True):
  # Lógica do cálculo
  if operacao == "Soma (+)":
    resultado = num1 + num2
    st.success(f"O resultado da soma é: **{resultado}**")

  elif operacao == "Subtração (-)":
    resultado = num1 - num2
    st.success(f"O resultado da subtração é: **{resultado}**")

  elif operacao == "Multiplicação (*)":
    resultado = num1 * num2
    st.success(f"O resultado da multiplicação é: **{resultado}**")

  elif operacao == "Divisão (/)":
    if num2 == 0:
      st.error(
          "🚨 Erro matemático: Não é possível realizar uma divisão por zero!"
      )
    else:
      resultado = num1 / num2
      st.success(f"O resultado da divisão é: **{resultado}**")
