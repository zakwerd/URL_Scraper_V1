import requests
from bs4 import BeautifulSoup, NavigableString, Tag

def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if the response status code is 4XX/5XX
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return None

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Function to process a single element
    def process_element(element, result=[]):
        for content in element.children:
            if isinstance(content, NavigableString):
                text = content.strip()
                if text:  # Avoid adding empty strings
                    result.append(text)
            elif isinstance(content, Tag):
                if content.name in ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'li']:
                    # For block elements, add text and two newlines
                    process_element(content, result)
                    result.append('\n\n')
                elif content.name == 'br':
                    # For <br>, add a single newline
                    result.append('\n')
                else:
                    # For any other tag, just process it without adding newlines
                    process_element(content, result)
        return result
    
    # Process the whole HTML body
    text_elements = process_element(soup.body)
    return ''.join(text_elements)

def save_text_to_file(text, filename="scraped_text.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

