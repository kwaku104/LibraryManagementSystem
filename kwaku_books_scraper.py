def is_good_response(response):
    '''
        Returns True if the response seems to be HTML, False otherwise.
    '''
    content_type = response.headers['Content-Type'].lower()
    return (response.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)

def convert_date(raw_date):
    monthsDict = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06',
              'Jul': '07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}
    
    raw_date = raw_date.split()
    
    day = raw_date[0]
    month = monthsDict[raw_date[1]]
    year = raw_date[2]
    
    return f'{year}-{month}-{day}'
    
    

def get_books_links(search_parameter):
    '''
        Returns the links to books from the search results. These links are then accessed to 
        scrape the information needed from each book
    '''
    response = requests.get(f'https://www.bookdepository.com/search?searchTerm={search_parameter}&search=Find+book')
    
    if not is_good_response(response):
        return 'Could not get the links.'
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    #Set limit to number of books you want to get information for.
    links = [book.find('a')['href'] for book in soup.find_all('h3', attrs={'class':'title'}, limit=5)]
    
    return links


def get_books_info(search_parameter):
    links = get_books_links(search_parameter)
    
    books_info = []
    
    for link in links:
        response = requests.get(f'https://www.bookdepository.com{link}')
    
        soup = BeautifulSoup(response.content, 'html.parser')
    
        title = soup.find('h1', attrs={'itemprop':'name'}).text.strip()
        author = soup.find('span', attrs={'itemprop':'author'}).text.strip()
        isbn = soup.find('span', attrs={'itemprop': 'isbn'}).text.strip()
        raw_date = soup.find('span', attrs={'itemprop':'datePublished'}).text.strip()
    
        published_date = convert_date(raw_date)
        
        
    
        book_info = {'Title': title,
                     'Author': author,
                     'ISBN': isbn,
                     'Published Date': published_date
                    }
        books_info.append(book_info)
    
    return books_info