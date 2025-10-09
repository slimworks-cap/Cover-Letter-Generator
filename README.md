# Cover Letter Generator

<!-- TABLE OF CONTENTS -->
<header>Table of Contents</header>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#initial-setup">Intial Setup</a></li>
    <li><a href="#usage">Usage</a></li>
  </ol>

<!-- ABOUT THE PROJECT -->
# About The Project

Writing cover letters are some of the most tedious part of the employment process for any prospective applicant. Writing and editing a single page from scratch could take at least 30 minutes to an hour; which is time that could be better spent browsing for more job postings for said applicant.

This project aims to leverage generative AI to reduce the time spent by applicants on writing cover letters. 

![Imgur](https://imgur.com/C0IzNuY.jpeg)

This project is written in python using the module Tkinter for GUI for ease of use as well as LLM model llama 3.3 via Groq API to generate text and is packaged into an executable file using Pyinstaller.

<ins>**Note**</ins>:
In the future, this project may have more customization options available to the user, such as being able to select different LLM models, as well as being able to set the amount of tokens that the model processes, but, for now the default LLM model will only be "llama-3.3-70b-versatile".

Unfortunately, this project is only usable <ins>only</ins> for Windows OS at this current version and there are no plans in the near future to make this available to Mac OS or Linux. 

# Built With
* [Python][Python-url]
* [Tkinter][Tkinter-url]
* [Pyinstaller][Pyinstaller-url]
* [Groq][Groq-url]

<!-- Initial Set up -->
# Initial Setup

In order to use this project to generate cover letters, a user must download the executable file and then acquire a Groq API key. Please see instructions below: 

<ol>
  <li>First the user will need the download the <a href=https://github.com/slimworks-cap/Cover-Letter-Generator/raw/refs/heads/main/Cover%20Letter%20Generator.exe>executable file</a></li>
  <li>The user will then need to acquire a Groq API Key from this <a href=https://console.groq.com/docs/overview>site</a>.</li>
    <ul>
      <li>The User will need to create a Groq Account to be able to generate API Keys.</li>
      <li>After creating an account the user must click on API Keys hyperlink on the upper right hand corner of the page.</li>
         <img src=https://imgur.com/jwJV6IY.png width="400" height="60">
      <li>Click "Create API Key" button to generate the key.</li>
         <img src=https://imgur.com/ReEtEeE.png width="600" height="100">
      <li>Copy the API Key and save it. Make sure to keep the API Key confidential as it may be misused if shared or stolen.</li>
         <img src=https://imgur.com/5u3WhGa.png width="550" height="300">
    </ul>
   <li>After completing the above steps to creating the API Key the user can now launch the executable file to see the User Interface</li>
</ol>

# Usage

Launching the executable file will open User Interface (abbreviated as "UI") from which there are fields that need to be filled out.

<img src=https://imgur.com/C0IzNuY.jpeg width="750" height="400">

Copy and past the API Key to the API Key field as it <ins>must</ins> be filled in order to generate cover letters. Otherwise, A warning prompt will open to inform the user that the program will not work. 

Once the API Key field has been filled. The user should fill out the resume by clicking the "Browse" button on the UI and navigating to the folder of the resume from where the user will double click the resume file to fill out the field.

This is so that the LLM model can parse through the resume to get the relevant work experience of the user and then use it to write the cover letter. 

<img src=https://imgur.com/Baz4PH5.png width="750" height="400">

The user can now opt to find a job opening of in any job board site of their choosing (i.e. linkedin, indeed, or any corporations official job board) to fill out the fields "Company" ,"Job Position", "Job Description".

**Company**: is the legal entity that is hiring people to fulfill a specific role within the company.

**Job Position**: in this context, is a specific role or function that the company is hiring for in order to operate.

**Job description**: outlines the responsibilities and daily tasks of the prospective employee. 

For this example, we will use the below job posting on linkedin "Store Manager" for Starbucks in Little Elm, TX: 

<img src=https://imgur.com/NHcDLwA.png width="450" height="600">

In this example the Company is "Starbucks", the Job Position is "store manager" and the Job Description is all the details under "About the Job". These need to be copied onto the relevant fields. 

<img src=https://imgur.com/q0Dwvxw.png  width="750" height="400">

After filling out the appropriate fields, the user may now click "Generate" Button on the UI in order to generate a cover letter using details from the resume and the filled out fields. 

<img src=https://imgur.com/CdpjqIG.png width="750" height="400">

The user may opt to edit the cover letter on the left pane, likewise, the user may click the generate button again to generate a new cover letter.

Once the user is happy with the generated cover letter they may click the **"Save"** button in order to save the cover letter in either <ins>word file (.docx)</ins> or <ins>text file (.txt)</ins> by default the file will save in the documents directory of the user but user may freely save it in any other location. 

<ins>**Note**</ins>: Sometimes the generated cover letter will contain sidenotes made by the LLM Model such as the example below. Hence, <ins> User may need to proof read their generated letter before saving and submitting their cover letter. </ins>

<img src=https://imgur.com/ZOj8aRY.png width="500" height="400">

# Changes

By default This application uses "llama-3.3-70b-versatile" as the model to generate cover letters. However, Some of the more tech-savvy users of this application may prefer to use other LLM models that Groq Supports such as the ones below: 

* llama-3.1-8b-instant
* llama-3.3-70b-versatile
* meta-llama/llama-guard-4-12b
* openai/gpt-oss-120b
* openai/gpt-oss-20b
* whisper-large-v3
* whisper-large-v3-turbo

LLM models behave differently and therefore generate content differently from each other, even if they are made by the same company. 

hence, if in case you (the user) would like to use any of the above models. You may opt to change the model by clicking on model menu on the upper left side of the application GUI and then clicking the "List of Models" Sub menu to select any among the available list of production LLM models that Groq supports. 

<img src=https://imgur.com/a3hewNV.png>

In order to check the current model that is being used by the application, you may simply click the option "Check Current Model" in the Model Menu to show a notification stating the current model being used in the application and consequently the one you will be using to generate the cover letter. 

<img src=https://imgur.com/Bjw9lFL.png>

**Note:** Some of the models may not be available for use and will output an error. In this case feel free to select any other model that works. 

I have also added a "File" Menu bar with an option to clear all text boxes In order to create an easy an accessible option to clear all of the text boxes should the user feel the need to have a blank slate when generating a cover letter for a new role they are applying for. 

<img src=https://i.imgur.com/TkitESe.png>


# Acknowledgments

I would not have been able to complete this project without the help of these wonderful guides: 

* [TKDocs - Modern Tk Best Practices][Tkinter-url] - Guide for Tkinter

* [RealPython - Using PyInstaller to Easily Distribute Python Applications][Pyinstaller-guide-url] - Guide for Pyinstaller

While there are many online guides about how to create GUI's using Pythons built in Tkinter, "TKDocs - Modern Tk Best Practices" provides a comprehensive and detailed guide on creating a modern and responsive GUI. 

Likewise, RealPython has a wonderful guide for packaging Python scripts into standalone executable applications for use in various operating sofrware using Pyinstaller!

Please do give them a read as they have helped me as they potentially may help you~

<!-- MARKDOWN LINKS & IMAGES -->

[Python-url]: https://www.python.org/
[Tkinter-url]: https://tkdocs.com/
[Pyinstaller-url]: https://pyinstaller.org/en/stable/index.html
[Pyinstaller-guide-url]: https://realpython.com/pyinstaller-python/#using-pyinstaller
[Groq-url]: https://groq.com/
[Groq-API-url]: https://console.groq.com/docs/overview
<!-- [executable-file-url]: https://github.com/slimworks-cap/Cover-Letter-Generator/raw/refs/heads/main/Cover%20Letter%20Generator.exe -->
