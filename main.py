import PySimpleGUI as sg
#import faster_than_requests as requests

sg.theme('TealMono')   
headings = ['     File     ', '     Size     ', '     Downloaded     ', '     Speed     ', '     Time Elapsed     ']
data = [['data' for row in range(5)]for col in range(10)]

file_layout = [
[sg.Text('File URL', size=(15,1)), sg.InputText()],
[sg.Text('Target Directory',size=(15,1)), sg.InputText(), sg.FolderBrowse()],
[sg.Button('Download', size=(15,1)), sg.Button('Clear')]
]



jobs_layout = [
[sg.Table(data,headings=headings,row_height=50,auto_size_columns=True,justification="center")]
]


settings_layout = [

]

layout = [
[sg.TabGroup([[sg.Tab('File', file_layout), sg.Tab('Jobs', jobs_layout), sg.Tab('Settings', settings_layout)]])],
[sg.Text("Logs")],
[sg.Output(size=(75,5))],
]




# Create the Window
window = sg.Window('fafDM', layout, finalize=True)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):   # if user closes window or clicks cancel
        break
    if event is "Jobs":
    	currlayout = "hi"
    print(event)
    print(values)

window.close()