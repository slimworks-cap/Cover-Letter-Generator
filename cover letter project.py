from docx import Document
from docx.shared import Cm
from docx.shared import Pt
from docx.shared import Length
from docx.shared import RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

#hard coded stuff
source_repository = 'https://github.com/slimworks-cap/Cover-Letter-Project'
document = Document('Cover Letter template.docx')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# # user input
user_name = input("Please Enter Your Name: ")
user_phone = input("Please Enter Your Contact Number: ")
user_email = input("Please Enter Your Current Email: ")
user_address = input("Please Enter Your Current Address: ")
company = input("Please Enter The Company you are generating a Cover Letter for: ")

# ---------------------------------------------------------------- #
def get_address(x):
    #opens googles web page
    driver.get('https://www.google.com/')
    #finds the search bar in the html elements of the webpage
    search = driver.find_element(By.NAME, 'q')
    search.send_keys(x)
    search.send_keys(Keys.ENTER)
    # seems that the common class name for addresses in google searches are as follows: 'LrzXr'
    search = driver.find_element(By.CLASS_NAME, 'LrzXr').text
    return search

# ---------------------------------------------------------------- #
def get_body(x):
# This should be manually inputted by the user, maybe we should put
    text =  f"""
Dear human resource analyst of {x}, I have wanted to be involved in the industry of the company that you are employed by for a very long time. After browsing through your company’s job page, I have found that one of the positions you offer has the sort of work that I am interested in pursuing as a long-term career path.

In my most recent work experience, I worked as a reference data analyst for the terms and conditions data team of MSCI Hong Kong Limited. In my role, the tools that I use on a daily basis are SQL (oracle) in order to query data from our database, UNIX to monitor the Autosys Jobs and the logs of the scripts that normalizes our data into our database, as well as PowerBI to monitor the quality of our data as well as Proprietary Quality Assurance frameworks. I am also able to program python and have completed a data visualization project with PowerBI and Python windows task scheduler.

Although this profession is not within the traditional scope of my field of work (Finance) I am still intrigued and eager to learn about the role I am applying for, and with this in mind I feel that I may be a strong candidate for the position that I have applied for as it is the perfect role for me to further my career. However, although if you feel that I may be a better fit for a different sort of position, I would still be very open to applying for it. I hope to hear a reply from you soon.

Sincerely,
            """

    return text
# ---------------------------------------------------------------- #
def set_major_font(x):
    paragraph = document.add_paragraph()
    run = paragraph.add_run(x)
    font = run.font
    font.name = 'Proxima Nova'
    font.size = Pt(11)
    font.bold = True
    return paragraph
# ---------------------------------------------------------------- #
def set_body_font(x):
    paragraph = document.add_paragraph()
    run = paragraph.add_run(x)
    font = run.font
    font.name = 'Proxima Nova'
    font.size = Pt(11)
    font.bold = False
    return paragraph
# ---------------------------------------------------------------- #
def set_minor_font(x):
    paragraph = document.add_paragraph()
    run = paragraph.add_run(x)
    font = run.font
    font.name = 'Calibri (Heading)'
    font.size = Pt(10)
    font.color.rgb = RGBColor(102, 102, 102)
    return paragraph
# ---------------------------------------------------------------- #
def set_sign_off_font(x):
    paragraph = document.add_paragraph()
    run = paragraph.add_run(x)
    font = run.font
    font.name = 'Proxima Nova'
    font.size = Pt(14)
    font.bold = True
    font.color.rgb = RGBColor(212, 175, 55)
    return paragraph
# ------------------------Start of the Code----------------------- #

# use the info taken by the functions and put them in variables
address = get_address(company)
body = get_body(company)

# adding the sender information
sender = set_major_font(user_name)


sender_phone = set_minor_font(user_phone)
format = sender_phone.paragraph_format
format.right_indent = Cm(13)
format.space_after = Pt(0)

sender_address = set_minor_font(user_address)
format = sender_address.paragraph_format
format.right_indent = Cm(13)
format.space_after = Pt(0)

sender_email = set_minor_font(user_email)
format = sender_email.paragraph_format
format.right_indent = Cm(13)

# adding address of the addressee
sendee = set_major_font(company)
sendee_address = set_minor_font(address)
format = sendee_address.paragraph_format
format.right_indent = Cm(13)

# adding body
set_body = set_body_font(body)
format = set_body.paragraph_format
# format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY_HI
format.right_indent = Cm(1.5)
format.space_before = Pt(10)
format.space_after = Pt(0)


# adding sign off of addressee
sign_off = set_sign_off_font(user_name)
format = sign_off.paragraph_format
format.space_before = Pt(0)

# add footer
section = document.sections[0]
footer = section.footer
footer = footer.paragraphs[0]
footer.text = f'This cover letter was generated by a script written in this repository: {source_repository}'

# save the document
document.save(f'Cover Letter ({company}).docx')

# Nice to have items
    # Run time notification
        # Need Time module for this
    # Automatically place file in a specific directory
    # Notification on the creation of the file which gives file0 name and directory where its located
        # use OS module for this
    # Try and except clause in the selenium part of the code
        # in order to check if we can get an address in the first place, if not then skip and add a placeholer for user to input manually
    #

# Stretch Goals
    # Create a tkinter app for this
    # args statement to differentiate if its a user and not me using the code
