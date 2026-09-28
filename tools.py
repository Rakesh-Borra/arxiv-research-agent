import arxiv
from smolagents import tool


@tool
def search_arxiv(
    query: str,
    max_results: int = 3,
    sort_by: str = "relevance"
) -> list:
    """
    Searches arXiv for academic papers based on a query.

    Args:
        query: The search terms, for example 'LLM agents'.
        max_results: The maximum number of papers to return. Defaults to 3.
        sort_by: Use 'relevance' for relevant papers or 'recent' for
            recent papers that are also relevant to the query.

    Returns:
        A list of dictionaries containing title, authors, year,
        published date, url, and abstract.
    """

    client = arxiv.Client()

    # For recent searches, first retrieve a larger group of
    # papers ranked by relevance.
    search_limit = max_results * 5 if sort_by == "recent" else max_results

    search = arxiv.Search(
        query=query,
        max_results=search_limit,
        sort_by=arxiv.SortCriterion.Relevance
    )

    results = []

    for paper in client.results(search):
        authors = ", ".join(
            author.name for author in paper.authors
        )

        results.append({
            "title": paper.title,
            "authors": authors,
            "year": paper.published.year,
            "published": paper.published.strftime("%Y-%m-%d"),
            "url": paper.entry_id,
            "abstract": paper.summary
        })

    # From the relevant papers, put the newest ones first.
    if sort_by == "recent":
        results.sort(
            key=lambda paper: paper["published"],
            reverse=True
        )

    return results[:max_results]