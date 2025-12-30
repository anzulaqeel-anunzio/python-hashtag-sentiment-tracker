# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import random
from textblob import TextBlob
from .config import HASHTAGS

# Mock data generator to simulate social media posts
def generate_mock_posts(hashtag, count=10):
    templates = [
        "I love {hashtag}! It's so useful.",
        "Honestly, {hashtag} is quite frustrating today.",
        "Just started learning about {hashtag}, interesting stuff.",
        "Why is {hashtag} so difficult?",
        "Best day ever thanks to {hashtag}!",
        "{hashtag} is okay, nothing special.",
        "Can't believe what happened with {hashtag}.",
        "Everyone needs to check out {hashtag}.",
        "I hate {hashtag} right now.",
        "So confused by {hashtag}."
    ]
    
    posts = []
    for _ in range(count):
        text = random.choice(templates).format(hashtag=hashtag)
        posts.append(text)
    return posts

def analyze_sentiment(hashtag):
    posts = generate_mock_posts(hashtag)
    results = []
    
    total_polarity = 0
    
    print(f"\nAnalyzing sentiment for {hashtag}...")
    
    for post in posts:
        analysis = TextBlob(post)
        polarity = analysis.sentiment.polarity
        total_polarity += polarity
        
        sentiment_label = "Neutral"
        if polarity > 0.1: sentiment_label = "Positive"
        elif polarity < -0.1: sentiment_label = "Negative"
        
        results.append({
            "text": post,
            "polarity": round(polarity, 2),
            "label": sentiment_label
        })
        
    avg_polarity = total_polarity / len(posts)
    return results, avg_polarity

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
