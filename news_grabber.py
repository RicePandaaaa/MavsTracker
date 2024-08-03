import requests
import dotenv

def get_latest_news(term):
    # Load the API key from an environment variable
    api_key = dotenv.get_key(".env", 'NEWS_API_KEY')
    if not api_key:
        raise ValueError("No API key found. Please set the NEWS_API_KEY environment variable.")

    # Construct the API URL
    url = f"https://newsapi.org/v2/everything?q={term}&apiKey={api_key}"

    # Make the HTTP request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve news: {response.status_code}")
        return []

    # Parse the JSON response
    news_data = response.json()
    articles = news_data['articles']
    
    # Extract relevant information from the articles
    news = []
    for article in articles[:min(len(articles), 5)]:
        title = article['title']
        link = article['url']
        summary = article['description'] if article['description'] else 'No summary available'
        news.append({"title": title, "link": link, "summary": summary})

    return news
