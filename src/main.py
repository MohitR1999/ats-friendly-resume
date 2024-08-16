from elements.resume_education import Education
from elements.resume_experience import Experience
from elements.resume_project import Project
from elements.resume_skill import Skill

from sections.resume_section import Section

from constants.resume_constants import RESUME_ELEMENTS_ORDER
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle
from constants.resume_constants import NAME_PARAGRAPH_STYLE, CONTACT_PARAGRAPH_STYLE
from constants import FULL_COLUMN_WIDTH
import json
import os
import configparser


def get_education_element(element) -> Education:
    e = Education()
    e.set_institution(element['institution'])
    e.set_course(element['course'])
    e.set_location(element['location'])
    e.set_start_date(element['start_date'])
    e.set_end_date(element['end_date'])
    return e

def get_experience_element(element) -> Experience:
    e = Experience()
    e.set_company(element['company'])
    e.set_title(element['title'])
    e.set_location(element['location'])
    e.set_start_date(element['start_date'])
    e.set_end_date(element['end_date'])
    e.set_description(element['description'])
    return e

def get_project_element(element) -> Project:
    e = Project()
    e.set_title(element['title'])
    e.set_description(element['description'])
    e.set_link(element['link'])
    return e

def get_skills_element(element) -> Skill:
    e = Skill()
    e.set_title(element['title'])
    e.set_elements(element['elements'])
    return e

def generate_resume(output_file_path, author, elements, table_styles) -> None:
    resume_doc = SimpleDocTemplate(output_file_path, pagesize=A4, showBoundary=0, leftMargin = 0.5 * inch, rightMargin= 0.5 * inch, topMargin = 0.2 * inch, bottomMargin = 0.1 * inch, title = f"Resume of {author}", author = author)
    table = Table(elements, colWidths=[FULL_COLUMN_WIDTH * 0.7, FULL_COLUMN_WIDTH * 0.3], spaceBefore=0, spaceAfter=0)
    table.setStyle(TableStyle(table_styles))
    resume_elements = [table]
    resume_doc.build(resume_elements)

if __name__ == "__main__":
    # Initialize the config
    config = None
    debug = 'false'
    author = 'anonymous'
    email = 'abc@xyz.com'
    address = 'XXX'
    phone = '00-0000000000'
    
    if (os.path.isfile('./constants/config.ini')):
        config = configparser.ConfigParser()
        config.read('./constants/config.ini')
        # Check if debug option is present
        if (config.has_option('global', 'debug')):
            debug = config.get('global', 'debug')
        
        # Check if author is present
        if (config.has_option('global', 'author')):
            author = config.get('global', 'author')

        # Check if email address is present
        if (config.has_option('global', 'email')):
            email = config.get('global', 'email')

        # Check if address is present
        if (config.has_option('global', 'address')):
            address = config.get('global', 'address')

        # Check if author is present
        if (config.has_option('global', 'phone')):
            phone = config.get('global', 'phone')

    OUTPUT_PDF_PATH = f"./{author.lower().replace(' ', '_')}_resume.pdf"
    
    # Initialize all the data elements
    data = {}
    resume_data = {}
    table = []
    running_row_index = [0]
    file_path = './data/input.json'
    table_styles = []
    table_styles.append(('ALIGN', (0, 0), (0, -1), 'LEFT'))
    table_styles.append(('ALIGN', (1, 0), (1, -1), 'RIGHT'))
    table_styles.append(('LEFTPADDING', (0, 0), (-1, -1), 0))
    table_styles.append(('RIGHTPADDING', (0, 0), (-1, -1), 0))
    table_styles.append(('BOTTOMPADDING', (0, running_row_index[0]), (1, running_row_index[0]), 6))
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    education_elements = []
    experience_elements = []
    project_elements = []
    skill_elements = []
    for element in data['education']:
        education_elements.append(get_education_element(element))
        
    for element in data['experience']:
        experience_elements.append(get_experience_element(element))
        
    for element in data['projects']:
        project_elements.append(get_project_element(element))
        
    for element in data['skills']:
        skill_elements.append(get_skills_element(element))
    
    resume_data['education'] = Section('Education', education_elements)
    resume_data['experience'] = Section('Experience', experience_elements)
    resume_data['projects'] = Section('Projects', project_elements)
    resume_data['skills'] = Section('Skills', skill_elements)
    
    # Prepare a table
    # Append the name and contact
    table.append([
        Paragraph(author, NAME_PARAGRAPH_STYLE)
    ])
    running_row_index[0] += 1
    
    table.append([
        Paragraph(f"{email} | {phone} | {address}", CONTACT_PARAGRAPH_STYLE),
    ])
    table_styles.append(('BOTTOMPADDING', (0, running_row_index[0]), (1, running_row_index[0]), 1))
    running_row_index[0] += 1
    
    for element in RESUME_ELEMENTS_ORDER:
        if element in resume_data:
            section_table = resume_data[element].get_section_table(running_row_index, table_styles)
            for entry in section_table:
                table.append(entry)
    
    # Prepare table styles
    
    # Build the resume
    generate_resume(OUTPUT_PDF_PATH, author, table, table_styles)