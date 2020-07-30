import os


def get_app_dir():
    return os.environ['PROJ_HOME']

def get_app_file(*paths):
    return path_join(get_app_dir(), *paths)

def get_webapp_dir(*paths):
    return path_join(get_app_dir(), 'webapp', *paths)

def get_tmp_dir(*paths):
    return get_webapp_dir('tmp', *paths)

def path_exist(path: str):
    return os.path.exists(path)

def path_join(*paths):
    return os.path.join(*paths)

def is_dir(path: str):
    return os.path.isdir(path)

def is_file(path: str):
    return os.path.isfile(path)

def get_dir_path(path: str):
    return os.path.dirname(path)

def get_dir_name(path: str):
    return get_file_name(get_dir_path(path))

def get_file_path(file: str):
    return os.path.join(get_app_dir(), file)

def get_file_name(path: str):
    return os.path.basename(path)
