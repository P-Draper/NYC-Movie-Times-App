<p align="center">
    <a href=""><img src="https://img.shields.io/pypi/l/ansicolortags.svg" /></a>
    <a href=""><img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" /></a>
    <br>
    <a href="https://docs.python.org/3/index.html"><img src="https://img.shields.io/badge/python-%2320232a?style=for-the-badge&logo=python&logoColor=ffdd54" /></a>
    <br>
    <a href=""><img src="https://dtmvamahs40ux.cloudfront.net/gl-academy/course/course-1212-bs.jpg" /></a>

</p>

<h1 align="center"><b>NYC Movie times App</b></h1>
<h4 align="center">A web application built using BeautifulSoup and Custome Tkinter for viewing up to date movie times from independant theaters in the NYC area. This interface allows users to view scraped data from multiple sites in one place. </h4>


## Table of Contents

- [Introduction](#introduction)
- [Technical Requirements](#technical-requirements)
- [Project Structure](#project-structure)
- [Key Functionalities](#key-functionalities)
- [Getting Started](#getting-started)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The NYC Movie times App provides a way for users to see up to date data from multiple different independant theaters in the NYC area in one place so that they can make a better informed decision about their viewing experience.

## Technical Requirements

To run the NYC Movie times App locally, you need the following:

- Python 3.7 or later
- CustomTkinter 5.2.0 or later
- BeautifulSoup 4.12.2 or later

## Project Directory Hierarchy

Upon successful setup (see **Getting Started**), you should see the following project directory hierarchy.

```
NYC Movie times App/
├── app.py
├── synscraper.py
├── mgscraper.py
├── test.py
├── REFLECTION.md
├── Pipfile
└── README.md
```

- `app.py`: Main application file containing the Dash app code and callbacks.
- `synscraper.py`: Webscraper built to target data from Syndicated Theater.
- `mgscraper.py` : Webscraper built to target data from Metrograph Theater.
- `test.py` : Test file made to view the 'soup', or the initial parse from 
    beautifulsoup so that it can be more easily manipulated.
- `Pipfile` and `Pipfile.lock`: Files specifying project dependencies when using `pipenv`.
- `REFLECTION.md`: Notes on beautifulsoup and tkinter.
- `README.md`: Project documentation providing an overview, setup instructions, and other details.

## Key Functionalities

    Current functionality of the app is to scrape the Metrograph and Syndicated sites for the titles and showtimes and populate it to the CTkinter.


    In the future I will add -
    1. functionality to permanently store the data so that you could view legacy data if you were interested and so that if your system goes offline you can still pull information that you've snapshotted.
    2. functionality to cross reference titles automatically with the imdb api.
    3. functionality to sign in and set alerts for your account (tied to email) that a specific movie (or director's films) is playing.
    4. functionality to alert for special Q&A events.
    5. search filters/toggles
    6. location services to search for theaters closest to you, or sort by range.

## Getting Started

1. Clone this repository to your local machine:

```bash
git clone git@github.com:P-Draper/NYC-Movie-Times-App.git
```

2. Navigate to the project directory:

```bash
cd NYC-Movie-Times-App
```

3. Install the required dependencies using pipenv:

```bash
pipenv install
```

4. Run the Dash app:

```bash
pipenv run python app.py
```

## Dependencies

The NYC Movie times App relies on the following libraries:

- BeautifulSoup: A Python library designed for webscraping.
- CustomTkinter: A Python UI-library based on Tkinter which provides customizable widgets.

## Contributing

Contributions to the NYC Movie times App are welcome! If you encounter any issues, have feature suggestions, or would like to contribute code, please open an issue or pull request on the GitHub repository.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
