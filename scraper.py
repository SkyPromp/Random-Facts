from bs4 import BeautifulSoup
import requests


def fact():
    return BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Special:Random").text, 'lxml').find("div", id="mw-content-text").find("div", class_='mw-parser-output').find_all("p")[1].text.strip()


def subjectAndFact():
    return (lambda x: [x.find("h1", id="firstHeading").text, x.find("div", id="mw-content-text").find("div", class_='mw-parser-output').find_all("p")[1].text.strip()])(BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Special:Random").text, 'lxml'))


print(subjectAndFact())
