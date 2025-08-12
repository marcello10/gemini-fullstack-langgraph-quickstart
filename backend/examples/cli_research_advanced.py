import argparse
import asyncio
from langchain_core.messages import HumanMessage
from agent.graph import graph


async def main_advanced() -> None:
    """Run the research agent with advanced streaming."""
    parser = argparse.ArgumentParser(description="Run the LangGraph research agent with streaming")
    parser.add_argument("question", help="Research question")
    parser.add_argument(
        "--initial-queries",
        type=int,
        default=3,
        help="Number of initial search queries",
    )
    parser.add_argument(
        "--max-loops",
        type=int,
        default=2,
        help="Maximum number of research loops",
    )
    parser.add_argument(
        "--reasoning-model",
        default="gemini-2.5-pro",
        help="Model for the final answer",
    )
    args = parser.parse_args()
    
    state = {
        "messages": [HumanMessage(content=args.question)],
        "initial_search_query_count": args.initial_queries,
        "max_research_loops": args.max_loops,
        "reasoning_model": args.reasoning_model,
    }

    print(f"🔍 Iniciando pesquisa: {args.question}")
    print("=" * 50)
    
    final_messages = None
    
    # Streaming com múltiplos modos
    async for stream_mode, chunk in graph.astream(
        state, 
        stream_mode=["updates", "messages"]
    ):
        if stream_mode == "updates":
            # Atualização de progresso dos nós
            for node_name, node_output in chunk.items():
                print(f"\n📍 {node_name.upper()}:")
                
                if node_name == "generate_query":
                    queries = node_output.get("search_query", [])
                    print(f"   🔗 {len(queries)} consultas geradas:")
                    for i, query in enumerate(queries, 1):
                        print(f"   {i}. {query}")
                        
                elif node_name == "web_research":
                    sources = node_output.get("sources_gathered", [])
                    results = node_output.get("web_research_result", [])
                    print(f"   🌐 {len(sources)} fontes coletadas")
                    if results:
                        preview = results[0][:100] + "..." if len(results[0]) > 100 else results[0]
                        print(f"   📄 Preview: {preview}")
                        
                elif node_name == "reflection":
                    is_sufficient = node_output.get("is_sufficient", False)
                    loops = node_output.get("research_loop_count", 0)
                    print(f"   🤔 Loop {loops} - {'Suficiente' if is_sufficient else 'Precisa mais pesquisa'}")
                    
                elif node_name == "finalize_answer":
                    final_messages = node_output.get("messages", [])
                    print(f"   ✅ Resposta finalizada!")
                    
        elif stream_mode == "messages":
            # Streaming de tokens do LLM
            token, metadata = chunk
            if hasattr(token, 'content') and token.content:
                node = metadata.get("langgraph_node", "unknown")
                print(f"🤖 [{node}] {token.content}", end="", flush=True)

    # Exibir resultado final
    if final_messages:
        print("\n" + "=" * 50)
        print("📝 RESPOSTA FINAL:")
        print("=" * 50)
        print(final_messages[-1].content)


def main():
    """Wrapper for async main function."""
    asyncio.run(main_advanced())


if __name__ == "__main__":
    main() 