import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meu Monitor financeiro", layout="centered")

st.title("📊 Monitor Financeiro Pessoal")

# --- SEÇÃO DE ENTRADAS ---
st.header("💰 Entradas (Renda)")
col1, col2 = st.columns(2)
with col1:
    salario = st.number_input("Salário Mensal", min_value=0.0, step=100.0)
with col2:
    freelance = st.number_input("Freelance / Extras", min_value=0.0, step=50.0)

total_entradas = salario + freelance

# --- SEÇÃO DE SAÍDAS ---
st.header("💸 Saídas (Contas)")

with st.expander("Contas de Casa", expanded=True):
    aluguel = st.number_input("Aluguel", min_value=0.0, step=50.0)
    agua = st.number_input("Água", min_value=0.0, step=10.0)
    luz = st.number_input("Luz (Força)", min_value=0.0, step=10.0)

with st.expander("Cartão e Outros"):
    cartao = st.number_input("Fatura do Cartão", min_value=0.0, step=10.0)
    outros = st.number_input("Outras Despesas", min_value=0.0, step=10.0)

total_saidas = aluguel + agua + luz + cartao + outros
saldo_final = total_entradas - total_saidas

---

# --- RESUMO FINAL ---
st.header("📝 Resumo do Mês")
c1, c2, c3 = st.columns(3)
c1.metric("Total Entradas", f"R$ {total_entradas:.2f}")
c2.metric("Total Saídas", f"R$ {total_saidas:.2f}", delta=f"-{total_saidas:.2f}", delta_color="inverse")
c3.metric("Saldo Livre", f"R$ {saldo_final:.2f}")

# Alerta de saúde financeira
if saldo_final < 0:
    st.error("Cuidado! Suas despesas superaram sua renda.")
elif saldo_final > 0:
    st.success("Parabéns! Você está terminando o mês no azul.")
