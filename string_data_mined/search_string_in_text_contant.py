


class TextStringSearcher:
    def __init__(self, input_string):
        self.input_string = input_string
        self.minded_string = []
        self.serch_after = None
        self.serch_before = None


    def set_text_after_to_be_find(self, serch_after):
        self.serch_after = serch_after

    def set_text_before_to_be_find(self, serch_before):
        self.serch_before = serch_before

    def _calculate_string(self, line_input):
        return (line_input.split(self.serch_after, 1)[1]).replace(" ", "")

    def generate_array(self, total_match_needed = False):
        for line_input in self.input_string:
            if self.serch_after in line_input:
                return_string = self._calculate_string(line_input)
                if (self.serch_before != None) and (self.serch_before in return_string):
                    return_string = return_string.split(self.serch_before, 1)[0]
                    if total_match_needed:
                        self.minded_string.append(return_string)
                if not(total_match_needed):
                    self.minded_string.append(return_string)

    def get_string(self):
        return(self.minded_string)