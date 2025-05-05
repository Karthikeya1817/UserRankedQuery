🔍 Wikipedia-Based Dynamic Search Assistant
This is a text-based intelligent assistant that allows users to search topics using simple queries and returns real-time summaries from Wikipedia. If Wikipedia does not have an entry, it suggests reliable alternative search links (e.g., Google, Bing, DuckDuckGo). It also maintains user interaction data to recommend related topics and dynamically rank queries based on interest.

🔧 Core Features:
🧠 Wikipedia Summary Retrieval

Uses the wikipedia-api Python library to fetch and display up to 500 characters of a Wikipedia article summary for a user-entered topic.

❌ Intelligent Fallback

If no Wikipedia page is found, it offers direct search engine links for further exploration.

🔄 Dynamic Query Suggestions

Based on past searches, the assistant suggests related topics using NLP-like word reuse (e.g., turning “Machine Learning” into “Machine applications” or “future of Learning”).

📊 Query Ranking System

It tracks which queries the user found most useful and ranks them at the end of the session. This mimics how search engines learn user preferences.
