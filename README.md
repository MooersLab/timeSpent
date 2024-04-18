![Version](https://img.shields.io/static/v1?label=timeSpent&message=0.2&color=brightcolor)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)


# Google Sheets Workbook for tracking time spent by project



## Problems being addressed

1. Serious time management requires measuring where your time is expended.

2. Time spent on some activities must be documented for some large projects.
The only honest way to do so is to track the time spent on those projects.

## Solutions tested

1. Use iCal with a separate calendar for each project. I did this for about a year. The software for extracting the times was proprietary, and *iCal* began to choke when tracking many projects. 

2. Use Google Calendar with a separate calendar per project. You insert into *gcal* a new event for a particular project and then drag the box to span the time range spent on that project. The free GTimeReport software can extract the time spent on each calendar and export it to an Excel or CSV file.
This approach was slow and tedious and became more so when the number of projects reached about 300.
I used this approach for many years.

3. Use org-mode in Emacs to track the effort by project. 
Each project is a separate headline.
Each headline can have a time-logging system stored in each project's logbook property.
The advantage of this approach is that the time tracking can be integrated with the org-agenda.
The problem with automated loggers is that they tend to fail to capture the spin-up and wind-down times spent on a project.
In additon, Org files with more than 10,000 lines tend to become difficult to scroll.
If you can fold up clusters of projects, the folded information is prone to be accidentally deleted.
I tried this approach for about a year.

4. ***Use Google Sheets with one sheet per month and one workbook per year.*** The events are entered as they happen. The cells are coded to convert start and end times into hours represented by real numbers. Each event has a project code. The worksheet is exported to a CSV file at the end of the month, and a Python script filters and sums the time expended by certain clusters of projects. I store the link to the Google Sheet workbook in my browser's toolbar for rapid access. The workbook pops up much faster than iCal, gCal, or Excel.

I started the fourth approach in May 2022. I have been using it daily. The barrier to usage is much lower. It is vastly faster and superior to the first three approaches, and the number of projects does not limit it. 
I really liked the near-instant access via a hyperlink.

After several months, I imported the Google Sheets into a single table in an SQLite database so that I could control the storage of this information.
I have 8311 events stored in two years of recording.
I developed a separate system of Python scripts to summarize the data and generate graphical reports.
I will post these in a separate repository someday.

## How to use

- Download the Excel file, import it into Google Sheets, and store it on your Google Drive.
- Rename the workbook as desired.
- Open the Sheet for the current month.
- Scroll down to the current day and start entering work events by project.

I track my commute times because these are helpful reference points that flank my workday.
You can edit the times to match when you commute.
Insert more rows between the commute rows as the need arises throughout the day.
The events are entered in chronological order as they occur.
If I work on one project in two or more time blocks, these get separate entries.

I update the sheet after finishing the effort on a project.
I record to the nearest 15 minutes. 
Greater precision is folly because you then tend to avoid capturing the spin-up and spin-down time associated with switching projects.
If there are many short and related events, they may be lumped together.


Take care to stay caught up.
I make updates every 2-3 hours.
It is a pain to catch up because your memory fades, and the data becomes less accurate as time passes.
It takes much longer to make the entries at the end of the day than to keep it updated as the day progresses.
The former approach can be accurate if you keep a separate record on paper or in a text file, but this approach is wasteful due to the redundant effort.

I use a unique four-digit code for each project.
This code starts the name of a corresponding project folder in my home directory.
I include the folder name to check the accuracy of the project number.
These codes are defined in a separate Google Sheet and org files for use with org-agenda.
I will post about this system later.

For rapid access, remember to store the link the the notebook in the browser toolbar or in a private HTML file  that serves as your private homepage. 
## How to analyze

Edit the path to the exported CSV file in the above Python Script, extractTime.py, and edit the Project ID list to suit your needs.
Read the comments of the script for more instructions.

## Update table

|Version      | Changes                                                                                                                                    | Date                 |
|:-----------:|:------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------:|
| Version 0.2 |  Added badges and update table. Cleaned up the prose in README.md.                                                                         | 2024 April 18        |


## Funding Sources
NIH: R01 CA242845, R01 AI088011
NIH: P30 CA225520 (PI: R. Mannel); P20GM103640 and P30GM145423 (PI: A. West)




