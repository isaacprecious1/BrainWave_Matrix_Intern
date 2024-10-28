#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


df =pd .read_csv(r"C:\Users\Unity\Downloads\synthetic_social_media_data (1).csv")


# In[3]:


df


# In[4]:


#1. What is the overall sentiment distribution in the dataset?
#Question: How many posts are classified as Positive, Negative, or Neutral?

# Count sentiment labels
sentiment_counts = df['Sentiment Label'].value_counts()


# In[5]:


# Plot the sentiment distribution
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])
plt.title('Sentiment Distribution')
plt.xlabel('Sentiment')
plt.ylabel('Number of Posts')
plt.xticks(rotation=0)
plt.show()   


# In[6]:


#2. Which topics/products/events have the highest positive sentiment?
#Question: What are the top 5 posts with the most likes that are classified as Positive?

# Filter for positive sentiments and sort by likes
top_positive_posts = df[df['Sentiment Label'] == 'Positive'].nlargest(5, 'Number of Likes')


# In[7]:


(top_positive_posts[['Post Content', 'Number of Likes']])


# In[8]:


# Plotting
plt.figure(figsize=(10, 6))
plt.barh(top_positive_posts['Post Content'], top_positive_posts['Number of Likes'], color='lightgreen')
plt.title('Top 5 Positive Posts by Number of Likes')
plt.xlabel('Number of Likes')
plt.ylabel('Post Content')
plt.grid(axis='x')
plt.tight_layout()
plt.show()


# In[9]:



#Insights:
#High Engagement:

#All five posts have a high number of likes, ranging from 992 to 1000. This suggests that the content resonates well with the audience, indicating effective messaging or emotional appeal.
#Content Themes:

#While the exact content is partially truncated, common themes in positive posts often include:
#Inspiration or Motivation: Posts that convey hopeful or uplifting messages tend to perform well.
#Relevance to Current Events: If these posts relate to significant societal issues or current trends, they may engage more viewers.
#Personal Stories or Experiences: Posts that share relatable experiences or narratives can evoke empathy and encourage interaction.

    #Engagement Metrics:

#The small difference in the number of likes (from 992 to 1000) suggests that all five posts are similarly effective in terms of engagement, indicating a competitive space among these top posts.

#Audience Reaction:

#The fact that these posts are categorized as "Positive" implies that they likely reflect a tone or message that the audience finds appealing, uplifting, or affirmative.

#Potential Topics:

#While the full content is not visible, phrases like "Scientist message," "environment," and "dream" hint at themes such as science, environmental awareness, and personal aspirations, which are often well-received topics in social media discourse.


# In[10]:


#3. What are the trends in sentiments over time?
#Question: How does the sentiment trend look over the months?

    # Convert the post date to datetime
    
df['Post Date and Time'] = pd.to_datetime(df['Post Date and Time'])


# In[11]:


# Create a new column for month
df['Month'] = df['Post Date and Time'].dt.to_period('M')


# In[12]:


# Count sentiments by month
monthly_sentiments = df.groupby(['Month', 'Sentiment Label']).size().unstack(fill_value=0)


# In[13]:


# Plot the trends
monthly_sentiments.plot(kind='line', marker='o')
plt.title('Sentiment Trends Over Time')
plt.xlabel('Month')
plt.ylabel('Number of Posts')
plt.legend(title='Sentiment')
plt.xticks(rotation=45)
plt.show()


# In[14]:


#4. What is the average engagement (likes, shares, comments) by sentiment?
#Question: What are the average likes, shares, and comments for each sentiment label?

# Calculate average engagement metrics by sentiment

average_engagement = df.groupby('Sentiment Label').agg({
    'Number of Likes': 'mean',
    'Number of Shares': 'mean',
    'Number of Comments': 'mean'
}).reset_index()

(average_engagement)


# In[15]:


# Melt the DataFrame for easier plotting
average_engagement_melted = average_engagement.melt(id_vars='Sentiment Label', 
                                                     value_vars=['Number of Likes', 'Number of Shares', 'Number of Comments'],
                                                     var_name='Engagement Type', 
                                                     value_name='Average')


# In[16]:


# Plotting
plt.figure(figsize=(10, 6))
sns.barplot(data=average_engagement_melted, x='Sentiment Label', y='Average', hue='Engagement Type')
plt.title('Average Engagement Metrics by Sentiment Label')
plt.xlabel('Sentiment Label')
plt.ylabel('Average Engagement')
plt.legend(title='Engagement Type')


# In[17]:


##Insights:
#Likes:

