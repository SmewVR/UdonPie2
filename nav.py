from itertools import cycle

udon_types = {
  'AINavMeshAgentRef': 'UnityEngineAINavMeshAgentRef'
}

x = []


def iterate():
    total_items = len(udon_types)
    for item in cycle(udon_types.items()):
        if total_items == 0:
            break
        print(item)
        total_items -= 1

iterate()