import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from groq import Groq
from docx2txt import process
from docx import Document

# ---------------------------------------------------------------- #
def get_resume():
    
    file = filedialog.askopenfilename()
    res_pos.delete(0, END)
    res_pos.insert(0, file)
    
    return

# ---------------------------------------------------------------- #
def generate_letter():

    if api_pos.get() != '':

        client = Groq(api_key=api_pos.get().strip())
        
        company = com_pos.get().strip()

        resume = process(res_pos.get().strip())

        role = job_pos.get().strip()

        details = desc_pos.get(1.0, END)

        prompt = f'Write for me the ideal body of a cover letter for this company: {company}. for this role: {role}. here are more details about the role {details}. Use my resume as a reference {resume}'

        messages = [

            {
                'role': 'system',
                'content': 'you are a recruiter'
            },
            {
                'role': 'user',
                'content': prompt
            }
        
        ]

        chat_completion = client.chat.completions.create(
                temperature=1.0,
                n=1,
                model='llama-3.3-70b-versatile',
                max_tokens=10000,
                messages=messages
        )

        chat_completion.usage.total_tokens
        
        generated_letter = (chat_completion.choices[0].message.content) 

        content_box.delete(1.0, END)
        content_box.insert(END, generated_letter)

        return 
        
    else: 

        messagebox.showwarning(title='Warning', message='Warning: You have not input the API Key which is required to run this program')


# ---------------------------------------------------------------- #
def save_letter():

    file_types = [
        ('Word Document', '*.docx'),
        ('Text File', '*.txt')
        ]

    intl_dir = os.path.expanduser('~/Documents')
    intl_name = 'Cover Letter'

    file_path = filedialog.asksaveasfilename(
        initialfile=intl_name, 
        defaultextension='.docx', 
        filetypes=file_types,
        initialdir=intl_dir
        )
    
    file_extn = file_path.split('.')

    if file_extn[1] == 'docx':

        try:
                doc = Document()
                text_content = content_box.get(1.0, END)
                print(text_content)
                print(type(text_content))
                doc.add_paragraph(text_content)
                doc.save(file_path)

        except Exception as e:
            messagebox.showwarning(title='File Error', message=f'Error in saving file: {str(e)}')

    elif file_extn[1] == 'txt':

        try:
            with open(file_path, 'w') as file:
                text_content = content_box.get(1.0, END)
                file.write(text_content)

        except Exception as e:
            messagebox.showwarning(title='File Error', message=f'Error in saving file: {str(e)}')


    return

# ----------------------------------- GUI Configuration ------------------------------------ #

root = Tk()
root.title('Cover Letter Generator')

mainframe = ttk.Frame(root, padding = (3,3,12,12))
content = ttk.Frame(mainframe, borderwidth=5, relief='ridge', height=300, width=500)

# API Key GUI Config
api_lbl = ttk.Label(mainframe, text = 'API Key')
api_pos= ttk.Entry(mainframe)

resume_lbl = ttk.Label(mainframe, text = 'Resume')
res_pos = ttk.Entry(mainframe, textvariable='sample')
browse = ttk.Button(mainframe, text = 'Browse', command=get_resume)

company_lbl = ttk.Label(mainframe, text = 'Company')
com_pos = ttk.Entry(mainframe)

job_lbl = ttk.Label(mainframe, text = 'Job Position')
job_pos = ttk.Entry(mainframe)

desc_lbl = ttk.Label(mainframe, text = 'Job Description')
desc_pos = Text(mainframe)

generate = ttk.Button(mainframe, text='Generate', command=generate_letter)
save_as = ttk.Button(mainframe, text='Save', command=save_letter)

mainframe.grid(column=0, row=0, sticky = (N,S,E,W))
content.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N,S,E,W))
api_lbl.grid(column=3, row=0, columnspan=2, sticky=(N,S), padx=5)
api_pos.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=3, padx=5)


resume_lbl.grid(column=3, row=1, columnspan=2, sticky=(N,W), pady=(50,0), padx=(10,300))
res_pos.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=(50,0), padx=(85,80))
browse.grid(column=3, row=1, columnspan=2, sticky=(N,E), pady=(49,0), padx=(305,0))
company_lbl.grid(column=3, row=1, columnspan=2, sticky=(N,W), pady=(80,0), padx=(10,300))
com_pos.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=(80,0), padx=(85,0))
job_lbl.grid(column=3, row=1, columnspan=2, sticky=(N,W), pady=(110,0), padx=(10,300))
job_pos.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=(110,0), padx=(85,0))
desc_lbl.grid(column=3, row=1, columnspan=2, sticky=(N), pady=(150,0), padx=5)
desc_pos.grid(column=3, row=1, columnspan=2, sticky=(N,S,E,W), pady=(168,20), padx=5)

save_as.grid(column=3,row=4)
generate.grid(column=4, row=4)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=3)
mainframe.columnconfigure(1, weight=3)
mainframe.columnconfigure(2, weight=3)
mainframe.columnconfigure(3, weight=1)
mainframe.columnconfigure(4, weight=1)
mainframe.rowconfigure(1, weight=1)

# ---------------------------------------- Content ----------------------------------------- #
content_box = Text(content)
scroll = ttk.Scrollbar(content, orient=VERTICAL, command=content_box.yview) 

content_box.grid(column=0, row=0, sticky=(N,E,S,W)) 
scroll.grid(column=1, row=0, sticky=(N,S))

content.columnconfigure(0, weight=3)
content.rowconfigure(0, weight=1)
content_box.configure(yscrollcommand=scroll.set)

#  --------------------------------------- Mainloop ---------------------------------------- #
root.mainloop()