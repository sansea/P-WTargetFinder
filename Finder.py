import requests

#################
#Your Info Here #
#################

#put your API between the ''
API = ''
#Minium Infra per city after the =
minimium_Infra = 
#Your Score After the =
your_score = 


#Todo
#possible discord bot
#see if nation was in the last 5000 wars as a way of gauging recent wars.
#webscrabing for more accurate target finding this voids the discord bot option though.




########################
#Don't edit below here #
########################
potentional_targets = []

#Math for War range
max_score = your_score + your_score * .75
min_score = your_score * 75 / 100


Nations = f'https://politicsandwar.com/api/v2/nations/{API}/&min_score={min_score}&max_score={max_score}&alliance_id=0'

##Pulling API data on countries within war range
response = requests.get(Nations)
response = response.json()

for nation in response['data']:
    #Calculating expected score based off the scoring calculation of P&W
    #Score = ((Cities - 1)*50) + (Infrastructure * 0.025)
    expected_score = nation['cities'] * 50 + nation['cities'] * minimium_Infra / 100 * 5
    if nation['war_policy'] != 5 and nation['score'] >= expected_score and nation['offensive_wars'] == 0 and nation['defensive_wars'] == 0 and nation['v_mode_turns'] == 0 and nation['color'] != 0:
        print(nation['nation'] + " is being added to the target list.")
        potentional_targets.append(nation['nation_id'])


#Open the file
myfile = open('Targets.txt', 'w')

#Write all nations to file for easy use.
for nation in potentional_targets:
    myfile.write("\n" + "https://politicsandwar.com/nation/id=" + str(nation))
    
myfile.close()





