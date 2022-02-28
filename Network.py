nodes = {}
links = {}
id_count = 0
updated = False


# provides ids for all components, counting up
def get_id():
    global id_count
    id_count = id_count + 1
    return str(id_count)


def get_with_id(component_id):
    if component_id in nodes:
        return nodes[component_id]
    if component_id in links:
        return links[component_id]


def remove_with_id(component_id):
    if component_id in nodes:
        nodes.pop(component_id)
    if component_id in links:
        links.pop(component_id)


class Component:
    def __init__(self, attributes):
        self.attributes = attributes
        self.id = 0

    def set_id(self, component_id):
        self.id = component_id


class Node(Component):
    def __init__(self, ip, mac, port, attributes):
        super().__init__(attributes)
        self.ip_address = ip
        self.mac_address = mac
        self.port = port

    def add_to_network(self):
        node_id = get_id()
        super().set_id(node_id)
        nodes[node_id] = self
        return node_id


class Controller(Node):
    def __init__(self, ip, mac, port, attributes={}):
        super().__init__(ip, mac, port, attributes)
        self.group = "C"


class Host(Node):
    def __init__(self, ip, mac, port, attributes={}):
        super().__init__(ip, mac, port, attributes)
        self.group = "H"


class Switch(Node):
    def __init__(self, ip, mac, port, attributes={}):
        super().__init__(ip, mac, port, attributes)
        self.group = "S"


class Link(Component):
    def __init__(self, source_id, target_id, link_value, attributes={}):
        super().__init__(attributes)
        self.source = source_id
        self.target = target_id
        self.value = link_value

    def add_to_network(self):
        edge_id = get_id()
        super().set_id(edge_id)
        links[edge_id] = self
        return edge_id

