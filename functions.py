import sys
import datetime
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def read_pkl(path, mode):
	file = open(path, mode)
	content = pickle.load(file)
	file.close()
	return content

def write_pkl(object, path, mode):
	file = open(path, mode)
	pickle.dump(object, file)
	file.close()


def time_spent(date, data):
	seconds = 0.
	for v in data:
		if pd.Timestamp(v[0]).date() == date.date():
			seconds = seconds + (pd.Timestamp(v[1]) - pd.Timestamp(v[0])).seconds
	return seconds




