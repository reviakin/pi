import requests


def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    params = {"q": "stars:>50000"}
    response = requests.get(gh_api_repo_search_url, params=params)

    print(response.text)


if __name__ == '__main__':
    repos_with_most_stars()
