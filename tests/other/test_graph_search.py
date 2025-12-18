import pytest

from patterns.other.graph_search import GraphSearch


@pytest.fixture
def sample_graph():
    return {
        "A": ["B", "C"],
        "B": ["C", "D"],
        "C": ["D", "G"],
        "D": ["C"],
        "E": ["F"],
        "F": ["C"],
        "G": ["E"],
        "H": ["C"],
    }


def test_graph_search_initialization(sample_graph):
    graph_search = GraphSearch(sample_graph)
    assert graph_search.graph == sample_graph


def test_find_path_dfs_simple(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_path_dfs("A", "D")
    assert path is not None
    assert path[0] == "A"
    assert path[-1] == "D"


def test_find_path_dfs_middle_start(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_path_dfs("G", "F")
    assert path is not None
    assert path[0] == "G"
    assert path[-1] == "F"


def test_find_path_dfs_unreachable(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_path_dfs("C", "H")
    assert path is None


def test_find_path_dfs_nonexistent_node(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_path_dfs("C", "X")
    assert path is None


def test_find_path_dfs_same_start_end(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_path_dfs("A", "A")
    assert path == ["A"]


def test_find_all_paths_dfs(sample_graph):
    graph_search = GraphSearch(sample_graph)
    paths = graph_search.find_all_paths_dfs("A", "D")
    assert len(paths) > 0
    assert all(path[0] == "A" and path[-1] == "D" for path in paths)


def test_find_shortest_path_dfs(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_shortest_path_dfs("A", "D")
    assert path is not None
    assert path[0] == "A"
    assert path[-1] == "D"
    # Should be shortest path
    assert len(path) <= 4


def test_find_shortest_path_bfs(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_shortest_path_bfs("A", "D")
    assert path is not None
    assert path[0] == "A"
    assert path[-1] == "D"


def test_find_shortest_path_bfs_middle_start(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_shortest_path_bfs("G", "F")
    assert path is not None
    assert path[0] == "G"
    assert path[-1] == "F"


def test_find_shortest_path_bfs_unreachable(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_shortest_path_bfs("A", "H")
    assert path is None


def test_find_shortest_path_bfs_nonexistent_node(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_shortest_path_bfs("A", "X")
    assert path is None


def test_find_shortest_path_bfs_same_start_end(sample_graph):
    graph_search = GraphSearch(sample_graph)
    path = graph_search.find_shortest_path_bfs("A", "A")
    assert path == ["A"]


def test_empty_graph():
    empty_graph = {}
    graph_search = GraphSearch(empty_graph)
    path = graph_search.find_path_dfs("A", "B")
    assert path is None


def test_single_node_graph():
    single_node = {"A": []}
    graph_search = GraphSearch(single_node)
    path = graph_search.find_path_dfs("A", "A")
    assert path == ["A"]

