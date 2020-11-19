import requests


def repos_with_most_stars(total_count=10, min_stars=50000):

    gh_api_repo_search_url = "https://api.github.com/search/repositories"

    params = {
        "q": create_query(min_stars=min_stars, languages=["JavaScript"]),
        "sort": "stars",
        "order": "desk",
        "total_count": f"{total_count} "
    }

    return requests.get(gh_api_repo_search_url, params=params)


def create_query(min_stars, languages):
    query = f"stars:>{min_stars} "

    if languages == None:
        languages = ["JavaScript", "Python"]

    for language in languages:
        query += f"language:{language} "

    return query


if __name__ == '__main__':
    items = repos_with_most_stars(total_count=10).json().get('items')

    for i in items:
        language = i.get('language')
        stars = i.get('stargazers_count')
        name = i.get('name')

        print(f"'{name}' on {language} : {stars} ⭐️")
