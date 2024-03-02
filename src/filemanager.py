import os


class FileManager:
    """ A class to facilitate path management and file operations for common file-related tasks.

    Methods can be split into the following groups:
    - Path Validation (e.g., is_file, is_directory)
    - Path Manipulation (e.g., path_join, get_file_extension)
    - File Operations (e.g., create_file, delete_file)
    - File Content Management (e.g., read_content, write_content)
    - Directory Operations (e.g., create_directory, delete_directory)

    Author
    ------
    Sean O'Hara

    Attributes
    ----------
    path: ``None`` (default) or str
        Optional attribute, defines the global path used for all methods.
            ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'`` or ``'C:\\Users\\johndoe\\Documents'``

    Methods
    -------
    Path Validation
        is_file(path)
            Checks if a path points to a file.

        is_directory(path)
            Checks if a path points to a directory.

        is_valid_path(path)
            Checks if path is a file, directory, parent directory, or includes file extension.

        path_exists(path)
            Checks if a path pointing to a file or directory exists.

    Path Manipulation
        path_join(components)
            Joins multiple path components into a single path.
        
        change_directory(path)
            Changes the current working directory.

        get_current_directory()
            Returns the current working directory path.

        get_parent_directory(path)
            Returns the parent directory of a path (if any).

        get_base_name(path)
            Returns the base name of a path (if any).

        get_file_extension(path)
            Returns the file extension of a path (if any).

    File Operations
        create_file(path):
            Creates a new file.

        rename_file(new_path, path):
            Renames an existing file.

        delete_file(path):
            Deletes an existing file.

    File Content Management
        read_content(path):
            Reads the file content.

        write_content(content, path):
            Writes the provided content to a file.

        append_content(content, path):
            Appends the provided content to a file.

        read_line(path):
            Reads single line of a file.

        read_all_lines(path):
            Reads all lines of a file.

        write_lines(lines, path):
            Writes the provided lines to a file.

        clear_file_content(path):
            Clears the file content.
    
    Directory Operations
        list_directory_contents(path):
            Lists the contents of a directory.

        create_directory(path):
            Creates a new directory.

        rename_directory(new_path, path):
            Renames an existing directory.

        delete_directory(path):
            Deletes an existing directory.
    """
    def __init__(self, path=None):
        if path is None:
            self._path = self.get_current_directory()
        else:
            self.path = path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        if isinstance(value, str) and self.is_valid_path(value):
            self._path = value
        else:
            raise ValueError('Invalid path attribute')

    # --- Path Validation Methods ---

    def is_file(self, path=None):
        """ Checks if a path points to a file.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``

        Returns
        -------
        bool
            ``True`` if file exists, otherwise ``False``.
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'validate file')
        return os.path.isfile(path)
    
    def is_directory(self, path=None):
        """ Checks if a path points to a directory.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the directory.
                ex: ``'C:\\Users\\johndoe\\Documents'``

        Returns
        -------
        bool
            ``True`` if directory exists, otherwise ``False``.
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'validate directory')
        return os.path.isdir(path)

    def is_valid_path(self, path=None):
        """ Checks if path is a file, directory, parent directory, or includes file extension.
        Returns
        -------
        bool
            ``True`` if path is valid, otherwise ``False``.
        """
        is_file = self.is_file(path)
        is_dir = self.is_directory(path)
        is_par = True if self.get_parent_directory(path) else False
        has_ext = True if self.get_file_extension(path) else False
        return is_file or is_dir or has_ext or is_par

    def path_exists(self, path=None):
        """ Checks if a path pointing to a file or directory exists.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file or directory.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'`` or ``'C:\\Users\\johndoe\\Documents'``

        Returns
        -------
        bool
            ``True`` if path exists, otherwise ``False``.
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'validate path')
        return os.path.exists(path)

    # --- Path Manipulation Methods ---

    def path_join(self, *components):
        """ Joins multiple path components into a single path.

        Parameters
        ----------
        *components: positional arguments
            Any number of path components as strings.
                ex: ``'C:\\Users\\johndoe\\Documents'``, ``'file.txt'``

        Returns
        -------
        str
            The joined single path.
        """
        for component in components:
            self._validate_params(component, str, 'join path')
        return os.path.join(*components)
    
    def change_directory(self, path=None):
        """ Changes the current working directory.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the directory.
                ex: ``'C:\\Users\\johndoe'``
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'change directory')
        os.chdir(path)

    def get_current_directory(self):
        """ Returns the current working directory path.

        Returns
        -------
        str
            The current working directory path.
        """
        return os.getcwd()

    def get_parent_directory(self, path=None):
        """ Returns the parent directory of a path (if any).

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the directory.
                ex: ``'C:\\Users\\johndoe\\Documents'``

        Returns
        -------
        str
            The parent directory path (if any).
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'get parent directory')
        return os.path.dirname(path)

    def get_base_name(self, path=None):
        """ Returns the base name of a path (if any).

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file/directory.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``

        Returns
        -------
        str
            The base name of a path (if any).
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'get base name')
        return os.path.basename(path)
    
    def get_file_extension(self, path=None):
        """ Returns the file extension of a path (if any).

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``

        Returns
        -------
        str
            The file extension of a path (if any).
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'get file extension')
        return os.path.splitext(path)[1]

    # --- File Operations Methods ---

    def create_file(self, path=None):
        """ Creates a new file.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'create file')
        self._op_handler(path, 'write')

    def rename_file(self, new_path, path=None):
        """ Renames an existing file.

        Parameters
        ----------
        new_path: str
            The path of the new file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file2.txt'``
        
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file1.txt'``
        """
        path = self._path if path is None else path
        self._validate_params((new_path, path), (str, str), 'rename file')
        self._op_handler(path, 'rename', new_path)

    def delete_file(self, path=None):
        """ Deletes an existing file.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'delete file')
        self._op_handler(path, 'remove')

    # --- File Content Management Methods ---

    def read_content(self, path=None):
        """ Reads the file content.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``

        Returns
        -------
        str
            The file content.
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'read content')
        return self._op_handler(path)

    def write_content(self, content, path=None):
        """ Writes the provided content to a file.

        Parameters
        ----------
        content: str
            The content to write.

        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``
        """
        path = self._path if path is None else path
        self._validate_params((content, path), (str, str), 'write content')
        self._op_handler(path, 'write', content)

    def append_content(self, content, path=None):
        """ Appends the provided content to a file.

        Parameters
        ----------
        content: str
            The content to append.
            
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``
        """
        path = self._path if path is None else path
        self._validate_params((content, path), (str, str), 'append content')
        self._op_handler(path, 'append', content)

    def read_line(self, path=None):
        """ Reads single line of a file.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``

        Returns
        -------
        str
            The line of the file.
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'read line')
        return self._op_handler(path, 'readline')

    def read_all_lines(self, path=None):
        """ Reads all lines of a file.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``

        Returns
        -------
        list
            The lines of the file.
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'read lines')
        return self._op_handler(path, 'readlines')

    def write_lines(self, lines, path=None):
        """ Writes the provided lines to a file.

        Parameters
        ----------
        lines: list
            The lines to write.
            
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``
        """
        path = self._path if path is None else path
        self._validate_params((lines, path), (list, str), 'write lines')
        self._op_handler(path, 'writelines', lines)

    def clear_file_content(self, path=None):
        """ Clears the file content.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the file.
                ex: ``'C:\\Users\\johndoe\\Documents\\file.txt'``
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'clear content')
        self._op_handler(path, 'write')

    # --- Directory Operations Methods ---

    def list_directory_contents(self, path=None):
        """ Lists the contents of a directory.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the directory.
                ex: ``'C:\\Users\\johndoe\\Documents'``
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'list directory')
        return self._op_handler(path, 'listdir')

    def create_directory(self, path=None):
        """ Creates a new directory.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the directory.
                ex: ``'C:\\Users\\johndoe\\Documents'``
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'create directory')
        self._op_handler(path, 'mkdir')

    def rename_directory(self, new_path, path=None):
        """ Renames an existing directory.

        Parameters
        ----------
        new_path: str
            The path of the new directory.
                ex: ``'C:\\Users\\johndoe\\Documents\\folder2'``
        
        path: ``None`` (default) or str
            Optional parameter, the path of the directory.
                ex: ``'C:\\Users\\johndoe\\Documents\\folder1'``
        """
        path = self._path if path is None else path
        self._validate_params((new_path, path), (str, str), 'rename directory')
        self._op_handler(path, 'rename', new_path)

    def delete_directory(self, path=None):
        """ Deletes an existing directory.

        Parameters
        ----------
        path: ``None`` (default) or str
            Optional parameter, the path of the directory.
                ex: ``'C:\\Users\\johndoe\\Documents'``
        """
        path = self._path if path is None else path
        self._validate_params(path, str, 'delete directory')
        self._op_handler(path, 'rmdir')

    def _validate_params(self, params, types, op):
        if not isinstance(params, (list, tuple, dict, set)):
            params = (params,)
        if not isinstance(types, (list, tuple, dict, set)):
            types = (types,)
        for param, type_ in zip(params, types):
            if not (param and isinstance(param, type_)):
                raise ValueError(f'Unable to {op}: invalid parameter')

    def _op_handler(self, path, op='read', data=''):
        try:
            if op == 'listdir':
                return os.listdir(path)
            elif op == 'mkdir':
                os.mkdir(path)
            elif op == 'rename':
                os.rename(path, data)
            elif op in ('remove', 'rmdir'):
                os.remove(path) if op == 'remove' else os.rmdir(path)
            else:
                mode = op[0]
                with open(path, mode) as f:
                    if op == 'read':
                        return f.read()
                    elif op in ('write', 'append'):
                        f.write(data)
                    elif op == 'readline':
                        return f.readline()
                    elif op == 'readlines':
                        return f.readlines()
                    elif op == 'writelines':
                        f.writelines(data)
        except FileNotFoundError:
            raise FileNotFoundError('No such file or directory') from None
        except FileExistsError:
            raise FileExistsError('File already exists') from None
        except PermissionError:
            raise PermissionError('Insufficient file permissions') from None
        except OSError:
            raise OSError('OS error during file operation') from None
        except UnicodeDecodeError:
            raise ValueError('Unable to read file content') from None
        except Exception as e:
            raise ValueError(e) from None
