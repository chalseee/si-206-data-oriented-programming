## Winter 2017
## SI 206 - Programming I

## Extra Credit Assignment

####### INSTRUCTIONS #######

## This assignment is extra credit, and it is especially encouraged for those who found the midterm or concepts before the midterm challenging or who would like to revisit them.

## In this assignment you will revisit eight exercises from the midterm. We have chosen these questions based on class-wide midterm statistics AND which specific concepts these questions address. For extra credit, you may complete any of the ones that you did not receive full points for on the midterm!

## For each of these problems, you are required to correctly solve each exercise, in either a comment or writing code, as appropriate, in this file, and add a reflection underneath your solution in comments that briefly describes:

## - What your confusion or misunderstanding was on the midterm OR what was incorrect about the answer that you put on the exam if you answered the question.

## - Why the correct answer is correct. If the answer involves writing code, write 1-3 sentences explaining what the code does, or comment each line. If the answer involves determining code output, write 1-3 sentences explaining why it outputs that code. If the answer is a multiple choice question, write 1-2 sentences about why that option (or those options) are the correct ones.

# Brevity is encouraged! correctness is also important.

## You could potentially get UP TO 400 extra credit points in the course with this assignment. Each question revisit is worth 50 points. You may complete as many or as few of these six as you want, as long as you did not get full credit on them on the midterm.

## You may use any resources, help, etc. to complete this. You must write the comments explaining incorrect/correct answers by yourself, in your own words. When we release a solution set for the midterm, you may use that, you may use the rubric that shows correct answers, and you may certainly run the code to test it out! We encourage you to come up with the answer on your own and test it by running the code so you really test your understanding.

## This file must run without syntax errors when you turn it in. Everything that needs commenting-out should be commented out, and it should not include any characters that cannot be in a Python file, etc. (Copying and pasting from e.g. Word can cause that, so be careful.) Test it before you turn it in!

## Deadline to submit on Canvas: Tuesday, March 14th at 11:59 PM

############ END INSTRUCTIONS ############
print("\n*******\n")

## (Midterm 3). What is the output after the following code runs?

def func(x):
    for item in x:
        return x

print(func([1,2]))

## Put your answer to the question here:
	# [1,2]

## Put your comment explanations/reflections here:
#  - For this problem, I answered 1 instead of [1,2]. I did this because I made a mistake and assumed that the problem would be returning the variable ‘item’ instead of ‘x’. 
#  - [1,2] is the correct answer because the return statement in func(x) says to return whatever was passed in (which was [1,2]). item just refereed to the first object in [1,2] but actually had no effect on what the function returns.
 		
print("\n*******\n")

## (Midterm 6) Which of the following statements (in comments) are valid to create an instance of class Card and save it to the variable x, with no errors? (Reference cards.py / the code on the exam)

# a. x = Card.create()
# b. x = Card(2.3)
# c. x = Card(5,3)
# d. x = Card(2)
# e. x = Card.__init__
# f. x = Card(1, "Queen")

## Put your answer to the question here:

	# I got this question correct on the midterm

## Put your comment explanations/reflections here:


print("\n*******\n")

## (Midterm 7). Write an additional method for the Card class called compare_rank. You can assume the method is correctly placed inside the class, but you can write it by copying the Card class definition into this file, OR you can write it and test it in the cards.py file and copy it into this file commented out. (Otherwise, it won't run!)

## This method should return a boolean value True if the input rank number is larger than the Card's rank, and False if it is smaller or equal to the Card's rank.

## For example, the following code should work correctly when placed inside the Card class definition, if the compare_rank method is defined correctly:

# c = Card(2,11)
# print(c.compare_rank(4)) # should print False
# print(c.compare_rank(13)) # should print True

## Remember this code WILL NOT RUN here without the Card class definition here and the method defined properly.

