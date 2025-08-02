#!/usr/bin/env python3
"""
🎯 EXERCÍCIO 3: Grafo de Estados
Objetivo: Entender a estrutura e fluxo do grafo LangGraph
"""

import os
import sys
sys.path.append('../backend/src')

from agent.graph import graph
from agent.state import OverallState
from agent.configuration import Configuration
from langchain_core.messages import HumanMessage

def exercicio_1_estrutura_grafo():
    """Analise a estrutura do grafo"""
    print("🏗️ EXERCÍCIO 1: Estrutura do Grafo")
    print("=" * 40)
    
    print(f"📊 Informações do Grafo:")
    print(f"  - Nome: {graph.name}")
    print(f"  - Tipo: {type(graph).__name__}")
    
    # Nós do grafo
    if hasattr(graph, 'nodes'):
        print(f"  - Nós: {list(graph.nodes.keys())}")
    
    print(f"\n🔄 Fluxo de Execução:")
    print("  START → generate_query → web_research → reflection → finalize_answer → END")
    print("                             ↑              ↓")
    print("                             └── (se insuficiente)")
    
    return graph

def exercicio_2_configuracao_runnable():
    """Teste configuração runnable"""
    print("\n⚙️ EXERCÍCIO 2: Configuração Runnable")
    print("=" * 45)
    
    # Configuração padrão
    config_padrao = Configuration()
    print(f"🔧 Configuração Padrão:")
    print(f"  - Query model: {config_padrao.query_generator_model}")
    print(f"  - Reflection model: {config_padrao.reflection_model}")
    print(f"  - Answer model: {config_padrao.answer_model}")
    print(f"  - Initial queries: {config_padrao.number_of_initial_queries}")
    print(f"  - Max loops: {config_padrao.max_research_loops}")
    
    # Configuração customizada para teste
    config_teste = Configuration(
        number_of_initial_queries=2,
        max_research_loops=1,
        query_generator_model="gemini-2.0-flash"
    )
    print(f"\n🧪 Configuração de Teste:")
    print(f"  - Initial queries: {config_teste.number_of_initial_queries}")
    print(f"  - Max loops: {config_teste.max_research_loops}")
    print(f"  - Query model: {config_teste.query_generator_model}")
    
    return config_padrao, config_teste

def exercicio_3_estado_inicial():
    """Prepare estado inicial para execução"""
    print("\n📊 EXERCÍCIO 3: Estado Inicial")
    print("=" * 35)
    
    pergunta = "What are the benefits of renewable energy?"
    
    estado_inicial = {
        "messages": [HumanMessage(content=pergunta)],
        "search_query": [],
        "web_research_result": [],
        "sources_gathered": [],
        "initial_search_query_count": 2,  # Reduzido para teste
        "max_research_loops": 1,  # Reduzido para teste
        "research_loop_count": 0,
        "reasoning_model": "gemini-2.5-flash"
    }
    
    print(f"❓ Pergunta: {pergunta}")
    print(f"🔍 Queries iniciais: {estado_inicial['initial_search_query_count']}")
    print(f"🔄 Loops máximos: {estado_inicial['max_research_loops']}")
    print(f"🤖 Modelo: {estado_inicial['reasoning_model']}")
    
    print(f"\n📋 Estrutura do Estado:")
    for chave, valor in estado_inicial.items():
        if chave == "messages":
            print(f"  - {chave}: {len(valor)} mensagem(s)")
        elif isinstance(valor, list):
            print(f"  - {chave}: lista vazia ({len(valor)} itens)")
        else:
            print(f"  - {chave}: {valor}")
    
    return estado_inicial

def exercicio_4_tipos_estado():
    """Demonstre diferentes tipos de estado"""
    print("\n🏷️ EXERCÍCIO 4: Tipos de Estado")
    print("=" * 35)
    
    from agent.state import QueryGenerationState, WebSearchState, ReflectionState
    
    print("📁 Estados Disponíveis:")
    print("  1. OverallState - Estado global do agente")
    print("  2. QueryGenerationState - Para geração de queries")
    print("  3. WebSearchState - Para pesquisa web")
    print("  4. ReflectionState - Para reflexão e análise")
    
    # Simule diferentes estados
    query_state = {
        "search_query": [
            {"query": "renewable energy benefits", "rationale": "Main topic"},
            {"query": "solar wind power advantages", "rationale": "Specific types"}
        ]
    }
    
    web_state = {
        "search_query": "renewable energy benefits",
        "id": "1"
    }
    
    reflection_state = {
        "is_sufficient": False,
        "knowledge_gap": "Missing information about costs",
        "follow_up_queries": ["renewable energy costs 2024"],
        "research_loop_count": 1,
        "number_of_ran_queries": 2
    }
    
    print(f"\n🔍 QueryGenerationState exemplo:")
    print(f"  - Queries: {len(query_state['search_query'])}")
    
    print(f"\n🌐 WebSearchState exemplo:")
    print(f"  - Query: {web_state['search_query']}")
    print(f"  - ID: {web_state['id']}")
    
    print(f"\n🤔 ReflectionState exemplo:")
    print(f"  - Suficiente: {reflection_state['is_sufficient']}")
    print(f"  - Lacuna: {reflection_state['knowledge_gap']}")
    print(f"  - Follow-ups: {len(reflection_state['follow_up_queries'])}")
    
    return query_state, web_state, reflection_state

