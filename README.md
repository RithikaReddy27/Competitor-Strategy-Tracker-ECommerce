# Competitor-Strategy-Tracker-ECommerce

## Project Overview
This project focuses on creating a real-time competitive intelligence tool for e-commerce businesses. It provides actionable insights by monitoring competitor pricing, discount strategies, and customer sentiment. The solution leverages:
- **Machine Learning**: Predictive modeling with ARIMA.
- **LLMs**: Sentiment analysis using Hugging Face Transformers and Groq.
- **Integration**: Slack notifications for real-time updates.

## Features
1. **Competitor Data Aggregation**: Track pricing and discount strategies.
2. **Sentiment Analysis**: Analyze customer reviews for actionable insights.
3. **Predictive Modeling**: Forecast competitor discounts.
4. **Slack Integration**: Get real-time notifications on competitor activity.

## Steps

### 1. Competitor Data Aggregation
- Use a web scraping tool like **BeautifulSoup** to extract competitor product pricing and discounts.
- Store the data in a simple file (CSV or JSON) for now.

### 2. Sentiment Analysis
- Scrape customer reviews of competitor products.
- Use a pre-trained **Hugging Face** sentiment analysis model to analyze reviews.

### 3. Predictive Modeling (ARIMA)
- Collect historical pricing data from competitors.
- Use **ARIMA** to predict future pricing trends based on the historical data.
