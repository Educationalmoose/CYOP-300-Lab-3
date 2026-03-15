"""
Name: Mason Conaway
Course: CYOP 300
Date 3/11/2026
"""
import os
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# gets the directory of the current main.py file
script_dir = os.path.dirname(os.path.abspath(__file__))

alabama = {'name':'Alabama', 'abbr': 'AL', 'capital':'Montgomery',
           'population': '5237750', 'flower': 'Camellia'}
alaska = {'name':'Alaska', 'abbr': 'AK', 'capital':'Juneau',
          'population': '747379', 'flower': 'Alpine Forget-me-not'}
arizona = {'name':'Arizona', 'abbr': 'AZ', 'capital':'Phoenix',
           'population':'7801100','flower':'Saguaro cactus blossom'}
arkansas = {'name':'Arkansas', 'abbr': 'AR', 'capital':'Little Rock',
            'population': '3126140', 'flower': 'Apple blossom'}
california = {'name':'California','abbr':'CA','capital':'Sacramento',
             'population':'39896400','flower':'California poppy'}
colorado = {'name':'Colorado','abbr':'CO','capital':'Denver',
            'population':'6069800','flower':'Rocky Mountain columbine'}
connecticut = {'name':'Connecticut','abbr':'CT','capital':'Hartford',
               'population':'3739160','flower':'Mountain Laurel'}
delaware = {'name':'Delaware', 'abbr': 'DE', 'capital':'Dover',
            'population': '1082900', 'flower': 'Peach Blossom'}
florida = {'name':'Florida', 'abbr': 'FL', 'capital':'Tallahassee',
           'population': '24306900', 'flower': 'Orange Blossom'}
georgia = {'name':'Georgia', 'abbr': 'GA', 'capital':'Atlanta',
           'population': '11413800', 'flower': 'Cherokee Rose'}
hawaii = {'name':'Hawaii', 'abbr': 'HI', 'capital':'Honolulu',
          'population': '1455660', 'flower': 'Lokelani'}
idaho = {'name':'Idaho', 'abbr': 'ID', 'capital':'Boise',
         'population': '2062610', 'flower': 'Syringa'}
illinois = {'name':'Illinois', 'abbr': 'IL', 'capital':'Springfield',
            'population': '12846000', 'flower': 'Violet'}
indiana = {'name':'Indiana', 'abbr': 'IN', 'capital':'Indianapolis',
           'population': '7012560', 'flower': 'Peony'}
iowa = {'name':'Iowa', 'abbr': 'IA', 'capital':'Des Moines',
        'population': '3287640', 'flower': 'Wild Rose'}
kansas = {'name':'Kansas', 'abbr': 'KS', 'capital':'Topeka',
          'population': '3008820', 'flower': 'Wild Native Sunflower'}
kentucky = {'name':'Kentucky', 'abbr': 'KY', 'capital':'Frankfort',
            'population': '4663930', 'flower': 'Goldenrod'}
louisiana = {'name':'Louisiana', 'abbr': 'LA', 'capital':'Baton Rouge',
             'population': '4617080', 'flower': 'Louisiana Iris'}
maine = {'name':'Maine', 'abbr':'ME','capital':'Augusta',
         'population':'1415740','flower':'White Pine Cone and Tassel'}
maryland = {'name':'Maryland', 'abbr': 'MD', 'capital':'Annapolis',
            'population': '6355540','flower': 'Black-Eyed Susan'}
massachusetts = {'name':'Massachusetts', 'abbr': 'MA', 'capital':'Boston',
                 'population': '7275380','flower': 'Mayflower'}
michigan = {'name':'Michigan', 'abbr': 'MI', 'capital':'Lansing',
            'population': '10077331', 'flower': 'Apple Blossom'}
minnesota = {'name':'Minnesota', 'abbr': 'MN', 'capital':'St. Paul',
             'population': '5706494','flower': 'Pink & White lady\'s slipper'}
mississippi = {'name':'Mississippi', 'abbr': 'MS', 'capital':'Jackson',
               'population': '2961279', 'flower': 'Coreopsis'}
missouri = {'name':'Missouri', 'abbr': 'MO', 'capital':'Jefferson City',
            'population': '6154913','flower': 'White Hawthorn Blossom'}
montana = {'name':'Montana', 'abbr': 'MT', 'capital':'Helena',
           'population': '1084225', 'flower': 'Bitterroot'}
