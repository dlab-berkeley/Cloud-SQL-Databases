# D-Lab Cloud SQL Databases Workshop

[![Datahub](https://img.shields.io/badge/launch-datahub-blue)](http://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2FCloud-SQL-Databases&urlpath=lab%2Ftree%2FCloud-SQL-Databases%2F) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dlab-berkeley/Cloud-SQL-Databases/HEAD) [![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

This repository contains the materials for D-Lab’s SQL Fundamentals workshop series. 

### Prerequisites
Some prior experience with SQL and Python is preferable.

Check D-Lab's [Learning Pathways](https://dlab-berkeley.github.io/dlab-workshops/python_path.html) to figure out which of our workshops to take!


## Workshop Goals

This is a hands-on workshop on analyzing Social Media Data using Cloud Databases, specifically Google Cloud Platform's BigQuery. In this session, you'll learn how to leverage existing Reddit and other publicly available datasets in the cloud, import additional data, and perform meaningful analyses relevant to social science research. By the end of this workshop, you will:

**NOTE for LBL Employees:** Please be aware that for LBNL employees all research use of social media data and publicly available data about people must be reviewed by the The Human & Animal Regulatory Committees (HARC) Office. Email HARC@lbl.gov(link sends e-mail) for more information.

## Learning Objectives

After completing Cloud SQL Databases, you will be able to:
• Understand the basics of Google Cloud Platform (GCP) and BigQuery.
• Explore and query public datasets on BigQuery, focusing on Reddit and Wikipedia data.
• Perform complex SQL queries to extract meaningful insights from large datasets.
• Cross-reference Reddit and Wikipedia data with other public datasets.
• Import external data (e.g., data available through the UC Berkeley Library) into BigQuery.
• Use Python and PRAW to scrape recent Reddit data and import it into BigQuery.
• Develop skills in data analysis relevant to computational social science.
    
This workshop does **not** cover the following:
- Basics of SQL or Python. This is covered in [SQL Fundamentals](https://github.com/dlab-berkeley/SQL-Fundamentals/).

## Workshop Structure

Cloud SQL Databases is a 2 hour workshop, and is delivered in a lecture-style coding walkthrough interrupted by challenge problems and a break. Instructors and TAs are dedicated to engaging you in the classroom and answering questions in plain language.

1. **[Part 1: BigQuery on Google Cloud Platform](BigQuery-GCP.ipynb)**
2. **[Part 2: Reddit Data API with PRAW](Praw-Reddit.ipynb)**


## Is Python not working on your laptop?

If you do not have Anaconda installed and the materials loaded on your workshop by the time it starts, we *strongly* recommend using the UC Berkeley Datahub to run the materials for these lessons. You can access the DataHub by clicking this button:

[![Datahub](https://img.shields.io/badge/launch-datahub-blue)](http://dlab.datahub.berkeley.edu/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fdlab-berkeley%2FCloud-SQL-Databases&urlpath=lab%2Ftree%2FCloud-SQL-Databases%2F)

The DataHub downloads this repository, along with any necessary packages, and allows you to run the materials in a Jupyter notebook that is stored on UC Berkeley's servers. No installation is necessary from your end - you only need an internet browser and a CalNet ID to log in. By using the DataHub, you can save your work and come back to it at any time. When you want to return to your saved work, just go straight to [DataHub](https://datahub.berkeley.edu), sign in, and you click on the `Cloud-SQL-Databases` folder.

If you don't have a Berkeley CalNet ID, you can still run these lessons in Binder, which is another cloud-based option. Click this button:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/dlab-berkeley/Cloud-SQL-Databases/HEAD)

Note: Using Binder, you unfortunately cannot save your work.

# About the UC Berkeley D-Lab

D-Lab works with Berkeley faculty, research staff, and students to advance data-intensive social science and humanities research. Our goal at D-Lab is to provide practical training, staff support, resources, and space to enable you to use R for your own research applications. Our services cater to all skill levels and no programming, statistical, or computer science backgrounds are necessary. We offer these services in the form of workshops, one-to-one consulting, and working groups that cover a variety of research topics, digital tools, and programming languages.  

Visit the [D-Lab homepage](https://dlab.berkeley.edu/) to learn more about us. You can view our [calendar](https://dlab.berkeley.edu/events/calendar) for upcoming events, learn about how to utilize our [consulting](https://dlab.berkeley.edu/consulting) and [data](https://dlab.berkeley.edu/data) services, and check out upcoming [workshops](https://dlab.berkeley.edu/events/workshops).

# Other D-Lab Python Workshops

Here are other Python workshops offered by the D-Lab:

### Basic competency

* [SQL Fundamentals](https://github.com/dlab-berkeley/Cloud-SQL-Databases/)
* [Python Data Wrangling and Manipulation with Pandas](https://dlab.berkeley.edu/events/python-data-wrangling-and-manipulation-pandas/2024-10-10)

# Contributors
* Aaron Culich
