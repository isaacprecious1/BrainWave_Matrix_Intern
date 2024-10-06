#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


##create a sale data analysis of any commercial store.


# In[3]:


df=pd.read_csv(r"Downloads\officesupply.csv")


# In[4]:


df


# # data cleaning

# In[5]:


#checking for null value
df.isnull().sum()


# In[6]:


df.dtypes


# In[7]:


##CONVERT DATE from object to date and time
df['Date']=pd.to_datetime(df['Date'])


# In[8]:


df.dtypes


# In[9]:


## to derive year,month and day from the coloum date 
df['year']=df['Date'].dt.year
df['month']=df['Date'].dt.month_name()
df['day']=df['Date'].dt.day_name()


# In[10]:


df


# In[11]:


##coverting saleprice and manufacturingprice from int to float
df['SalePrice']=df['SalePrice'].astype(float)
df['ManufacturingPrice']=df['ManufacturingPrice'].astype(float)


# In[12]:


df


# # Sales Analysis 

# In[13]:


thecorrelation= df['SalePrice'].corr(df['UnitsSold'])
thecorrelation


# In[14]:


#Insights
##The correlation coefficient of approximately 
#−
##0.065
#−0.065 indicates a very weak negative correlation between SalePrice and UnitsSold.
#This suggests that changes in SalePrice have little to no impact on UnitsSold, and 
#if there is any relationship, it is minor and negative. 
#Therefore, pricing does not seem to be a significant factor in influencing sales,


# In[15]:


##1. what is the total revenue for each product
total_sales_for_products=df.groupby('Product')['SalePrice'].sum().reset_index()


# In[16]:


total_sales_for_products.sort_values(by='SalePrice', ascending=False)


# In[17]:


plt. figure(figsize=(6,4))
thevalue =plt.bar(total_sales_for_products['Product'],total_sales_for_products['SalePrice'], color =['red', 'blue'])
for bar in thevalue:
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{bar.get_height():2f}', ha ='center', va='bottom')
plt.xlabel('Product')
plt.ylabel('SalePrice')
plt.title('Total Sales by Products')
plt.show()


# In[18]:


# Insights
#Biro is the top performer by a significant margin, indicating strong demand.
#Other products, like Notepad and Markers, have lower sales but are relatively close in revenue.
#The performance gap suggests potential areas for improvement in marketing or product strategies for the lower-selling items.


# In[19]:


# 2. Total revenue generated by each segment
df['Revenue'] = df['UnitsSold'] * df['SalePrice']
total_revenue_segment = df.groupby('Segment')['Revenue'].sum().reset_index()


# In[20]:


#This shows the total income generated from the sales by each goods, and  biro generated more income than other goods 


# In[21]:


("Total Revenue by Segment:")
(total_revenue_segment)


# In[22]:


