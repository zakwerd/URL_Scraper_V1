from url_scraper import *
from url_data_collect import *
from graph import *


def main():
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
