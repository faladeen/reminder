import tkinter as tk
from turtle import window_height, window_width 


def main():
  root = tk.Tk()
  root.title('Reminder ... !')
  # root.geometry('600x400+50+50')

  window_width = 600
  window_height = 400

  # get screen dimension
  screen_width = root.winfo_screenwidth()
  screen_height = root.winfo_screenheight()

  # find the center point 
  center_x = int(screen_width/4 - window_width/2)
  center_y = int(screen_height/4 - window_height/2)

  # set position of the window to the center of screen 
  root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

  message = tk.Label(root, text="Hello Tkinter")
  message.pack()

  root.mainloop()


if __name__ == '__main__':
  main()
