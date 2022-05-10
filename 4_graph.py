graph = {}

graph["you"] = ["alice", "bob", "claire"]  # list of neighbors
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []  # empty means they have no neighbors
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []
