import argparse
import json
from typing import Set
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup


def extract_absolute_links(url: str) -> Set[str]:
    """
    Extract all absolute links from a given URL
    Args:
        url (str): the URL to search links in.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    links = set()
    for link in soup.find_all("a"):
        href = link.get("href")
        parsed_href = urlparse(href)
        if parsed_href.netloc:
            # If href has netloc then it corresponds to an absolute URL
            # It isn't clear in the problem statement if we only need sub urls or all links
            # We can skip this if we don't want to list external links
            links.add(href)
        elif parsed_href.path:
            # Else the href is a sub url of our `url` parameter
            # We only need the path without the params
            absolute_url = urljoin(url, parsed_href.path)
            links.add(absolute_url)
    return links


def format_output(links: Set[str], output_format: str):
    if output_format == "stdout":
        for link in links:
            print(link)
    if output_format == "json":
        json_output = {}
        for link in links:
            parsed_link = urlparse(link)
            base_domain = f"{parsed_link.scheme}://{parsed_link.netloc}"
            relative_path = parsed_link.path
            if base_domain in json_output:
                json_output[base_domain].append(relative_path)
            else:
                json_output[base_domain] = [relative_path]
        print(json.dumps(json_output, indent=4))


def main():
    # Parse arguments using argparse (docs in https://docs.python.org/3/library/argparse.html)
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', nargs='+', required=True, help='HTTP URLs')
    parser.add_argument('-o', '--output', choices=['stdout', 'json'], required=True, help='Output format')
    args = parser.parse_args()

    full_links = set()
    # We can parallelize this for faster execution time
    for url in args.urls:
        links = extract_absolute_links(url)
        full_links = full_links.union(links)

    format_output(full_links, args.output)


if __name__ == '__main__':
    main()
