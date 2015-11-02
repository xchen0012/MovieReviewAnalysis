import pandas as pd 
import time
import re
import nltk
from nltk.corpus import stopwords
from bs4 import BeautifulSoup


def preprocessText(text):
	#delete punctuation
	text_letters = re.sub("[^a-zA-Z]",
						  " ",
						  text);
	#lower the letter. 
	lowercase = text_letters.lower();
	#delete stop words. 
	words = lowercase.split();
	words = [w for w in words if not w in stopwords.words("english")]

	return " ".join(words);

def preprocessData (filename):
	train = pd.read_csv(filename, header = 0, delimiter="\t",
			quoting = 3);

	#example1 = BeautifulSoup(train["review"][0], "html.parser")

	clean_train_reviews = [];

	for i, review in enumerate(train["review"]):
		if (i + 1) % 1000 == 0:
			print "processed %d data." % (i)

		text = BeautifulSoup(review, "html.parser");
		review = preprocessText(text.get_text());
		clean_train_reviews.append(review);

	return train; 

if __name__ == "__main__":
	data = preprocessData("./labeledTrainData.tsv");
	#print data; 
