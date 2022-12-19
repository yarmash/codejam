#!/usr/bin/env python3

"""Fetch problems data and dump it to a json file."""

import json
import logging
import re
from datetime import date
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

ARCHIVE_URL = 'https://codingcompetitions.withgoogle.com/codejam/archive'
FIRST_YEAR = 2008
MIN_ROUNDS_PER_YEAR = 7
MIN_PROBLEMS_PER_ROUND = 3

logger = logging.getLogger(__file__)


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            # logging.FileHandler('debug.log'),
            logging.StreamHandler(),
        ]
    )


class year_cards():
    """Wait until cards for all years are present"""
    def __init__(self, locator, cards_number):
        self.locator = locator
        self.cards_number = cards_number

    def __call__(self, driver):
        year_cards = driver.find_elements(By.CSS_SELECTOR, self.locator)
        logger.info('Found %s year cards', len(year_cards))
        if len(year_cards) == self.cards_number:
            return year_cards
        return False


class round_containers():
    """Wait until all rounds' containers are present"""
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        containers = driver.find_elements(By.XPATH, self.locator)
        logger.info('Found %s rounds', len(containers))
        if len(containers) >= MIN_ROUNDS_PER_YEAR:
            return containers
        return False


class problem_containers():
    """Wait until all problems' containers are present"""
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        containers = driver.find_elements(By.CSS_SELECTOR, self.locator)
        logger.info('Found %s problems', len(containers))
        if len(containers) >= MIN_PROBLEMS_PER_ROUND:
            return containers
        return False


def dump_rounds(driver):
    logger.info('Getting url: %s', ARCHIVE_URL)
    driver.get(ARCHIVE_URL)

    num_years = date.today().year - FIRST_YEAR + 1  # number of years in the archive
    logger.info('Expecting %s year cards', num_years)

    cards = WebDriverWait(driver, 20).until(
        year_cards('.archive .mdc-layout-grid__cell:not(.archive-headings)', num_years)
    )

    years = []

    for card in cards:
        year = card.find_element(By.XPATH, './/p[1]').text.split()[-1]
        url = card.find_element(By.XPATH, './/a').get_attribute('href')
        years.append({'name': year, 'url': url})

    for year in years:
        logger.info('Processing year %s', year['name'])
        rounds = process_year(driver, year['url'])
        year['rounds'] = rounds

    with open('dump.json', 'w') as dump_file:
        json.dump(years, dump_file)


def process_year(driver, year_link):
    driver.get(year_link)

    round_divs = WebDriverWait(driver, 20).until(
        round_containers('//div[contains(@class, "schedule-row__past")]')
    )
    round_divs.reverse()

    rounds = []

    for div in round_divs:
        round_name = div.find_element(By.XPATH, './/span').text
        round_url = div.find_element(
            By.XPATH,
            './/div[contains(@class, "schedule-row-cell--action")]//a[contains(.,"View")][contains(.,"arrow_forward")]'
        ).get_attribute('href')

        rounds.append({'name': round_name, 'url': round_url})

    for round in rounds:
        logger.info("Processing round '%s'", round['name'])
        problems = process_round(driver, round['url'])
        round['problems'] = problems
    return rounds


def process_round(driver, round_link):
    driver.get(round_link)
    problem_divs = WebDriverWait(driver, 20).until(
        problem_containers('div.problems-nav-selector-item-container')
    )
    problems = []
    for div in problem_divs:
        problem_name = div.find_element(By.XPATH, './/p').get_attribute('textContent').strip()
        assert problem_name
        problem_url = div.find_element(By.XPATH, './/a[contains(.,"Open problem")]').get_attribute('href')
        problems.append({'name': problem_name, 'url': problem_url})

    for problem in problems:
        logger.info("Processing problem '%s'", problem['name'])
        test_sets = process_problem(driver, problem['url'])
        problem['test_sets'] = test_sets
    return problems


def process_problem(driver, problem_url):
    driver.get(problem_url)
    test_sets_container = WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#problem-select-selected-text'))
    )
    test_sets = re.findall(r'\b\d+pts\b', test_sets_container.text)
    return test_sets


def main():
    setup_logging()

    options = webdriver.ChromeOptions()
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    options.add_argument(f'--user-agent={user_agent}')
    options.add_argument('--incognito')

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        dump_rounds(driver)
    finally:
        driver.quit()


if __name__ == '__main__':
    sys.exit(main())
