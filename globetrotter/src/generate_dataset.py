import json
import requests
from typing import List, Dict
import time

def create_city_dataset() -> List[Dict]:
    dataset = [
        {
            "city": "Paris",
            "country": "France",
            "clues": [
                "This city is home to a famous tower that sparkles every night",
                "Known as the 'City of Love' and a hub for fashion and art",
                "Home to the world's largest art museum"
            ],
            "fun_fact": [
                "The Eiffel Tower was supposed to be dismantled after 20 years but was saved because it was useful for radio transmissions!",
                "Paris has only one stop sign in the entire city—most intersections rely on priority-to-the-right rules",
                "The Louvre was originally built as a fortress in the 12th century"
            ],
            "trivia": [
                "This city is famous for its croissants and macarons",
                "Paris was originally a Roman city called Lutetia",
                "There's a replica of the Statue of Liberty on the Seine River"
            ]
        },
        {
            "city": "Tokyo",
            "country": "Japan",
            "clues": [
                "This city has the busiest pedestrian crossing in the world",
                "Home to the world's largest fish market",
                "Known for its cherry blossom festivals in spring"
            ],
            "fun_fact": [
                "Tokyo has the world's busiest train station - Shinjuku Station serves over 3.5 million passengers daily",
                "There are over 36,000 vending machines in Tokyo",
                "The city has more Michelin-starred restaurants than any other city in the world"
            ],
            "trivia": [
                "The city was originally called Edo",
                "Tokyo's Imperial Palace is built on the site of the old Edo Castle",
                "The city's subway system is so complex that some stations employ professional pushers to help pack trains"
            ]
        },
        {
            "city": "New York",
            "country": "USA",
            "clues": [
                "Home to a famous green statue in the harbor",
                "Known as 'The City That Never Sleeps'",
                "Has a huge park in the middle of the city"
            ],
            "fun_fact": [
                "More than 800 languages are spoken in this city",
                "The first pizzeria in America opened here in 1905",
                "The subway system has 722 miles of track"
            ],
            "trivia": [
                "Wall Street was named after an actual wall that protected the Dutch colony",
                "The city was briefly the capital of the United States",
                "The Brooklyn Bridge is older than Tower Bridge in London"
            ]
        },
        {
            "city": "London",
            "country": "United Kingdom",
            "clues": [
                "Home to a famous clock tower nicknamed 'Big Ben'",
                "Known for its red double-decker buses",
                "Has a giant Ferris wheel by the river"
            ],
            "fun_fact": [
                "The city has six official ravens at the Tower of London",
                "The London Underground is the oldest underground railway network in the world",
                "There's a law that states it's illegal to die in the Houses of Parliament"
            ],
            "trivia": [
                "The Great Fire of 1666 destroyed 80% of the city",
                "London Bridge has been sold and rebuilt multiple times",
                "The city was founded by the Romans in 43 AD"
            ]
        },
        {
            "city": "Rome",
            "country": "Italy",
            "clues": [
                "Home to an ancient amphitheater where gladiators fought",
                "Has a tiny country within its borders",
                "Known for its countless fountains and piazzas"
            ],
            "fun_fact": [
                "People throw about €3,000 into the Trevi Fountain every day",
                "The city has over 2,000 fountains",
                "The Pantheon has the world's largest unreinforced concrete dome"
            ],
            "trivia": [
                "The city was founded in 753 BC",
                "All roads really did lead to Rome in ancient times",
                "The Colosseum could hold up to 50,000 spectators"
            ]
        },
        {
            "city": "Sydney",
            "country": "Australia",
            "clues": [
                "Famous for its opera house with sail-like roofs",
                "Has one of the world's largest natural harbors",
                "Home to the world's largest steel arch bridge"
            ],
            "fun_fact": [
                "The Opera House took 14 years to build and cost $102 million",
                "The Sydney Harbour Bridge is nicknamed 'The Coathanger'",
                "Bondi Beach is one of the oldest surfing beaches in the world"
            ],
            "trivia": [
                "The city was founded as a penal colony in 1788",
                "Sydney Tower is the second tallest observation tower in the Southern Hemisphere",
                "The city hosted the 2000 Summer Olympics"
            ]
        },
        {
            "city": "Dubai",
            "country": "United Arab Emirates",
            "clues": [
                "Home to the world's tallest building",
                "Has artificial islands shaped like palm trees",
                "Known for its indoor ski resort"
            ],
            "fun_fact": [
                "The police force uses luxury cars including Lamborghinis",
                "The city has the world's largest choreographed fountain system",
                "25% of the world's cranes were once operating in this city"
            ],
            "trivia": [
                "It was a small fishing village until the 1960s",
                "The city has no address system - locations are described using landmarks",
                "It has the world's first 7-star hotel"
            ]
        },
        {
            "city": "Singapore",
            "country": "Singapore",
            "clues": [
                "Known for its iconic hotel with an infinity pool on top",
                "Has a giant Ferris wheel called the Flyer",
                "Famous for its street food and hawker centers"
            ],
            "fun_fact": [
                "It's illegal to sell or import chewing gum",
                "The city has the world's first night safari",
                "Half of the country is covered in green space"
            ],
            "trivia": [
                "The name means 'Lion City' in Sanskrit",
                "It's one of only three city-states in the world",
                "The national language is Malay, but English is the main language used"
            ]
        },
        {
            "city": "Venice",
            "country": "Italy",
            "clues": [
                "A city built on water with no roads",
                "Famous for its carnival masks and gondolas",
                "Known for its beautiful glass-making tradition"
            ],
            "fun_fact": [
                "The city is built on millions of wooden piles",
                "There are 417 bridges connecting 118 islands",
                "The city sinks about 1-2 millimeters per year"
            ],
            "trivia": [
                "Marco Polo was born here",
                "The city was an independent republic for over 1,000 years",
                "The first public casino in the world opened here in 1638"
            ]
        },
        {
            "city": "Barcelona",
            "country": "Spain",
            "clues": [
                "Home to an unfinished cathedral by Gaudí",
                "Known for its unique modernist architecture",
                "Has a famous street called Las Ramblas"
            ],
            "fun_fact": [
                "The Sagrada Familia has been under construction for over 135 years",
                "The city has 9 UNESCO World Heritage sites",
                "Barcelona's beach is artificial - it was created for the 1992 Olympics"
            ],
            "trivia": [
                "The city was founded by the Romans",
                "It's the only city to receive a Royal Gold Medal for architecture",
                "The Columbus Monument points to Libya, not America"
            ]
        },
        # ... [Additional cities will be added here]
    ]
    
    return dataset

def save_dataset(dataset: List[Dict], filename: str):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    dataset = create_city_dataset()
    save_dataset(dataset, 'dataset.json')
    print(f"Dataset created with {len(dataset)} cities") 