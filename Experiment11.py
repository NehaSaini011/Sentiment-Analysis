print("🚀 Starting our Tweet Sentiment Analysis project!")
print("📦 Loading our tools (libraries)...")

import pandas as pd          # For working with data tables
import matplotlib.pyplot as plt  # For making charts
import numpy as np           # For math operations
import random               # For creating random sample data

# These might need to be installed first in Google Colab:
# !pip install textblob
from textblob import TextBlob  # For analyzing sentiment

print("✅ All tools loaded successfully!")

def create_sample_tweets(topic="pizza", number_of_tweets=100):
      
    print(f"📝 Creating {number_of_tweets} sample tweets about '{topic}'...")
    
    # Sample positive tweets (people like the topic)
    positive_tweets = [
        f"I absolutely love {topic}! Best thing ever! 😍",
        f"{topic} makes my day so much better! ❤️",
        f"Just had amazing {topic}. So happy right now! 🎉",
        f"{topic} is the best! Everyone should try it 👍",
        f"Having {topic} with friends. Life is good! 😊",
        f"Can't get enough of {topic}! It's incredible 🌟",
        f"{topic} always puts me in a great mood! 😄"
    ]
    
    # Sample negative tweets (people don't like the topic)
    negative_tweets = [
        f"Really disappointed with {topic}. Not good at all 😞",
        f"{topic} is overrated. Don't understand the hype 👎",
        f"Had terrible {topic} today. Waste of money 💸",
        f"Why do people like {topic}? It's awful 😤",
        f"{topic} gave me a headache. Never again! 😣",
        f"Worst {topic} experience ever. So frustrated 😠",
        f"{topic} is not worth it. Very disappointing 😔"
    ]
    
    # Sample neutral tweets (people are just talking about it)
    neutral_tweets = [
        f"Just saw some {topic}. It exists, I guess 🤷",
        f"Meeting friends for {topic} later today",
        f"Store has {topic} on sale this week",
        f"My sister likes {topic} but I'm not sure",
        f"Reading about {topic} for my homework assignment",
        f"{topic} is available in many different varieties",
        f"Some people prefer {topic}, others don't. That's normal"
    ]
    
    # Combine all tweets
    all_sample_tweets = positive_tweets + negative_tweets + neutral_tweets
    
    # Create random tweets by picking from our samples
    tweets = []
    for i in range(number_of_tweets):
        # Pick a random tweet and add some variation
        tweet = random.choice(all_sample_tweets)
        tweets.append(tweet)
    
    # Create a data table (DataFrame) with our tweets
    tweet_data = pd.DataFrame({
        'tweet_number': range(1, number_of_tweets + 1),
        'tweet_text': tweets,
        'topic': topic
    })
    
    print(f"✅ Created {len(tweet_data)} tweets about '{topic}'!")
    return tweet_data

def analyze_tweet_sentiment(tweet_text):
   
       # Create a TextBlob object (this analyzes the text)
    blob = TextBlob(tweet_text)
    
    # Get the polarity score (ranges from -1 to 1)
    # -1 = very negative, 0 = neutral, 1 = very positive
    polarity = blob.sentiment.polarity
    
    # Classify the sentiment based on the score
    if polarity > 0.1:        # Clearly positive
        return "Positive"
    elif polarity < -0.1:     # Clearly negative
        return "Negative"
    else:                     # Close to neutral
        return "Neutral"

def add_sentiment_to_tweets(tweet_data):
  
    print("🧠 Analyzing sentiment of all tweets...")
    print("   (This means figuring out if each tweet is positive, negative, or neutral)")
    
    # Analyze each tweet and store the result
    sentiments = []
    for tweet in tweet_data['tweet_text']:
        sentiment = analyze_tweet_sentiment(tweet)
        sentiments.append(sentiment)
    
    # Add the sentiment results to our data table
    tweet_data['sentiment'] = sentiments
    
    print("✅ Sentiment analysis complete!")
    return tweet_data

def create_sentiment_charts(tweet_data, topic):
      
    print("📊 Creating beautiful charts...")
    
    # Count how many tweets are positive, negative, and neutral
    sentiment_counts = tweet_data['sentiment'].value_counts()
    
    # Set up our chart area (2 charts side by side)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Chart 1: Pie Chart (circle chart showing percentages)
    colors = ['#2ecc71', '#e74c3c', '#95a5a6']  # Green, Red, Gray
    labels = sentiment_counts.index
    sizes = sentiment_counts.values
    
    ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', 
            startangle=90, textprops={'fontsize': 12})
    ax1.set_title(f'Sentiment About "{topic.title()}" - Pie Chart', 
                  fontsize=14, fontweight='bold')
    
    # Chart 2: Bar Chart (rectangles showing counts)
    bars = ax2.bar(sentiment_counts.index, sentiment_counts.values, 
                   color=colors, alpha=0.8)
    
    # Add numbers on top of each bar
    for i, bar in enumerate(bars):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 1,
                f'{int(height)}', ha='center', va='bottom', fontsize=12)
    
    ax2.set_title(f'Sentiment About "{topic.title()}" - Bar Chart', 
                  fontsize=14, fontweight='bold')
    ax2.set_xlabel('Sentiment Type', fontsize=12)
    ax2.set_ylabel('Number of Tweets', fontsize=12)
    
    # Make the charts look nice
    plt.tight_layout()
    plt.show()
    
    print("✅ Charts created successfully!")
    
    return sentiment_counts

