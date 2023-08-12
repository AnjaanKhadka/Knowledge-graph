# Knowlege-graph

## Scraping

Steps involved in Scraping thehimilayantimes.

1. I collected 10 categories.
2. For each category I scraped links from 10 pages of content, each page had around 20 articles, and stored the link in a meta_data.csv file.
3. Then I scraped content text for the 2000 links collected.
4. I also made sure to keep their categories, titles, Published dates, and time. This may come in handy for some other tasks.

## Data Cleaning

Duplicate contents as well as empty contents were removed from the data. Unrecognized Characters were also removed from the data.

## Building Directed Graph

To build a directed graph I found a really good [repository entitled enhanced-subject-verb-object-extraction](https://github.com/rock3125/enhanced-subject-verb-object-extraction) by [rock3125](https://github.com/rock3125) that can split sentences into subject-verb and object. I used this model for splitting each sentence in my dataset to subject, verb, and object.

Knowledge graph made with 5 articles.

![image](https://github.com/AnjaanKhadka/Knowlege-graph/assets/43941329/af335b9d-f96e-4a3a-9e81-6ef656cbfd77)

Knowledge Graph made with 50 articles.

![image](https://github.com/AnjaanKhadka/Knowlege-graph/assets/43941329/aad4aa4d-763c-4d3f-a82e-7f11c9b5cd1c)

I attempted to Draw the graph with each sentence collected in Networkx. Since there very large number of sentences in the entire text. (around 50k sentences) This resulted in the graph being too complicated. Later I reduced the number of considered articles.

I planned to convert questions into subject-object pair and find the path between the subject and object of the questions. I planned to display all the sentences in that path as answers to the question. This could be true if sentences were not so sparse. Since sentences were sparse, most of the time object was unreachable from the subject. There are various solutions to this problem. An optimal solution would be to simplify subjects and objects so that they can match easily with one another. This should dense the graph, thus making this approach somewhat workable. Another solution would be to use some deep learning language model to identify subjects and objects. This model will select a subject and object from a pool of text data it was trained on. This limits multiple variations of the same words to form different nodes, thus making this approach of question-answering possible.
