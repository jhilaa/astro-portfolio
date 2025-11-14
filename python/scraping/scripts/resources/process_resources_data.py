import requests
from bs4 import BeautifulSoup
import csv

from scraping.utils import utils

def natural_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\natural_resources.csv", rows, ";")
    
    
def resources_by_planet_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\resources_by_planet.csv", rows, ";")
    
    
def refined_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\refined_resources.csv", rows, ";")
    
    
def atmospheric_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\atmospheric_resources.csv", rows, ";")
    
    
def composed_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\natural_resources.csv", rows, ";")
    
    
def composed_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\composed_resources.csv", rows, ";")
    
    
def other_resources_data_to_csv(soup: BeautifulSoup):
    rows=[]
    utils.export_csv(r"scraping\data\other_resources.csv", rows, ";")



print("✅ Scraping terminé, fichier resources.csv généré")

