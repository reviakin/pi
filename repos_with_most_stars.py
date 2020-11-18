import requests


def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    response = requests.get(gh_api_repo_search_url)

    print(response.text)


if __name__ == '__main__':
    repos_with_most_stars()
