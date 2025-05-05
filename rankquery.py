!pip install wikipedia-api
import wikipediaapi
import random

# Set up Wikipedia API with user-agent
USER_AGENT = "MyCustomSearchEngine/1.0 (contact: your_email@example.com)"  # Change this!

# Store search history & dynamic ranking
search_history = []
query_rankings = {}

def fetch_wikipedia(query):
    """Fetches summary from Wikipedia if available, else provides alternative links."""
    wiki = wikipediaapi.Wikipedia(
        language="en",
        user_agent=USER_AGENT
    )

    page = wiki.page(query)

    if page.exists():
        summary = page.summary[:500]  # Display first 500 characters
        print(f"\n📖 **Wikipedia Summary for '{query}':**\n{summary}\n")
        return query  # Return query if Wikipedia data is found
    else:
        print("\n❌ No Wikipedia page found. Searching for alternative links...\n")
        fetch_alternative_links(query)
    return None  # Return None if no Wikipedia page exists

def fetch_alternative_links(query):
    """Simulate fetching alternative sources (e.g., Google Search links)."""
    print(f"🔗 Suggested links for '{query}':")
    print(f"- https://www.google.com/search?q={query.replace(' ', '+')}")
    print(f"- https://duckduckgo.com/?q={query.replace(' ', '+')}")
    print(f"- https://www.bing.com/search?q={query.replace(' ', '+')}\n")

def generate_related_queries():
    """Dynamically generate related queries based on user search history."""
    if not search_history:
        return ["Artificia""Simulate fetching alternative sources (e.g., Google Search links)."""
    print(f"🔗 Suggested links for '{query}':")
    print(f"- https://www.google.com/search?q={query.replace(' ', '+')}")
    print(f"- https://duckduckgo.com/?q={query.replace(' ', '+')}")
    print(f"- https://www.bing.com/search?q={query.replace(' ', '+')}\n")

def generate_related_queries():
    """Dynamically generate related queries based on user search history."""
    if not search_history:
        return ["Artificial Intelligence", "Machine Learning", "Data Science"]  # Default topics

    last_query = search_history[-1].lower().split()
    related_queries = []

    # Use words from previous searches to generate new suggestions
    for past_query in reversed(search_history):
        words = past_query.split()
        if len(words) > 1:
            related_queries.append(f"{words[0]} applications")
            related_queries.append(f"{words[-1]} research")
        else:
            related_queries.append(f"{past_query} in AI")
            related_queries.append(f"future of {past_query}")

    # Ensure unique related queries & limit to 3 suggestions
    return list(set(related_queries))[:3]

def update_query_rankings(clicked_query):
    """Dynamically update query rankings based on user interaction."""
    if clicked_query in query_rankings:
        query_rankings[clicked_query] += 1
    else:
        query_rankings[clicked_query] = 1

def display_search_rankings():
    """Display search rankings based on recorded user clicks."""
    print("\n📊 **Search Rankings (Based on User Clicks):**")
    ranked_queries = sorted(query_rankings.items(), key=lambda x: x[1], reverse=True)
    for i, (query, score) in enumerate(ranked_queries, 1):
        print(f"{i}. {query} (Clicks: {score})")

def search_engine():
    """Main loop for the search engine."""
    while True:
        # Step 1: Ask user for query
        query = input("\n🔍 What do you want to search about? (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            break

        # Fetch Wikipedia data and store in search history
        search_history.append(query)
        fetched_query = fetch_wikipedia(query)  # Fetch Wikipedia data

        if fetched_query:
            update_query_rankings(fetched_query)  # Update ranking if Wikipedia page found

        # Step 2: Ask if user wants to search more
        while True:
            more_search = input("\nDo you want to search more? (yes/no): ").strip().lower()
            if more_search == "no":
                break

            # Show related queries based on search history
            related_queries = generate_related_queries()
            print("\n🔄 **Suggested Related Queries:**")
            for i, rq in enumerate(related_queries, 1):
                print(f"{i}. {rq}")

            choice = input("\nDo you want to continue with a related query or enter a new one? (choose number/new): ").strip().lower()

            if choice.isdigit() and 1 <= int(choice) <= len(related_queries):
                new_query = related_queries[int(choice) - 1]
            else:
                new_query = input("\nEnter a new search query: ").strip()

            # Fetch Wikipedia data again for new query
            search_history.append(new_query)
            fetched_query = fetch_wikipedia(new_query)

            if fetched_query:
                update_query_rankings(fetched_query)  # Update ranking if Wikipedia page found

        # Step 3: Simulate user clicking on a query (ranking update)
        clicked_query = input("\nEnter the search query you found most useful: ").strip()
        if clicked_query:
            update_query_rankings(clicked_query)

    # Final Step: Show ranked search results
    display_search_rankings()
    print("\n✅ Search session ended. Thank you for using the search engine!")

# Run the search engine
search_engine()

