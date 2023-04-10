# README

## Overview

This README file provides information on how to run the program, as the aswered question at the coding challange description.

## Running the Program

To run the program, please follow these steps:

1. Add the four CSV files (bills.csv, legislators.csv, vote_results.csv, votes.csv) to the data-set folder.
2. Open the terminal and navigate to the directory containing the main.py file.
3. Run the command "python3 main.py".
4. The resulting CSV files (bills.csv and legislators-support-oppose-count.csv) will be generated and saved in the results folder.

## Answered Questions

### Discuss your solution’s time complexity. What tradeoffs did you make?

To facilitate the discussion, let us define the following variables: "b" as the number of bills, "l" as the number of legislators, "v" as the number of votes, and "r" as the number of vote results. To read the input CSV files, we need to iterate over all of them, resulting in a time complexity of O(b + l + v + r).

Generating the "legislators-support-oppose-count.csv" file requires two separate iterations, one over the legislators and another over the vote results, resulting in a time complexity of O(l + r).

On the other hand, generating the "bill.csv" file requires separate iterations over the legislators, vote results, votes, and bills, resulting in a time complexity of O(b + l + v + r).

The coding challenge description states that Quorum frequently handles a large volume of publicly available government data. Because of that I prioritized performance, and, therefore, I created extra dictionaries and arrays, which may increase the space used by the functions. However, the overall space complexity of the solution is O(b + l + v + r).

### How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?

If I were to add new columns to my data models, I would need to make changes to the csv generator functions. The extent of these changes would depend on how the new columns interact with the current logic and how they fit into the resulting CSV files.

If the new columns are simply additional columns in the output files, the impact on the logic may not be severe. However, if the new columns require changes to the existing logic, I would need to carefully consider the modifications needed to accommodate the new data.

### How would you change your solution if instead of receiving CSVs of data, you were given a list of legislators or bills that you should generate a CSV for?

If I were given a list of legislators or bills instead of CSV files, I would need to analyze the data format to determine how to read the data and how to fit it into the data models used in my solution.

To generate new CSV files from the received data, I would need to understand the requirements of the new output and update my solution accordingly. This may involve changes to the existing code, such as modifying the data parsing and transformation steps to handle the new data format, or adding new code to generate the desired output format.

### How long did you spend working on the assignment?

I did not work on the coding challenge all at once, but rather over the course of my weekend. In total, I spent around 2.5h on it.