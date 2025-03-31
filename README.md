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
* [Groq][Groq-url]

<!-- Initial Set up -->
# Initial Setup

In order to use this project to generate cover letters, a user must download the executable file and then acquire a Groq API key. Please see instructions below: 

<ol>
  <li>First the user will need the download the <a href=[executable-file-url]>executable file</a></li>
  <li>The user will then need to acquire a Groq API Key from this <a href=[[Groq-API-url]]>site</a>.</li>
    <ul>
      <li>The User will need to create a Groq Account to be able to generate API Keys.</li>
      <li>After creating an account the user must click on API Keys hyperlink on the upper right hand corner of the page.</li>
         <img src=https://imgur.com/jwJV6IY.png width="400" height="60">
      <li>Click "Create API Key" button to generate the key.</li>
         <img src=https://imgur.com/ReEtEeE.png width="600" height="100">
      <li>Copy the API Key and save it. Make sure to keep the API Key confidential as it may be misused if shared or stolen.</li>
         <img src=https://imgur.com/5u3WhGa.png width="550" height="300">
    </ul>
   <li>After completing the above steps to creating the API Key the user can now launch the executable file to see the user interface</li>
</ol>

# Usage

Before continuing 

# Acknowledgments

I would not have been able to complete this project without the help of this wonderful guide: 

* [TKDocs - Modern Tk Best Practices][Tkinter-url] - Guide for Tkinter

While there are many online guides about how to create GUI's using Pythons built in Tkinter, "TKDocs - Modern Tk Best Practices" provides a comprehensive and detailed guide on creating a modern and responsive GUI. 

Please do give them a read as they have helped me as they potentially may help you~

<!-- MARKDOWN LINKS & IMAGES -->

[Python-url]: https://www.python.org/
[Tkinter-url]: https://tkdocs.com/
[Groq-url]: https://groq.com/
[Groq-API-url]: https://console.groq.com/docs/overview
[executable-file-url]: https://github.com/slimworks-cap/Cover-Letter-Generator/raw/refs/heads/main/Cover%20Letter%20Generator.exe
