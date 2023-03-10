# Workbook for tracking time spent by progect

## Problems being addressed

1. Serious time management requires measuring where your time is expended.

2. For some large projects, time spent on some activites has to be documented.
The only honest way to do so is to track the time spent on those projects.

## Solutions tested

1. Use iCal with a separate calendar for each project. I did this for about a year. The software for extracting the times was proprietary and iCal began to choke when tracking a large number of projects. 

2. Use Google Calendar with a separate calendar per project. You insert into gcal a new event for a particular project and then drag the box to span the time range spent on that project. The free GTimeReport software can extract the time spent on each calendar and export it to an Excel or csv file.
This approach was slow, tedious, and became more so when the number of projects reached about 300.

3. Use org-mode in Emacs to track the effort by project. 
Each project is a separate headline.
Each headline can have a time logging system that is stored in the logbook property of each project.
The advantage of this approach is that the time tracking can be integrated with org-agenda.
The problem with automated loggers is that they tend to fail to capture your spin up and winddown times spent on a project.
In additon, Org files with more than 10,000 lines tend to become difficult to scroll.
You can fold up cluters of project and the folded information is prone to being accidently deleted.
I tried this approach for about a year.

4. ***Use Google Sheets with one sheet per month and one workbook per year.*** The event are entered as they happen. The cells are coded to converted start and end times into hours represened by real numbers. Each event is has a project code. The worksheet is exported to a csv file at the end of the month and a Python script is used to filter and sum the time expended by certain clusters of projects. A store the link to the Google Sheet workbook in the toolber of my browser for rapid access. The workbook pops up much faster than iCal, gCal or Excel.

I started the fourth approach in May 2022. I have been using it daily. The barrier to usage is much lower. It is vastly faster and superior to the first three approaches, and it is not limited by number of projects.

## How to use

Download the Excel file and import into Google Sheets and store on your Google Drive.
Rename the workbook as desired.
Open the Sheet for the current month.
Scroll down to the current day and starting entering work events by project.

I track my commute times because these are useful referenece points that flank my workday.
You can edit the times to match when you commute.
Insert more rows between the commute rows as the need arises through the day.
The events are entered in chronological order as they occur.
If I work on one project in two or more time blocks, these get separate entries.

I update the sheet after finishing effort on a project.
Take care not to fall behind.
It is a pain to catch up becuase your memory fades.
It takes much longer to make the entries at the end of the day than to keep it updated as the day progresses.

I use a unique four digit code for each project.
This code starts the name of a corresponding project folder in my home directory.
I include the folder name to check the accuracy of the project number.
These codes are defined in a separate Google Sheet and in org files for use with org-agenda.
I post about this system later.
It is not needed to use this time tracking system.

I track events in increments of 15 minutes.
If there are a bunch of short and releated events, they may be lumped together.

Remember to store the link the the notebook in the browser toolbar or a link in a private HTML file for rapid access.

## How to analyze

Edit the path to the exported csv file in the above Python Script, extractTime.py and edit the list of Project IDs to suit your needs.
Read the comments of the script for more instructions.


