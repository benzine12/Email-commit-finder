# GitHub Email Finder

## Description
A Python script that retrieves email addresses associated with a GitHub user's public commit events.

## Features
- Searches a GitHub user's public events
- Extracts email addresses from commit events
- Handles various API response scenarios

## Prerequisites
- Python 3.x
- `requests` library

## Installation
1. Clone the repository
2. Install required dependencies:
   ```
   pip install requests
   ```

## Usage
```bash
python app.py
```
When prompted, enter a GitHub username to find associated emails.

## Limitations
- Only finds emails from public commit events
- Requires the GitHub user to have public events
- Limited by GitHub API rate limits

## Notes
- Useful for basic email discovery
- Not guaranteed to find an email for every user
