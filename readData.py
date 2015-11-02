import pandas as pd 

if __name__ == "__main__":
	train = pd.read_csv("./data.csv", header= 0, delimiter=",", quoting = 3);
	print train;

