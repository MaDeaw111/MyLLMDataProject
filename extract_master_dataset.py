import os
import re
import json

def parse_md_file(content, is_thai=False):
    # Normalize line endings
    content = content.replace('\r\n', '\n')
    
    # Extract Title
    title_match = re.search(r'^#\s+(.*)', content, re.MULTILINE)
    title = title_match.group(1).strip() if title_match else ""
    
    # Headers to locate sections
    purpose_header = "## วัตถุประสงค์หลัก (ทำไปเพื่ออะไร)" if is_thai else "## Core Purpose & Objectives (ทำไปเพื่ออะไร)"
    synthesis_header = "## เนื้อหาเจาะลึก" if is_thai else "## Deep-Dive Synthesis"
    app_header = "## การประยุกต์ใช้ในการฝึกซ้อมจริง" if is_thai else "## Practical Coaching Application"
    qa_header = "## ตัวอย่างคำถาม-คำตอบ" if is_thai else "## Sample QA Pair"
    related_header = "## หัวข้อที่เกี่ยวข้อง" if is_thai else "## Related Topics"
    
    # Helper to get content between headers
    def get_section(text, start_header, next_headers):
        idx = text.find(start_header)
        if idx == -1:
            return ""
        start_pos = idx + len(start_header)
        
        end_pos = len(text)
        for nh in next_headers:
            n_idx = text.find(nh, start_pos)
            if n_idx != -1 and n_idx < end_pos:
                end_pos = n_idx
                
        tag_idx = text.find("#llm-deep-backlog", start_pos)
        if tag_idx != -1 and tag_idx < end_pos:
            end_pos = tag_idx
            
        return text[start_pos:end_pos].strip()

    purpose = get_section(content, purpose_header, [synthesis_header, app_header, qa_header, related_header])
    synthesis = get_section(content, synthesis_header, [app_header, qa_header, related_header])
    app = get_section(content, app_header, [qa_header, related_header])
    qa_section = get_section(content, qa_header, [related_header])
    
    # Parse QA Section into Question and Answer
    question = ""
    answer = ""
    if qa_section:
        q_prefix = "**คำถาม:**" if is_thai else "**Question:**"
        a_prefix = "**คำตอบ:**" if is_thai else "**Response:**"
        
        q_idx = qa_section.find(q_prefix)
        a_idx = qa_section.find(a_prefix)
        
        if q_idx != -1 and a_idx != -1:
            question = qa_section[q_idx + len(q_prefix):a_idx].strip()
            answer = qa_section[a_idx + len(a_prefix):].strip()
            
    return {
        'title': title,
        'purpose': purpose,
        'synthesis': synthesis,
        'app': app,
        'question': question,
        'answer': answer
    }

def main():
    en_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
    th_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics_TH"
    output_dir = r"C:\Users\usEr\MyLLMDataProject\DatasetOutput"
    output_file = os.path.join(output_dir, "bilingual_badminton_master_dataset.jsonl")
    
    os.makedirs(output_dir, exist_ok=True)
    
    system_prompt = "You are a professional badminton coaching assistant. Provide accurate, structured, and technical information based on the BWF Coaching Framework and manuals."
    
    dataset_records = []
    
    # 1. PROCESS ENGLISH FILES
    print("Scanning English files...")
    en_files_count = 0
    for root, dirs, files in os.walk(en_dir):
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                en_files_count += 1
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    parsed = parse_md_file(content, is_thai=False)
                    
                    # Entry 1: Comprehensive curriculum node
                    doc_prompt = f"Provide a comprehensive coaching guide, objectives, deep-dive synthesis, and practical application for: {parsed['title']}"
                    doc_response = content.strip()
                    dataset_records.append({
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": doc_prompt},
                            {"role": "assistant", "content": doc_response}
                        ]
                    })
                    
                    # Entry 2: Specific QA Pair if extracted successfully
                    if parsed['question'] and parsed['answer']:
                        dataset_records.append({
                            "messages": [
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": parsed['question']},
                                {"role": "assistant", "content": parsed['answer']}
                            ]
                        })
                except Exception as e:
                    print(f"Error processing English file {filepath}: {e}")
                    
    print(f"Processed {en_files_count} English files.")
    
    # 2. PROCESS THAI FILES
    print("Scanning Thai files...")
    th_files_count = 0
    for root, dirs, files in os.walk(th_dir):
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                th_files_count += 1
                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        content = file.read()
                    
                    parsed = parse_md_file(content, is_thai=True)
                    
                    # Entry 1: Comprehensive curriculum node in Thai
                    doc_prompt = f"ขอคำแนะนำการโค้ชระดับวิชาชีพ บทวิเคราะห์เจาะลึก และการประยุกต์ใช้งานซ้อมในสนามจริงสำหรับหัวข้อ: {parsed['title']}"
                    doc_response = content.strip()
                    dataset_records.append({
                        "messages": [
                            {"role": "system", "content": system_prompt},
                            {"role": "user", "content": doc_prompt},
                            {"role": "assistant", "content": doc_response}
                        ]
                    })
                    
                    # Entry 2: Specific QA Pair in Thai if extracted successfully
                    if parsed['question'] and parsed['answer']:
                        dataset_records.append({
                            "messages": [
                                {"role": "system", "content": system_prompt},
                                {"role": "user", "content": parsed['question']},
                                {"role": "assistant", "content": parsed['answer']}
                            ]
                        })
                except Exception as e:
                    print(f"Error processing Thai file {filepath}: {e}")
                    
    print(f"Processed {th_files_count} Thai files.")
    
    # 3. WRITE MASTER JSONL DATASET
    print(f"Writing {len(dataset_records)} records to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as out:
        for record in dataset_records:
            out.write(json.dumps(record, ensure_ascii=False) + '\n')
            
    print("Master dataset extraction completed successfully!")

if __name__ == "__main__":
    main()
