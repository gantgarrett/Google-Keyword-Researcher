import requests
import string
import json
import pandas as pd

url = "https://suggestqueries.google.com/complete/search"
alphabet = string.ascii_lowercase

def jsonList_LetterBefore(keyword):
	List = []
	for letter in alphabet:
		params = {"client": "Chrome", "q": letter + " " + keyword}
		r = requests.get(url, params = params)
		x = r.json()
		List.append(x[1])
	return List

def jsonList_LetterAfter(keyword):
	List = []
	for letter in alphabet:
		params = {"client": "Chrome", "q": keyword + " " + letter}
		r = requests.get(url, params = params)
		x = r.json()
		List.append(x[1])
	return List

keyword = input("Enter a keyword: ")

LetterAfterList = jsonList_LetterAfter(keyword)
print (LetterAfterList)

df = pd.DataFrame(LetterAfterList).stack().reset_index()
df.to_csv(r'/home/garrett/Desktop/GoogleSuggest.csv', mode='a', header=False)