def exercicio_5_simulacao_fluxo():
    """Simule o fluxo sem executar"""
    print("\n🎭 EXERCÍCIO 5: Simulação de Fluxo")
    print("=" * 40)
    
    print("🎬 Simulando execução do agente:")
    print()
    
    # Etapa 1
    print("1️⃣ GENERATE_QUERY")
    print("   ├─ Recebe: 'What are the benefits of renewable energy?'")
    print("   ├─ Processa: Gemini 2.0 Flash gera queries")
    print("   └─ Retorna: ['renewable energy benefits', 'solar wind advantages']")
    print()
    
    # Etapa 2
    print("2️⃣ WEB_RESEARCH (paralelo para cada query)")
    print("   ├─ Query 1: 'renewable energy benefits'")
    print("   │   ├─ Executa: Google Search API")
    print("   │   └─ Resultado: Texto + citações")
    print("   ├─ Query 2: 'solar wind advantages'")
    print("   │   ├─ Executa: Google Search API")
    print("   │   └─ Resultado: Texto + citações")
    print("   └─ Combina: Todos os resultados")
    print()
    
    # Etapa 3
    print("3️⃣ REFLECTION")
    print("   ├─ Analisa: Resultados da pesquisa")
    print("   ├─ Decide: Informação suficiente?")
    print("   ├─ Se NÃO: Gera follow-up queries")
    print("   └─ Se SIM: Continua para finalização")
    print()
    
    # Etapa 4
    print("4️⃣ FINALIZE_ANSWER")
    print("   ├─ Sintetiza: Todos os resultados")
    print("   ├─ Formata: Resposta com citações")
    print("   └─ Retorna: Resposta final estruturada")
    print()
    
    print("🏁 FIM: Resposta completa entregue ao usuário")

def exercicio_6_verificar_api():
    """Verifica se pode executar o agente"""
    print("\n🔍 EXERCÍCIO 6: Verificação de API")
    print("=" * 40)
    
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    
    if api_key:
        print("✅ API Key encontrada!")
        print(f"🔐 Prefixo: {api_key[:10]}...")
        print("🚀 Você pode executar o agente completo!")
        return True
    else:
        print("❌ API Key não encontrada!")
        print("💡 Para executar o agente real:")
        print("   1. Obtenha uma chave em: https://ai.google.dev/")
        print("   2. Crie arquivo .env na pasta backend/")
        print("   3. Adicione: GEMINI_API_KEY=sua_chave_aqui")
        return False

if __name__ == "__main__":
    print("🎓 EXERCÍCIOS PRÁTICOS - GRAFO DE ESTADOS")
    print("=" * 55)
    
    # Execute os exercícios
    grafo = exercicio_1_estrutura_grafo()
    config_padrao, config_teste = exercicio_2_configuracao_runnable()
    estado_inicial = exercicio_3_estado_inicial()
    query_state, web_state, reflection_state = exercicio_4_tipos_estado()
    exercicio_5_simulacao_fluxo()
    api_disponivel = exercicio_6_verificar_api()
    
    print(f"\n📋 RESUMO:")
    print(f"✅ Estrutura do grafo analisada")
    print(f"✅ Configurações testadas")
    print(f"✅ Estado inicial preparado")
    print(f"✅ Tipos de estado demonstrados")
    print(f"✅ Fluxo simulado")
    print(f"{'✅' if api_disponivel else '❌'} API {'disponível' if api_disponivel else 'indisponível'}")
    
    print(f"\n🚀 PRÓXIMO PASSO:")
    if api_disponivel:
        print("Execute: python 04_execucao_real.py")
    else:
        print("Configure API key e depois execute: python 04_execucao_real.py")
    
    print(f"\n💡 DICA IMPORTANTE:")
    print("O grafo LangGraph executa os nós em ordem específica.")
    print("Cada nó recebe e modifica o estado global!")