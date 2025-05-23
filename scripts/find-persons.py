# Import libraries
import re
import os


# Specify the path to the folder with the articles
articles_path = "../articles/"

# Assign the list of persons to be found
person_list = ["Netanyahu", "Biden", "Trump", "Erdogan"]

# Create a dictionary for storing the counts
counts = {}

# Get a list of the article file names - how? :


# Loop through the articles - for each article search for each person
for article in articles:
    article_path = os.path.join(articles_path, article)
    
    with open(article_path, 'r', encoding='utf-8') as file:
        text = file.read()
    for person in person_list:
        results = re.findall(person, text)
        count = len(results)
        
        # Add to count in dictionary - but what if it is not in the dictionary?
        
# For each article add the number of results to the dictionary - for each person in list


# Create list for storing tsv


# Add tsv header to the list


# Loop through results dictionary - append to list for tsv


# Join list of tab-separated strings using newline (\n)


# Export list to output tsv file
