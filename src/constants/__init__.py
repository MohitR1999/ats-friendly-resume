from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_RIGHT, TA_JUSTIFY

PAGE_WIDTH, PAGE_HEIGHT = A4
FULL_COLUMN_WIDTH = (PAGE_WIDTH - 1 * inch)
GARAMOND_REGULAR_FONT_PATH = '../res/fonts/EBGaramond-Regular.ttf'
GARAMOND_REGULAR = 'Garamond_Regular'

GARAMOND_BOLD_FONT_PATH = '../res/fonts/EBGaramond-Bold.ttf'
GARAMOND_BOLD = 'Garamond_Bold'

GARAMOND_SEMIBOLD_FONT_PATH = '../res/fonts/EBGaramond-SemiBold.ttf'
GARAMOND_SEMIBOLD = 'Garamond_Semibold'

pdfmetrics.registerFont(ttfonts.TTFont(GARAMOND_REGULAR, GARAMOND_REGULAR_FONT_PATH))
pdfmetrics.registerFont(ttfonts.TTFont(GARAMOND_BOLD, GARAMOND_BOLD_FONT_PATH))
pdfmetrics.registerFont(ttfonts.TTFont(GARAMOND_SEMIBOLD, GARAMOND_SEMIBOLD_FONT_PATH))