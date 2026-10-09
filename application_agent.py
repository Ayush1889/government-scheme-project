def application_agent(scheme):
    """
    Provides application information for a government scheme.
    """

    return {
        "scheme_name": scheme.get("scheme_name", "N/A"),

        "documents": scheme.get(
            "documents_required",
            "Document information is not available."
        ),

        "steps": scheme.get(
            "application_process",
            "Application process information is not available."
        ),

        "official_website": scheme.get(
            "application_url",
            "Official application URL is not available."
        ),

        "source": scheme.get(
            "source_url",
            "Official source is not available."
        )
    }