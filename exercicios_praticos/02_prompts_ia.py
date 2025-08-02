#!/usr/bin/env python3
"""
🎯 EXERCÍCIO 2: Prompts e IA Generativa
Objetivo: Entender como funcionam os prompts do sistema
"""

import os
import sys
sys.path.append('../backend/src')

from agent.prompts import (
    query_writer_instructions,
    web_searcher_instructions, 
    reflection_instructions,
    answer_instructions,
    get_current_date
)
from agent.utils import get_research_topic
from langchain_core.messages import HumanMessage, AIMessage

def exercicio_1_data_atual():
    """Teste função de data atual"""
    print("📅 EXERCÍCIO 1: Data Atual")
    print("=" * 40)
    
    data_atual = get_current_date()
    print(f"📆 Data atual formatada: {data_atual}")
    return data_atual

def exercicio_2_prompt_queries():
    """Teste prompt de geração de queries"""
    print("\n🔍 EXERCÍCIO 2: Prompt de Geração de Queries")
    print("=" * 50)
    
    data_atual = get_current_date()
    topico_pesquisa = "What are the latest developments in quantum computing?"
    numero_queries = 3
    
    prompt_formatado = query_writer_instructions.format(
        current_date=data_atual,
        research_topic=topico_pesquisa,
        number_queries=numero_queries
    )
    
    print(f"📝 Tópico: {topico_pesquisa}")
    print(f"🔢 Número de queries: {numero_queries}")
    print(f"\n📋 Prompt formatado:")
    print("-" * 60)
    print(prompt_formatado[:500] + "..." if len(prompt_formatado) > 500 else prompt_formatado)
    print("-" * 60)
    
    return prompt_formatado

def exercicio_3_prompt_pesquisa():
    """Teste prompt de pesquisa web"""
    print("\n🌐 EXERCÍCIO 3: Prompt de Pesquisa Web")
    print("=" * 45)
    
    data_atual = get_current_date()
    topico_pesquisa = "machine learning applications in healthcare"
    
    prompt_pesquisa = web_searcher_instructions.format(
        current_date=data_atual,
        research_topic=topico_pesquisa
    )
    
    print(f"🎯 Tópico de pesquisa: {topico_pesquisa}")
    print(f"\n📋 Prompt de pesquisa:")
    print("-" * 40)
    print(prompt_pesquisa)
    print("-" * 40)
    
    return prompt_pesquisa

def exercicio_4_prompt_reflexao():
    """Teste prompt de reflexão"""
    print("\n🤔 EXERCÍCIO 4: Prompt de Reflexão")
    print("=" * 40)
    
    topico = "artificial intelligence trends"
    sumarios_simulados = [
        "AI is rapidly growing in healthcare applications...",
        "Machine learning models are becoming more efficient...",
        "Ethical concerns about AI deployment are increasing..."
    ]
    
    prompt_reflexao = reflection_instructions.format(
        research_topic=topico,
        summaries="\n\n---\n\n".join(sumarios_simulados)
    )
    
    print(f"🎯 Tópico: {topico}")
    print(f"📚 Número de sumários: {len(sumarios_simulados)}")
    print(f"\n📋 Prompt de reflexão:")
    print("-" * 40)
    print(prompt_reflexao[:400] + "..." if len(prompt_reflexao) > 400 else prompt_reflexao)
    print("-" * 40)
    
    return prompt_reflexao

def exercicio_5_extrair_topico():
    """Teste extração de tópico de conversação"""
    print("\n💬 EXERCÍCIO 5: Extração de Tópico")
    print("=" * 40)
    
    # Conversa simples
    print("📞 Conversa simples:")
    mensagens_simples = [HumanMessage(content="What is quantum computing?")]
    topico_simples = get_research_topic(mensagens_simples)
    print(f"  Mensagem: {mensagens_simples[0].content}")
    print(f"  Tópico extraído: {topico_simples}")
    
    # Conversa complexa
    print(f"\n📞 Conversa complexa:")
    mensagens_complexas = [
        HumanMessage(content="Tell me about AI"),
        AIMessage(content="AI is a field of computer science..."),
        HumanMessage(content="What about machine learning specifically?"),
        AIMessage(content="Machine learning is a subset of AI..."),
        HumanMessage(content="Can you give examples of ML in healthcare?")
    ]
    topico_complexo = get_research_topic(mensagens_complexas)
    print(f"  Número de mensagens: {len(mensagens_complexas)}")
    print(f"  Tópico extraído: {topico_complexo[:100]}...")
    
    return topico_simples, topico_complexo

def exercicio_6_prompt_resposta():
    """Teste prompt de resposta final"""
    print("\n✅ EXERCÍCIO 6: Prompt de Resposta Final")
    print("=" * 45)
    
    data_atual = get_current_date()
    topico = "renewable energy trends 2024"
    sumarios = [
        "Solar energy costs have decreased by 15% in 2024...",
        "Wind power installations reached record highs...",
        "Battery storage technology improved significantly..."
    ]
    
    prompt_resposta = answer_instructions.format(
        current_date=data_atual,
        research_topic=topico,
        summaries="\n---\n\n".join(sumarios)
    )
    
    print(f"🎯 Tópico: {topico}")
    print(f"📚 Sumários: {len(sumarios)} resultados")
    print(f"\n📋 Prompt de resposta:")
    print("-" * 40)
    print(prompt_resposta[:300] + "..." if len(prompt_resposta) > 300 else prompt_resposta)
    print("-" * 40)
    
    return prompt_resposta

if __name__ == "__main__":
    print("🎓 EXERCÍCIOS PRÁTICOS - PROMPTS E IA GENERATIVA")
    print("=" * 60)
    
    # Execute todos os exercícios
    data = exercicio_1_data_atual()
    prompt_queries = exercicio_2_prompt_queries()
    prompt_pesquisa = exercicio_3_prompt_pesquisa()
    prompt_reflexao = exercicio_4_prompt_reflexao()
    topico_simples, topico_complexo = exercicio_5_extrair_topico()
    prompt_resposta = exercicio_6_prompt_resposta()
    
    print(f"\n📋 RESUMO DOS EXERCÍCIOS:")
    print(f"✅ Data atual obtida: {data}")
    print(f"✅ Prompt de queries formatado ({len(prompt_queries)} chars)")
    print(f"✅ Prompt de pesquisa formatado ({len(prompt_pesquisa)} chars)")
    print(f"✅ Prompt de reflexão formatado ({len(prompt_reflexao)} chars)")
    print(f"✅ Tópicos extraídos: simples e complexo")
    print(f"✅ Prompt de resposta formatado ({len(prompt_resposta)} chars)")
    
    print(f"\n🚀 PRÓXIMO PASSO:")
    print("Execute: python 03_grafo_estados.py")
    
    print(f"\n💡 DICA:")
    print("Observe como cada prompt é estruturado e formatado.")
    print("Tente modificar os prompts para diferentes domínios!")