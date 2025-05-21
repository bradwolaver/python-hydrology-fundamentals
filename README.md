# Python Basics for Water Professionals: A Step-by-Step Guide

This repository contains materials for a 6-session short course designed to introduce hydrology professionals to Python fundamentals for water data analysis. The course emphasizes practical skills for importing, manipulating, visualizing, and analyzing hydrologic datasets, leveraging modern AI tools to assist in code development and comprehension.

## Course Goal

The primary goal of this short course is to introduce the Hydrology Bureau to Python fundamentals for water data analysis. Through 6 practical sessions, participants will learn essential skills for working with hydrologic data—from importing and manipulating datasets to creating visualizations and conducting analyses.

## Online Course Materials

Jupyter Notebook files and supporting materials for each session are available.


## Session Breakdown

**Session 1: Getting Started with Python and Jupyter Notebook**
- **Objective:** Learn to install Anaconda and launch Jupyter Notebook for Python programming.
- **Key Topics:** Installing Anaconda, exploring Jupyter Notebook features (File Browser, Running Terminals and Kernels, Table of Contents, Extension Manager Tabs, Cells), essential Markdown formatting, and leveraging AI tools for code generation and comprehension.
- **Expected Outcome:** Attendees will have a functioning Python environment ready for coding in subsequent sessions.

**Session 2: Python Environments**
- **Objective:** Focuses on managing Python environments using Conda, teaching how to create and maintain isolated workspaces for different projects.
- **Key Topics:** Creating, activating, deactivating, backing up, removing, and loading Python environments using Anaconda Prompt to manage libraries and dependencies.
- **Expected Outcome:** Understanding how to manage project-specific Python environments for reproducible analysis.

**Session 3: Importing Data from Structured Data Files (Text, CSV, Excel)**
- **Objective:** Introduce fundamental data handling skills using Python's pandas library.
- **Key Topics:** Importing and inspecting tab-delimited text data files (e.g., historical streamflow data from the USGS gage at Embudo), creating pandas DataFrames, basic DataFrame operations, and generating visualizations using matplotlib.
- **Expected Outcome:** Comfort with importing data into a pandas DataFrame, inspecting data, and creating basic plots.

**Session 4: Simplified USGS Data Download, Data Conversion, and Hydrographs**
- **Objective:** Advance Python skills by introducing hydrofunctions for retrieving USGS stream gage data.
- **Key Topics:** Downloading, analyzing, and visualizing data from multiple gages, creating publication-ready hydrographs, generating comprehensive data analysis reports using ydata-profiling, and using f-strings for code development.
- **Expected Outcome:** Ability to download, prepare, plot, and perform exploratory data analysis on USGS gage data.

**Session 5: Converting Data and a Little More Plotting**
- **Objective:** Build on data handling skills by focusing on converting and aggregating USGS streamflow data to different temporal scales and units.
- **Key Topics:** Transforming daily streamflow measurements (cubic feet per second) into monthly, irrigation season, and annual acre-feet summaries, and creating plots using matplotlib and seaborn.
- **Expected Outcome:** Proficiency in converting streamflow data and creating advanced plots, including boxplots and customized hydrographs.

**Session 6: Extracting Data from Unstructured Text Files (Parsing Fortran Text Output Files)**
- **Objective:** Tackle working with legacy data by parsing Fortran-generated text files.
- **Key Topics:** Using Python's text processing capabilities and regular expressions to identify patterns in data, extracting and converting streamflow depletion rates and aquifer parameters into usable Python data structures, and creating annotated plots of net stream depletion.
- **Expected Outcome:** Understanding fundamental programming concepts like flow control and gaining practical experience with file handling and text parsing.

## Next Steps in Python

The course provides a foundation for further Python development in various areas, including:
- **Groundwater Modeling with FloPy:** Utilizing FloPy for MODFLOW groundwater models.
- **Time Series Analysis:** Applying machine learning approaches (e.g., LSTM networks) and specialized tools like Neural Hydrology and Pastas for hydrologic time series.
- **Statistical Applications in Hydrology:** Using the statsmodels Python module for statistical tests and advanced time series modeling on hydrologic data.
- **Geospatial Analysis Tools:** Handling geospatial data with GeoPandas and automating spatial analysis workflows with ArcPy (ArcGIS Pro) and QGIS Python API.
- **APIs:** Programmatic Data Access: Learning to interact with APIs like OpenET for streamlined data collection and analysis.

## Disclaimer
While efforts have been made to ensure accuracy, updates to Python versions, broken dependencies, and typos may occur. Users are encouraged to verify information with official Python documentation and utilize search engines, AI tools, or IDEs for debugging.