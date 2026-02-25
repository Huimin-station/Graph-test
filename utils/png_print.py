def get_png(agent):
    graph_png = agent.get_graph().draw_mermaid_png()
    with open("../agent/graph_show/graph.png", "wb") as f:
        f.write(graph_png)
