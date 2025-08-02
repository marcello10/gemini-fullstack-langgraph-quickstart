# 🎓 Exercícios Práticos - Agente LangGraph + Gemini

Este diretório contém exercícios práticos progressivos para estudar e dominar o agente de pesquisa inteligente construído com LangGraph e Google Gemini.

## 📋 Estrutura dos Exercícios

### 1️⃣ **01_configuracao_basica.py**
**Objetivo**: Entender configurações e estados básicos

🎯 **O que você vai aprender**:
- Como funciona a classe `Configuration`
- Estrutura dos estados do agente
- Validação de API Key
- Criação de estados iniciais

⏱️ **Tempo estimado**: 15 minutos

```bash
python 01_configuracao_basica.py
```

---

### 2️⃣ **02_prompts_ia.py** 
**Objetivo**: Compreender prompts e IA generativa

🎯 **O que você vai aprender**:
- 4 tipos de prompts do sistema
- Formatação de prompts com variáveis
- Extração de tópicos de conversação
- Estrutura de instruções para LLMs

⏱️ **Tempo estimado**: 20 minutos

```bash
python 02_prompts_ia.py
```

---

### 3️⃣ **03_grafo_estados.py**
**Objetivo**: Entender a arquitetura LangGraph

🎯 **O que você vai aprender**:
- Estrutura do grafo de estados
- Fluxo de execução entre nós
- Diferentes tipos de estado
- Simulação do pipeline

⏱️ **Tempo estimado**: 25 minutos

```bash
python 03_grafo_estados.py
```

---

### 4️⃣ **04_execucao_real.py**
**Objetivo**: Executar o agente completo

🎯 **O que você vai aprender**:
- Execução real do agente
- Análise de resultados
- Comparação de configurações
- Debugging e otimização

⏱️ **Tempo estimado**: 30-45 minutos
⚠️ **Requer**: GEMINI_API_KEY configurada

```bash
python 04_execucao_real.py
```

---

### 5️⃣ **05_customizacoes.py**
**Objetivo**: Personalizar e experimentar

🎯 **O que você vai aprender**:
- Criação de prompts personalizados
- Configurações especializadas
- Agentes para domínios específicos
- Métricas customizadas
- Ideias para desenvolvimento futuro

⏱️ **Tempo estimado**: 40 minutos

```bash
python 05_customizacoes.py
```

---

## 🚀 Como Começar

### Pré-requisitos
1. **Python 3.11+**
2. **Dependências instaladas**: `pip install .` na pasta backend/
3. **API Key do Gemini**: Configure no arquivo `.env`

### Configuração Inicial
```bash
# 1. Navegue para o diretório
cd exercicios_praticos/

# 2. Configure a API Key (necessário para exercícios 4 e 5)
echo "GEMINI_API_KEY=sua_chave_aqui" > ../backend/.env

# 3. Execute os exercícios em ordem
python 01_configuracao_basica.py
python 02_prompts_ia.py
python 03_grafo_estados.py
python 04_execucao_real.py    # Requer API Key
python 05_customizacoes.py    # Requer API Key
```

---

## 📊 Progressão de Aprendizado

```
Iniciante    Intermediário    Avançado
    |             |             |
    v             v             v
Ex 1 → Ex 2 → Ex 3 → Ex 4 → Ex 5
```

### 🟢 **Nível Iniciante** (Exercícios 1-2)
- Conceitos básicos
- Configuração e setup
- Estrutura de dados
- Prompts e formatação

### 🟡 **Nível Intermediário** (Exercício 3)
- Arquitetura LangGraph
- Fluxo de estados
- Pipeline de execução
- Debugging básico

### 🔴 **Nível Avançado** (Exercícios 4-5)
- Execução real
- Análise de performance
- Customizações avançadas
- Desenvolvimento futuro

---

## 🎯 Objetivos de Aprendizado

### Após completar todos os exercícios, você será capaz de:

✅ **Configurar e executar** o agente LangGraph
✅ **Entender a arquitetura** de grafos de estados
✅ **Modificar prompts** para diferentes domínios
✅ **Customizar configurações** para casos específicos
✅ **Analisar resultados** e métricas de performance
✅ **Criar agentes especializados** para suas necessidades
✅ **Debuggar e otimizar** execuções
✅ **Planejar desenvolvimentos** futuros

---

## 🔧 Dicas de Estudo

### 💡 **Dicas Gerais**
- Execute os exercícios **em ordem**
- Leia os comentários no código
- Experimente **modificar parâmetros**
- **Documente suas descobertas**
- Teste com **suas próprias perguntas**

### 🐛 **Debugging**
- Use `print()` para acompanhar execução
- Analise logs de erro cuidadosamente
- Teste com configurações menores primeiro
- Verifique sua API Key se houver erros

### ⚡ **Otimização**
- Comece com `max_research_loops=1`
- Use `initial_search_query_count=2` para testes
- Escolha modelos mais rápidos para experimentação
- Salve resultados para análise posterior

---

## 📚 Recursos Adicionais

### 📖 **Documentação**
- [LangGraph Concepts](https://langchain-ai.github.io/langgraph/concepts/)
- [Google Gemini API](https://ai.google.dev/docs)
- [LangChain Agents](https://python.langchain.com/docs/use_cases/autonomous_agents/)

### 🎥 **Tutoriais**
- [LangGraph YouTube Playlist](https://youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x)
- [Building AI Agents](https://www.deeplearning.ai/short-courses/)

### 💬 **Comunidade**
- [LangChain Discord](https://discord.gg/langchain)
- [Reddit r/LangChain](https://reddit.com/r/LangChain)
- [GitHub Discussions](https://github.com/langchain-ai/langgraph/discussions)

---

## 🎖️ Certificação Informal

Após completar todos os exercícios, você pode se considerar **proficiente** em:

- ✅ Agentes LangGraph
- ✅ Integração com Google Gemini  
- ✅ Desenvolvimento de sistemas de pesquisa inteligente
- ✅ Customização de agentes de IA

---

## 🚀 Próximos Passos

1. **Complete todos os exercícios**
2. **Implemente suas próprias modificações**
3. **Crie um agente para seu domínio específico**
4. **Contribua com melhorias para o projeto**
5. **Compartilhe seu conhecimento com a comunidade**

---

**Boa sorte nos seus estudos! 🎉**

*Se tiver dúvidas, consulte a documentação ou entre em contato com a comunidade.*