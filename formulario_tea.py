import streamlit as st

st.set_page_config(page_title="Avaliação TEA", layout="centered")

st.title("📋 Formulário de Avaliação Inicial – Crianças com TEA")

# --- INFORMAÇÕES BÁSICAS ---
st.header("👤 Informações da Criança")
nome = st.text_input("Nome da Criança")
idade = st.number_input("Idade", min_value=0, max_value=20, step=1)
sexo = st.radio("Sexo", ["Masculino", "Feminino"])
data = st.date_input("Data da Avaliação")
profissional = st.text_input("Nome do Profissional")
cargo = st.text_input("Cargo/Função")

st.markdown("---")

# Função para somar e exibir resultado
def bloco_avaliacao(nome_grupo, perguntas):
    st.subheader(nome_grupo)
    total = 0
    for pergunta in perguntas:
        nota = st.slider(pergunta, 1, 5, 3)
        total += nota
    prioridade = "Baixa"
    if total >= 20:
        prioridade = "Alta"
    elif total >= 14:
        prioridade = "Média"
    st.success(f"Total: {total}/25 — Prioridade: {prioridade}")
    return total, prioridade

# --- GRUPOS DE AVALIAÇÃO ---
total_sociais, p1 = bloco_avaliacao("🧩 Habilidades Sociais", [
    "Inicia interações sociais espontaneamente?",
    "Mantém contato visual durante interações?",
    "Demonstra interesse em compartilhar atividades?",
    "Compreende regras básicas de convivência?",
    "Demonstra empatia com os outros?"
])

total_sensorial, p2 = bloco_avaliacao("🧠 Estimulação Sensorial e Motora", [
    "Apresenta sensibilidade a estímulos (sons, luzes, texturas)?",
    "Tem dificuldade em coordenação motora fina?",
    "Tem dificuldade em coordenação motora grossa?",
    "Reage com agitação ou isolamento a estímulos?",
    "Consegue manter controle do corpo em atividades?"
])

total_comunicacao, p3 = bloco_avaliacao("💬 Comunicação Alternativa", [
    "Utiliza comunicação verbal ou não verbal?",
    "Expressa desejos e necessidades?",
    "Compreende comandos simples?",
    "Usa gestos, figuras ou dispositivos de comunicação?",
    "Necessita apoio constante para se comunicar?"
])

total_avd, p4 = bloco_avaliacao("🧼 Atividades da Vida Diária (AVD)", [
    "Participa das rotinas básicas (alimentação, higiene)?",
    "Precisa de ajuda total para atividades cotidianas?",
    "Mostra iniciativa em pequenas tarefas?",
    "Resiste em aprender rotinas?",
    "Tem autonomia compatível com a idade?"
])

total_familiar, p5 = bloco_avaliacao("🧍‍♀️ Apoio Familiar", [
    "Família compreende o diagnóstico?",
    "Família relata sobrecarga emocional ou física?",
    "Responsáveis participam das orientações?",
    "Dificuldade em aplicar rotinas terapêuticas em casa?",
    "Possui rede de apoio adequada?"
])

# --- RESUMO FINAL ---
st.markdown("---")
st.header("📊 Resumo Final")

st.markdown(f"""
**Habilidades Sociais:** {total_sociais}/25 — **{p1}**  
**Sensorial e Motora:** {total_sensorial}/25 — **{p2}**  
**Comunicação Alternativa:** {total_comunicacao}/25 — **{p3}**  
**AVD:** {total_avd}/25 — **{p4}**  
**Apoio Familiar:** {total_familiar}/25 — **{p5}**
""")

# Exportar ou salvar?
if st.button("📥 Salvar Avaliação (em CSV)"):
    import pandas as pd
    df = pd.DataFrame([{
        "Nome": nome,
        "Idade": idade,
        "Sexo": sexo,
        "Data": str(data),
        "Profissional": profissional,
        "Cargo": cargo,
        "Sociais": total_sociais,
        "Sensorial": total_sensorial,
        "Comunicação": total_comunicacao,
        "AVD": total_avd,
        "Familiar": total_familiar
    }])
    df.to_csv(f"avaliacao_{nome.replace(' ', '_')}.csv", index=False)
    st.success("Arquivo salvo com sucesso!")

