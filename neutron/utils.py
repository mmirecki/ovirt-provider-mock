

def get_id_from_path(path):
    slash_index = str.find(path, "/")

    if slash_index < 0:
        return None

    return path[slash_index+1:]
