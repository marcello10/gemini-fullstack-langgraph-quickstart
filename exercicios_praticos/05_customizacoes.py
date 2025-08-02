#!/usr/bin/env python3
"""
🎯 EXERCÍCIO 5: Customizações e Experimentos
Objetivo: Modificar e personalizar o agente para diferentes casos de uso
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
from agent.configuration import Configuration
from agent.graph import graph
from langchain_core.messages import HumanMessage

def exercicio_1_prompt_personalizado():
    """Crie prompts personalizados para domínios específicos"""
    print("🎨 EXERCÍCIO 1: Prompts Personalizados")
    print("=" * 45)
    
    # Prompt para pesquisa acadêmica
    prompt_academico = """Você é um assistente de pesquisa acadêmica especializado.
Sua tarefa é gerar consultas de pesquisa para artigos científicos e papers acadêmicos.

Instruções:
- Foque em termos técnicos e científicos
- Inclua anos recentes (2020-2024)
- Busque por papers peer-reviewed
- Use termos em inglês para melhor cobertura
- Prefira queries que encontrem artigos de revistas conceituadas

Tópico de pesquisa: {research_topic}
Data atual: {current_date}
Número de queries desejadas: {number_queries}

Formato da resposta:
{{
    "rationale": "Explicação técnica da estratégia de busca",
    "query": ["query1", "query2", "query3"]
}}

Contexto: {research_topic}"""

    # Prompt para análise de mercado
    prompt_mercado = """Você é um analista de mercado especializado em tendências comerciais.
Sua tarefa é gerar consultas para pesquisa de dados de mercado, tendências e oportunidades.

Instruções:
- Foque em dados financeiros e de mercado
- Inclua termos como "market trends", "revenue", "growth"
- Busque por relatórios de empresas e análises
- Considere diferentes geografias (global, regional)
- Inclua aspectos de competitividade

Tópico: {research_topic}
Data: {current_date}
Queries: {number_queries}

Formato:
{{
    "rationale": "Estratégia de análise de mercado",
    "query": ["query comercial 1", "query comercial 2"]
}}

Contexto: {research_topic}"""

    # Prompt para verificação de fatos
    prompt_verificacao = """Você é um verificador de fatos especializado em análise crítica.
Sua tarefa é gerar consultas para verificar a veracidade de informações.

Instruções:
- Busque múltiplas fontes independentes
- Inclua termos como "fact check", "verified", "official"
- Procure por fontes governamentais e organizações confiáveis
- Considere diferentes perspectivas
- Foque em evidências e dados verificáveis

Afirmação a verificar: {research_topic}
Data: {current_date}
Queries: {number_queries}

Formato:
{{
    "rationale": "Estratégia de verificação",
    "query": ["verificação 1", "verificação 2"]
}}

