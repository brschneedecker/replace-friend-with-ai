# chats-ai

## Background

This project trains an N-gram langauge model to generate text based on text communications between you and a friend. Text communications are parsed from several storage formats.

 * **Jabber**: Jabber stores chats locally as HTML files. The contents of these Jabber chat messages were extracted from this HTML for training the language model.
 * **SMS**: SMS messages were exported to XML using the [SMS Backup & Restore](https://play.google.com/store/apps/details?id=com.riteshsahu.SMSBackupRestore&hl=en_US&gl=US) Android app. The contents of these messages were extracted from the XML according to the phone number specified in the configuration file (see below for more information).

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
conda-env remove -n chats_ai_env
```

### Run Instructions

When you clone the repository you will get a file called ```example.config.py```. Rename this file to ```config.py``` and set the parameters in the file according.
* ```my_name```: Your name!
* ```buddy_name```: Your friend's name
* ```buddy_number```: Your friend's number (for filtering SMS message XML to correct messages)

Start the program with the following terminal command:
```bash
python3 chats_ai.py [-h] n path
```

Example with a 3-gram model and source data in folder "corpus"
```bash
python3 chats_ai.py 3 corpus
```

You will then be presented with a prompt to enter the maximum number of tokens you'd like to see in the generated message. An example is shown below. Note that
```bash
Please enter the message length in tokens or 'q' to quit: 8
Mirror . dingus
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* https://www.pluralsight.com/guides/extracting-data-html-beautifulsoup
* https://www.geeksforgeeks.org/how-to-scrape-data-from-local-html-files-using-python/
* https://beautiful-soup-4.readthedocs.io/en/latest/index.html?highlight=select_one
* https://www.geeksforgeeks.org/how-to-parse-local-html-file-in-python/
* https://stackoverflow.com/questions/14924200/loading-huge-xml-files-and-dealing-with-memoryerror
* https://www.geeksforgeeks.org/command-line-interface-programming-python/

