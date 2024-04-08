import functions
import PySimpleGUI as sg

layout = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window = sg.Window("MY TODO APP",layout=[[layout],[input_box, add_button]])
window.read()
window.close()

