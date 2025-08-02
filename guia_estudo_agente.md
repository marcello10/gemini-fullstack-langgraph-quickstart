# 🎓 Guia de Estudo: Agente de Pesquisa LangGraph + Gemini

## 📋 Visão Geral do Projeto

Este é um agente de pesquisa inteligente que:
- ✅ Gera queries de busca otimizadas
- ✅ Realiza pesquisa web usando Google Search API
- ✅ Reflete sobre resultados e identifica lacunas
- ✅ Sintetiza resposta final com citações

## 🏗️ Arquitetura Principal

```
backend/src/agent/
├── graph.py          # ⭐ NÚCLEO: Grafo de estados LangGraph
├── state.py          # 📊 Estados e tipos de dados
├── configuration.py  # ⚙️ Configurações do agente
├── prompts.py        # 🎯 Prompts para IA generativa
├── tools_and_schemas.py # 🛠️ Schemas estruturados
├── utils.py          # 🔧 Utilitários e citações
└── app.py           # 🚀 FastAPI server
```

## 📚 Plano de Estudo Prático

### 1️⃣ **PRIMEIRO PASSO: Executar o Exemplo**

```bash
# Configurar ambiente
cd backend
pip install .

# Criar .env com sua GEMINI_API_KEY
echo "GEMINI_API_KEY=sua_chave_aqui" > .env

# Testar o agente
python examples/cli_research.py "What are the latest trends in renewable energy?"
```

**🎯 Objetivo**: Ver o agente funcionando antes de estudar o código

---

### 2️⃣ **ENTENDER OS ESTADOS (state.py)**

#### Estados Principais:
- **OverallState**: Estado global do agente
- **QueryGenerationState**: Para geração de queries
- **WebSearchState**: Para pesquisa web
- **ReflectionState**: Para reflexão e análise

#### 💡 Exercício Prático:
```python
# Teste no Python REPL
from agent.state import OverallState
from langchain_core.messages import HumanMessage

# Simule um estado inicial
state = {
    "messages": [HumanMessage(content="What is AI?")],
    "search_query": [],
    "web_research_result": [],
    "sources_gathered": [],
    "initial_search_query_count": 3,
    "max_research_loops": 2,
    "research_loop_count": 0,
    "reasoning_model": "gemini-2.5-pro"
}
```

---

### 3️⃣ **ESTUDAR CONFIGURAÇÃO (configuration.py)**

#### Parâmetros Configuráveis:
- **query_generator_model**: "gemini-2.0-flash"
- **reflection_model**: "gemini-2.5-flash" 
- **answer_model**: "gemini-2.5-pro"
- **number_of_initial_queries**: 3
- **max_research_loops**: 2

#### 💡 Exercício Prático:
```python
from agent.configuration import Configuration

# Teste diferentes configurações
config = Configuration(
    max_research_loops=5,
    number_of_initial_queries=5
)
print(f"Loops máximos: {config.max_research_loops}")
print(f"Queries iniciais: {config.number_of_initial_queries}")
```

---

### 4️⃣ **ANALISAR PROMPTS (prompts.py)**

#### 4 Tipos de Prompts:

1. **query_writer_instructions**: Gera queries de busca
2. **web_searcher_instructions**: Dirige a pesquisa web
3. **reflection_instructions**: Analisa resultados
4. **answer_instructions**: Sintetiza resposta final

#### 💡 Exercício Prático:
```python
from agent.prompts import query_writer_instructions, get_current_date

# Teste formatação de prompt
current_date = get_current_date()
formatted_prompt = query_writer_instructions.format(
    current_date=current_date,
    research_topic="Latest AI developments",
    number_queries=3
)
print(formatted_prompt)
```

---

### 5️⃣ **COMPREENDER O GRAFO (graph.py)**

#### Fluxo de Execução:
```
START → generate_query → web_research → reflection → finalize_answer → END
                            ↑              ↓
                            └── (se insuficiente)
```

#### Nós Principais:

##### 🔍 **generate_query()**
```python
# O que faz:
# 1. Recebe pergunta do usuário
# 2. Usa Gemini 2.0 Flash para gerar queries
# 3. Retorna lista de queries otimizadas
```

