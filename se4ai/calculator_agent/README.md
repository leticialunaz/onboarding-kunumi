## Configuração do ambiente

### 1. Ambiente virtual

Criei e ativei um ambiente virtual (`venv`) para isolar as dependências do projeto:

```bash
python -m venv venv
```

# Linux/macOS
source venv/bin/activate


### 2. Instalação das dependências

Com o ambiente virtual ativo, instalei as bibliotecas necessárias:

```bash
pip install -U langgraph langchain langchain-google-genai
```

### 3. Chave de API

Em vez da chave da Anthropic usada no tutorial original, usei uma chave gratuita da API do Google (Gemini), gerada no [Google AI Studio](https://aistudio.google.com).

A chave fica numa variável de ambiente:

```bash
export GOOGLE_API_KEY="sua-chave-aqui"
```