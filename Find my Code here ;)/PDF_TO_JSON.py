import fitz  
import json

def pdf_to_text(pdf_path):
    # Open the PDF file
    document = fitz.open(pdf_path)
    text = ""

    # Extract text from each page
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()

    return text

def text_to_json(text):
    sections = {}
    current_section = None

    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        if line.lower() in ['summary', 'experience', 'education', 'skills', 'projects', 
                            'campus engagement', 'course completion', 'awards and achievements']:
            current_section = line.lower()
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)
        else:
            sections['other'] = sections.get('other', []) + [line]

    return sections

def save_to_json(data, json_path):
    with open(json_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def main(pdf_path, json_path):
    text = pdf_to_text(pdf_path)
    resume_json = text_to_json(text)
    save_to_json(resume_json, json_path)
    print(f"JSON data has been saved to {json_path}")

if __name__ == "__main__":
    pdf_path = 'MY_Resume_Overall.pdf'  # Our PDF file
    json_path = 'resume.json'  # Our JSON file
    main(pdf_path, json_path)
