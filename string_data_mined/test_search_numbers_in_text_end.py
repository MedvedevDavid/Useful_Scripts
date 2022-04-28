import unittest

import search_number_in_text_contant as converter
import search_string_in_text_contant as text_converter

class TestReportGenerationNumberSum(unittest.TestCase):

    def initialize_test_object(self, input_string):
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = 0x")
        converter_obj.set_number_system("0x")
        converter_obj.generate_sum_and_array()
        return converter_obj


    def test_element_construction(self):
        input_string = "string"
        converter_obj = self.initialize_test_object(input_string)
        self.assertEqual(converter_obj.get_element_sum(), 0)


    def test_element_count_1(self):
        input_string = "Line = 0x01".split("\n")
        converter_obj = self.initialize_test_object(input_string)
        self.assertEqual(converter_obj.get_element_sum(), 1)
    

    def test_element_count_2(self):
        input_string = "Line = 0x02".split("\n")
        converter_obj = self.initialize_test_object(input_string)
        self.assertEqual(converter_obj.get_element_sum(), 2)


    def test_element_count_12(self):
        input_string = "Line = 0x12".split("\n")
        converter_obj = self.initialize_test_object(input_string)
        self.assertEqual(converter_obj.get_element_sum(), 18)



    def test_element_count_A2(self):
        input_string = "Line = 0xA2".split("\n")
        converter_obj = self.initialize_test_object(input_string)
        self.assertEqual(converter_obj.get_element_sum(), 162)


    def test_element_count_MultipleLines(self):
        input_string = "Line = 0xA2 \nLine = 0x01".split("\n")
        converter_obj = self.initialize_test_object(input_string)
        self.assertEqual(converter_obj.get_element_sum(), 163)


    def test_element_count_MultipleLines_coma(self):
        input_string = "Line = 0xA2, \nLine = 0x01".split("\n")
        converter_obj = self.initialize_test_object(input_string)
        self.assertEqual(converter_obj.get_element_sum(), 163)


    def test_non_hexadecimal(self):
        input_string =  "Line = 2 \nLine = 1".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = ")
        #converter_obj.set_number_system("") #default number system is decimal
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_sum(), 3)
        self.assertEqual(converter_obj.get_element_list(), [2,1])

    def test_element_array_MultipleLines_coma(self):
        input_string = "Line = 0xA2, \nLine = 0x01".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = 0x")
        converter_obj.set_number_system("0x")
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_list(), [162,1])


    def test_hexadecimal_without_in_text(self):
        input_string =  "Line = 0x2 \nLine = 0x1".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = ")
        converter_obj.set_number_system("0x") 
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_sum(), 3)


    def test_element_count_MultipleLines_coma_and_hex_numbers(self):
        input_string =  "Line = 0x2, 0x1 \nLine = 0x4,0x3".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = ")
        converter_obj.set_number_system("0x")
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_sum(), 10)


    def test_element_count_MultipleLines_coma_and_numbers(self):
        input_string =  "Line = 2,1 \nLine = 4, 3".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = ")
        converter_obj.set_number_system("")
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_sum(), 10)


    def test_element_count_MultipleLines_coma_and_hex_numbers_multiple(self):
        input_string =  "Line = 0x2, 0x1 ,0x1 \nLine = 0x4,0x3".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = ")
        converter_obj.set_number_system("0x")
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_sum(), 11)

    def test_element_count_MultipleLines_coma_and_hex_numbers_multiple_capital_X(self):
        input_string =  "Line = 0x2, 0X1 ,0x1 \nLine = 0x4,0X3".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = ")
        converter_obj.set_number_system("0x")
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_sum(), 11)

    def test_element_count_MultipleLines_coma_and_numbers_multiple(self):
        input_string =  "Line = 2,1,1 ,1,1,1,1\nLine = 4, 3".split("\n")
        converter_obj = converter.TextNumberSearcher(input_string)
        converter_obj.set_text_to_be_find("Line = ")
        converter_obj.set_number_system("")
        converter_obj.generate_sum_and_array()
        self.assertEqual(converter_obj.get_element_sum(), 15)


class TestReportGenerationString(unittest.TestCase):

    def test_string_at_the_end(self):
        input_string =  "Line = apple\n".split("\n")
        converter_obj = text_converter.TextStringSearcher(input_string)
        converter_obj.set_text_after_to_be_find("Line = ")
        converter_obj.generate_array()
        self.assertEqual(converter_obj.get_string(), ["apple"])

    def test_string_at_the_end_invalid(self):
        input_string =  "Line = apple\n".split("\n")
        converter_obj = text_converter.TextStringSearcher(input_string)
        converter_obj.set_text_after_to_be_find("Line : ")
        converter_obj.generate_array()
        self.assertEqual(converter_obj.get_string(), [])

    def test_string_at_the_end_2_lines(self):
        input_string =  "Line = apple \nLine = banana ".split("\n")
        converter_obj = text_converter.TextStringSearcher(input_string)
        converter_obj.set_text_after_to_be_find("Line = ")
        converter_obj.generate_array()
        self.assertEqual(converter_obj.get_string(), ["apple", "banana"])

    def test_string_at_the_between(self):
        input_string =  "Line = apple,averithing \nLine = banana, ".split("\n")
        converter_obj = text_converter.TextStringSearcher(input_string)
        converter_obj.set_text_after_to_be_find("Line = ")
        converter_obj.set_text_before_to_be_find(",")
        converter_obj.generate_array()
        self.assertEqual(converter_obj.get_string(), ["apple", "banana"])

    def test_string_at_the_between_total_match(self):
        input_string =  "Line = apple,averithing \nLine = banana ".split("\n")
        converter_obj = text_converter.TextStringSearcher(input_string)
        converter_obj.set_text_after_to_be_find("Line = ")
        converter_obj.set_text_before_to_be_find(",")
        converter_obj.generate_array(True)
        self.assertEqual(converter_obj.get_string(), ["apple"])

if __name__ =='__main__':
    unittest.main()