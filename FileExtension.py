import pathlib


def extension(path):
    try:
        p = pathlib.PurePosixPath(path).suffix
        if not pathlib.Path(path).exists():
            raise ValueError
    except ValueError:
        p = "cannot find file extension"

    return p
