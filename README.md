# Knowledge-graph

## Scraping

Steps involved in Scraping thehimilayantimes.

1. I collected 10 categories.
2. For each category I scraped links from 10 pages of content, each page had around 20 articles, and stored the link in a meta_data.csv file.
3. Then I scraped content text for the 2000 links collected.
4. I also made sure to keep their categories, titles, Published dates, and time. This may come in handy for some other tasks.

## Data Cleaning

Duplicate contents as well as empty contents were removed from the data. Unrecognized Characters were also removed from the data.

## Building Directed Graph

I have ectracted subject, object, relationship for each sentence and added an edge from subject to object with relationship as the edge. On doing this for 2000 pages of articles, Directed graph was drawn.

Knowledge graph made with 5 articles.

![image](https://github.com/AnjaanKhadka/Knowlege-graph/assets/43941329/af335b9d-f96e-4a3a-9e81-6ef656cbfd77)

Knowledge Graph made with 50 articles.

![image](https://github.com/AnjaanKhadka/Knowlege-graph/assets/43941329/aad4aa4d-763c-4d3f-a82e-7f11c9b5cd1c)

I drew graph from 2000 aarticles from scraped data and used it to extract required information when necessary. When a questio is asked often subject, object or relationship is missing, by comparing it to the graph, This system can get related information to the question. Due to very low effort simplification of subject object relationship system, this system could not reliably used for information extraction.

Requirements are listed in requirements.txt file. Use

    pip install -r requirements.txt 

to install the requirements.

To Scrae and collect information from web Use

    python scrape.py

you can use more catagories or more pages from single catagories. Slightly edit the file to achieve just that.

After collecting the data, filter the text using filter.py file. This cleans data from useless characters.

    python filter.py

Then you can generate graph using generate_graph.py file

    python generate_graph.py

After this process you can infer your model. Or you can directly infer my model. to infer model, above steps of scraping, filtering and generting graph can be skipped.

    python infer.py
