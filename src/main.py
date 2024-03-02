import PySimpleGUI as sg
from filemanager import FileManager
import mbox
import subprocess
import time

VERSION = 'v1.0.0'
GUI_TITLE = 'P4 Search'
GUI_ICON = 'searching.ico'

file_manager = FileManager()

def set_theme(name):
    """ Sets the theme of the GUI.

    Parameters
    ----------
    name: str
        The GUI theme name.
    """
    sg.theme(name)

def define_layout():
    """ Defines the layout of the GUI.

    Returns
    -------
    list
        The GUI layout.
    """    
    layout = [
        [sg.Text('Path')],
        [
            sg.InputText(key='-PATH-', tooltip='Folder path to search'),
            sg.FolderBrowse(initial_folder=file_manager.get_current_directory())
        ],
        [sg.Text('Pattern')],
        [
            sg.InputText(key='-PATTERN-', tooltip='Search pattern to match (literal text or regex)'),
            sg.Button('Search', bind_return_key=True)
        ],
        [sg.Checkbox('Case Sensitive', key='-CASE-', tooltip='Case sensitivity of search pattern')],
        [sg.Text('Output')],
        [sg.Multiline(size=(120, 20), key='-OUTPUT-', horizontal_scroll=True, disabled=True)],
        [sg.Text('Status: Idle', key='-STATUS-', tooltip='Progress of the file search'), sg.Push(), sg.Text(VERSION)]
    ]
    return layout

def create_window(layout):
    """ Creates the GUI window based on the GUI layout.

    Parameters
    ----------
    layout: list
        The GUI layout.

    Returns
    -------
    PySimpleGUI.PySimpleGUI.Window
        The GUI window object.
    """
    return sg.Window(title=GUI_TITLE, layout=layout, icon=GUI_ICON)

def start_event(window):
    """ Starts the event loop for the GUI window object.

    Parameters
    ----------
    window: PySimpleGUI.PySimpleGUI.Window
        The GUI window object.
    """
    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == 'Search':
            path = values['-PATH-']
            pattern = values['-PATTERN-']
            case = values['-CASE-']
            if not path:
                show_error('Missing path')
            elif not file_manager.is_directory(path):
                show_error('Invalid path')
            elif not pattern:
                show_error('Missing pattern')
            else:
                update_GUI_element(window, '-OUTPUT-', refresh=True)
                file_manager.change_directory(path)
                args = ['-n', '-s', '-e', pattern, file_manager.get_base_name(path) + '\*\*.py']
                if not case:
                    args.insert(0, '-i')
                update_GUI_element(window, '-STATUS-', 'Status: In Progress', refresh=True)
                output = send_command(args)
                if output != 'CANCEL':
                    total, results = (len(output.splitlines()), output) if output else (0, '')
                    update_GUI_element(window, '-OUTPUT-', f'**{total} matches found**\n{results}')
                    update_GUI_element(window, '-STATUS-', 'Status: Complete', refresh=True)
                    time.sleep(1)
                update_GUI_element(window, '-STATUS-', 'Status: Idle')
    window.close()

def update_GUI_element(window, key, value='', refresh=False):
    """ Updates the GUI window element based on the provided key and value.

    Parameters
    ----------
    window: PySimpleGUI.PySimpleGUI.Window
        The GUI window object.

    key: str
        The key of the GUI window element.

    value: str
        The value of the GUI window element.

    refresh: bool
        Whether or not to force the GUI window to refresh.
    """
    window[key].update(value)
    if refresh:
        window.refresh()

def send_command(args):
    """ Sends a p4 grep command based on the provided arguments.

    Parameters
    ----------
    args: list
        The list of command arguments.
    """
    cmd = ['p4', 'grep'] + args
    result = subprocess.run(cmd, capture_output=True)
    try:
        error = result.stderr.decode()
        if error:
            btn_select = show_error(error, 'RETRYCANCEL')
            return send_command(args) if btn_select == 'RETRY' else btn_select
        else:
            return result.stdout.decode()
    except Exception as e:
        show_error(str(e))
        return 'CANCEL'

def show_error(text, button='OK'):
    """ Shows an error message box based on the provided text and button.

    Parameters
    ----------
    text: str
        The text shown on message box.
    """
    return mbox.show(title=GUI_TITLE, text=text, icon='ICONERROR', button=button)

def main():
    set_theme('Default1')
    gui_layout = define_layout()
    gui_window = create_window(gui_layout)
    start_event(gui_window)

if __name__ == '__main__':
    main()