#Negative Sentiment: The average number of likes is the highest (532.34), which is unexpected, as one might assume negative content would attract fewer likes.
#Neutral Sentiment: Slightly lower than negative (488.40).
#Positive Sentiment: The lowest average likes (488.87), indicating that positive posts may not always generate the highest engagement in terms of likes.
#Shares:

#Negative Sentiment: Also has the highest average shares (252.97), suggesting that negative content is more likely to be shared, potentially because it provokes strong reactions or resonates with shared experiences of frustration or concern.
#Neutral Sentiment: Slightly lower than negative shares (251.96).
#Positive Sentiment: The lowest shares (240.09), which might indicate that while people enjoy positive content, they are less likely to share it compared to negative content.
#Comments:

#Negative Sentiment: Has the fewest average comments (99.75), suggesting that while people react to negative posts (likes and shares), they might not engage in discussions as much.
#Neutral Sentiment: Has the highest average comments (105.33), indicating that neutral posts might prompt more discussion or inquiry.
#Positive Sentiment: Falls in between (103.33), showing that positive content can also drive discussions but not as much as neutral content.
#Overall Observations:
#Engagement Dynamics: The data suggests a complex relationship between sentiment and engagement metrics. Negative posts may attract more immediate reactions (likes and shares), but they do not foster discussion as effectively as neutral posts do.

#Emotional Response: Negative content might elicit strong emotions that drive sharing, while neutral content might provoke thought and discussion without the emotional charge of negativity or positivity.

#Strategic Content Approach: For content creators or marketers, this data suggests the need for a balanced approach:

#Engage with Emotion: Craft content that evokes strong emotions (both positive and negative) to drive likes and shares.
#Encourage Discussion: Use neutral or thought-provoking content to foster dialogue, which can enhance community engagement.
 #   In summary, while negative content tends to drive immediate engagement, neutral content encourages conversation, highlighting the importance of a varied content strategy to engage an audience effectively.




# In[18]:


#5. Which language posts receive the highest engagement for specific sentiments?
#Question: What is the average number of likes for Positive posts by language?

# Filter for positive sentiments and calculate average likes by language

average_likes_by_language = df[df['Sentiment Label'] == 'Positive'].groupby('Language')['Number of Likes'].mean().reset_index()



# In[19]:


# Sort and display
average_likes_by_language = average_likes_by_language.sort_values(by='Number of Likes', ascending=False)
(average_likes_by_language)


# In[20]:


# Plotting
plt.figure(figsize=(10, 6))
plt.bar(average_likes_by_language['Language'], average_likes_by_language['Number of Likes'], color='skyblue')
plt.title('Average Likes by Language (Positive Sentiment)')
plt.xlabel('Language')
plt.ylabel('Average Number of Likes')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# In[21]:




### Insights:

#1. **Top Performing Languages**:
  # - **French (fr)** has the highest average likes (503.71), followed closely by **Chinese (zh)** at 500.88. This suggests that content in these languages resonates particularly well with their audiences.
   #- **English (en)** and **Spanish (es)** have similar averages (488.45 and 488.10, respectively), indicating that they attract comparable engagement levels.
   #- **German (de)** has the lowest average likes (468.02), which may suggest lesser engagement in that language compared to the others.

#2. Cultural Factors:
 #  - The higher engagement in French and Chinese could reflect cultural factors or the types of content being shared in those languages. Certain topics or styles might be more appealing to audiences in these regions.
  # - Content that is culturally relevant or resonates with current trends in French and Chinese-speaking communities may drive higher engagement.

#3. Language Popularity:
 #  - English is a widely spoken language globally, but the engagement metrics suggest that the content may not be as compelling in terms of likes compared to French or Chinese. This could imply that content quality or context plays a significant role in audience interaction.
  
#4. Market Opportunities:
  # - The higher likes for French and Chinese posts indicate potential areas for focused marketing or content creation strategies. If you’re aiming to boost engagement, exploring themes that appeal to these audiences could be beneficial.

### Recommendations:

#- **Content Strategy**: Tailor content to suit the cultural and contextual preferences of the top-performing languages. For example, explore trends, popular topics, or influencers within the French and Chinese-speaking communities.

#- **Engagement Tactics**: Consider experimenting with different types of content (videos, infographics, articles) in the languages with higher likes to see if engagement can be increased even further.

#- **Analyze Further**: Look into the types of posts that garnered the most likes in each language. Understanding what content performs well can help refine future strategies.

#- **Community Engagement**: Foster community interaction in the languages with higher engagement by encouraging comments and shares, which can enhance overall visibility and interaction.

#In summary, the data suggests that posts in French and Chinese generate the most likes, highlighting the importance of cultural relevance in content creation. Tailoring strategies to leverage these insights can improve engagement across different language audiences.