def create_simple_report(tweet_data, sentiment_counts, topic):
        
    print("📝 Writing your analysis report...")
    
    total_tweets = len(tweet_data)
    most_common_sentiment = sentiment_counts.index[0]  # The most common sentiment
    
    # Find example tweets for each sentiment
    positive_example = tweet_data[tweet_data['sentiment'] == 'Positive']['tweet_text'].iloc[0] \
                      if 'Positive' in sentiment_counts.index else "None found"
    
    negative_example = tweet_data[tweet_data['sentiment'] == 'Negative']['tweet_text'].iloc[0] \
                      if 'Negative' in sentiment_counts.index else "None found"
    
    neutral_example = tweet_data[tweet_data['sentiment'] == 'Neutral']['tweet_text'].iloc[0] \
                     if 'Neutral' in sentiment_counts.index else "None found"
    
    # Create the report
    report = f"""
🎉 SENTIMENT ANALYSIS REPORT 🎉
Topic: {topic.title()}
Date: Today
Analyzed by: You (great job!)

📊 SUMMARY OF RESULTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Total tweets analyzed: {total_tweets}
• Most common feeling: {most_common_sentiment}

📈 DETAILED BREAKDOWN:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    # Add details for each sentiment type
    for sentiment in ['Positive', 'Negative', 'Neutral']:
        if sentiment in sentiment_counts.index:
            count = sentiment_counts[sentiment]
            percentage = (count / total_tweets) * 100
            
            # Choose appropriate emoji
            emoji = "😊" if sentiment == "Positive" else "😞" if sentiment == "Negative" else "😐"
            
            report += f"• {emoji} {sentiment}: {count} tweets ({percentage:.1f}%)\n"
    
    report += f"""
💡 WHAT THIS MEANS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    
    # Provide simple interpretation
    if most_common_sentiment == "Positive":
        report += f"Great news! Most people seem to have positive feelings about {topic}!"
    elif most_common_sentiment == "Negative":
        report += f"It looks like many people have concerns or negative feelings about {topic}."
    else:
        report += f"People seem to have mixed or neutral feelings about {topic}."
    
    report += f"""

📝 EXAMPLE TWEETS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
😊 Positive example: "{positive_example[:100]}..."

😞 Negative example: "{negative_example[:100]}..."

😐 Neutral example: "{neutral_example[:100]}..."

🎓 WHAT YOU LEARNED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• How to analyze emotions in text
• How to create data visualizations
• How to interpret social media sentiment
• Basic data science skills!

🌟 NEXT STEPS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Try analyzing a different topic
• Increase the number of tweets
• Learn about real Twitter API integration
• Share your findings with friends!

Great job completing your first sentiment analysis project! 🎉
"""
    
    print("✅ Report generated!")
    return report

def run_complete_analysis(topic="pizza", num_tweets=100):
    
    print("="*60)
    print("🎯 WELCOME TO TWEET SENTIMENT ANALYSIS!")
    print("="*60)
    print(f"Topic: {topic}")
    print(f"Number of tweets: {num_tweets}")
    print("="*60)
    
    # Step 1: Create sample data
    tweet_data = create_sample_tweets(topic, num_tweets)
    
    # Step 2: Analyze sentiment
    tweet_data = add_sentiment_to_tweets(tweet_data)
    
    # Step 3: Show some example results
    print("\n📋 Here are 5 example tweets with their sentiment:")
    print("-" * 50)
    for i in range(min(5, len(tweet_data))):
        tweet = tweet_data.iloc[i]
        print(f"{i+1}. {tweet['sentiment']}: \"{tweet['tweet_text'][:60]}...\"")
    
    # Step 4: Create charts
    print("\n" + "="*60)
    sentiment_counts = create_sentiment_charts(tweet_data, topic)
    
    # Step 5: Generate report
    print("\n" + "="*60)
    report = create_simple_report(tweet_data, sentiment_counts, topic)
    
    # Print the report
    print("\n" + "="*60)
    print(report)
    
    # Step 6: Save results (optional)
    filename = f"sentiment_analysis_{topic.lower().replace(' ', '_')}.csv"
    tweet_data.to_csv(filename, index=False)
    print(f"💾 Results saved to: {filename}")
    
    print("\n🎉 Analysis complete! Great job!")
    return tweet_data, report

print("🚀 Ready to start your analysis!")
print("💡 Tip: Try topics like 'coffee', 'homework', 'vacation', 'gaming', etc.")
print()

# ⭐ CHANGE THESE VALUES TO CUSTOMIZE YOUR ANALYSIS:
YOUR_TOPIC = "coffee"           # ← Change this to your topic!
NUMBER_OF_TWEETS = 150          # ← Change this number if you want!

# Run the complete analysis
data, report = run_complete_analysis(YOUR_TOPIC, NUMBER_OF_TWEETS)
