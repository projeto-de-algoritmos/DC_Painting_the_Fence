import pydotplus

fence = [0]
enumerated_fence = []
commands = []
graph = pydotplus.Dot(graph_type='digraph')

n = int(input())
fence += [int(x) for x in input().split()]
enumerated_fence = list(enumerate(fence))


def solve(l, r, h, parent=None):
    if l > r:
        return 0

    min_idx = min(enumerated_fence[l:r+1], key=lambda p: p[1])[0]

    node_info = f'[{l}, {r}]'
    edge = None
    if parent:
        edge = pydotplus.Edge(parent, node_info)
        graph.add_edge(edge)

    h_strokes_l = solve(l, min_idx - 1, fence[min_idx], node_info)
    h_strokes_r = solve(min_idx + 1, r, fence[min_idx], node_info)
    h_strokes_local = fence[min_idx] - h

    h_strokes = h_strokes_local + h_strokes_l + h_strokes_r
    v_strokes = r - l + 1

    if v_strokes <= h_strokes:
        if edge is not None:
            edge = pydotplus.Edge(
                node_info,
                parent,
                label=f'vertical = {v_strokes}',
                labelfontcolor='green'
            )
            graph.add_edge(edge)
        return v_strokes

    if edge is not None:
        edge = pydotplus.Edge(
            node_info,
            parent,
            label=f'horizontal = {h_strokes}',
            labelfontcolor='green'
        )
        graph.add_edge(edge)
    return h_strokes

print('Mínimo de movimentos:', solve(1, n, 0))
graph.write_png('result.png')
