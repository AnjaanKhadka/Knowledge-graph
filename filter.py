import pandas as pd
import re

if __name__ == "__main__":
    df = pd.read_csv('scraped_data/contents.csv')
    
    df = df[df['catagory'] == 'Nepal'].head(50)
    
    sentences = []
    for i,item in df.iterrows():
        text = item['text']
        
        
        if type(text) != str:
            continue
        
        # to remove all non alphanumeric characters except , and .
        text = re.sub(r'[^a-zA-Z0-9,\.\s]', '', text)
        
        # To remove dots from abbreviations U.S.A. -> USA
        text = re.sub(r'(?:[A-Z]\.)+', lambda x: x.group().replace(".","") , text)
        
        # Split into sentences
        for sent in re.split(r'\.\s*',text)[:-1]:
            if len(sent) < 10:
                continue
            sentences.append(sent)
    # pd.DataFrame(sentences, columns = ['sentences']).to_csv('scraped_data/filtered_sentences.csv', index = False)
    
    pd.DataFrame(sentences, columns = ['sentences']).to_csv('scraped_data/filtered_sentences_tiny.csv', index = False)
    
    
        