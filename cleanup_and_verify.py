import os
import re
import sys
import shutil
from process_all import classify, process_file

sys.stdout.reconfigure(encoding='utf-8')

def main():
    topics_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
    categories = [
        '1_Technical_Skills',
        '2_Tactical_And_Match_Play',
        '3_Movement_And_Biomechanics',
        '4_Physical_And_Sport_Science',
        '5_Coaching_Methodology'
    ]
    
    # Create category directories if they don't exist
    for cat in categories:
        os.makedirs(os.path.join(topics_dir, cat), exist_ok=True)
        
    print("Scanning root of GeneratedTopics/ for loose Markdown files...")
    loose_files = [f for f in os.listdir(topics_dir) if f.endswith('.md') and os.path.isfile(os.path.join(topics_dir, f))]
    
    if not loose_files:
        print("No loose Markdown files found in the root of GeneratedTopics/.")
    else:
        print(f"Found {len(loose_files)} loose files. Moving and enriching...")
        for filename in loose_files:
            filepath = os.path.join(topics_dir, filename)
            category = classify(filename)
            dest_dir = os.path.join(topics_dir, category)
            print(f"Moving '{filename}' to '{category}'...")
            process_file(filepath, dest_dir)
            
    print("\nStarting verification of all files inside the category subfolders...")
    errors = []
    total_checked = 0
    
    for cat in categories:
        cat_path = os.path.join(topics_dir, cat)
        if not os.path.exists(cat_path):
            errors.append(f"Directory {cat} does not exist")
            continue
        for f in os.listdir(cat_path):
            if f.endswith('.md'):
                total_checked += 1
                filepath = os.path.join(cat_path, f)
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                # Check for metadata
                if not content.startswith(f"Category: [[{cat}]]"):
                    errors.append(f"{f} does not start with 'Category: [[{cat}]]'")
                    
                # Check for required sections
                if "## Core Purpose & Objectives" not in content:
                    errors.append(f"{f} is missing 'Core Purpose & Objectives'")
                if "## Deep-Dive Synthesis" not in content:
                    errors.append(f"{f} is missing 'Deep-Dive Synthesis'")
                if "## Practical Coaching Application" not in content:
                    errors.append(f"{f} is missing 'Practical Coaching Application'")
                if "## Sample QA Pair" not in content:
                    errors.append(f"{f} is missing 'Sample QA Pair'")
                if "#llm-deep-backlog" not in content:
                    errors.append(f"{f} is missing '#llm-deep-backlog'")
                    
    print(f"Checked {total_checked} files.")
    if errors:
        print(f"Verification failed! Found {len(errors)} errors:")
        for err in errors[:20]:
            print(f" - {err}")
    else:
        print("Verification successful! All files are in their correct category subfolders and fully enriched.")

if __name__ == '__main__':
    main()
