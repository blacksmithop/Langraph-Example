def stream_graph_updates(graph, user_input: str):
    for event in graph.stream({"messages": [("user", user_input)]}):
        for value in event.values():
            yield value["messages"][-1].content
