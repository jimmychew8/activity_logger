"""Plots a csv file indicating the activity and duration of the activity.
Will display bar graph on plotly."""

import csv
import numpy as np
import plotly.tools as tls
import plotly.plotly as py
from plotly.graph_objs import *
import convert

tls.set_credentials_file(username='....', api_key='....')

def data_entry():
	"""Return a plotly bar graph of the csv activities file."""

	x_axis = []
	y_axis = []

	# Read the csv file with the time values 
	with open('workfile.txt', 'r') as csvfile: 
		data_file = csv.reader(csvfile, delimiter='/')
		for row in data_file:
			x_axis.append(row[0])
			y_axis.append(convert.convert_tuple(row[1], 'hour'))

	# Create the Plotly Graph
	data = Data([
	    Bar(
	        x = x_axis,
	        y = y_axis
	    )
	])
	plot_url = py.plot(data, filename='basic-bar')
	

if __name__ == '__main__':
	data_entry()

