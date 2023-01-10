import pycountry
from tkinter import Tk, Label, Button, Entry
from phone_iso3166.country import phone_country

class Country_Identity:
    
    def __init__(self, App):
        self.window = App
        self.window.title("Phone number Tracker")
        self.window.geometry("500x400")
        self.window.configure(bg="white")
        self.window.resizable(False, False)

        # Application menu
        Label(App, text="Enter a phone number",fg="black", font=("Times", 20), bg="white").place(x=150,y= 30)
        self.phone_number = Entry(App, width=16, font=("Arial", 15), relief="flat")
        self.track_button = Button(App, text="Track Country", bg="white", relief="sunken")
        self.country_label = Label(App,fg="black", font=("Times", 20), bg="white")

        # Place widgets on the window
        self.phone_number.place(x=170, y=120)
        self.track_button.place(x=200, y=200)
        self.country_label.place(x=100, y=280)

        # Linking button with countries 
        self.track_button.bind("<Button-1>", self.Tracker)
    
    def Tracker(self, event):
        
        phone_number = self.phone_number.get()
        country = "Country is Unknown"
        if phone_number:
            tracked = pycountry.countries.get(alpha_2=phone_country(phone_number))

            if tracked:
                    if hasattr(tracked, "official_name"):
                        country = tracked.official_name
                    else:
                        country = tracked.name
        self.country_label.configure(text=country)



PhoneTracker = Tk()
MyApp = Country_Identity(PhoneTracker)
PhoneTracker.mainloop()