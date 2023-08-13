import pandas as pd
import networkx as nx
import spacy
import matplotlib.pyplot as plt


def get_common_svos():


    df = pd.read_csv("scraped_data/filtered_sentences_tiny.csv")
    # df = pd.read_csv("scraped_data/filtered_sentences.csv")
   
    
    # # G = nx.DiGraph()
    # subjs = {}
    # svo_list = []
    # for i, item in df.iterrows():
    #     tokens = nlp(item['sentences'])
    #     svos = findSVOs(tokens) 
    #     for svo in svos:
    #         if len(svo) != 3:
    #             continue
           
    #         sub, verb, obj = svo
            
    #         sub = sub.lower()
    #         obj = obj.lower()
    #         svo_list.append([sub, verb, obj])
    #         if sub in subjs:
    #             subjs[sub] += 1
    #         else:
    #             subjs[sub] = 1
    #         if obj in subjs:
    #             subjs[obj] += 1
    #         else:
    #             subjs[obj] = 1
                
    # # for k,v in list(subjs.items()):
    # #     if v < 5:
    # #         del subjs[k]
            
    # for s,v,o in svo_list:
    #     if s in subjs and o in subjs:
    #         continue
    #     else:
    #         svo_list.remove([s,v,o])
        
    # return svo_list
    
    # clean_text = ".".join(df['sentences'].tolist())
    
    
    #PROCESSING THE TEXT OF THE ARTICLE
    nlp = spacy.load('en_core_web_sm')
    G = nx.DiGraph()
    # doc = nlp(clean_text)
    # sentences = list(doc.sents)
    # for sentence in sentences:
     
    for sentence in df['sentences'].tolist():
        sentence = nlp(sentence)   
        sub = None
        obj = None
        relationship = None

        for token in sentence:
            if "subj" in token.dep_:
                sub = token.text
            elif "obj" in token.dep_:
                obj = token.text
            elif token.dep_ in ("attr", "acomp"):
                relationship = token.text

            if sub and obj and relationship:
                G.add_node(sub)
                G.add_node(obj)
                G.add_edge(sub, obj, relationship = relationship, sentence = str(sentence))

        if not sub or not obj:
            for token in sentence:
                if token.ent_type_ == "PERSON":
                    if not sub:
                        sub = token.text
                    elif not obj:
                        obj = token.text
            if sub and obj and relationship:
                G.add_node(sub)
                G.add_node(obj)
                G.add_edge(sub, obj, relationship = relationship, sentence = str(sentence))
    # Complete graph
    nx.write_gexf(G, "graph.gexf")      
    
    # strongly_connected_components = list(nx.strongly_connected_components(G))
    # largest_component = max(strongly_connected_components, key=len)

    # G = G.subgraph(largest_component)  
    
    # nx.write_gexf(G, "graph_largest_component.gexf")  
            
    # G.add_edge(sub, obj, label = verb)
            
    # nx.write_gexf(G, "graph.gexf")
# def generate_graph(svo_list):
#     G = nx.DiGraph()
#     for svo in svo_list:
#         sub, verb, obj = svo
#         G.add_edge(sub, obj, label = verb)
#     n

def draw_graph():
    G = nx.read_gexf("graph.gexf")
    # largest_component = max(nx.strongly_connected_components(G), key=len)
    # G = G.subgraph(largest_component)
    print(G.number_of_nodes())
    nx.draw(G, with_labels = True)
    plt.show()

    
if __name__ == "__main__":
    svo_list = get_common_svos()
    # generate_graph(svo_list)
    # draw_graph()

    