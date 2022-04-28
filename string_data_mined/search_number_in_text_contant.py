'''The File is including the necesarry implementation to search
specific text or number after a defined text'''
class TextNumberSearcher:
    '''The class is to search numbers after specific texts'''
    def __init__(self, string_to_analyse):
        self._string_to_analise = string_to_analyse
        self._text_to_be_find = None
        self._number_system = ""
        self._separators = ","
        self._element_list = []
        self._count_of_element = 0

    def set_text_to_be_find(self, text_to_be_find):
        '''Set the specific test after which the number is looked for'''
        self._text_to_be_find = text_to_be_find

    def set_separators(self, separator):
        '''The function is intended to set separatos which are separating the numbers'''
        self._separators =separator

    def set_number_system(self, number_system):
        '''Set in which numbersystem the number is expected, the default is decimal'''
        self._number_system = number_system

    def get_element_list(self):
        '''Returns the list of element if calculated which is in the line
        which setisfing teh condition'''
        return self._element_list

    def get_element_sum(self):
        '''The element_count is returning with the sum of the mentioned numbers in the file'''
        return self._count_of_element

    def generate_sum_and_array(self):
        '''Generate the array and counts from the input string'''
        self._count_of_element = 0
        if self._number_system == "":
            for line_of_string in self._string_to_analise:
                if self._text_to_be_find in line_of_string:
                    self._count_decimals(line_of_string)
        else:
            for line_of_string in self._string_to_analise:
                line_of_string = self._changecapital_number_system_identifier(line_of_string)
                if self._text_to_be_find in line_of_string:
                    self._count_non_decimals(line_of_string)
                

    def _count_decimals(self, line_of_string):
        '''Count sum of decimals and create the array of decimals'''
        number_with_separators=line_of_string.split(self._text_to_be_find, 1)[1]
        number_array_with_comas = number_with_separators.split(self._separators, 1)
        counts = number_array_with_comas[0]
        try:
            self._count_of_element += int((self._number_system + counts),0)
            self._element_list.append(int((self._number_system + counts),0))
        except ValueError:   
            pass #print("Not a number") 
        if len(number_array_with_comas)>1:
            self._count_more_than_one_decimals(number_array_with_comas)

    def _count_more_than_one_decimals(self, number_array_with_comas):
        '''called if more than one decimal was separated by the separator
        Count sum of decimals and create the array of decimals'''
        elements_to_be_splitt = number_array_with_comas[1]
        if self._separators in elements_to_be_splitt:
            self._count_of_element += self._splitt_add_append(elements_to_be_splitt, self._separators)
        else:
            try:
                self._count_of_element += int(elements_to_be_splitt,0)
                self._element_list.append( int(elements_to_be_splitt,0))
            except ValueError:   
                pass #print("Not a number") 
    def _count_non_decimals(self, line_of_string):
        '''Count sum of none decimals and create the array of decimals'''
        line_of_string = line_of_string.replace(self._separators, "")
        counts=line_of_string.split(self._number_system, 1)[1]
        if self._number_system in counts:
            self._count_of_element += (self._splitt_add_append(counts, self._number_system))
        else:
            try:
                self._count_of_element += int((self._number_system + counts),0)
                self._element_list.append( int((self._number_system + counts),0))
            except ValueError:   
                pass #print("Not a number") 
    def _changecapital_number_system_identifier(self, line_of_string):
        line_of_string = line_of_string.replace("X", "x")
        return line_of_string

    def _splitt_add_append(self, input_text, splitt_base):
        '''Recursive function which is counting and
        separating until the end of the input string'''
        counts=input_text.split(splitt_base, 1)
        try:
            retval = int((self._number_system + counts[0]),0)
            self._element_list.append(int((self._number_system + counts[0]),0))
        except ValueError:   
            pass #print("Not a number") 
        if splitt_base in counts[1]:
            retval += (self._splitt_add_append(counts[1],splitt_base))
            self._element_list.append(self._splitt_add_append(counts[1], splitt_base))
        else:
            try:
                retval += int((self._number_system + counts[1]),0)
                self._element_list.append( int((self._number_system + counts[1]),0))
            except ValueError:   
                pass #print("Not a number") 
        return retval
