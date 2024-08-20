# Platform Engineer Case study

Please note that I did not have time to implement unit tests to check the written code. Normally I would create unit tests using pytest and a step in the CICD to do unit testing as well.

## Part 1
In order to ensure that the program works well for you please install the requirements listed in `requirements.txt` or use docker to test the program.

In this part I created a python script called `url_link_extractor.py` to extract links from a list of urls. 
You can use the program by executing `python url_link_extractor.py -u "https://news.ycombinator.com/" -o "stdout"`.

There were some ambiguities for me when it comes to this task:
* I was not sure if we only want to extract suburls corresponding to the given url, or if we also want to extract external links: The program that I coded extracts all links that are found in the given URLs
* I'm not sure if the output must be sorted or not. I used a set to keep deduplicated links therefore the outputs might not be sorted.

