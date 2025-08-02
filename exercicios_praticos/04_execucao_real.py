#!/usr/bin/env python3
"""
🎯 EXERCÍCIO 4: Execução Real do Agente
Objetivo: Executar o agente completo e analisar resultados
ATENÇÃO: Requer GEMINI_API_KEY configurada!
"""

import os
import sys
import time
import json
sys.path.append('../backend/src')

from agent.graph import graph
from agent.configuration import Configuration
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv

def verificar_prerequisites():
    """Verifica se todos os pré-requisitos estão atendidos"""
    print("🔍 VERIFICANDO PRÉ-REQUISITOS")
    print("=" * 40)
    
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        print("❌ GEMINI_API_KEY não encontrada!")
        print("💡 Para configurar:")
        print("   1. Obtenha uma chave em: https://ai.google.dev/")
        print("   2. Crie arquivo .env na pasta backend/")
        print("   3. Adicione: GEMINI_API_KEY=sua_chave_aqui")
        return False
    
    print(f"✅ API Key encontrada: {api_key[:10]}...")
    
    try:
        from google.genai import Client
        client = Client(api_key=api_key)
        print("✅ Cliente Gemini inicializado")
        return True
    except Exception as e:
        print(f"❌ Erro ao inicializar cliente: {e}")
        return False

def exercicio_1_execucao_simples():
    """Execute o agente com pergunta simples"""
    print("\n🚀 EXERCÍCIO 1: Execução Simples")
    print("=" * 40)
    
    pergunta = "What is artificial intelligence?"
    
    print(f"❓ Pergunta: {pergunta}")
    print(f"⏳ Executando agente...")
    
    # Estado inicial simplificado
    estado = {
        "messages": [HumanMessage(content=pergunta)],
        "initial_search_query_count": 2,  # Reduzido para teste rápido
        "max_research_loops": 1,  # Apenas 1 loop para teste
        "reasoning_model": "gemini-2.0-flash"
    }
    
    inicio = time.time()
    
    try:
        resultado = graph.invoke(estado)
        fim = time.time()
        
        print(f"✅ Execução concluída em {fim - inicio:.2f}s")
        print(f"📊 Análise do resultado:")
        
        # Analise o resultado
        if "messages" in resultado and resultado["messages"]:
            ultima_mensagem = resultado["messages"][-1]
            print(f"  - Tipo da resposta: {ultima_mensagem.type}")
            print(f"  - Tamanho da resposta: {len(ultima_mensagem.content)} chars")
            print(f"  - Início da resposta: {ultima_mensagem.content[:100]}...")
        
        if "search_query" in resultado:
            print(f"  - Queries geradas: {len(resultado['search_query'])}")
            print(f"  - Queries: {resultado['search_query']}")
        
        if "sources_gathered" in resultado:
            print(f"  - Fontes coletadas: {len(resultado['sources_gathered'])}")
        
        if "research_loop_count" in resultado:
            print(f"  - Loops executados: {resultado['research_loop_count']}")
        
        return resultado
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        print(f"💡 Verifique se sua API key está válida")
        return None

def exercicio_2_execucao_detalhada():
    """Execute com configuração mais detalhada"""
    print("\n🔬 EXERCÍCIO 2: Execução Detalhada")
    print("=" * 45)
    
    pergunta = "What are the latest developments in renewable energy in 2024?"
    
    print(f"❓ Pergunta: {pergunta}")
    
    # Configuração mais robusta
    estado = {
        "messages": [HumanMessage(content=pergunta)],
        "initial_search_query_count": 3,
        "max_research_loops": 2,
        "reasoning_model": "gemini-2.5-pro"
    }
    
    print(f"⚙️ Configuração:")
    print(f"  - Queries iniciais: {estado['initial_search_query_count']}")
    print(f"  - Loops máximos: {estado['max_research_loops']}")
    print(f"  - Modelo: {estado['reasoning_model']}")
    
    print(f"⏳ Executando (pode levar alguns minutos)...")
    
    inicio = time.time()
    
    try:
        resultado = graph.invoke(estado)
        fim = time.time()
        
        print(f"✅ Execução concluída em {fim - inicio:.2f}s")
        
        # Análise detalhada
        analise_resultado_detalhada(resultado)
        
        return resultado
        
    except Exception as e:
        print(f"❌ Erro na execução: {e}")
        return None

def analise_resultado_detalhada(resultado):
    """Analisa resultado em detalhes"""
    print(f"\n📊 ANÁLISE DETALHADA DO RESULTADO:")
    print("=" * 50)
    
    # Mensagens
    if "messages" in resultado:
        print(f"💬 Mensagens: {len(resultado['messages'])}")
        for i, msg in enumerate(resultado["messages"]):
            print(f"  {i+1}. {msg.type}: {len(msg.content)} chars")
    
    # Queries de busca
    if "search_query" in resultado:
        print(f"\n🔍 Queries de Busca: {len(resultado['search_query'])}")
        for i, query in enumerate(resultado["search_query"]):
            print(f"  {i+1}. {query}")
    
    # Resultados de pesquisa
    if "web_research_result" in resultado:
        print(f"\n🌐 Resultados de Pesquisa: {len(resultado['web_research_result'])}")
        for i, res in enumerate(resultado["web_research_result"]):
            print(f"  {i+1}. {len(res)} chars")
    
    # Fontes coletadas
    if "sources_gathered" in resultado:
        print(f"\n📚 Fontes Coletadas: {len(resultado['sources_gathered'])}")
        fontes_unicas = set()
        for fonte in resultado["sources_gathered"]:
            if isinstance(fonte, dict) and "value" in fonte:
                fontes_unicas.add(fonte["value"])
        print(f"  - Fontes únicas: {len(fontes_unicas)}")
    
    # Estatísticas
    if "research_loop_count" in resultado:
        print(f"\n📈 Estatísticas:")
        print(f"  - Loops executados: {resultado['research_loop_count']}")
        
    # Resposta final
    if "messages" in resultado and resultado["messages"]:
        resposta_final = resultado["messages"][-1].content
        print(f"\n📝 Resposta Final:")
        print(f"  - Tamanho: {len(resposta_final)} caracteres")
        print(f"  - Tem citações: {'[' in resposta_final and '](' in resposta_final}")
        print(f"  - Prévia: {resposta_final[:200]}...")

