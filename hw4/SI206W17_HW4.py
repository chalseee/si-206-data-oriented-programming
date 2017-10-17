import unittest
import requests
from bs4 import BeautifulSoup

## SI 206 - W17 - HW4
## COMMENT WITH:
## Your section day/time: Friday/9AM
## Any names of people you worked with on this assignment: Cristian Guillen
		##We worked together on solving the last two parts of the project together and on parsing the data in different ways.

#####################

## PART 1 (100 points) - Get the HTML data from http://www.nytimes.com (the New York Times home page) and save it in a file called nytimes_data.html.

## Write the Python code to do so here.
nytimestext = requests.get('https://nytimes.com').text
fileref = open('nytimes_data.html', 'w', encoding='utf-8')
fileref.write(nytimestext)
fileref.close()
#####################

## PART 2 (200 points)
## Write code to get the first 10 headlines from the New York Times, based on the data you saved in the file in Part 1, and save those strings in a list called nytimes_headlines. 

## Note that you will almost certainly need to do some investigation on the http://nytimes.com website to do this correctly, even after saving the file in Part 1.

## The strings that should be elements of your lists will be different depending upon when you accessed the data, but they should probably be somewhat like this:

## U.S. Files Charges Against Rahami in Series of Bombings
## In a Play, a Take of a Bombing. A Block Away, a Real Explosion
## The Interpreter: The War We'd Rather Not Talk About

## .. et cetera, for 10 headline strings.

## Weed out the headlines that do not have any text, for instance the headlines that are linked to pictures or video but without any text content. You should not add these to the list nor count them towards the limit of 10. Ignore them completely.

## Not sure where to start? This link might very helpful: http://www.practicepython.org/solution/2014/07/10/17-decode-a-web-page-solutions.html

## We have included a couple of unit tests to check some things about your result, but we will also be checking your code against our OWN version of a nytimes_data.html file, which will almost certainly be different from yours, and your code should still work to get the first 10 text headlines from our file!

## Write your code to complete this task here.
## HINT: Remember that you'll need to open the file you created in Part 1, read the contets into one big string, and make a BeautifulSoup object out of that string!
## NOTE that the provided link does not include saving the online data in a file as part of the process. But it still provides very useful hints/tricks about how to look for and identify the headlines on the NY Times page.

soup = BeautifulSoup(nytimestext, 'html.parser')

nytimes_headlines = []
for heading in soup.find_all(class_='story-heading'):
	if heading.a: 
		nytimes_headlines.append(heading.a.text.replace('\n', ' ').strip())
	else: 
		nytimes_headlines.append(heading.contents[0].strip())

nytimes_headlines = nytimes_headlines[:10]

#####################

## PART 3 (200 points)

## Go to this URL: https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All

## Use the requests library (or other Python code that has the same effect) and Beautiful Soup to gather, from that web page, each of the names and the titles.
## You should create a dictionary called umsi_titles which contains the names and the titles for each person on that page. For example, your dictionary should include the following key-value pairs (and a bunch more...):

## "Lindsay Blackwell":"PhD Student"
## "Reginald Beasley":"Admissions and Student Affairs Assistant"
## "Daniel Atkins III":"Professor Emeritus of Information, School of Information and Professor Emeritus of Electrical Engineering and Computer Science, College of Engineering"

## We have provided unit tests for this problem which you must pass to gain all 200 points for this part.

## Write code to complete this task here. We've gotten you started... note that it'll be difficult to continue if you don't understand what the provided code does!

response = requests.get('https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=All')
htmldoc = response.text

soup = BeautifulSoup(htmldoc,'html.parser')
people = soup.find_all('div', {'property':'dc:title'})
title = soup.find_all('div', {'class':'field-name-field-person-titles'})
umsi_titles = {}
listppl = []
listtitle = []


for p in people:
	listppl.append(p.get_text())

for t in title:
	listtitle.append(t.get_text())

count = 0
for y in listppl:
	umsi_titles[y] = listtitle[count]
	count += 1

## It may be helpful to translate the following from English to code:

## For each element in the list saved in the variable people,
## Find the container that holds the name that belongs to that person (HINT: look for something unique, like a property element...)
## Find the container that holds the title that belongs to that person (HINT: a class name)
## Grab the text of each of those elements and put them in the dictionary umsi_titles properly










######### UNIT TESTS; DO NOT CHANGE ANY CODE BELOW THIS LINE #########
#### NOTE: hard-coding to pass any of these tests w/o following assignment instructions is not acceptable for points
class HW4_Part2(unittest.TestCase):
	def test_first_last_elem(self):
		self.assertEqual(type(nytimes_headlines[0]),type(""), "Testing that the first type in the nytimes_headlines list is a string")
		self.assertEqual(type(nytimes_headlines[-1]),type(""), "Testing that the last type in the nytimes_headlines list is a string")
	def length_of_ten(self):
		self.assertEqual(len(nytimes_headlines),10, "Testing that there are ten headlines in the list")

class HW4_Part3(unittest.TestCase):
	def test_key_value(self):
		self.assertEqual(umsi_titles["Eytan Adar"],"Associate Professor of Electrical Engineering and Computer Science, College of Engineering and Associate Professor of Information, School of Information", "Testing one key-value pair that should be in your umsi_titles diction")
	def test_key_value2(self):
		self.assertEqual(umsi_titles["Ben Armes"],"Videographer", "Testing another key-value pair that should be in your umsi_titles diction")
	def test_len_items(self):
		self.assertEqual(len(umsi_titles.keys()),20, "Testing that there are 20 keys in the dictionary umsi_titles")
	def test_full_dict_items(self): 
		self.assertEqual(sorted(umsi_titles.items()),[('Alicia Baker', 'Administrative Assistant'), ('Andrea Barbarin', 'PhD student'), ('Ben Armes', 'Videographer'), ('Daniel Atkins III', 'Professor Emeritus of Information, School of Information and Professor Emeritus of Electrical Engineering and Computer Science, College of Engineering'), ('Deborah Apsley', 'Director of Human Resources and Support Services'), ('Eytan Adar', 'Associate Professor of Electrical Engineering and Computer Science, College of Engineering and Associate Professor of Information, School of Information'), ('Julia Adler-Milstein', 'Associate Professor of Information, School of Information and Associate Professor of Health Management and Policy, School of Public Health'), ('Lindsay Blackwell', 'PhD student'), ('Mark Ackerman', 'George Herbert Mead Collegiate Professor of Human-Computer Interaction, Professor of Information, School of Information and Professor of Electrical Engineering and Computer Science, College of Engineering'), ('Marsha Antal', 'School Registrar'), ('Mohamed Abbadi', 'PhD student'), ('Nancy Benovich Gilby', 'Ehrenberg Director of Entrepreneurship, Adjunct Clinical Associate Professor of Information and Research Investigator, School of Information'), ('Rasha Alahmad', 'PhD student'), ('Reginald Beasley', 'Admissions and Student Affairs Assistant'), ('Sarah Argiero', 'Academic Advisor'), ('Seyram Avle', 'Research Investigator, Information and Research Fellow, School of Information'), ('Tawfiq Ammari', 'PhD student'), ('Todd Ayotte', 'Director of Finance'), ('Vadim Besprozvany', 'Lecturer III in Information, School of Information and Intermittent Lecturer in Residential College, College of Literature, Science, and the Arts'), ('Wei Ai', 'PhD student')], "Testing the entire dictionary contents")

if __name__ == "__main__":
	unittest.main(verbosity=2)