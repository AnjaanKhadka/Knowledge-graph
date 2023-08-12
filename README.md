# Knowlege-graph

## Scraping

Steps involved in Scraping thehimilayantimes.

1. I collected 10 catagories.
2. For each catagories I scraped links from 10 pages of content, each page had around 20 articles, and stored the link in meta_data.csv file.
3. Then I scraped content text for the 2000 links collected.
4. I also made sure to keep their catagories, title, Published date and time. This may come in handy for some other tasks.

## Data Cleaning

Duplicate contents as well as empty contents were removed from the data. Unrecognized Characters were also removed from the data.

## Building Directed Graph

To build directed graph I found a really good [repository entitled enhanced-subject-verb-object-extraction](https://github.com/rock3125/enhanced-subject-verb-object-extraction) by [rock3125](https://github.com/rock3125) that can split sentences into subject verb and object. I used this model for splitting each sentences in my dataset to subject, verb and object.

I attempted to Draw the graph with each sentence collected in networkx. Since there very large number of sentences in the entire text. (around 50k sentences) This resulted in graph being too complicated. Later I reduced the number of considered articles.

I planned to convert questions into subject object pair and find path between the subject and object of the questions. I planned to display all the sentences in that path as answer for the question. This could be true if sentences were not so sparse. Since sentences were sparse, most of the time object was unreachable from the subject. There are various solutions to this problem. Optimal solution would be to simplify subjects and objects so that they can match easily with one another. This should densen the graph, thus making this approach somewhat workable. Another solution would be to use some deep learning language model to identify subject and object. This model will select subject and object from a pool of text data it was trained on. This limits multiple varitions of the same words to form different nodes, thus making thus approah of question answering possible.
