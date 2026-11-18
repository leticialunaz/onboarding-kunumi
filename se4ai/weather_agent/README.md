# Onboarding LangGraph Agent

Projeto de exemplo de um agente conversacional assíncrono com LangGraph e
LangChain. O agente usa o modelo `gpt-4.1-mini` e pode chamar uma ferramenta de
consulta de clima.

## Requisitos

- Python 3.10 ou superior
- Git
- Uma chave de API da OpenAI

## Configuração

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/leticialunaz/onboarding-kunumi.git
cd onboarding-kunumi/se4ai
```

Crie e ative um ambiente virtual. No Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
python -m pip install -r requirements.txt
```

Crie um arquivo `.env` nesta pasta com sua chave da OpenAI:

```dotenv
OPENAI_API_KEY=sua-chave-aqui
```

O arquivo `.env` está listado no `.gitignore`; não compartilhe nem versione sua
chave de API.

## Executar

Para iniciar a demonstração do agente:

```bash
python -m tests.test_agent
```

O script envia uma mensagem ao modelo e imprime a resposta. É necessária uma
chave válida da OpenAI, e a execução pode consumir créditos da API.

Para executar a ferramenta de clima isoladamente, sem chamar o modelo:

```bash
python -m tests.test_tools
```

## Como funciona

- `agent.py` configura o modelo, o prompt e o fluxo do grafo: o agente pode
  responder diretamente ou chamar a ferramenta e então retornar ao modelo.
- `state.py` define o estado de conversação, acumulando as mensagens do usuário,
  do agente e das ferramentas.
- `tools.py` define `get_current_weather`, a ferramenta disponível para o agente.

**Limitação da demonstração:** `get_current_weather` não consulta um serviço
meteorológico. Ela retorna uma resposta fixa ("sunny, 72°F") para a localização
informada; portanto, não deve ser usada como previsão real.

Os arquivos em `tests/` são scripts demonstrativos executáveis, não uma suíte de
testes automatizada. Em particular, `test_agent.py` faz uma chamada real à API
da OpenAI, que é paga.
