from tkinter import *
from analyze_sentiment import SentimentManager

window = Tk()
window.title("I get you're Probably Angry")
window.config(padx=50, pady=50)
sentiment_manager = SentimentManager()

def analyze_input():
    result = sentiment_manager.analyze(input_sentence_entry.get())
    if result[0]['label'] == 'POSITIVE':
        emoji_btn.config(text='🤩')
    elif result[0]['label'] == 'NEGATIVE':
        emoji_btn.config(text='😿')
    input_sentence_entry.delete(0, END)
    window.after(2000, lambda: emoji_btn.config(text="🫨"))  # Reset after 2 seconds

input_sentence_entry = Entry(width=100)
input_sentence_entry.grid(column=2, row=1)

emoji_btn = Button( text="🫨", font=('Arial', 60, 'bold'),
                    highlightthickness=0, 
                    command = analyze_input)

emoji_btn.grid(column=2, row=2)


window.mainloop()