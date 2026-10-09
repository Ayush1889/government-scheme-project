from rag import search_schemes


def discovery_agent(user_query, top_k=3):
    """
    Find government schemes relevant to the user's question.
    """

    results = search_schemes(
        user_query,
        top_k=top_k
    )

    return results