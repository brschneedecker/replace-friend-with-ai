# jabber-html

This project parses the HTML representations of locally archived Jabber messages and stores them as a custom object.

The end goal of the project is to create a chat bot that generates sweet, sweet memes from the source message data.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installation

Clone the repository

```bash
git clone https://github.com/brschneedecker/jabber-html.git
```

Navigate to the repo directory

```bash
cd [clone path]/jabber-html
```

Create conda environment to install required packages

```bash
conda env create --file=environment.yaml
```

Activate the newly created environment

```bash
conda activate chats_ai_env
```

If you have issues with the environment after creation, you can remove it with the following

```bash
conda-env remove -n jabber_html_env
```

### Run Instructions

TBD

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup
* https://www.geeksforgeeks.org/how-to-scrape-data-from-local-html-files-using-python/
* https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=select_one
* https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/
* https://stackoverflow.com/questions/14924200/loading-huge-xml-files-and-dealing-with-memoryerror

