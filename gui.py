import functions
import FreeSimpleGUI as sg
label = sg.Text("Type in to-do")
input_box = sg.InputText(tooltip="enter to-do")
add_button = sg.Button("Add")
Win = sg.Window('My-to-do App',layout=[[label,],[input_box,add_button]])
Win.read()
Win.close()