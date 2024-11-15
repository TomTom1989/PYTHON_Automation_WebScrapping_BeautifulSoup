A Python script that retrieves and displays the top 10 songs from the Billboard Hot 100 chart website for a given date using BeautifulSoup and requests.

Features:
1) User Input:
Prompts the user to enter a date in the format YYYY-MM-DD.
Validates the date format before proceeding.

2) Web Scraping:
Sends a request to the Billboard Hot 100 webpage for the specified date.
Parses the HTML content using BeautifulSoup to extract song titles and artists.

3) Output:
Displays the top 10 songs along with their respective artists.

4) Custom Headers:
Includes a user-agent header to prevent scraping blocks.
