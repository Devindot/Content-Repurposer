import requests
from bs4 import BeautifulSoup
import re
import subprocess
import json

def get_youtube_transcript(url):
    """
    Fetches the transcript for a YouTube video using the command-line tool.
    This final version correctly handles the tool's specific output format.
    """
    try:
        video_id_match = re.search(r"(?<=v=)[^&#]+", url)
        video_id_match = video_id_match or re.search(r"(?<=be/)[^&#]+", url)
        video_id = video_id_match.group(0)

        # Command to run the CLI tool
        command = ["youtube_transcript_api", video_id]
        
        result = subprocess.run(
            command, 
            capture_output=True, 
            text=True, 
            # We set check=False because the tool prints errors to stdout
            check=False 
        )
        
        # If the command failed, return the error message
        if result.returncode != 0:
            return f"Error: youtube_transcript_api command failed: {result.stderr or result.stdout}"

        # The tool's output is not perfect JSON, so we can't parse it directly.
        # Instead, we will use a regular expression to find all the text segments.
        # This is a much more robust way to extract the content.
        text_matches = re.findall(r"'text':\s*'([^']*)'", result.stdout)
        
        if not text_matches:
            return "Error: Could not parse any text from the transcript output."

        # Join all the found text segments together
        transcript = " ".join(text_matches)
        
        # Replace newline characters with spaces for cleaner text
        transcript = transcript.replace('\\n', ' ')
        
        return transcript
        
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"

def get_article_text(url):
    """Fetches and cleans the text content of a blog article."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        paragraphs = soup.find_all('p')
        article_text = " ".join([para.get_text() for para in paragraphs])
        
        if not article_text:
            return "Error: Could not find any paragraph text on the page. The site may be blocking content."
            
        return article_text
    except Exception as e:
        return f"Error fetching article text: {e}"

def fetch_content_from_url(url):
    """Determines the URL type and calls the appropriate fetcher."""
    if "youtube.com" in url or "youtu.be" in url:
        return get_youtube_transcript(url)
    else:
        return get_article_text(url)