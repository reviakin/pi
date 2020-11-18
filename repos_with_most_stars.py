import requests


def repos_with_most_stars(total_count=10, q="stars:>50000"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    params = {"q": q, "total_count": total_count}

    response = requests.get(gh_api_repo_search_url, params=params)

    return response


def madeJson(req):
    return req.json()


if __name__ == '__main__':
    items = madeJson(repos_with_most_stars(total_count=10)).get('items')

    for i in items:
        language = i.get('language')
        stars = i.get('stargazers_count')
        name = i.get('name')

        print(f"{name} / {language} : {stars}")
