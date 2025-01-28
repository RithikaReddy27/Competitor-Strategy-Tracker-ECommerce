# -*- coding: utf-8 -*-
"""Scraper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UhlJn2SpouSeBT4zz16gN2RyaU33dMai
"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
from datetime import datetime, timedelta

def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": "productTitle"})
        title_value = title.text  # content inside span tag
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

def get_price(soup):
    try:
        price = soup.find("span", attrs={"class": "a-price-whole"}).text.strip()[:-1]
        price = price.replace(",", "")  # remove the comma from the price
    except:
        price = ""
    return price

def get_discount(soup):
    try:
        discount = soup.find(
            "span", attrs={"class": "a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"}
        ).text.strip()[1:-1]
    except:
        discount = ""
    return discount

def get_review(soup, max_length=100):
    try:
        review_div = soup.find("div", class_="a-expander-content reviewText review-text-content a-expander-partial-collapse-content")
        if review_div:
            review_span = review_div.find("span")
            if review_span:
                # Extract the text and remove unnecessary newlines or extra spaces
                review = review_span.get_text(strip=True)
                review = ' '.join(review.split())  # Replace multiple spaces with a single space

                # Shorten the review to the specified max length
                if len(review) > max_length:
                    review = review[:max_length] + "..."  # Add ellipsis if review is too long

                return review
    except:
        return ""



# Function to generate past dates
def get_past_dates(n):
    today = datetime.today()
    dates = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(n)]
    return dates

HEADERS = {
    'User-agent': '',
    'Accept-Language': 'en-US, en;q=0.5'
}

URLS = {
    "boAt Rockerz 255": "https://www.amazon.in/boAt-Rockerz-255-Pro-Earphones/dp/B08TV2P1N8",
    "Oneplus Bullets Z2": "https://www.amazon.in/Oneplus-Bluetooth-Wireless-Earphones-Bombastic/dp/B09TVVGXWS",
    "Realme Buds Wireless 3 Neo": "https://www.amazon.in/realme-Buds-Wireless-Bluetooth-Resistannt/dp/B0D3HT2S1M",
    "JBL Tune 215BT": "https://www.amazon.in/JBL-Playtime-Bluetooth-Earphones-Assistant/dp/B08FB2LNSZ"
}

# Scrape Price, Discount, Rating, Review for each product
competitor_data_today = pd.DataFrame(columns=["Product_name", "Price", "Discount", "Date"])
reviews_today = pd.DataFrame(columns=["Product_name", "Review"])

# Generate a list of past dates (e.g., for the past 7 days)
past_dates = get_past_dates(7)  # Scrape data for the past 7 days

for product, url in URLS.items():
    for date in past_dates:
        competitor_data = {"Product_name": [], "Price": [], "Discount": [], "Date": []}
        reviews_data = {"Product_name": [], "Review": []}

        page = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(page.content, "html.parser")

        # Extract data
        title = get_title(soup)
        price = get_price(soup)
        discount = get_discount(soup)
        review = get_review(soup)

        # Store competitor data
        competitor_data["Product_name"].append(title)
        competitor_data["Price"].append(price)
        competitor_data["Discount"].append(discount)
        competitor_data["Date"].append(date)  # Use past date for each entry

        # Concatenate the data to the DataFrame
        competitor_data_today = pd.concat([competitor_data_today, pd.DataFrame(competitor_data)], ignore_index=True)

        # Store review data
        reviews_data["Product_name"].append(title)
        reviews_data["Review"].append(review)
        reviews_today = pd.concat([reviews_today, pd.DataFrame(reviews_data)], ignore_index=True)

# Save to CSV
today = time.strftime("%Y-%m-%d")
competitor_data_today.to_csv(f"competitor_data.csv", index=False)
reviews_today.to_csv(f"reviews_data.csv", index=False)

print(f"Competitor data and reviews saved to CSV files for {today}!")