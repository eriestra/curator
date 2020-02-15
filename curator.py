#!/usr/bin/python
# -*- coding: utf8 -*-
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
import json
import time 

option = webdriver.ChromeOptions()
option.add_argument(" - incognito")
option.add_argument('headless')

browser = webdriver.Chrome(options=option)

course_title = "javascript"

course_outline = {
  "Fundamentos de programación": [
    "variables",
    "primitives",
    "types",
    "conditionals",
    "control flow",
    "logical operators",
    "math operators",
  ],
  "DOM y JQuery": [
    "Document Object Model",
    "JQuery",
  ],
  "ECMAScript 6": [
    "NodeJS",
    "Babel",
    "NPM",
    "ES6"
  ],
  "Algoritmia y Estructuras de datos": [
    "Arrays",
    "Filesystem",
    "Data Structures",
    "Algorithms",
    "Sorting"
  ],
  "JSON y APIs": [
    "JSON",
    "REST API"
  ],
  "Programación Asíncrona": [
    "Async",
    "Callstack",
    "Event loop"
  ],
}

learning_keywords = {
  "Video" : "&tbm=vid",
  "Tutorial" : "+tutorial",
  "Quiz" : "+quiz",
  "CheatSheet" : "+cheatsheet",
  "Book" : "+book",
  "Course" : "+course",
}

# Applications: tbm=app
# Blogs: tbm=blg
# Books: tbm=bks
# Discussions: tbm=dsc
# Images: tbm=isch
# News: tbm=nws
# Patents: tbm=pts
# Places: tbm=plcs
# Recipes: tbm=rcp
# Shopping: tbm=shop
# Video: tbm=vid

output = {}

for topic, blocks in course_outline.items():
  output[topic] = {}
  for block in blocks:
    output[topic][block] = {}
    for key, value in learning_keywords.items():
      output[topic][block][key] = []
      query = course_title + "+" + block.lower().replace(' ','+')
      browser.get("https://www.google.com/search?&q=" + query + "+" + value)
      contents = browser.find_elements_by_class_name('r')
      for content in contents:
        try:
          url = content.find_element_by_tag_name('a')
          lines = content.text.split('\n')
        
          print ("Query: " + query + value)
          print ("Resource: " + lines[0])
          print ("Type: " + key)
          print ("URL: " + url.get_attribute("href"))
          print ("--------")

          item = {}

          item['title'] = lines[0]
          item['type'] = key
          item['URL'] = url.get_attribute("href")

          output[topic][block][key].append(item)
        except: 
          pass
      
        time.sleep(1)

browser.close()