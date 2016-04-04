

def get_id_from_path(path):
    slash_index = str.find(path, "/")
    if slash_index < 0:
        return None
    return path[slash_index+1:]


def update_field_if_present(port, received_port, name):
    if getattr(received_port, name, None):  # existing port is updated
        port[name] = received_port[name]
