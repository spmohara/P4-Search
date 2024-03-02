"""
A module to show message boxes in Windows-based Python applications.

Author: Sean O'Hara
"""

import ctypes

def show(title='My title', text='My text', button='OK', icon='ICONINFORMATION'):
    """ Shows a message box based on the provided parameters.

    Parameters
    ----------
    title: str
        The title shown on message box.

    text: str
        The text shown on message box.

    button: str
        The button(s) shown on message box.
            ``'OK'`` (default), ``'OKCANCEL'``, ``'ABORTRETRYIGNORE'``, ``'YESNOCANCEL'``,
            ``'YESNO'``, ``'RETRYCANCEL'``, ``'CANCELTRYCONTINUE'``, ``'OKHELP'``

    icon: str
        The icon shown on message box.
            ``'NOICON'``, ``'ICONSTOP'``, ``'ICONERROR'``, ``'ICONHAND'``, ``'ICONQUESTION'``,
            ``'ICONEXCLAMATION'``, ``'ICONWARNING'``, ``'ICONINFORMATION'`` (default), ``'ICONASTERISK'``

    Returns
    -------
    str
        The button the user clicked on message box.
            ``'OK'``, ``'CANCEL'``, ``'ABORT'``,  ``'RETRY'``,
            ``'IGNORE'``,  ``'YES'``, ``'NO'``, ``'TRYAGAIN'``, ``'CONTINUE'``
    """
    return_values = {
        1: 'OK',
        2: 'CANCEL',
        3: 'ABORT',
        4: 'RETRY',
        5: 'IGNORE',
        6: 'YES',
        7: 'NO',
        10: 'TRYAGAIN',
        11: 'CONTINUE'
    }

    btn_value, icon_value = _validate_param(title=title, text=text, button=button, icon=icon)
    style = btn_value + icon_value
    return return_values[ctypes.windll.user32.MessageBoxW(0, text, title, style)]

def _validate_param(**kwargs):
    button_values = {
        'OK': 0,
        'OKCANCEL': 1,
        'ABORTRETRYIGNORE': 2,
        'YESNOCANCEL': 3,
        'YESNO': 4,
        'RETRYCANCEL': 5,
        'CANCELTRYCONTINUE': 6,
        'OKHELP': 0x4000
    }

    icon_values = {
        'NOICON': 0x00,
        'ICONSTOP': 0x10,
        'ICONERROR': 0x10,
        'ICONHAND': 0x10,
        'ICONQUESTION': 0x20,
        'ICONEXCLAMATION': 0x30,
        'ICONWARNING': 0x30,
        'ICONINFORMATION': 0x40,
        'ICONASTERISK': 0x40
    }

    param_values = {'button': button_values, 'icon': icon_values}
    return_values = []
    for key, value in kwargs.items():
        if key in ('title', 'text') and isinstance(value, str):
            continue
        elif key in param_values and value in param_values[key]:
            return_values.append(param_values[key][value])
        else:
            raise ValueError('Invalid {} parameter specified'.format(key))
    return return_values

if __name__ == '__main__':
    show()
