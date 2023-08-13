import spacy
import networkx as nx
import itertools

def get_sub_obj_rel(sentence):
    sub = []
    obj = []
    relationship = []

    for token in sentence:
        if "subj" in token.dep_:
            sub.append(token.text)
        elif "obj" in token.dep_:
            obj.append(token.text)
        elif token.dep_ in ("attr", "acomp"):
            relationship.append(token.text)

    return sub, obj, relationship


if __name__ == "__main__":
    
    nlp = spacy.load('en_core_web_sm')
    

    input_question = input("Enter your question: ")
    
    input_question = nlp(input_question)
    
    subs, objs, relationships = get_sub_obj_rel(input_question)
           
    
    G = nx.read_gexf("graph.gexf")
    # print(G.nodes())
    
    print(f"subjs: {subs}, objs: {objs} , relationships: {relationships}")

    # pairs = list(itertools.product(A, B)) + list(itertools.product(A, C)) + list(itertools.product(B, C))
    
    for sub, obj in itertools.product(subs,objs):    
        if sub in G.nodes() and obj in G.nodes():
            if G.has_edge(sub, obj):
                print(G.get_edge_data(sub, obj)['sentence'])
    
    for sub, relationship in itertools.product(subs,relationships):
        if sub in G.nodes():
            for node in G.neighbors(sub):
                if G.get_edge_data(sub, node)['relationship'] == relationship:
                    print(G.get_edge_data(sub, node)['sentence'])
    
    for obj, relationship in itertools.product(objs,relationships):
        if obj in G.nodes():
            for node in G.neighbors(obj):
                if G.get_edge_data(obj, node)['relationship'] == relationship:
                    print(G.get_edge_data(obj, node)['sentence'])
   
    # elif relationship:
    #     if sub in G.nodes():
    #         for node in G.neighbors(sub):
    #             if G.get_edge_data(sub, node)['relationship'] == relationship:
    #                 print(G.get_edge_data(sub, node)['sentence'])
    #     if obj in G.nodes():
    #         for node in G.neighbors(obj):
    #             if G.get_edge_data(obj, node)['relationship'] == relationship:
    #                 print(G.get_edge_data(obj, node)['sentence'])
    # else:
    #     print("I don't know")
    
    