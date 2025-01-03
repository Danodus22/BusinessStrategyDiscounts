# Business strategy on Discounts
***A Case Study in Data Cleaning & Analysis for an E-Commerce Tech Company***

## Summary
This case study of a fictional company explores the impact of discounts on customer loyalty and sales. However, the initial dataset is inconsistent and unreliable, requiring extensive data cleaning before meaningful conclusions can be drawn.

The company has placed great faith in the potential of data analysis and hopes your work will finally resolve a long-standing debate:
**Is discounting beneficial to the overall business strategy?**

## Situation
The company, based in Europe, specializes in selling tech products and accessories. It is currently divided over whether discounting is a viable long-term strategy.

**The Marketing Team Lead** argues that discounts are advantageous in the long run, boosting customer acquisition, satisfaction, and retention, ultimately fostering business growth.
**The Company Board**, however, is concerned about the negative impact of aggressive discounts. Recent quarterly results showed an increase in order volume but a decline in total revenue. The board prefers that the company positions itself in the premium market segment, focusing on quality rather than competing on price.

Your primary tasks will involve evaluating the dataset’s quality and performing a variety of data cleaning processes before addressing the core business questions.
At the end of this project, you will present your findings and analysis to the company board.

## Languages and Libraries Used
The complexity of these tasks will require you to use `Python` and specifically `Pandas`.
Using additional libraries like `matplotlib`, `seaborn` and `numpy` is a great way to show results in a beautiful way of data storytelling!

## Key Learnings
- 80% of time for cleaning and preparing data. 20% for the analysis.
- Good data analysts and scientists make data usable and trustworthy to answer business questions.
- Experienced the steps of data preparation and analysis using a good and realistic case study.
- I applied many steps and methods that were necessary to be able to make a recommendation to the board members at the end.
- Combined Business and Data Knowledge to answer whether or not it is beneficial to discount products to the company.

## Using the files and data sources
- **data**
    - **cleaned**
        - brands_cleaned.csv
        - orderlines_cleaned.csv
        - orderlines_products_df.csv
        - orders_cleaned.csv
        - products_brands_df.csv
        - products_categorized.csv
        - products_cleaned.csv
    - **raw**
        - brands.csv
        - orderlines.csv
        - orders.csv
        - products.csv
- **notebooks**
    - 01_Data_exploration_cleaning.ipynb
    - 02_Product_category_creation.ipynb
    - 03_Merge_tables_for_analysis.ipynb
    - 04_Data_analyses.ipynb
- **scripts**
    - data_overview.py

You find the 4 raw csv-files to start working on it here:
`../data/raw`
The cleaned and prepared for analysis csv-files are here:
`../data/cleaned`

All Jupyter-Notebooks are in a seperated folder `../notebooks` and sorted numerical:
Start with `01_Data_exploration_cleaning.ipynb`

Save data files and notebooks to your harddrive.
If necessary update paths (and reference file/table names) in all Jupyter notebooks (first section of each notebook) so that link is made to where files are actually saved

## Installation and requirements
Install the dependencies if necessary:
   pip install -r requirements.txt
