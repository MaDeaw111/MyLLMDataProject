import json
import os
import random

def merge_and_validate():
    dataset_dir = r"C:\Users\usEr\MyLLMDataProject\DatasetOutput"
    files = [
        "bwf_coach_education_coaches_manual_l1-2nd-edition-midres_dataset.jsonl",
        "BWF_Coach_Manual_Level_2_English_dataset.jsonl",
        "CE-Level-3_DIGITAL_dataset.jsonl"
    ]
    
    combined_items = []
    seen_prompts = set()
    duplicate_count = 0
    
    for filename in files:
        filepath = os.path.join(dataset_dir, filename)
        if not os.path.exists(filepath):
            print(f"Error: {filepath} does not exist.")
            continue
            
        print(f"Processing {filename}...")
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        file_item_count = 0
        for line_num, line in enumerate(lines, 1):
            line = line.strip()
            if not line:
                continue
                
            # Parse as JSON to validate syntax
            try:
                item = json.loads(line)
            except json.JSONDecodeError as e:
                print(f"Syntax Error in {filename} at line {line_num}: {e}")
                continue
                
            # Validate schema
            if "messages" not in item:
                print(f"Schema Error in {filename} at line {line_num}: 'messages' key missing.")
                continue
                
            messages = item["messages"]
            if not isinstance(messages, list) or len(messages) != 3:
                print(f"Schema Error in {filename} at line {line_num}: 'messages' must be a list of 3 items.")
                continue
                
            # Check role structure
            roles = [msg.get("role") for msg in messages]
            if roles != ["system", "user", "assistant"]:
                print(f"Schema Error in {filename} at line {line_num}: Roles must be ['system', 'user', 'assistant']. Got {roles}")
                continue
                
            # De-duplicate check on user prompt
            user_content = messages[1].get("content", "").strip()
            if user_content in seen_prompts:
                print(f"Warning: Duplicate user prompt found in {filename} at line {line_num}: {user_content[:60]}...")
                duplicate_count += 1
                continue
                
            seen_prompts.add(user_content)
            combined_items.append(item)
            file_item_count += 1
            
        print(f"Successfully loaded and validated {file_item_count} items from {filename}.")
        
    print(f"Total valid items: {len(combined_items)} (Skipped {duplicate_count} duplicate(s))")
    
    # Shuffle for better training distribution
    random.seed(42)
    random.shuffle(combined_items)
    
    # Save the output file
    output_path = os.path.join(dataset_dir, "train_dataset.jsonl")
    with open(output_path, 'w', encoding='utf-8') as f:
        for item in combined_items:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')
            
    print(f"Saved merged dataset of {len(combined_items)} items to {output_path}")

if __name__ == "__main__":
    merge_and_validate()
