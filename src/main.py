from url_scraper import *
from url_data_collect import *
from graph import *

def setup_files():
    # Open and clear scraped_text.txt
    with open('scraped_text.txt', 'w') as file:
        pass  # Opening in 'w' mode and closing the file clears it.

    # Open and clear url_data.txt
    with open('url_data.txt', 'w') as file:
        pass  # Similarly, this clears the file.

def main():
    setup_files()
    url = input("Enter the webpage URL: ")
    html_content = fetch_page_content(url)
    
    if html_content:
        
        
        # Scrape the text
        text = extract_text_from_html(html_content)
        save_text_to_file(text)
        print(f"Text has been saved to 'scraped_text.txt'.")

        # Collect data from scraped text
        scraped_text = read_scraped_text()
        word_frequencies = count_word_frequencies(scraped_text)
        write_word_frequencies_to_file(word_frequencies)
        print("Word frequencies have been written to 'url_data.txt'.")

        # Graph The data
        graph_word_frequency(word_frequencies)
        

if __name__ == "__main__":
    main()