nebraska = {'name':'Nebraska', 'abbr': 'NE', 'capital':'Lincoln',
            'population': '1961504', 'flower': 'Goldenrod'}
nevada = {'name':'Nevada', 'abbr': 'NV', 'capital':'Carson City',
          'population': '3104614', 'flower': 'Sagebrush'}
new_hampshire = {'name':'New Hampshire','abbr':'NH','capital':'Concord',
                 'population':'1377529','flower':'Purple Lilac'}
new_jersey = {'name':'New Jersey', 'abbr': 'NJ', 'capital':'Trenton',
              'population': '9288994', 'flower': 'Violet'}
new_mexico = {'name':'New Mexico', 'abbr': 'NM', 'capital':'Santa Fe',
              'population': '2117522', 'flower': 'Yucca'}
new_york = {'name':'New York', 'abbr': 'NY', 'capital':'Albany',
            'population': '20201249', 'flower': 'Rose'}
north_carolina = {'name':'North Carolina','abbr':'NC','capital':'Raleigh',
              'population':'10439388','flower':'Carolina Lily'}
north_dakota = {'name':'North Dakota','abbr':'ND','capital':'Bismarck',
            'population':'779094','flower':'Wild Prairie Rose'}
ohio = {'name':'Ohio', 'abbr': 'OH', 'capital':'Columbus',
        'population': '11799448', 'flower': 'Red Carnation'}
oklahoma = {'name':'Oklahoma', 'abbr': 'OK', 'capital':'Oklahoma City',
            'population':'3959353','flower':'Oklahoma Rose'}
oregon = {'name':'Oregon', 'abbr': 'OR', 'capital':'Salem',
          'population': '4237256', 'flower': 'Oregon Grape'}
pennsylvania = {'name':'Pennsylvania', 'abbr': 'PA', 'capital':'Harrisburg',
                'population': '13002700','flower': 'Mountain Laurel'}
rhode_island = {'name':'Rhode Island', 'abbr': 'RI', 'capital':'Providence',
                'population': '1097379', 'flower': 'Violet'}
south_carolina = {'name':'South Carolina','abbr':'SC','capital':'Columbia',
              'population':'5118425','flower':'Yellow Jessamine'}
south_dakota = {'name':'South Dakota','abbr':'SD','capital':'Pierre',
            'population':'886667','flower':'American Pasque'}
tennessee = {'name':'Tennessee', 'abbr': 'TN', 'capital':'Nashville',
             'population': '6910840', 'flower': 'Iris'}
texas = {'name':'Texas', 'abbr': 'TX', 'capital':'Austin',
         'population': '32416700', 'flower': 'Bluebonnet'}
utah = {'name':'Utah', 'abbr': 'UT', 'capital':'Salt Lake City',
        'population': '3624400', 'flower': 'Sego Lily'}
vermont = {'name':'Vermont', 'abbr': 'VT', 'capital':'Montpelier',
           'population': '643077', 'flower': 'Red Clover'}
virginia = {'name':'Virginia', 'abbr': 'VA', 'capital':'Richmond',
            'population': '8631393','flower': 'American dogwood'}
washington = {'name':'Washington','abbr':'WA','capital':'Olympia',
              'population':'7705281','flower':'Coast Rhododendron'}
west_virginia = {'name':'West Virginia','abbr':'WV','capital':'Charleston',
              'population': '1793716','flower':'Rhododendron'}
wisconsin = {'name':'Wisconsin', 'abbr': 'WI', 'capital':'Madison',
             'population': '5893718', 'flower': 'Wood Violet'}
wyoming = {'name':'Wyoming', 'abbr': 'WY', 'capital':'Cheyenne',
           'population': '576851', 'flower': 'Indian Paintbrush'}

states_list = [
    alabama, alaska, arizona, arkansas, california, colorado, connecticut, delaware,
    florida, georgia, hawaii, idaho, illinois, indiana, iowa, kansas, kentucky,
    louisiana, maine, maryland, massachusetts, michigan, minnesota, mississippi,
    missouri, montana, nebraska, nevada, new_hampshire, new_jersey, new_mexico,
    new_york, north_carolina, north_dakota, ohio, oklahoma, oregon, pennsylvania,
    rhode_island, south_carolina, south_dakota, tennessee, texas, utah, vermont,
    virginia, washington, west_virginia, wisconsin, wyoming
]

