# -*- coding: utf-8 -*-


class PseudoTypeMixin:
    """
    Mixin class to serve as a base for creation of Pseudo class types.
    
    Classes derived from this class can implement custom methods depending
    on the i18n_type. Those custom method names must match the values
    available for i18n_type (settings.I18N_METHODS.keys()) in lower case
    and with an underscore in front of it.
    """
    def __init__(self, i18n_type):
        self.method_name = '_%s' % i18n_type.lower()

        # Declare method naming it accordingly to the i18n_type
        if not hasattr(self, self.method_name):
            setattr(self, self.method_name, self._base_compile)

    def _base_compile(self, string):
        raise NotImplementedError("Must be implemented in the child class.")

    # Should not be overridden
    def compile(self, string):
        """Run the correct method depending on the i18n_type."""
        return getattr(self, self.method_name)(string)  # .replace('\\\\', '\\')

    def _skip_char_around(self, string, char='\n'):
        """
        Custom pseudo method for skipping a given char around a string.
        
        The default char to be skipped is the new line (\n) one.
        
        Example:
            '\nHello\n' would call ``_base_compile`` with 'Hello' only.
        """
        starts, ends = '', ''
        n = len(char)
        if string.startswith(char):
            starts = string[:n]
            string = string[n:]
        if string.endswith(char):
            ends = string[-n:]
            string = string[:-n]
        string = self._base_compile(string)
        if starts:
            string = starts + string
        if ends:
            string = string + ends
        return string
