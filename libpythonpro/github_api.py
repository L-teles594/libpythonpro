import requests


def buscar_avatar(usuario):
    """
    Busca o avatar de um usuário no Github
    :param usuario: str com o nome do usuário
    :return: str com o link do avatar
    """
    url = f'https://api.github.com/users/{usuario}'

    avatar = requests.get(url=url)
    avatar = avatar.json()['avatar_url']
    return avatar


print(buscar_avatar('renzon'))
