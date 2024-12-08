from collections import defaultdict
from collections import deque
import re


def read_data(file_name):
    def get_edges(text):
        edges = []
        for line in text.split("\n"):
            if len(line) == 0:
                continue
            line = line.strip().split("|")
            edges.append((int(line[0]), int(line[1])))
        return edges

    def get_pages(text):
        pages_to_prod = []
        for line in text.split("\n"):
            if len(line) == 0:
                continue
            line = line.strip()
            pages_to_prod.append([int(x) for x in line.split(",")])
        return pages_to_prod

    with open(file_name, "r", encoding="utf-8") as fp:
        full_data = fp.read().strip()
        edges, page_lists = re.split(r"\n\s*\n", full_data)
        return get_edges(edges), get_pages(page_lists)


def build_graph(edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
    return graph


def validate(graph, pages):
    for i, page in enumerate(pages):
        children = graph[page]
        x = set(pages[:i])
        for child in children:
            if child in x:
                return []
    return pages


# def get_edges_and_vertices(text):

#     def get_edges(text):
#         edges = []
#         for line in text.split("\n"):
#             if len(line) == 0:
#                 continue
#             line = line.strip().split("|")
#             edges.append((int(line[0]), int(line[1])))
#         return edges

#     def get_vertices(edges):
#         vertices = set()
#         for left, right in edges:
#             vertices.add(left)
#             vertices.add(right)
#         return vertices

#     edges = get_edges(text)
#     vertices = get_vertices(edges)
#     return edges, vertices


# def get_pages_to_produce(text):
#     pages_to_prod = []
#     for line in text.split("\n"):
#         if len(line) == 0:
#             continue
#         line = line.strip()
#         pages_to_prod.append([int(x) for x in line.split(",")])
#     return pages_to_prod


# def topological_sort(vertices, edges):
#     graph = defaultdict(list)
#     in_edges = {v: 0 for v in vertices}

#     # populate the graph and in_edges dict
#     for u, v in edges:
#         graph[u].append(v)
#         in_edges[v] += 1

#     # initialize the queue and order_arr
#     queue = deque([v for v in vertices if in_edges[v] == 0])
#     print(in_edges)
#     topological_arr = []

#     while queue:
#         element = queue.popleft()
#         topological_arr.append(element)

#         for neighbor in graph[element]:
#             in_edges[neighbor] -= 1

#             if in_edges[neighbor] == 0:
#                 queue.append(neighbor)

#     return topological_arr


# def part_one(text, pages_to_prod_text):
#     edges, vertices = get_edges_and_vertices(text)
#     ordered_elements = topological_sort(vertices, edges)

#     sample_pages_to_prod = get_pages_to_produce(pages_to_prod_text)

#     selected_pages = []
#     for page_to_prod in sample_pages_to_prod:
#         topo_idx = 0
#         page_idx = 0

#         while page_idx < len(page_to_prod) and topo_idx < len(ordered_elements):
#             if ordered_elements[topo_idx] == page_to_prod[page_idx]:
#                 topo_idx += 1
#                 page_idx += 1
#             else:
#                 while (
#                     topo_idx < len(ordered_elements)
#                     and ordered_elements[topo_idx] != page_to_prod[page_idx]
#                 ):
#                     topo_idx += 1

#         if page_idx == len(page_to_prod):
#             selected_pages.append(page_to_prod)

#     return sum([x[len(x) // 2] for x in selected_pages])


if __name__ == "__main__":
    sample_page_orders = """
                        47|53
                        97|13
                        97|61
                        97|47
                        75|29
                        61|13
                        75|53
                        29|13
                        97|29
                        53|29
                        61|53
                        97|53
                        61|29
                        47|13
                        75|47
                        97|75
                        47|61
                        75|61
                        47|29
                        75|13
                        53|13"""

    sample_pages_to_produce = """
                                75,47,61,53,29
                                97,61,53,29,13
                                75,29,13
                                75,97,47,61,53
                                61,13,29
                                97,13,75,29,47"""

    edges, pages = read_data("./data/day_05_example.txt")
    graph = build_graph(edges)
    valid_pages = []
    for page in pages:
        valid = validate(graph, page)
        valid_pages.append(valid)

    print(sum([x[len(x) // 2] for x in valid_pages if x]))
