#!/usr/bin/env python3
"""
🎯 EXERCÍCIO 1: Configuração Básica
Objetivo: Entender como funciona a configuração do agente
"""

import os
import sys
sys.path.append('../backend/src')

from agent.configuration import Configuration
from agent.state import OverallState
from langchain_core.messages import HumanMessage

def exercicio_1_configuracao():
    """Teste básico de configuração"""
    print("🔧 EXERCÍCIO 1: Configuração Básica")
    print("=" * 50)
    
    # 1. Configuração padrão
    config_padrao = Configuration()
    print(f"📊 Configuração Padrão:")
    print(f"  - Modelo gerador: {config_padrao.query_generator_model}")
    print(f"  - Modelo reflexão: {config_padrao.reflection_model}")
    print(f"  - Modelo resposta: {config_padrao.answer_model}")
    print(f"  - Queries iniciais: {config_padrao.number_of_initial_queries}")
    print(f"  - Loops máximos: {config_padrao.max_research_loops}")
    
    # 2. Configuração customizada
    print(f"\n🎛️ Configuração Customizada:")
    config_custom = Configuration(
        number_of_initial_queries=5,
        max_research_loops=3,
        query_generator_model="gemini-2.5-flash"
    )
    print(f"  - Queries iniciais: {config_custom.number_of_initial_queries}")
    print(f"  - Loops máximos: {config_custom.max_research_loops}")
    print(f"  - Modelo gerador: {config_custom.query_generator_model}")
    
    return config_padrao, config_custom

def exercicio_2_estado():
    """Teste básico de estados"""
    print("\n📊 EXERCÍCIO 2: Estados do Agente")
    print("=" * 50)
    
    # Criar estado inicial
    estado_inicial = {
        "messages": [HumanMessage(content="What is artificial intelligence?")],
        "search_query": [],
        "web_research_result": [],
        "sources_gathered": [],
        "initial_search_query_count": 3,
        "max_research_loops": 2,
        "research_loop_count": 0,
        "reasoning_model": "gemini-2.5-pro"
    }
    
    print(f"💬 Mensagem inicial: {estado_inicial['messages'][0].content}")
    print(f"🔍 Queries iniciais: {estado_inicial['initial_search_query_count']}")
    print(f"🔄 Loops máximos: {estado_inicial['max_research_loops']}")
    print(f"🤖 Modelo reasoning: {estado_inicial['reasoning_model']}")
    
    return estado_inicial

def exercicio_3_validacao_api():
    """Valida se a API key está configurada"""
    print("\n🔑 EXERCÍCIO 3: Validação API Key")
    print("=" * 50)
    
    from dotenv import load_dotenv
    load_dotenv()
    
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        print("✅ API Key encontrada!")
        print(f"🔐 Primeiros caracteres: {api_key[:10]}...")
        return True
    else:
        print("❌ API Key não encontrada!")
        print("💡 Crie um arquivo .env na pasta backend/ com:")
        print("   GEMINI_API_KEY=sua_chave_aqui")
        return False

if __name__ == "__main__":
    print("🎓 EXERCÍCIOS PRÁTICOS - CONFIGURAÇÃO E ESTADOS")
    print("=" * 60)
    
    # Execute os exercícios
    config_padrao, config_custom = exercicio_1_configuracao()
    estado = exercicio_2_estado()
    api_valida = exercicio_3_validacao_api()
    
    print(f"\n📋 RESUMO:")
    print(f"✅ Configuração padrão criada")
    print(f"✅ Configuração custom criada")
    print(f"✅ Estado inicial simulado")
    print(f"{'✅' if api_valida else '❌'} API Key {'válida' if api_valida else 'inválida'}")
    
    print(f"\n🚀 PRÓXIMO PASSO:")
    if api_valida:
        print("Execute: python 02_prompts_ia.py")
    else:
        print("Configure sua GEMINI_API_KEY primeiro!")