## Put your answer to the question here:
def compare_rank (self, num):
	if (num > self.rank_num):
		return True
	if (num < self.rank_num):
		return False
	if (num == self.rank_num):
		return False

## Put your comment explanations/reflections here:
#  - For this problem, I my input comparison syntax was correct but the values I used in the comparison were incorrect.
#  - To correct my answer, I used the same code that I wrote in the exam. Only this time, I replaced all instances of the variable self.rank with self.rank_num. Otherwise, the logic of the problem is the same.


print("\n*******\n")

## (Midterm 9). Given the following code, there is 1 possible value of var such that every print statement will print out. What is the only possible type that value could be? (In your reflection/explanation, explain briefly why.)

var = " ???? replace this "
if var[1:3] == "py":
    print("Yup!")
if var[-1] == 'x':
    print("Nice")
if len(var) == 4:
    print(False)
if 'm' in var:
    print("Done")

## Put your answer to the question here:
	#string

## Put your reflections/explanations here:
#   - For this problem, I did give the correct answer, but I added other variable types as answers that weren’t correct. I was confused about what var would return when it is entered as different types.
#   - The correct answer type for var is string. It cannot be a list or a tuple, because if you access certain parts of a tuple or list in the same way var is accessed then a tuple or list will be returned. And if that happens, the selection will never be equivalent to the string selection and nothing will ever print.



print("\n*******\n")

## (Midterm 10). What will print when the following code runs? If there will be an error, say so.

stuff = {"purple": [9,106,506,'SI','Yu-Jen','Mauli'],"blue": "Cornflower", 42: "Green"}
print(stuff['purple'][3] + stuff["blue"][0]) 


## Put your answer to the question here:

	#I got this question correct on the midterm

## Put your comment explanations/reflections here:



print("\n*******\n")

## (Midterm 15, 15 number 2). (Also refer to the code and instructions on pages 7 and 8 of the midterm PDF.) Write 2 more tests for class Student to check that it does precisely what the description on page 7 says it ought to do. You should create a new test class in which to do put these tests. 

## Note that if you write them here, either they will not run without invoking unittest.main() -- which is OK, you need not do so -- OR they will all fail because the class Student is not defined. Still, we are looking for accurate, syntactically correct tests that will test the methods of class Student as specified in the question.

## Put your answer to the question here:

	# I got this question correct on the midterm.

## Put your reflections/explanations here. (Remember, brief.)



print("\n*******\n")

## (Midterm 18). Given the following code, you want to sort the list saved in lst1 to end up in the following order: ["happy","absence","something","synergy"]. Which of the 3 following named functiosn should be the KEY PARAMETER of the sorted function (replacing the question marks in the commented line below)?

lst1 = ["happy","absence","synergy","something"]

# (a)
def second_elem(x):
    return x[1]

# (b)
def sec_elements(lst):
    for x in lst:
        return x

# (c)
def sort_by(lst):
    return len(lst)

# this is the sorted line that needs one of those names as addition...
# sorted_lst1 = sorted(lst1, key = ???)


## Put your answer to the question here:

	#I got this question correct on the midterm

## Put your reflections/explanations here:

print("\n*******\n")

## (Midterm 21). Given the following code:

import requests
import json
baseurl = "http://itunes.apple.com/search"
params = {}
params["term"] = "Franz Ferdinand"
params["entity"] = "musicVideo"
r = requests.get(baseurl, params=params)

## What is the type of the variable r?

# a. A File object
# b. A BeautifulSoup object
# c. A Response object
# d. A string
# e. A dictionary

## Put your answer to the question here:

	# c. A Response object

## Put your reflections/explanations here:
#   - For this problem, I had answered type dictionary (e.) which was incorrect. I thought that when you call requests.get() your answers would immediately be in a dictionary that you could access
#   - The correct answer type for r is a response object because requests.get() returns a lot of information that isn’t a dictionary. It is an amalgamation of things that have been pulled from a server. It’s a response object.
