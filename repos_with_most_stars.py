import requests


def repos_with_most_stars(total_count=10, min_star=50000):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    params = {"q": f"stars:>{min_star} ", "total_count": total_count}

    return requests.get(gh_api_repo_search_url, params=params)


if __name__ == '__main__':
    items = repos_with_most_stars(total_count=10).json().get('items')

    for i in items:
        language = i.get('language')
        stars = i.get('stargazers_count')
        name = i.get('name')

        print(f"'{name}' on {language} : {stars} ⭐️")
