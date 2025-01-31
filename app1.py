
import streamlit as st
Riyadh1 = {
    'Leap 2025': {
        'genre': ['trending', 'tech'],
        'description': 'LEAP is an annual tech event that was founded in 2022 by the Ministry of Communication and Information Technology (Saudi Arabia) (MCIT), the Saudi Federation for Cybersecurity, Programming and Drones (SAFCSP) and Tahaluf, an Informa company.',
        'start_date': '2025-02-09',
        'end_date': '2025-02-12',
        'img': 'imgs\leap.png'
    },
    'Porter House':{
        'genre': ['restaurant'],
        'description': 'PORTERHOUSE Restaurant Porter House is considered one of the best steak and meat restaurants in Riyadh. The restaurant is 100% Saudi. It was established in 2016. Children are only allowed until 7 pm.',
        'img': 'imgs\porter_house.jpg'
    },
    'Mama Noura':{
        'genre': ['restaurant'],
        'description': 'Mama Noura is your destination to savor the most delicious oriental and Arabic food in Riyadh, with dishes that reflect the distinctive and authentic taste of traditional Arabic food.',
        'img': 'imgs\mama_noura.jpg'
    },
    'The National Musem': {
        'genre':['tourist attraction', 'historical'],
        'description': 'King Abdulaziz Historical Center (KAHC) is a cross-district heritage complex in Riyadh, Saudi Arabia, covering south of al-Murabba and north of al-Futah. Inaugurated in 1999, it includes several historic buildings and open green spaces that surround the Murabba Palace compound, which was the main residence and workplace of King Abdulaziz ibn Saud between 1938 and 1953.',
        'img': 'imgs\national_musem.jpg'
    },
    'Riyadh Zoo': {
        'genre':['tourist attraction', 'zoo'],
        'description': 'Riyad zoo is home to more than 1,300 animals from 190 species, which live in six protected areas.',
        'img': 'imgs\zoo.png'
    },
    'Boulevard City': {
        'genre': ['tourist attraction', 'restaurant', 'shopping', 'entertainment'],
        'description': 'Boulevard City contains gardens, dancing fountain, several cafes, local and global restaurants, shops for the most famous local and world brands, as well as many theatres for artistic and singing performances.',
        'img': 'imgs\city.jpeg'
    },
    'Taibah Market': {
        'genre': ['shopping', 'historical'],
        'description': "Souq Taibah is one of the oldest markets in Riyadh. Despite the sweep of modern commercial malls, it is still a main destination for the people of the city to purchase necessities, antiques, and many others, as the prices of its goods compete with the rest of the markets.",
        'img': 'imgs\souq-taibah.jpeg'
    },
    'Snow Village':{
        'genre': ['entertainment', 'trending'],
        'description': 'This place gives a good experience of snow games, fun and rides right in RIyadh. You don’t need any equipment to go there as they will provide you with a full gear for the adventure including gloves and an additional pair of socks.',
        'start_date': '2024-12-12',
        'end_date': '2025-02-02',
        'img': 'imgs\snow.jpg',
        'price': 27
    },
    'Saudi Cup 2025': {
        'genre': ['sprots', 'trending'],
        'description': 'The world’s finest thoroughbreds and jockeys descend on King Abdulaziz Racecourse in Riyadh for Saudi Cup Weekend 2025 with prize money of over US$37.5M on offer. A celebration of the best Saudi sporting, entertainment, cuisine, and cultural experiences headlined by the World’s Richest Race, the Saudi Cup where US$20M is to be won. As the pinnacle of style, sophistication, and glamour, this is Riyadh’s social event of the year and a jewel in the crown of international racing.',
        'start_date': '2025-02-21',
        'end_date': '2025-02-22',
        'img': 'imgs\saudi_cup.png',
        'price': 175
    }
    
    
}

Jeddah1 = {
    
    'AROYA Cruise': {
        'genre': ['trending', 'entertainment'],
        'description': 'The first ever remarkably Arabian cruise line, Our story began with an idea to offer our guests a vacation that is one of its kind, tailored to reflect the rich hospitality of the region that is unmatched anywhere in the world, to sail on an exceptional voyage in the red sea with an Arabian touch.',
        'start_date': '2024-12-16',
        'end_date': '2025-05-01',
        'img': 'imgs/aroya-cruises.jpg',
        'price': 1350
    },
    'Formula E': {
        'genre': ['trending', 'sports'],
        'description': 'the Kingdom of Saudi Arabia gets set to host another pair of races taking place on Friday 14 and Saturday 15 February 2025.',
        'start_date': '2025-02-14',
        'end_date': '2025-02-15',
        'img': 'imgs/formula.jpg',
        'price':70
    },
    
}
st.title('Tourism in Saudi Arabia')
st.write("Choose the cities you want to visit :")
Riyadh = st.checkbox("Riyadh")
Jeddah = st.checkbox("Jeddah")

eventType ={
"Riyadh" :  [genre for R in Riyadh1.values() for genre in R['genre']],
"Jeddah" :  [genre for J in Jeddah1.values() for genre in J['genre']]
}

def getOptions(cities):
    listEvent = []
    for city in cities:
        listEvent.extend(eventType[city])
    return sorted(set(listEvent))



if Riyadh and Jeddah:
    options = sorted(set(eventType["Riyadh"] + eventType["Jeddah"]))
    st.multiselect("Select the event type", options=getOptions(["Riyadh","Jeddah"]))
    st.write("R and J")
elif Riyadh:
    st.multiselect("Select the event type", options=getOptions(["Riyadh"]))
    st.write("R")
elif Jeddah:
    st.multiselect("Select the event type", options=getOptions(["Jeddah"]))
    st.write("J")