def menu():
    """Main Menu with options for user to navigate the program"""
    print("******************")
    print("     Welcome!")
    print("******************")

    while True:
        print("\nChoose an item from the menu below:")
        selection = input("\t1.  Display all U.S. States in Alphabetical Order"
                          "\n\t2.  Search For a Specific State"
                          "\n\t3.  Show Top 5 Populated States"
                          "\n\t4.  Update a State's Population"
                          "\n\t5.  Exit\n")
        match selection:
            case '1':
                sort_and_display_all_states()
                thank_user()
                continue
            case '2':
                search_for_state_and_return_facts()
                thank_user()
                continue
            case '3':
                show_top_5_states()
                thank_user()
                continue
            case '4':
                update_state_population()
                thank_user()
                continue
            case '5':
                thank_user()
                input()
                return
            case _:
                print("ERROR: Please select an option 1-5")
                continue

def sort_and_display_all_states():
    """Sorts the states alphabetically and displays all relevant information"""
    # creates a new list with the states from the dictionary sorted by the 'name' key
    sorted_states = sorted(states_list, key=lambda x: x['name'])
    for state in sorted_states:
        name = state.get('name')
        capital = state.get('capital')
        population = int(state.get('population'))
        flower = state.get('flower')
        print(f"NAME: {name}, CAPITAL: {capital}, "
              f"POPULATION: {population:,}, STATE FLOWER: {flower}")

def search_for_state_and_return_facts():
    """Search for a specific state by name or 2-digit state code"""
    while True:
        state_str = input("\nSearch for a state by entering its name or its"
                          " 2-character abbreviation:\n").lower()
        match = search_for_state(state_str)
        if match is not None:
            # gets the image path based on the root, the folder name, and the state name
            image_path = os.path.join(script_dir, 'Flowers', f'{match.get('name')}.jpg')
            # uses the image as the background for the graph
            img = np.asarray(Image.open(image_path))
            # plots the image and shows it to the user
            plt.imshow(img)
            plt.show()
            print("State facts for " + match.get('name') + ": ")
            print("\tCapital: " + match.get('capital'))
            print(f"\tPopulation: {int(match.get('population')):,}")
            print("\tState Flower: " + match.get('flower'))
            return
        print("ERROR: State not found. Check your spelling and try again.")

def show_top_5_states():
    """Returns a list of top 5 states with the highest population"""
    # sort the states by population and store it into a new list
    pop_sorted = sorted(states_list, key=lambda x: int(x['population']), reverse=True)
    new_list = pop_sorted[:5] # get the first 5 states
    names = [state['name'] for state in new_list] # make a new list with just the names
    populations = [int(state['population']) for state in new_list] # just the populations

    # setup matplotlib plot to show a bar graph with the top 5 state's data
    plt.bar(names, populations)
    plt.title('U.S. States with the Highest Populations')
    plt.xlabel('U.S. States')
    plt.ylabel('Population')
    plt.show()

def update_state_population():
    """Allows the user to update the population of a state"""
    while True:
        state_str = input("\nSearch for a state by entering its name or its"
                      " 2-character abbreviation: ").lower()
        match = search_for_state(state_str)
        if match is not None:
            print(f"SELECTED STATE: {match.get('name')}")
            print(f"CURRENT POPULATION: {int(match.get('population')):,}")
            new_pop = input("\nWhat would you like to set the population to?: \n")
            try:
                new_pop = int(new_pop) # by check if the input is an integer
                if new_pop >= 0:
                    match['population'] = str(new_pop) # set the population
                    print("Population set to " + str(new_pop))
                    break
                print("ERROR: Please enter a positive whole number for the new population")
            except ValueError:
                print("ERROR: Please enter a positive whole number for the new population")
        else:
            print("ERROR: State not found. Check your spelling and try again.")

def search_for_state(state_str):
    """Search for a specific state by name or 2-digit state code"""
    for state in states_list:
        # allows the user to get the state information with the name or abbreviation
        if state_str == state.get('name').lower() or state_str == state.get('abbr').lower():
            return state # end the loop early if a match is found to increase performance
    return None

def thank_user():
    """Thanks the user for participating"""
    print("\n**************************************")
    print("   Thank you for using the program!")
    print("**************************************")

menu()
