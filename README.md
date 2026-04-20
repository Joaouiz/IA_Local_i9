# Chatbot Inteligente para Startup de Energia Sustentável

Este projeto consiste em um chatbot baseado em Inteligência Artificial capaz de responder perguntas sobre uma startup que atua com reciclagem de baterias de veículos elétricos.

---

## Funcionalidades

*  Respostas automáticas baseadas em conteúdo da empresa
*  Uso de modelos de linguagem locais (LLM)
*  Execução offline (sem necessidade de API paga)
*  Suporte a múltiplos modelos (leve e avançado)

---

## Tecnologias Utilizadas

* Python
* Flask
* Flask-CORS
* Requests
* Ollama (execução de modelos locais)

---

## Modelos de IA

O sistema suporta diferentes modelos, permitindo adaptação conforme o hardware disponível:

* **tinyllama** → leve e rápido, mas é uma bosta.
* **mistral** → mais preciso, mas pesa muito, muito MESMO.

Para alternar entre modelos, basta modificar a variável no código:

```python
MODEL = "tinyllama"
# MODEL = "mistral"
```

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Joaouiz/IA_Local_i9.git
cd seu-repo
```

---

### 2. Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux
```

---

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

### 4. Instalar e iniciar o Ollama

Certifique-se de que o Ollama está instalado e rodando:

```bash
ollama run mistral
```

ou:

```bash
ollama run tinyllama
```

---

### 5. Executar o servidor

```bash
python app.py
```

O servidor será iniciado localmente, basta abrir o .html com um navegador para usar a IA.

---

## Integração com Frontend

Ti fode ai KKKKKKKKKKKKK

---

## Observações

* O desempenho depende do modelo utilizado e do hardware disponível
* Modelos maiores podem consumir mais memória e serem mais lentos
