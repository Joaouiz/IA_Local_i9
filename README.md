# Chatbot Inteligente para Startup de Energia Sustentável

Este projeto consiste em um chatbot baseado em Inteligência Artificial capaz de responder perguntas sobre uma startup que atua com reciclagem de baterias de veículos elétricos.

---

## Funcionalidades

*  Respostas automáticas baseadas em conteúdo da empresa
*  Uso de modelos de linguagem locais (LLM)
*  Execução offline (sem necessidade de API paga)
*  Suporte a múltiplos modelos offline(leve e avançado)
*  Opção entre o uso de API online e offline

---

## Tecnologias Utilizadas

* Python
* Flask
* Flask-CORS
* Requests
* Ollama (execução de modelos locais)
* ChatGPT
* Google AI Studio / Gemini

---

## Modelos de IA

O sistema suporta diferentes modelos offline, permitindo adaptação conforme o hardware disponível:

* **tinyllama** → leve e rápido, mas é uma bosta.
* **mistral** → mais preciso, mas pesa muito, muito MESMO.

Para alternar entre modelos, basta modificar a variável no código:

```python
# MODEL_LOCAL = "tinyllama"
MODEL_LOCAL = "mistral"
```

E para o uso da API online(recomendado) basta definir "True" ou "False", na linha a seguir:
```python
USAR_API = True  # True = Gemini | False = Ollama
```

---

## Como Executar o Projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Joaouiz/IA_Local_i9.git
cd IA_Local_i9
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

<details>
<summary>  Usar IA Local (Ollama)</summary>
  
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
python main.py
```

O servidor será iniciado localmente, basta abrir o .html com um navegador para usar a IA.

---
</details>

<details>
<summary>  Usar IA Online (Gemini)</summary>

### 4. Gerar a key para a utilização da API
No site:
```bash
https://aistudio.google.com/api-keys
```

---

### 5. Colar a key

Coloque a key gerada na seguinte linha do código:
```python
GEMINI_API_KEY = "Tua key aqui!"
```

---

### 6. Executar o servidor

```bash
python main.py
```

O servidor será iniciado, basta abrir o .html com um navegador para usar a IA.

</details>

## Integração com Frontend

O ChatGPT fez um HTML pra testar direto na web a IA, não irei me aprofundar aqui porque eu realmente não possuo conhecimento nessa área.

---

## Observações

* O desempenho depende do modelo utilizado e do hardware disponível
* Modelos maiores podem consumir mais memória e serem mais lentos
* O uso da API do Google é extremamente limitada com o plano grátis, para um uso mais massivo recomendo analisar os planos oferecidos pela plataforma.