Contexto: {research_topic}"""

    prompts_personalizados = {
        "acadêmico": prompt_academico,
        "mercado": prompt_mercado,
        "verificação": prompt_verificacao
    }
    
    print("📚 Prompts criados:")
    for nome, prompt in prompts_personalizados.items():
        tamanho = len(prompt)
        print(f"  - {nome.capitalize()}: {tamanho} caracteres")
    
    # Teste um prompt
    print(f"\n🧪 Teste do prompt acadêmico:")
    topico = "machine learning applications in healthcare"
    prompt_formatado = prompts_personalizados["acadêmico"].format(
        research_topic=topico,
        current_date=get_current_date(),
        number_queries=3
    )
    print(f"📋 Prompt formatado (primeiros 300 chars):")
    print(prompt_formatado[:300] + "...")
    
    return prompts_personalizados

def exercicio_2_configuracoes_especializadas():
    """Crie configurações para diferentes casos de uso"""
    print("\n⚙️ EXERCÍCIO 2: Configurações Especializadas")
    print("=" * 50)
    
    # Configuração para pesquisa rápida
    config_rapida = Configuration(
        query_generator_model="gemini-2.0-flash",
        reflection_model="gemini-2.0-flash", 
        answer_model="gemini-2.5-flash",
        number_of_initial_queries=1,
        max_research_loops=1
    )
    
    # Configuração para pesquisa aprofundada
    config_aprofundada = Configuration(
        query_generator_model="gemini-2.5-flash",
        reflection_model="gemini-2.5-pro",
        answer_model="gemini-2.5-pro",
        number_of_initial_queries=5,
        max_research_loops=3
    )
    
    # Configuração balanceada
    config_balanceada = Configuration(
        query_generator_model="gemini-2.0-flash",
        reflection_model="gemini-2.5-flash",
        answer_model="gemini-2.5-pro", 
        number_of_initial_queries=3,
        max_research_loops=2
    )
    
    configuracoes = {
        "Rápida": config_rapida,
        "Aprofundada": config_aprofundada, 
        "Balanceada": config_balanceada
    }
    
    print("🎛️ Configurações criadas:")
    for nome, config in configuracoes.items():
        print(f"\n📊 {nome}:")
        print(f"  - Query model: {config.query_generator_model}")
        print(f"  - Reflection model: {config.reflection_model}")
        print(f"  - Answer model: {config.answer_model}")
        print(f"  - Initial queries: {config.number_of_initial_queries}")
        print(f"  - Max loops: {config.max_research_loops}")
    
    return configuracoes

def exercicio_3_agente_especializado():
    """Simule criação de agente especializado"""
    print("\n🤖 EXERCÍCIO 3: Agente Especializado")
    print("=" * 45)
    
    print("🏥 Criando: Agente de Pesquisa Médica")
    
    # Estado especializado para pesquisa médica
    estado_medico = {
        "messages": [HumanMessage(content="What are the latest treatments for diabetes?")],
        "initial_search_query_count": 4,  # Mais queries para tópico complexo
        "max_research_loops": 3,  # Mais loops para precisão
        "reasoning_model": "gemini-2.5-pro",  # Modelo mais sofisticado
        # Campos customizados (simulação)
        "domain": "medical",
        "evidence_level": "peer_reviewed",
        "time_range": "last_2_years"
    }
    
    print(f"⚕️ Configuração do agente médico:")
    print(f"  - Domínio: {estado_medico['domain']}")
    print(f"  - Nível de evidência: {estado_medico['evidence_level']}")
    print(f"  - Período: {estado_medico['time_range']}")
    print(f"  - Queries: {estado_medico['initial_search_query_count']}")
    print(f"  - Loops: {estado_medico['max_research_loops']}")
    
    # Simular prompt médico personalizado
    prompt_medico = """Como assistente de pesquisa médica, gere queries para:
    - Artigos em PubMed e journals médicos
    - Ensaios clínicos e meta-análises  
    - Guidelines de organizações médicas
    - Estudos de eficácia e segurança
    
    Tópico: {research_topic}
    Foque em evidências científicas de alta qualidade."""
    
    print(f"\n📋 Prompt médico personalizado criado")
    print(f"   Foco: Evidências científicas de alta qualidade")
    
    return estado_medico

def exercicio_4_metricas_personalizadas():
    """Defina métricas para avaliar diferentes tipos de agente"""
    print("\n📊 EXERCÍCIO 4: Métricas Personalizadas")
    print("=" * 45)
    
    metricas = {
        "Pesquisa Acadêmica": {
            "sources_quality": "Percentual de fontes peer-reviewed",
            "recency": "Média de anos dos artigos citados",
            "citation_count": "Número de citações incluídas",
            "technical_depth": "Nível de detalhe técnico (1-5)",
            "methodology_coverage": "Cobertura de metodologias (1-5)"
        },
        
        "Análise de Mercado": {
            "data_freshness": "Idade dos dados de mercado (dias)",
            "source_diversity": "Número de fontes diferentes",
            "geographic_coverage": "Regiões cobertas",
            "financial_metrics": "Quantidade de métricas financeiras",
            "trend_analysis": "Qualidade da análise de tendências (1-5)"
        },
        
        "Verificação de Fatos": {
            "source_independence": "Independência das fontes (1-5)",
            "authority_level": "Nível de autoridade das fontes (1-5)",
            "bias_detection": "Detecção de viés (1-5)",
            "evidence_strength": "Força das evidências (1-5)",
            "contradiction_found": "Contradições identificadas (sim/não)"
        }
    }
    
    print("📈 Métricas definidas por tipo de agente:")
    for tipo, metrics in metricas.items():
        print(f"\n🎯 {tipo}:")
        for metrica, descricao in metrics.items():
            print(f"  - {metrica}: {descricao}")
    
    return metricas

def exercicio_5_pipeline_customizado():
    """Crie pipeline customizado de processamento"""
    print("\n🔄 EXERCÍCIO 5: Pipeline Customizado")
    print("=" * 45)
    
    # Simular pipeline para diferentes domínios
    pipelines = {
        "Pesquisa Científica": [
            "1. Gerar queries acadêmicas",
            "2. Filtrar por peer-review",
            "3. Analisar metodologias",
            "4. Verificar reprodutibilidade",
            "5. Sintetizar evidências"
        ],
        
        "Inteligência Comercial": [
            "1. Gerar queries de mercado",
            "2. Coletar dados financeiros",
            "3. Analisar competidores",
            "4. Identificar tendências",
            "5. Projetar oportunidades"
        ],
        
        "Jornalismo Investigativo": [
            "1. Gerar queries investigativas",
            "2. Verificar múltiplas fontes",
            "3. Checar credibilidade",
            "4. Detectar inconsistências",
            "5. Documentar evidências"
        ]
    }
    
    print("🏭 Pipelines customizados:")
    for nome, etapas in pipelines.items():
        print(f"\n🔧 {nome}:")
        for etapa in etapas:
            print(f"   {etapa}")
    
    return pipelines

def exercicio_6_teste_personalizado():
    """Execute um teste com customizações"""
    print("\n🧪 EXERCÍCIO 6: Teste Personalizado")
    print("=" * 40)
    
    # Verificar se API está disponível
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.getenv("GEMINI_API_KEY"):
        print("⚠️ API Key não encontrada - simulando execução")
        
        # Simular resultado
        resultado_simulado = {
            "tipo": "simulação",
            "queries_geradas": ["AI healthcare applications", "machine learning medical diagnosis"],
            "fontes_encontradas": 8,
            "loops_executados": 2,
            "tempo_estimado": "45s",
            "qualidade": "alta precisão acadêmica"
        }
        
        print("🎭 Resultado simulado:")
        for chave, valor in resultado_simulado.items():
            print(f"  - {chave}: {valor}")
        
        return resultado_simulado
    
    else:
        print("🚀 Executando teste real...")
        
        # Configuração personalizada para teste
        estado_teste = {
            "messages": [HumanMessage(content="What are the ethical implications of AI in healthcare?")],
            "initial_search_query_count": 2,  # Reduzido para teste
            "max_research_loops": 1,
            "reasoning_model": "gemini-2.0-flash"
        }
        
        try:
            import time
            inicio = time.time()
            resultado = graph.invoke(estado_teste)
            fim = time.time()
            
            print(f"✅ Teste concluído em {fim - inicio:.2f}s")
            print(f"📊 Queries: {len(resultado.get('search_query', []))}")
            print(f"📚 Fontes: {len(resultado.get('sources_gathered', []))}")
            
            return resultado
            
        except Exception as e:
            print(f"❌ Erro no teste: {e}")
            return None

def exercicio_7_ideias_futuras():
    """Brainstorm de ideias para desenvolvimento futuro"""
    print("\n💡 EXERCÍCIO 7: Ideias para o Futuro")
    print("=" * 40)
    
    ideias = {
        "Novos Domínios": [
            "🧬 Agente de pesquisa biomédica",
            "⚖️ Agente de pesquisa jurídica",
            "🌱 Agente de sustentabilidade",
            "💰 Agente de análise financeira",
            "🔬 Agente de pesquisa científica"
        ],
        
        "Funcionalidades": [
            "📊 Dashboard de métricas em tempo real",
            "🔔 Sistema de alertas para novas informações",
            "📈 Análise de tendências temporais",
            "🤝 Colaboração entre múltiplos agentes",
            "🎯 Personalização baseada em histórico"
        ],
        
        "Integrações": [
            "🔗 APIs de bases de dados especializadas",
            "📱 Interface mobile nativa",
            "🗣️ Interface de voz",
            "📧 Relatórios automáticos por email",
            "☁️ Deploy em múltiplas clouds"
        ],
        
        "Melhorias": [
            "🧠 Memória de longo prazo",
            "🎨 Visualizações interativas",
            "🔍 Busca semântica avançada",
            "⚡ Otimização de performance",
            "🛡️ Segurança e privacidade aprimoradas"
        ]
    }
    
    print("🚀 Ideias para desenvolvimento futuro:")
    for categoria, lista_ideias in ideias.items():
        print(f"\n📋 {categoria}:")
        for ideia in lista_ideias:
            print(f"   {ideia}")
    
    return ideias

if __name__ == "__main__":
    print("🎓 EXERCÍCIOS PRÁTICOS - CUSTOMIZAÇÕES E EXPERIMENTOS")
    print("=" * 65)
    
    # Execute todos os exercícios
    prompts = exercicio_1_prompt_personalizado()
    configs = exercicio_2_configuracoes_especializadas()
    agente = exercicio_3_agente_especializado()
    metricas = exercicio_4_metricas_personalizadas()
    pipelines = exercicio_5_pipeline_customizado()
    teste = exercicio_6_teste_personalizado()
    ideias = exercicio_7_ideias_futuras()
    
    print(f"\n🎉 PARABÉNS! TODOS OS EXERCÍCIOS CONCLUÍDOS!")
    print("=" * 50)
    
    print(f"📚 O que você aprendeu:")
    print(f"✅ Estrutura e arquitetura do agente")
    print(f"✅ Configuração e personalização")
    print(f"✅ Prompts e IA generativa")
    print(f"✅ Estados e fluxo de execução")
    print(f"✅ Customizações avançadas")
    
    print(f"\n🚀 PRÓXIMOS PASSOS SUGERIDOS:")
    print(f"1. 🔧 Implemente suas próprias customizações")
    print(f"2. 🎯 Crie agentes para domínios específicos")
    print(f"3. 📊 Desenvolva métricas personalizadas")
    print(f"4. 🔗 Integre com outras APIs e serviços")
    print(f"5. 🌟 Contribua com melhorias para o projeto")
    
    print(f"\n💡 RECURSOS PARA CONTINUAR ESTUDANDO:")
    print(f"📖 Documentação LangGraph: https://langchain-ai.github.io/langgraph/")
    print(f"🤖 Google Gemini API: https://ai.google.dev/docs")
    print(f"💬 Comunidade LangChain: Discord e GitHub")
    
    print(f"\n🎖️ Você agora tem conhecimento sólido sobre agentes LangGraph!")
    print(f"Continue experimentando e construindo coisas incríveis! 🚀")