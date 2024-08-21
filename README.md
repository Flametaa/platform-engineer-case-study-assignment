# Platform Engineer Case study

Please note that normally I would implement the following (but I did not find the time to do so):
* a pre-commit file to run linters and keep the code clean
* unit tests for the code

## Part 1
In order to ensure that the program works well for you please install the requirements listed in `requirements.txt` or use docker to test the program.

In this part I created a python script called `url_link_extractor.py` to extract links from a list of urls. 
You can use the program by executing `python url_link_extractor.py -u "https://news.ycombinator.com/" -o "stdout"`.

There were some ambiguities for me when it comes to this task:
* I was not sure if we only want to extract suburls corresponding to the given url, or if we also want to extract external links: The program that I coded extracts all links that are found in the given URLs
* I'm not sure if the output must be sorted or not. I used a set to keep deduplicated links therefore the outputs might not be sorted.

## Part 2

The Dockerfile can be found under the `Dockerfile` file:
* You can use `docker build -t mydocker .` to build the dockerfile
* You can then run `docker run -it mydocker -u "https://news.ycombinator.com" -o stdout` to test the image
* I used `trivy` to scan the image for vulnerabilities:
  * Trivy will analyze the layers of the Docker image and compare the installed packages and libraries against its vulnerability database. It will then provide a report highlighting any known vulnerabilities found.
  * We get the following result ![all vulnerabilities](./resources/full_scan.png)
  * The scan will show us which package is responsible for the vulnerability, the severity of each vulnerability, the reason of the vulnerability (in `Title`) and the version of the package that fixes the issue if it exists:
    * In this case I had a high vulnerability due to an old version of setuptools that I resolved by installing the new version in the requirements file.
    * We have 7 High and 1 Critical vulnerabilities that come from the base image ![High vulnerabilities](./resources/critical_high_scan.png):
      * We need to be aware of the vulnerabilities that we have to see if they can pause potential security threats or bugs.
      * We can look for an alternative base image that resolves the vulnerabilities if they pose a threat for our application.
* I packaged the app in a kubernetes `Pod` (we can also go for a `Deployment` but `pod` seemed more appropriate in this case)
  * you can use `kubectl apply -f ./kubernetes/pod.yaml` (I did not test this)

## Part 3

I used CircleCI for implementing the CICD However I did not integrate this with Github.
Note that we need to configure the env variables $DOCKERHUB_USERNAME and $DOCKERHUB_PASSWORD.
We also need to update the image field in the pod specs.

# Part 4

This part can be found under the subdirectory `domain_extraction`, here you can find:
* `input_file.txt` containing the test case given in the problem statement
* Please note that the following solutions only work for domain names with `.com` suffix
* `domain_extractor_approach1.sh`: Using awk and sed and sort
  * We start by deleting everything after `.com` using `sed` by capturing the substring that comes before `.com` and replacing the full string by `{captured_string}.com`
  * Then we will use awk to get all domain names by using any combination of the following separators `[/:.]`
    * Since we are sure our string ends with `com` now we only need to output the last two strings in lowercase, with a dot separator `tolower($(NF-1)"."$NF)`
  * Last we apply sort -u to sort and remove duplicates
* `domain_extractor_approach2.sh`:
  * Using grep we can extract the string that matches the regex pattern `[a-zA-Z0-9-]+\.com`:
    * This means that we will extract any alphanumeric character or dash that comes before `.com`
  * We then use tr to make the string lowercase
  * Finally we apply sort -u to sort and remove duplicates

## Bonus
* Web scraping 
* Text processing and regular expressions
* Containerization and orchestration with Docker and Kubernetes
* Continuous integration and continuous delivery
  * Automated testing and deployment
* Container Security