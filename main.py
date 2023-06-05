import tkinter
import ttkbootstrap as ttk

train_classes = {
    '170': "The Class 170 is a series of diesel multiple units built by Bombardier Transportation (previously Adtranz) at their Litchurch Lane Works in Derby. They are also known as Turbostar.",
    '205': "The British Rail Class 205 (3H) diesel-electric multiple units were built by BR at Eastleigh from 1957 to 1962, and in service for 47 years from BR Southern Region to Connex South Central and finally to the Southern franchise. They were eventually replaced by Class 171 Turbostar units.",
    '37': "The British Rail Class 37 is a diesel-electric locomotive also known as the English Electric Type 3. The Class was ordered as part of the British Rail modernisation plan.",
    '47': "The British Rail Class 47 is a class of British railway diesel-electric locomotive that was developed in the 1960s by Brush Traction. A total of 512 Class 47s were built at Crewe Works and Brush's Falcon Works, Loughborough between 1962 and 1968, which made them the most numerous class of British mainline diesel locomotive.",
    '31': "The British Rail Class 31 diesel locomotives, also known as the Brush Type 2 and originally as Class 30, were built by Brush Traction from 1957-62.",
    '70': "The British Rail Class 70 is a class of diesel-electric freight locomotives built by General Electric.",
    '73': "The British Rail Class 73 is an electro-diesel train, manufactured by British Rail Engineering Limited.",
    'e320': "The Eurostar e320 is a high-speed electric multiple unit train capable of speeds up to 320 km/h (200 mph).",
    '395': "Southeastern’s Javelin trains are high-speed electric multiple units capable of speeds up to 225 km/h (140 mph).",
    '158': "The British Rail Class 158 Express Sprinter is a diesel multiple unit (DMU) passenger train. They were built for British Rail between 1989 and 1992 by BREL at their Derby Worksf.",
    '755': "The British Rail Class 755 FLIRT is a class of bi-mode multiple unit passenger train built by Stadler Rail for Greater Anglia.",
    '156': "The British Rail Class 156 Super Sprinter is a diesel multiple unit (DMU) train intended for use on rural and regional services in Great Britain. They were built for British Rail between 1987 and 1989 by Metro-Cammell's Washwood Heath works.",
    '142': "The British Rail Class 142 Pacer is a type of two-car articulated railbus designed for use on rural and suburban services in Great Britain. They were built between 1985 and 1987 by BREL Derby and Leyland Bus.",
    '171': "The British Rail Class 171 Turbostar is a type of diesel multiple unit (DMU) passenger train used on Southern services on the non-electrified Oxted Line and Marshlink Line in South East England.",
    '222': "The British Rail Class 222 Meridian is a type of high-speed diesel-electric multiple unit passenger train used on services operated by East Midlands Railway on the Midland Main Line in England.",
    '180': "The British Rail Class 180 Adelante is a type of high-speed diesel-hydraulic multiple unit passenger train used on various services in Great Britain.",
    '175': "The British Rail Class 175 Coradia is a type of diesel multiple unit passenger train used in Great Britain. They were built from 1999 to 2001 by Alstom at Washwood Heath in Birmingham.",
    '91': "The British Rail Class 91 is a class of high-speed electric locomotives built by BREL at Crewe Works from 1988-1991 for use on the East Coast Main Line in Great Britain.",
    '66': "The British Rail Class 66 is a type of six-axle diesel-electric freight locomotive developed in part from the Class 59, for use on the railways of the UK. They were built by Electro-Motive Diesel (EMD) and introduced to traffic from 1998 to 2016.",
    '800': "The British Rail Class 800 – branded by Great Western Railway (GWR) as Intercity Express Train (IET), and London North Eastern Railway (LNER) as Azuma – is a type of bi-mode multiple unit train built by Hitachi Rail for GWR and LNERf.",
    '801': "The British Rail Class 801 Super Express is the electric multiple unit (EMU) variant of the Hitachi Super Express, based on the Hitachi A-train, high-speed trains to be used in the United Kingdom.",
    '802': "The British Rail Class 802 is a type of bi-mode multiple unit train built by Hitachi Rail for use on various services in Great Britain. They are part of the Hitachi AT300 product family and are closely related to the Class 800 and Class 801 trains used by other operators.",
    '377': "The British Rail Class 377 Electrostar is a type of electric multiple unit passenger train used on various services in Great Britain. They were built by Bombardier Transportation at their Derby Litchurch Lane Works from 2001-2014.",
    '357': "The British Rail Class 357 Electrostar is a type of electric multiple unit passenger train used on various services in Great Britain. They were built by Adtranz at their Derby Litchurch Lane Works from 1999-2002.",
    '150': "The British Rail Class 150 Sprinter is a type of diesel multiple unit (DMU) train intended for use on rural and suburban services in Great Britain. They were built for British Rail between 1984 and 1987 by BREL York.",
    '707': "The British Rail Class 707 Desiro City is a type of electric multiple unit passenger train used on various services in Great Britain. They were built by Siemens Mobility at their Krefeld-Uerdingen factory in Germany from 2014-2017.",
    '700': "The British Rail Class 700 Desiro City is a type of electric multiple unit passenger train used on Thameslink services in Great Britain. They were built by Siemens Mobility at their Krefeld-Uerdingen factory in Germany from 2014-2018.",
    '68': "The British Rail Class 68 is a type of mainline mixed-traffic diesel-electric locomotive manufactured by Stadler Rail for Direct Rail Services in the United Kingdom. They were introduced to traffic from 2013 to present.",
    '58': "The British Rail Class 58 is a class of Co-Co diesel locomotive designed for heavy freight. The narrow body with cabs at either end led to them being given the nickname 'Bone' by rail enthusiasts.",
    '56': "The British Rail Class 56 is a type of diesel locomotive designed for heavy freight work. It is a Type 5 locomotive, with a Ruston-Paxman power unit developing 3,250 bhp (2,423 kW), and has a Co-Co wheel arrangement.",
    '60': "The British Rail Class 60 is a class of Co-Co heavy freight diesel-electric locomotives built by Brush Traction. They are nicknamed Tugs by rail enthusiasts.",
    '67': "The British Rail Class 67 is a type of mainline diesel-electric locomotive built for the English Welsh & Scottish Railway (EWS) by Alstom at Meinfesa's Valencia plant in Spain. They were introduced to traffic from 1999 to 2000.",
    '302': "The British Rail Class 302 (pre-TOPS AM2) was a type of electric multiple unit (EMU) introduced between 1958 and 1960 for outer suburban passenger services on the London, Tilbury and Southend line[^1^][3].",
    '301': "The British Rail Class 301 was a proposed type of electric multiple unit (EMU) that was planned to be introduced on the London, Tilbury and Southend line. However, the class was never built.",
    '123': "The British Rail Class 123 was a type of diesel multiple unit (DMU) introduced in 1963 for use on the Western Region of British Railways. They were built by BR Swindon Works.",
    '303': "The British Rail Class 303 is a type of electric multiple unit (EMU) introduced in 1960 for use on the suburban rail network around Glasgow. They were built by Pressed Steel Company.",
    '321': "The British Rail Class 321 is a class of electric multiple unit (EMU) passenger train built by British Rail Engineering Limited's York Carriage Works in three batches between 1988 and 1991 for Network SouthEast and Regional Railways[^2^][2].",
    '322': "The British Rail Class 322 were electric multiple unit passenger trains which were built by British Rail Engineering Limited in 1990 for the Stansted Express service from London Liverpool Street to Stansted Airport[^3^][5].",
    '323': "The British Rail Class 323 is a class of electric multiple unit (EMU) passenger train built by Hunslet Transportation Projects and Holec. All 43 units were built from 1992 through to 1995, although mock-ups and prototypes were built and tested in 1990 and 1991[^4^][4].",
    '350': "The British Rail Class 350 Desiro is a type of electric multiple unit passenger train used on various services in Great Britain. They were built by Siemens Mobility at their Krefeld-Uerdingen factory in Germany from 2004-2014.",
    '360': "The British Rail Class 360 Desiro is a type of electric multiple unit passenger train used on various services in Great Britain. They were built by Siemens Mobility at their Krefeld-Uerdingen factory in Germany from 2002-2005.",
    '90': "The British Rail Class 90 Desiro is a type of electric locomotive used on various services in Great Britain. They were built by British Rail Engineering Limited at their Crewe Works factory in England from 1987-1990. They have a maximum speed of 110 mph and a power output of 5,000 hp.",
    '43': "The British Rail Class 43 High Speed Train (HST) or Intercity 125 is a high speed diesel locomotive, capable of speeds of up to 148 mph. Powered by a Paxman Valenta prime mover, the HST holds the record of the fastest revenue diesel passenger train, when it hit 144 mph between Newcastle and London King’s Cross, on the East Coast Main Line (ECML).",
    '15': "The British Rail Class 15 diesel locomotives, also known as the BTH Type 1, were designed by British Thomson-Houston, and built by the Yorkshire Engine Company and the Clayton Equipment Company, between 1957 and 1961. They were numbered D8200-D8243.",
    '80': "The British Rail Class 80 was a type of AC electric locomotive used on the West Coast Main Line in Great Britain. They were built by Metropolitan-Vickers at their Trafford Park factory in England from 1959-1962. They had a maximum speed of 100 mph and a power output of 2,720 hp.",
    '99': "The British Rail Class 99 was a classification given to British Rail's shipping fleet. They operated various types of ships, such as ferries, hovercrafts and hydrofoils, on routes across the English Channel, Irish Sea and North Sea. They were numbered from 99 001 to 99 999."
}

window = ttk.Window(themename="darkly")
window.geometry("500x500")
window.title("Class Information.")

class_input = ttk.Entry(window, font=("Arial", 12))
class_input.pack(pady=5)

def change_info():
    summary = train_classes.get(class_input.get(), "Could not find information about specified class.")
    information_box.config(text=summary)

get_info_button = ttk.Button(window, text="Get info!", command=change_info)
get_info_button.pack(pady=5)

information_box = ttk.Label(window, text="Enter a class to get information.", wraplength=470, font=("Arial", 10))
information_box.pack(pady=5)

warning_label = ttk.Label(window, text="Warning: Summaries may contain minimal error.", font=("Arial", 10), foreground="dark red")
warning_label.pack()
warning_label.place(relx=0.5, rely=0.95, anchor="center")

tkinter.mainloop()
