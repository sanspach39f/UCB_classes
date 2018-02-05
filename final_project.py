#Samuel Anspach Final Project

"""
1)
Write a program that takes as an argument the name of a directory (folder) 
and then finds the extension of each file. Then, for each extension found, 
it prints the number of files with that extension and the minimum, average, 
and maximum size for files with that extension in the selected directory.
"""

import os, re
import pandas as pd

pattern = re.compile(r'[\w\.]*\.([a-zA-Z]+)')

def function1():
    
    #First we get the directory to search through from the user
    directory = os.chdir(input("What directory do you want me to explore?"))
    
    #Define our dictionary to store our extension names, count, and sizes
    file_types = {}
    
    #Now we iterate through the user's inputted directory
    for file in os.listdir(directory):
        
        #For each object found, make sure it isn't a subdirectory or link
        if not os.path.isdir(file) and not os.path.islink(file):
            
            #Because we will eventually be comparing sizes of these files,
            #let's save ourselves some typing now by defining the filesize
            #variable.
            file_size = os.path.getsize(os.path.abspath(file))
            
            #Look for our pattern
            match = re.search(pattern,file)
            
            #The actual extension is in the matched object at the tagged
            #location number 1.
            extension = match.group(1)

            #Let's see if it in our dictionary already
            if extension in file_types.keys():
                
                #If we already have a record of this extension, let's 
                #add one to the count of files with this extension
                file_types[extension][0]+=1

                #Let's check how our filesize compares to what is currently the
                #maximum.

                if file_size > file_types[extension][3]:
                    
                    #If it is greater than the maximum, it is the new maximum
                    file_types[extension][3] = file_size
                    
                #Maybe it wasn't the maximum, but let's see if it is the new 
                #mimumum
                
                elif file_size < file_types[extension][1]:
                    file_types[extension][1] = file_size
                    
                #Now we have done all our comparisons - all that is left is to
                #calculate the average. This is completely separate from our
                #if statement - this part will run every time.
                
                file_types[extension][2] = (file_types[extension][2]+ 
                          file_size)/file_types[extension][0]
                
            
            else:
                
                #If we found no record, we should generate a new record for it
                #in our dictionary.
                file_types[extension] = [1,file_size,file_size,file_size]
    
    
    #While we could just answer the problem here, for legibility we will
    #convert the dictionary to a pandas DF - first we have to restructure the
    #dictionary.
    
    dictionary = {"Extension":[],"Count":[],"Minimum File Size":[],
                  "Average File Size":[],"Maximum File Size":[]}  
    for f in file_types:
        dictionary["Extension"].append(f)
        dictionary["Count"].append(file_types[f][0])
        dictionary["Minimum File Size"].append(file_types[f][1])
        dictionary["Average File Size"].append(file_types[f][2])
        dictionary["Maximum File Size"].append(file_types[f][3])        

    #Finally, we generate a DataFrame based off our new dictionary and
    #print out the columns in the order we choose
    
    data = pd.DataFrame(dictionary)
    print('\n')
    print(data[["Extension","Count","Minimum File Size","Average File Size",
                "Maximum File Size"]])

    
#Call the function and we're done.
#function1()

"""
2)
Write a text analyzer. It should be in a form of a function that takes a file 
name as an argument. It should read and analyze a text file and then print:
the top 5 most frequently used words in the file
the number of times the top 5 words are used
should be sorted by most frequently used count
the longest word in the document
the average size of each word
"""
def function2(file_name):
    
    #Let's read in the entire file first
    with open(file_name) as file:
        text = file.read()
    
    
    #We're going to need a couple ticker variables to track our analysis
    longest_word = ''
    words ={}
    avg_word_length =0
    total_length = 0
    

    #Here is our regular expression - we will split the entire text at every
    #point where we have one or multiple non-alphanumeric characters
    pattern = re.compile(r'[\W]+',re.IGNORECASE)
    
    #We will dump all our words into words_list
    words_list = re.split(pattern,text)
    
  
    #Here we will loop through each of our words. If we already have a record
    #of that word, we will add 1 to it's total count. Otherwise, we will
    #generate a new record in our list.
    for word in words_list:
        if word not in words:
            words[word]=1
        else:
            words[word]+=1
            
        #Additionally, within the loop we will keep track of the longest word
        #that we have seen so far
        if len(word)>len(longest_word):
            longest_word = word
            
        #We will also keep a running total of our character count
        total_length += len(word)
    
    #Calculation for average word length - our total character count over
    #the number of words we have
    avg_word_length = total_length/len(words_list)
 
    #Dictionary will organize our data so that we can construct a pandas
    #dataframe.
    
    dictionary = {"Word":[],"Number of Occurances": []}
    
    #Here we append all the words we found above along with their counts
    for word in words:
        dictionary["Word"].append(word)
        dictionary["Number of Occurances"].append(words[word])
        
    #Generating a pandas dataframe    
    data = pd.DataFrame(dictionary)
    
    #Because the problem asks for top 5 words - we'll need to sort our dataset.
    sorted_data =data.sort_values(by="Number of Occurances", 
                                  ascending = False)
    
    #Finally, we print the head of the summerized dataset along with the
    #longest word and average word length.
    print(sorted_data.head())
    print("The longest word is: ", longest_word)
    print("The average word length is: ",avg_word_length)
        
#function2("juicy.txt")



