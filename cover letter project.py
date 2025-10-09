import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from groq import Groq
from groq import BadRequestError
from docx2txt import process
from docx import Document

# ---------------------------------------------------------------- #
def get_resume():
    
    file = filedialog.askopenfilename()
    res_pos.delete(0, END)
    res_pos.insert(0, file)
    
    return

# ---------------------------------------------------------------- #
def clear():
    com_pos.delete(0, END)
    job_pos.delete(0, END)
    desc_pos.delete(1.0, END)
    content_box.delete(1.0, END)
    
    return

# # ---------------------------------------------------------------- #
# def set_save(): 
#     return

# ---------------------------------------------------------------- #
def get_model(x):
    
    global master_model_var
    master_model_var = x
    messagebox.showinfo(message=f'Current Model: {master_model_var}')
    
    return master_model_var
# ---------------------------------------------------------------- #
def check_model():
    # check check to see which model is being used right now, use dialog box
    
    global master_model_var
    messagebox.showinfo(message=f'Current Model: {master_model_var}')
    
    return
# ---------------------------------------------------------------- #
def generate_letter():
    
    try:
        if api_pos.get() != '':

            client = Groq(api_key=api_pos.get().strip())
            
            company = com_pos.get().strip()

            resume = process(res_pos.get().strip())

            role = job_pos.get().strip()

            details = desc_pos.get(1.0, END)

            prompt = f"""
                         Write for me the ideal body of a cover letter for this company: {company}. 
                         for this role: {role}. here are more details about the role {details}. 
                         Use my resume as a reference {resume}.
                      """
            
            model_var = master_model_var
            
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
                    model=model_var,
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
    except BadRequestError as e:
        messagebox.showwarning(title='Bad Request Error', message=f'Error with API request: {str(e)}') 

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
root.option_add('*tearOff', FALSE)

# variable that holds the LLM model that 
# the default model will be llama-3.3-70b-versatile
master_model_var = 'llama-3.3-70b-versatile'

# ----------------------------------- menu / menubar config -------------------------------- #

menubar = Menu(root)
m_file = Menu(menubar) 
m_model = Menu(menubar)
menubar.add_cascade(label="File", menu=m_file)
menubar.add_cascade(menu=m_model, label="Model")
root.config(menu=menubar)

# menu file commands
m_file.add_command(label='Clear', command=clear)
# m_file.add_command(label='Set Save Destination', command=set_save)

# menu model commands
model_list = ['llama-3.1-8b-instant', 'llama-3.3-70b-versatile', 'meta-llama/llama-guard-4-12b', 'openai/gpt-oss-120b', 'openai/gpt-oss-20b', 'whisper-large-v3', 'whisper-large-v3-turbo']

# model list for lust of models based on the hardcoded variable "model_list"
menu_model_list = Menu(m_model)
m_model.add_cascade(menu=menu_model_list, label='List Of Models')
for x in model_list:
    menu_model_list.add_command(label=x, command=lambda x=x: get_model(x))

menu_model_check = Menu(m_model)
m_model.add_command(label='Check Current Model', command=check_model)

# ---------------------------------------- mainframe ----------------------------------------- #
 
mainframe = ttk.Frame(root, padding = (3,3,12,12))
content = ttk.Frame(mainframe, borderwidth=5, relief='ridge', height=200, width=500)

# ----------------------------------------  API Key GUI Config ----------------------------------------- #

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
