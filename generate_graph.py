from subject_verb_object_extract import findSVOs, nlp
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def get_common_svos():


    df = pd.read_csv("scraped_data/filtered_sentences_tiny.csv")
    # df = pd.read_csv("scraped_data/filtered_sentences.csv")
   
    
    # G = nx.DiGraph()
    subjs = {}
    svo_list = []
    for i, item in df.iterrows():
        tokens = nlp(item['sentences'])
        svos = findSVOs(tokens) 
        for svo in svos:
            if len(svo) != 3:
                continue
           
            sub, verb, obj = svo
            
            sub = sub.lower()
            obj = obj.lower()
            svo_list.append([sub, verb, obj])
            if sub in subjs:
                subjs[sub] += 1
            else:
                subjs[sub] = 1
            if obj in subjs:
                subjs[obj] += 1
            else:
                subjs[obj] = 1
                
    # for k,v in list(subjs.items()):
    #     if v < 5:
    #         del subjs[k]
            
    for s,v,o in svo_list:
        if s in subjs and o in subjs:
            continue
        else:
            svo_list.remove([s,v,o])
        
    return svo_list
            
    # G.add_edge(sub, obj, label = verb)
            
    # nx.write_gexf(G, "graph.gexf")
def generate_graph(svo_list):
    G = nx.DiGraph()
    for svo in svo_list:
        sub, verb, obj = svo
        G.add_edge(sub, obj, label = verb)
    nx.write_gexf(G, "graph.gexf")

def draw_graph():
    G = nx.read_gexf("graph.gexf")
    # largest_component = max(nx.strongly_connected_components(G), key=len)
    # G = G.subgraph(largest_component)
    print(G.number_of_nodes())
    nx.draw(G, with_labels = True)
    plt.show()

    
if __name__ == "__main__":
    svo_list = get_common_svos()
    generate_graph(svo_list)
    draw_graph()

    