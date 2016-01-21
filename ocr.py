import pyocr
import pyocr.builders

#init OCR



tools = pyocr.get_available_tools()[:]

print(tools)
