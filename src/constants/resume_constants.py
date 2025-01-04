from constants import GARAMOND_REGULAR, GARAMOND_SEMIBOLD
from reportlab.lib.enums import TA_RIGHT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors

RESUME_ELEMENTS_ORDER = [
    'skills',
    'projects',
    'experience',
    'education',
    'achievements',
    'certifications'
]

JOB_DETAILS_PARAGRAPH_STYLE = ParagraphStyle('job_details_paragraph', leftIndent=12, fontName = GARAMOND_REGULAR, fontSize = 11, leading = 12.5, alignment = TA_JUSTIFY)
NAME_PARAGRAPH_STYLE = ParagraphStyle('name_paragraph', fontName = GARAMOND_SEMIBOLD, fontSize=16)
CONTACT_PARAGRAPH_STYLE = ParagraphStyle('contact_paragraph', fontName = GARAMOND_REGULAR, fontSize=12)
SECTION_PARAGRAPH_STYLE = ParagraphStyle('section_paragraph', fontName = GARAMOND_SEMIBOLD, fontSize=13, textTransform = 'uppercase')
COMPANY_HEADING_PARAGRAPH_STYLE = ParagraphStyle('company_heading_paragraph', fontName = GARAMOND_SEMIBOLD, fontSize=12)
COMPANY_TITLE_PARAGRAPH_STYLE = ParagraphStyle('company_title_paragraph', fontName = GARAMOND_REGULAR, fontSize=11)
COMPANY_DURATION_PARAGRAPH_STYLE = ParagraphStyle('company_duration_paragraph', fontName = GARAMOND_SEMIBOLD, fontSize=12, alignment = TA_RIGHT)
COMPANY_LOCATION_PARAGRAPH_STYLE = ParagraphStyle('company_location_paragraph', fontName = GARAMOND_REGULAR, fontSize=11, alignment = TA_RIGHT)

def appendSectionTableStyle(table_styles : list, running_row_index : list) -> None:
    table_styles.append(('TOPPADDING', (0, running_row_index[0]), (1, running_row_index[0]), 5))
    table_styles.append(('BOTTOMPADDING', (0, running_row_index[0]), (1, running_row_index[0]), 5))
    table_styles.append(('LINEBELOW', (0, running_row_index[0]), (-1, running_row_index[0]), 1, colors.black))