def exercicio_3_comparar_configuracoes():
    """Compare diferentes configurações"""
    print("\n⚖️ EXERCÍCIO 3: Comparando Configurações")
    print("=" * 50)
    
    pergunta = "What is machine learning?"
    
    configuracoes = [
        {
            "nome": "Rápida",
            "config": {
                "initial_search_query_count": 1,
                "max_research_loops": 1,
                "reasoning_model": "gemini-2.0-flash"
            }
        },
        {
            "nome": "Padrão", 
            "config": {
                "initial_search_query_count": 3,
                "max_research_loops": 2,
                "reasoning_model": "gemini-2.5-flash"
            }
        }
    ]
    
    resultados = []
    
    for setup in configuracoes:
        print(f"\n🧪 Testando configuração: {setup['nome']}")
        
        estado = {
            "messages": [HumanMessage(content=pergunta)],
            **setup["config"]
        }
        
        inicio = time.time()
        
        try:
            resultado = graph.invoke(estado)
            fim = time.time()
            
            resultado_info = {
                "nome": setup["nome"],
                "tempo": fim - inicio,
                "queries": len(resultado.get("search_query", [])),
                "fontes": len(resultado.get("sources_gathered", [])),
                "loops": resultado.get("research_loop_count", 0),
                "tamanho_resposta": len(resultado["messages"][-1].content) if resultado.get("messages") else 0
            }
            
            resultados.append(resultado_info)
            
            print(f"  ✅ Tempo: {resultado_info['tempo']:.2f}s")
            print(f"  📊 Queries: {resultado_info['queries']}")
            print(f"  📚 Fontes: {resultado_info['fontes']}")
            print(f"  🔄 Loops: {resultado_info['loops']}")
            print(f"  📝 Resposta: {resultado_info['tamanho_resposta']} chars")
            
        except Exception as e:
            print(f"  ❌ Erro: {e}")
    
    # Comparação final
    if len(resultados) > 1:
        print(f"\n📊 COMPARAÇÃO FINAL:")
        print("=" * 30)
        for res in resultados:
            print(f"{res['nome']}: {res['tempo']:.2f}s, {res['queries']} queries, {res['fontes']} fontes")

def salvar_resultado(resultado, nome_arquivo="resultado_agente.json"):
    """Salva resultado para análise posterior"""
    if not resultado:
        return
    
    # Converter para formato serializável
    resultado_serializable = {}
    for chave, valor in resultado.items():
        if chave == "messages":
            resultado_serializable[chave] = [
                {"type": msg.type, "content": msg.content} 
                for msg in valor
            ]
        else:
            resultado_serializable[chave] = valor
    
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        json.dump(resultado_serializable, f, indent=2, ensure_ascii=False)
    
    print(f"\n💾 Resultado salvo em: {nome_arquivo}")

if __name__ == "__main__":
    print("🎓 EXERCÍCIOS PRÁTICOS - EXECUÇÃO REAL DO AGENTE")
    print("=" * 60)
    
    # Verificar pré-requisitos
    if not verificar_prerequisites():
        print("\n❌ Pré-requisitos não atendidos!")
        print("Configure a API key e tente novamente.")
        sys.exit(1)
    
    print(f"\n🚀 Iniciando exercícios de execução...")
    
    # Exercício 1: Simples
    print(f"\n" + "="*60)
    resultado1 = exercicio_1_execucao_simples()
    if resultado1:
        salvar_resultado(resultado1, "resultado_simples.json")
    
    # Perguntar se quer continuar
    continuar = input(f"\n🤔 Executar exercício 2 (mais lento)? [y/N]: ").strip().lower()
    if continuar == 'y':
        resultado2 = exercicio_2_execucao_detalhada()
        if resultado2:
            salvar_resultado(resultado2, "resultado_detalhado.json")
    
    # Perguntar se quer comparar
    comparar = input(f"\n🤔 Executar comparação de configurações? [y/N]: ").strip().lower()
    if comparar == 'y':
        exercicio_3_comparar_configuracoes()
    
    print(f"\n🎉 EXERCÍCIOS CONCLUÍDOS!")
    print(f"💡 PRÓXIMOS PASSOS:")
    print(f"  1. Analise os arquivos JSON gerados")
    print(f"  2. Execute: python 05_customizacoes.py")
    print(f"  3. Experimente suas próprias perguntas!")