##### 🌐 **web_research()**  
```python
# O que faz:
# 1. Executa busca usando Google Search API
# 2. Processa resultados com grounding metadata
# 3. Gera citações e resolve URLs
```

##### 🤔 **reflection()**
```python
# O que faz:
# 1. Analisa resultados da pesquisa
# 2. Identifica lacunas de conhecimento
# 3. Decide se precisa mais pesquisa
# 4. Gera queries de follow-up se necessário
```

##### ✅ **finalize_answer()**
```python
# O que faz:
# 1. Sintetiza todos os resultados
# 2. Cria resposta final estruturada
# 3. Inclui citações apropriadas
```

#### 💡 Exercício Prático:
```python
# Teste nós individuais
from agent.graph import generate_query
from langchain_core.messages import HumanMessage

state = {
    "messages": [HumanMessage(content="What is quantum computing?")],
    "initial_search_query_count": 3
}

# Simule configuração (você precisará de uma API key válida)
# result = generate_query(state, config={})
# print(result)
```

---

### 6️⃣ **UTILITÁRIOS E CITAÇÕES (utils.py)**

#### Funções Importantes:

##### 🔗 **get_citations()**
```python
# Extrai citações da resposta do Gemini
# Cria links formatados para fontes
```

##### 🌐 **resolve_urls()**
```python
# Converte URLs longas em URLs curtas
# Mantém mapeamento para citações
```

##### 📝 **insert_citation_markers()**
```python
# Insere marcadores de citação no texto
# Formata como links markdown
```

#### 💡 Exercício Prático:
```python
from agent.utils import get_research_topic
from langchain_core.messages import HumanMessage, AIMessage

# Teste extração de tópico
messages = [
    HumanMessage(content="What is machine learning?"),
    AIMessage(content="Machine learning is..."),
    HumanMessage(content="Tell me more about neural networks")
]

topic = get_research_topic(messages)
print(f"Tópico extraído: {topic}")
```

---

## 🔬 Experimentos Avançados

### Experimento 1: Modificar Número de Queries
```python
# Teste com diferentes números de queries iniciais
for num_queries in [1, 3, 5]:
    print(f"\n=== Testando com {num_queries} queries ===")
    # Execute o agente com essa configuração
```

### Experimento 2: Diferentes Modelos
```python
# Teste diferentes modelos Gemini
models = ["gemini-2.0-flash", "gemini-2.5-flash", "gemini-2.5-pro"]
for model in models:
    print(f"\n=== Testando com {model} ===")
    # Execute com cada modelo
```

### Experimento 3: Customizar Prompts
```python
# Modifique prompts para domínios específicos
custom_prompt = """
Você é um especialista em tecnologia.
Gere queries técnicas específicas sobre: {research_topic}
...
"""
```

## 🎯 Desafios Práticos

### Desafio 1: Agente de Pesquisa Acadêmica
- Modifique prompts para buscar papers acadêmicos
- Adicione filtros por data de publicação
- Implemente citações no formato ABNT

### Desafio 2: Agente de Análise de Mercado
- Foque em dados financeiros e tendências
- Adicione análise de sentimentos
- Gere relatórios estruturados

### Desafio 3: Sistema de Verificação de Fatos
- Implemente verificação cruzada de fontes
- Adicione scoring de credibilidade
- Detecte informações contraditórias

## 📊 Métricas para Acompanhar

1. **Número de queries geradas**
2. **Número de loops de pesquisa**
3. **Qualidade das fontes encontradas**
4. **Tempo de execução total**
5. **Precisão das respostas**

## 🚀 Próximos Passos

1. **Entenda cada arquivo individualmente**
2. **Execute experimentos práticos**
3. **Modifique configurações gradualmente**
4. **Implemente suas próprias customizações**
5. **Crie novos tipos de agentes**

---

## 📚 Recursos Adicionais

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [Google Gemini API](https://ai.google.dev/docs)
- [LangChain Agents Guide](https://python.langchain.com/docs/use_cases/autonomous_agents/)

**Boa sorte nos seus estudos! 🎉**