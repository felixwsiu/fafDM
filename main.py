import PySimpleGUI as sg
from download import dlAsync
from job import Job

sg.theme('TealMono')   
headings = ['     File     ', '     Size     ', '     Downloaded     ', '     Speed     ', '     Time Elapsed     ']
data = [['data' for row in range(5)]for col in range(10)]

file_layout = [
[sg.Text('File URL', size=(20,1)), sg.InputText(key='URL')],
[sg.Text('Target Directory',size=(20,1)), sg.InputText(key='DIR'), sg.FolderBrowse()],
[sg.Text('Output Name (eg. File.zip)', size=(20,1)), sg.InputText(key='NAME')],
[sg.Text('Threads Allocated', size=(15,1)),sg.Spin([i for i in range(1,8)], initial_value=4,key='THREAD')],
[sg.Button('Download', size=(50,1)), sg.Button('Clear')],
[sg.Image(r'lightningmcqueen.png')]
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
    if event in (None, 'Cancel'):  
        break
    if event is "Jobs":
    	currlayout = "hi"
    if event is "Clear":
    	window['URL'].Update('')
    	window['DIR'].Update('')
    	window['NAME'].Update('')
    if event is "Download":
    	job = Job(values['URL'],values['DIR'],values['NAME'],values['THREAD'])

    	#return false if download start was unsuccessful
    	download = dlAsync(job)

    #print(event)
    #print(values)

window.close()