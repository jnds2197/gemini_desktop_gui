import google.generativeai as genai
import customtkinter

#gemini config
API_KEY = ''
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

#main function
def get_response():
    response = model.generate_content(entry.get())
    response_text.configure(state="normal")
    if response_text.get("0.0", "end") == "\n":
        response_text.insert("end", "Query: " + entry.get() + "\n")
        response_text.insert("end", "Response: " +response.text + "\n")
    else:
        response_text.insert("end", "\n" + "Query: " + entry.get() + "\n")
        response_text.insert("end", "Response: " +response.text + "\n")
    response_text.configure(state="disabled")
    entry.delete(first_index=0, last_index="end")

#window config
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
#CenterWindowToDisplay function source: https://github.com/TomSchimansky/CustomTkinter/discussions/1820
def CenterWindowToDisplay(Screen: customtkinter.CTk, width: int, height: int):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/1.25) - (width/1.25))
    y = int((screen_height/2) - (height/1.5))
    return f"{width}x{height}+{x}+{y}"
root = customtkinter.CTk()
root.geometry(CenterWindowToDisplay(root, 600, 400))
root.title('Gemini Desktop')
frame = customtkinter.CTkFrame(master=root)
frame.pack(fill="both", expand=False)
response_text = customtkinter.CTkTextbox(master=frame)
response_text.pack(pady=10, padx=10, fill="x")
response_text.configure(state="disabled")
label = customtkinter.CTkLabel(master=frame, text="Enter here any query you might have for Gemini.")
label.pack(pady=(20,0))
entry = customtkinter.CTkEntry(master=frame, placeholder_text="Type your query here")
entry.pack(pady=10, padx=10, fill="x")
def add_element_callback(event):
    get_response()
entry.bind("<Return>", add_element_callback)
entry.focus_set()
button = customtkinter.CTkButton(master=frame, text="Send", command=get_response)
button.pack(pady=15, padx=15)

root.mainloop()
