from datetime import datetime as date
day=date.today().strftime("%A")
print(day)
def get_day():
    if day=='Monday':
        bgcolor='blue'
        h1color='green'
        bgcolor={'bgclr':'blue','h1color':'green'}
    if day=='Tuesday':
        bgcolor = 'Aqua'
        h1color = 'red'
    if day=='Wednesday':
        bgcolor = 'Thistle'
        h1color = 'pink'
    if day=='Thursday':
        bgcolor = 'LightSeaGreen'
        h1color = 'white'
    if day=='Friday':
        bgcolor = 'orange'
        h1color = 'blue'
    if day=='Saturday':
        bgcolor = 'Tan'
        h1color = 'white'
    if day=='Sunday':
        bgcolor = 'pink'
        h1color = 'green'
    color={'bgcolor':bgcolor,'h1color':h1color}
    return color



