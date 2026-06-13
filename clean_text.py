import re
import os

def clean_file(input_path, output_path):
    print(f"Cleaning {input_path} -> {output_path}...")
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    lines = content.split('\n')
    cleaned_lines = []
    
    # Common headers/footers to skip
    skip_patterns = [
        re.compile(r'^BADMINTON COACH EDUCATION\s*►.*$', re.IGNORECASE),
        re.compile(r'^BWF BADMINTON COACH EDUCATION.*$', re.IGNORECASE),
        re.compile(r'^COACHES’ MANUAL.*$', re.IGNORECASE),
        re.compile(r'^COACHES\' MANUAL.*$', re.IGNORECASE),
        re.compile(r'^BADMINTON WORLD FEDERATION.*$', re.IGNORECASE),
        re.compile(r'^Unit \d+.*Kuala Lumpur.*$', re.IGNORECASE),
        re.compile(r'^\s*\d+\s*$'), # Isolated page numbers
    ]

    for line in lines:
        stripped = line.strip()
        # Skip matched headers/footers
        if any(pat.match(stripped) for pat in skip_patterns):
            continue
        cleaned_lines.append(line)

    # Rejoin and process paragraph wrapping
    text = '\n'.join(cleaned_lines)
    
    # Fix separated letters in bullets/text (e.g., "• P ublish" -> "• Publish", "• O rganise" -> "• Organise")
    text = re.sub(r'•\s+([A-Za-z])\s+([a-z])', r'• \1\2', text)
    text = re.sub(r'-\s+([A-Za-z])\s+([a-z])', r'- \1\2', text)
    text = re.sub(r'\b([A-Z])\s+([a-z]{2,})', r'\1\2', text)
    
    # Process paragraph wrapping:
    # If a line does not end with punctuation and is followed by a line starting with lowercase, join them.
    lines = text.split('\n')
    processed_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Skip empty lines
        if not line.strip():
            processed_lines.append("")
            i += 1
            continue
            
        # Try to join with subsequent lines
        while i + 1 < len(lines):
            next_line = lines[i+1].strip()
            if not next_line:
                break
            ends_with_flow = line.rstrip()[-1] not in ('.', '!', '?', ':', ';') if line.rstrip() else False
            starts_with_flow = next_line[0].islower() if next_line else False
            
            if "page" in next_line.lower() or "module" in next_line.lower():
                break
                
            if ends_with_flow and starts_with_flow:
                line = line.rstrip() + " " + next_line
                i += 1
            else:
                break
        processed_lines.append(line)
        i += 1

    # Remove consecutive empty lines (limit to max 2)
    final_lines = []
    empty_count = 0
    for line in processed_lines:
        if not line.strip():
            empty_count += 1
            if empty_count <= 2:
                final_lines.append("")
        else:
            empty_count = 0
            final_lines.append(line)
            
    cleaned_content = '\n'.join(final_lines)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    print(f"Successfully cleaned {input_path} -> {output_path} ({len(cleaned_content)} chars)")

if __name__ == "__main__":
    pdf_dir = r"C:\Users\usEr\MyLLMDataProject\RawNotes"
    for file in os.listdir(pdf_dir):
        if file.endswith(".md") and not file.endswith("_clean.md"):
            input_path = os.path.join(pdf_dir, file)
            output_path = os.path.join(pdf_dir, os.path.splitext(file)[0] + "_clean.md")
            clean_file(input_path, output_path)
