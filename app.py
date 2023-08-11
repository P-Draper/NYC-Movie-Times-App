import customtkinter
from mgscraper import MetrographScraper
from synscraper import SyndicatedScraper

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        #ctkinter set up
        customtkinter.set_appearance_mode('dark')
        customtkinter.set_default_color_theme('dark-blue')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        #creating tkinter layout
        self.textbox = customtkinter.CTkTextbox(master=self, width=800, height=800, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        #pulling in the data from our metrograph scraper
        metro_scraper = MetrographScraper('https://metrograph.com/nyc/')
        metro_film_data = metro_scraper.get_film_data()
        #pulling in the data from our syndicated scraper
        syndicated_scraper = SyndicatedScraper('https://ticketing.useast.veezi.com/sessions/?siteToken=dxdq5wzbef6bz2sjqt83ytzn1c')
        syndicated_film_data = syndicated_scraper.get_film_data()
        #iterate through the data and insert to tkinter
        self.textbox.insert('end', '_________________METROGRAPH THEATER_________________\n')
        for film in metro_film_data:
            self.textbox.insert("end", f"Title: {film['Title']}\n")
            self.textbox.insert("end", f"Synopsis: {film['Synopsis']}\n")
            self.textbox.insert("end", f"Date: {film['Date']}\n")
            self.textbox.insert("end", "\n")
        #iterate through the data and insert to tkinter
        self.textbox.insert('end', '_________________SYNDICATED THEATER________________\n')
        for film in syndicated_film_data:
            self.textbox.insert('end', f"Title: {film['Title']}\n")
            self.textbox.insert('end', f"Date: {film['Date']}\n")
            self.textbox.insert('end', f"Time: {film['Time']}\n")
            self.textbox.insert('end', "\n")

app = App()
app.mainloop()