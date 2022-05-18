from collections import deque  # Standard library to import the queue class


def person_is_seller(name):
    """Function to check if the last character of a person's name ends in m. Dummy function to fulfill task

    Args:
        name (string): The name/node to be searched

    Returns:
        Boolean: Returns True if last character is m, and False if last character is not m.
    """

    return name[-1] == "m"


def bfs(search_queue):
    """Breath First Search Algorithm. Searchs through a queue for a positive node

    Args:
        search_queue (queue)): A queue made from dictionaries pairing names as keys to a list of names as values

    Returns:
        Boolean: Returns True if person_is_seller function is true, and False if the person_is_seller fucntion is false
    """

    searched = {"not_a_name"}
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is mango seller!")
                return True
            else:
                searched.add(person)
                search_queue += graph[person]
    return False


if __name__ == "__main__":
    graph = {}
    graph["you"] = ["alice", "bob", "claire"]
    graph["bob"] = ["anuj", "peggy"]
    graph["alice"] = ["peggy"]
    graph["claire"] = ["thom", "johnny"]
    graph["anuj"] = []
    graph["peggy"] = ["alice"]
    graph["thom"] = []
    graph["johnny"] = []

    search_queue = deque()
    search_queue += graph["you"]

    bfs(search_queue)
