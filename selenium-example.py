from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver  = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
