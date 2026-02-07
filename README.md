# 🍒 AI Resume Optimizer | Edição Dark Cherry

Este projeto é um otimizador e gerador de currículos **ATS-first**, desenvolvido para profissionais que desejam controle total sobre sua apresentação. Ele utiliza IA para alinhar seu currículo a vagas específicas, eliminando a dependência de editores pagos.

O sistema utiliza o modelo **Meta Llama 3.3** via OpenRouter para analisar lacunas, sugerir melhorias e gerar um documento limpo e profissional.

> *Sem assinaturas. Sem marcas d'água. Sem retenção de dados.*

---

## 🚀 Por que este projeto existe?

Muitos construtores de currículos online:
* 💰 **Cobram caro** para liberar funções básicas de exportação em PDF.
* 🎨 **Priorizam design sobre função**, gerando layouts que os sistemas **ATS** não conseguem ler.
* 🤖 **Dão feedbacks genéricos** que não ajudam a passar em uma vaga específica.

---

## 🛠️ Como funciona?

1.  **Entrada:** Cole seu currículo e a descrição da vaga desejada no dashboard.
2.  **Otimização:** A IA analisa palavras-chave e reescreve experiências focando em resultados.
3.  **Refinamento:** Use o **Editor Dark Cherry** (com suporte a Markdown) para ajustes manuais.
4.  **Exportação:** Gere um PDF pronto para aplicação, otimizado para sistemas de RH.

---

# ⚙️ Instalação e Configuração
1. Requisitos
 - Python 3.9+
 - Uma chave de API do OpenRouter
   
2. Configurando o Ambiente
```bash
# Clone o repositório
git clone https://github.com/johnvrnas/ai-resume-optimizer.git
cd ai-resume-optimizer

# Crie e ative um ambiente virtual
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/activate

# Instale as dependências
pip install -r requirements.txt
```

3. Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto
```
OPENROUTER_API_KEY=sua_chave_aqui
```

---

# Modo de usar

1. Inicie o Servidor Backend:
```bash
python backend/main.py
```
2. Acesse a interface: Basta abrir o arquivo frontend/index.html em seu navegador.
3. Fluxo de Operação:
- Insira seus dados.
- CLique em "Otimizar Currículo".
- Confira o Match Score e edite o texto se necessário.
- Clique em "Baixa PDF Final".

---

# Detalhes do Output (PDF)
- Encoding - Latin-1 (Acentuação perfeita em PT-BR)
- Layout - ATS-Friendly (Coluna única)
- Tipografia - Helvetica (Legível por softwares de RH)

---

Feito por João Victor Rodrigues do Nascimento
  
