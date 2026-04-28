# Reddit Research & Analysis Tool

A Python-based tool for automated content retrieval and analysis from Reddit. 
Designed for researchers and analysts to monitor trends, analyze sentiment, and aggregate discussions from specific communities.

## Features
- **Automated Search**: Query Reddit for specific keywords across multiple subreddits.
- **Sentiment Analysis**: Analyze the tone of posts and comments (positive/negative/neutral).
- **Data Export**: Export results to CSV for further processing.
- **Rate Limiting**: Respects Reddit API limits with built-in backoff strategies.

## Usage
1. Create a Reddit App in your [Reddit preferences](https://www.reddit.com/prefs/apps/).
2. Configure `config.json` with your credentials.
3. Run `python main.py`.

## Disclaimer
This tool is intended for personal research and data analysis purposes only. It complies with Reddit's API terms of service.