plt.figure(figsize=(10, 6))
plt.bar(total_revenue_segment['Segment'], total_revenue_segment['Revenue'], color='skyblue')
plt.title('Total Revenue by Segment', fontsize=16)
plt.xlabel('Segment', fontsize=14)
plt.ylabel('Revenue (in Naira)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[23]:


# Insights
#Government Segment Dominance: The Government segment is the highest revenue generator by a substantial margin, indicating strong demand or larger contract sizes within this market. This could suggest opportunities for the business to further capitalize on government contracts or expand offerings tailored to this segment.

#Small Business Contribution: The Small Business segment follows as the second highest contributor to revenue, which highlights its significance to overall business performance. This segment could be a critical focus for growth strategies and marketing efforts.

#Enterprise Revenue: The Enterprise segment generates a respectable amount but is notably lower than the Government and Small Business segments. This may indicate opportunities for growth or the need for enhanced value propositions to attract more enterprise clients.

#Lower Performance in Channel Partners and Midmarket: Both the Channel Partners and Midmarket segments contribute significantly less to overall revenue. This suggests potential areas for improvement, such as revisiting partnership strategies, enhancing product offerings, or increasing marketing efforts targeted at these segments.

#Conclusion
#The revenue distribution among segments highlights the importance of focusing on Government and Small Business markets while exploring opportunities to boost sales in the Enterprise, Channel Partners, and Midmarket segments. Targeted strategies tailored to each segment could enhance overall revenue performance.




# In[24]:


# 3. State with the highest total units sold
total_units_sold_state = df.groupby('State')['UnitsSold'].sum()
highest_units_sold_state = total_units_sold_state.idxmax()


(f"State with highest total units sold: {highest_units_sold_state}")


# In[25]:


### Insights on State with Highest Total Units Sold

#The analysis indicates that "Enugu State" has the highest total units sold, showcasing its prominence in your sales performance. Here are some key insights:

#1. Market Potential: Enugu State's leading position suggests a strong market presence and customer demand in that region. This could indicate favorable market conditions or a well-targeted sales strategy that resonates with local consumers.

#2. Focus on Enugu: Given its performance, there may be opportunities to further capitalize on this market. Consider exploring tailored marketing strategies, promotions, or product offerings that align with the preferences of consumers in Enugu.

#3. Comparison with Other States**: Understanding what differentiates Enugu from other states in terms of sales can provide insights into successful practices. Factors such as pricing, product mix, customer engagement, and distribution channels may be contributing to its success.

#4. Resource Allocation**: With Enugu State showing the highest units sold, it may be beneficial to allocate more resources—such as sales personnel, marketing efforts, or inventory—to this region to sustain and potentially enhance sales further.

### Conclusion

#Overall, Enugu State represents a significant opportunity for growth and continued success. Leveraging the insights gained from this market could help inform broader strategies across other regions as well.


# In[26]:


# 4. Average discount for each product category
# Assuming 'Discount Band' represents discount categories
average_discount = df.groupby('Product')['SalePrice'].mean()

("Average Sale Price by Product:")
(average_discount)


# In[27]:


plt.figure(figsize=(10, 6))
plt.bar(average_discount.index, average_discount.values, color='lightblue')
plt.title('Average Sale Price by Product', fontsize=16)
plt.xlabel('Product', fontsize=14)
plt.ylabel('Average Sale Price (in Naira)', fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[28]:


# Insights
#Notepad Premium Pricing: The Notepad has the highest average sale price, suggesting that it may be positioned as a premium product. This indicate strong demand or unique features that justify a higher price point.

#Mid-Range Products: The Stapler, Pencil, and Markers fall within a similar pricing range, indicating that these products may compete closely in the market. Marketing strategies could focus on differentiating these products to enhance sales.

#Biro and A4 Paper: Both Biro and A4 Paper have the lowest average prices among the categories. This might suggest a competitive pricing strategy to attract customers, but it could also imply lower profit margins.

#Price Sensitivity: The variation in average sale prices highlights different price sensitivity across product categories. Understanding customer perceptions and preferences for each category could inform pricing strategies.

#Opportunities for Optimization: Analyzing the average discounts or promotional strategies for these products could reveal further opportunities for improving sales or adjusting pricing strategies to maximize profitability.

#Conclusion
#Overall, the average sale prices reflect varying market positions and customer perceptions across product categories. Targeted strategies that consider these insights could help optimize pricing, enhance marketing efforts, and ultimately drive sales performance.


# In[29]:


# 5. Sales variation by month across different states
df['Month'] = df['Date'].dt.to_period('M')
monthly_sales = df.groupby(['Month', 'State'])['Revenue'].sum().reset_index()


# In[30]:


("Monthly Sales by State:")
(monthly_sales)


# In[31]:


plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='bar', stacked=True, ax=plt.gca(), colormap='tab10')
plt.title('Monthly Sales by State', fontsize=16)
plt.xlabel('State', fontsize=14)
plt.ylabel('Revenue (in Naira)', fontsize=14)
plt.xticks(rotation=45)
plt.legend(title='Month', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[32]:


### Insights on Sales Variation by Month Across Different States

#The analysis of monthly sales across different states reveals significant variations in revenue. Here are the key insights:

#1. Enugu State's Dominance: In both January 2013 and January 2014, Enugu State stands out with the highest revenues, indicating strong market presence and demand. The revenue growth from about $7.83 million in 2013 to approximately $25.94 million in 2014 suggests that Enugu State is experiencing substantial growth.

#2. Consistent Performance in Imo State: Imo State shows notable performance as well, with revenue figures closely following Enugu. This consistency indicates a stable customer base and potential for growth strategies similar to those employed in Enugu.

#3. Significant Revenue in Major States: States like Lagos and Ogun also contribute significantly to overall sales, especially in January 2014, with Lagos generating around $8.67 million. This suggests that these states may be key markets worth focusing on for targeted marketing campaigns and promotions.

#4. Variation Across Other States: States like Ondo, Osun, and Oyo demonstrate varied revenue performance. For example, Osun State shows an increase in revenue from $2.89 million in January 2013 to approximately $13.16 million in January 2014, indicating a potential growth trajectory that could be further explored.

#5. Opportunities for Analysis: The variation in monthly sales across states presents opportunities for deeper analysis. Factors such as local market conditions, economic activities, and seasonal effects could be influencing these sales patterns. Understanding these dynamics could inform future sales strategies.

#6. Seasonal Trends: The data suggests that certain months may yield higher sales across states. Analyzing trends over multiple months could uncover seasonality effects, allowing for optimized inventory and marketing strategies tailored to peak sales periods.

### Conclusion

#Overall, the insights into monthly sales variation highlight the importance of understanding regional performance and market dynamics. States like Enugu and Imo present significant opportunities for growth, while others may require targeted strategies to enhance sales performance. Leveraging this information could drive more effective business decisions and marketing efforts.


# In[33]:


# 6. Profit margin for each product sold
df['Profit'] = (df['SalePrice'] - df['ManufacturingPrice']) * df['UnitsSold']
df['ProfitMargin'] = (df['Profit'] / (df['SalePrice'] * df['UnitsSold'])) * 100
profit_margin_product = df.groupby('Product')['ProfitMargin'].mean()


# In[34]:


("Average Profit Margin by Product:")
(profit_margin_product)


# In[35]:


plt.figure(figsize=(10, 6))
plt.bar(profit_margin_product.index, profit_margin_product.values, color=['lightblue' if x >= 0 else 'salmon' for x in profit_margin_product])
plt.title('Average Profit Margin by Product', fontsize=16)
plt.xlabel('Product', fontsize=14)
plt.ylabel('Average Profit Margin (%)', fontsize=14)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


# In[36]:


### Insights on Profit Margin for Each Product Sold

#The average profit margins for each product are as follows:

#1. A4 Paper: 84.49%
#2. Biro: 46.43%
#3. Pencil: 72.30%
#4. Markers: -478.50%
#5. Notepad: -1054.46%
#6. Stapler: -1182.03%

### Key Insights

#1. Strong Performance of A4 Paper: A4 Paper boasts the highest average profit margin at 84.49%, indicating a very favorable cost structure and strong demand. This suggests that it is a key product for profitability.

#2. Biro's Positive Margin: The Biro has a positive profit margin of 46.43%, although significantly lower than A4 Paper. This indicates that while it contributes positively to profits, there may be opportunities to enhance profitability through pricing or cost management.

#3. Concerns with Negative Margins: The other products—Markers, Notepad, and Stapler—show alarming negative profit margins, especially the Notepad and Stapler with margins of -1054.46% and -1182.03%, respectively. This suggests that the costs of manufacturing these products far exceed the revenue generated from sales, indicating a critical need for review.

#4. Pricing and Cost Analysis Needed: The negative profit margins point to potential issues in pricing strategies, manufacturing costs, or market positioning. A thorough analysis of the costs associated with these products and a reevaluation of their pricing strategy are essential to improve profitability.

#5. Market Positioning: Understanding why certain products like Markers, Notepad, and Stapler are underperforming in terms of profit margins can provide insights into market demand, competition, and consumer preferences. Adjusting marketing strategies or product features may be necessary to regain profitability.

### Conclusion

#The profit margin analysis highlights significant disparities among products. While A4 Paper and Biro contribute positively to profitability, the severe negative margins of Markers, Notepad, and Stapler warrant urgent attention. Strategic adjustments in pricing, cost management, and market positioning could help improve the overall profitability of the product line.

