# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

from tracker.config import HASHTAGS
from tracker.analyzer import analyze_sentiment

def main():
    print("Starting Social Media Hashtag Sentiment Tracker...")
    
    for hashtag in HASHTAGS:
        results, avg = analyze_sentiment(hashtag)
        
        print(f"\n--- Results for {hashtag} ---")
        print(f"Average Sentiment Polarity: {avg:.2f} (-1.0 to 1.0)")
        
        print("\nSample Posts:")
        for res in results[:3]: # Show first 3 samples
            print(f"[{res['label']}] {res['text']} (Score: {res['polarity']})")

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
