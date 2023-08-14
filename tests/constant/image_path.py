from pathlib import Path

PAGE = 'pages'
IMAGE = 'images'


class ImagePath:
    TAB_MY_PROFILE = Path.cwd().parent.joinpath(PAGE).joinpath(IMAGE).joinpath('tab_my_profile.png')
