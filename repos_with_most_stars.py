import requests
from repository import Repository


def repos_with_most_stars(
    total_count=10,
    min_stars=50000,
    sort="stars",
    order="desk"
):

    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    params = {
        "q": create_query(min_stars=min_stars, languages=["JavaScript"]),
        "sort": sort,
        "order": order,
        "total_count": f"{total_count} "
    }

    response = requests.get(gh_api_repo_search_url, params=params)

    if response.status_code != 200:
        raise RuntimeError(
            f"an error occurred. status code was {response.status_code}"
        )
    else:
        return response.json().get('items')


def create_query(min_stars, languages):
    query = f"stars:>{min_stars} "

    if languages == None:
        languages = ["JavaScript", "Python"]

    for language in languages:
        query += f"language:{language} "

    return query


if __name__ == '__main__':
    repos = repos_with_most_stars(total_count=10)

    for repo in repos:
        item = Repository(
            name=repo.get('name'),
            number_of_stars=repo.get('stargazers_count'),
            language=repo.get('language'),
        )

        print(item)
