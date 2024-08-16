from constants.resume_constants import SECTION_PARAGRAPH_STYLE, appendSectionTableStyle
from reportlab.platypus import Paragraph

class Section:
    def __init__(self, heading : str, elements = []):
        self.heading = heading
        self.elements = elements
        
    def set_elements(self, elements : list) -> None:
        self.elements = elements
        
    def add_element(self, element) -> None:
        self.elements.append(element)
        
    def get_section_table(self, running_row_index : list, table_styles : list) -> list:
        section_table = []
        section_table.append(
            [ Paragraph(self.heading, SECTION_PARAGRAPH_STYLE) ]
        )
        appendSectionTableStyle(table_styles, running_row_index)
        running_row_index[0] += 1
        for element in self.elements:
            element_table = element.get_table_element(running_row_index, table_styles)
            for entry in element_table:
                section_table.append(entry)
        return section_table