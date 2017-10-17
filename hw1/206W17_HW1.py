import operator

# SI 206 Winter 2017
# Homework 1 - Code

##COMMENT YOUR CODE WITH:
# Section Day/Time: Friday/9AM
# People you worked with:
#########

## Task A. String manipulation (function 'string_manip')
def string_manip(s):
    s = s.strip() ##   First, remove any leading and trailing spaces from the input string.
    s = s.upper() ##   Convert the input string to upper case.
    s = s.replace(" ", "#") ##   Replace any remaining spaces in the string with the pound sign '#'.
    s = s.replace("UMSI", "") ##   Remove any occurrences of the string "UMSI" from the string.
    if len(s) == 1: ##   If the remaining string is a single character just return that string.
        return s        ##  Otherwise, return the string in reverse.
    return s[::-1]

## Task B. Dictionaries and sorting (function 'name_counts')
##Sort list of names, return as a sorted list of tuples (or dictionary)
def name_counts(names):
    uniques = set(names)
    uniques = list(uniques)

    for u in range(len(uniques)):
        uniques[u] = (uniques[u], names.count(uniques[u]))
    uniques = sorted(uniques, key = lambda x:x[0])
    uniques = sorted(uniques, key = lambda x:-x[1])
    return uniques
    

## TASK C. Iteration and accumulation
# It should return a string that contains the uppercase versions of the first character of each of the strings in the input list.
def build_acronym(ls):
    acronym = ""
    for x in range(len(ls)):
        temp_string = ls[x]
        acronym += temp_string[0].upper()
    return acronym

## TASK D. Python user-defined types
#If a house's color is "blue", its size should be "big". If a house's color is "red", its size should be "small". Otherwise, its size should be "medium".
class House(object):
    def __init__(self,color,street,number):
        self.house_color = color
        self.street_name = street
        self.address_number = number

    def __str__(self):
        return "This is a {} house, located at {} {}.".format(self.house_color,self.address_number,self.street_name)

    def determine_size(self): #Add a method to the class called determine_size that returns a string that describes the house's size. 
        if self.house_color == "blue":
            return "big"
        if self.house_color == "red":
            return "small"
        return "medium"


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected):
  score = 0;
  if got == expected:
    score = 25
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
    total = 0
    print()
    print ('Task A: string manipulation'
    """\nEach OK is worth 25 points.""")
    total += test(string_manip(' Colleen van Lent'), 'TNEL#NAV#NEELLOC')
    total += test(string_manip('  276 876'), '678#672')
    total += test(string_manip('!UMSI!'), '!!')
    total += test(string_manip('UMSI'), '')
    total += test(string_manip(''), '')

    print("\n\n")
    print('Task B: name_counts'
    """ \nEach OK is worth 25 points.""")
    total += test(name_counts([]), [])
    total += test(name_counts(['Christopher']), [('Christopher', 1)])
    total += test(name_counts(['Christopher', 'Christopher', 'Christopher']), [('Christopher', 3)])
    total += test(name_counts(['Eddie', 'Bacon', 'Christopher', 'Christopher', 'Christopher', 'Bacon', 'Bacon']), [('Bacon', 3), ('Christopher', 3), ('Eddie', 1)])
    total += test(name_counts(['Bacon', 'Catherine', 'Eddie', 'Bacon', 'Becca', 'Christopher', 'Bacon', 'Eddie', 'Mike']), [('Bacon', 3), ('Eddie', 2), ('Becca', 1), ('Catherine', 1), ('Christopher', 1), ('Mike', 1)])
    total += test(name_counts(["Cai","Cai","Bette","Ferdinand","Ferdinand","Emmett","Bette","Cai","Bette","Emmett",]),[("Bette",3),("Cai",3),("Emmett",2),("Ferdinand",2)])

    print("\n\n")
    print('Task C: build_acronym'
    """ \nEach OK is worth 25 points.""")
    total += test(build_acronym(["thank","goodness","ice","freezes"]),"TGIF")
    total += test(build_acronym(["pretty","yurts","tumble","hard","on","northerly slopes"]),"PYTHON")
    total += test(build_acronym(["yay"]),"Y")
    total += test(build_acronym([]),"")
    total += test(build_acronym(["Hooray","Ice cream"]),"HI")

    print("\n\n")
    print('Task D: determine_size'
    """ \nEach OK is worth 25 points.""")
    nh = House("blue","State",206)
    nh2 = House("red","Main",506)
    nh3 = House("purple","Liberty",281)
    nh4 = House("brick","Kingsley",110)
    
    total += test(nh.determine_size(),"big")
    total += test(nh2.determine_size(),"small")
    total += test(nh3.determine_size(),"medium")
    total += test(nh4.determine_size(),"medium")

    print("\n\n")
    print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
