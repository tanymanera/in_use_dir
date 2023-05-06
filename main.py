import PySimpleGUI as sg
import tools

def create_layout(elements_list):
    # Define the padding to use for the buttons
    button_padding = (0, 0)

    # Define the font to use for the text
    text_font = 'Helvetica 18'

    # Define the layout of the GUI
    layout = [[sg.Button(element[0], pad=button_padding, font=text_font, size=(15,1))] 
              for element in elements_list if element[2]=='y']
    
    # bottome per aprire file .csv
    layout.append([sg.Button("CSV", pad=button_padding, font=text_font, size=(15,1), button_color='green')])

    return layout

def create_gui(elements_list):

    # Set the PySimpleGUI theme to "Dark Blue 3"
    sg.theme('Reddit')

    layout = create_layout(elements_list)

    # Create the PySimpleGUI window
    window = sg.Window('My Dirs', layout, location=(5,5))

    # Event loop to process GUI events
    while True:
        event, values = window.read()
        # print(event, values)
        for element in elements_list:
            if event == element[0]:
                tools.open_explorer(element[1])
        if event == 'CSV':
            tools.open_csv()
            elements_list = tools.read_dir('dirs.csv')
            layout = create_layout(elements_list)
            window.close()
            window = sg.Window('My Dirs', layout, location=(5,5))
            window.refresh()

        if event == sg.WIN_CLOSED:
            break

    # Close the window when the event loop exits
    window.close()

# Example usage:
my_list = tools.read_dir('dirs.csv')
create_gui(my_list)
