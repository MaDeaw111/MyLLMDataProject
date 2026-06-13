import os
import re
import shutil

# BWF Categories
CATEGORIES = [
    '1_Technical_Skills',
    '2_Tactical_And_Match_Play',
    '3_Movement_And_Biomechanics',
    '4_Physical_And_Sport_Science',
    '5_Coaching_Methodology'
]

# Classification function based on BWF standards and keyword analysis
def classify(filename):
    name = filename.lower()
    
    # 3. Movement and Biomechanics
    if any(k in name for k in ['movement', 'footwork', 'lunge', 'split_step', 'biomechanics', 'kinetic', 'kinematic', 'traveling', 'chasse', 'crossover', 'recovery', 'base_position', 'landing', 'pronation', 'supination', 'deceleration']):
        return '3_Movement_And_Biomechanics'
        
    # 4. Physical and Sport Science
    if any(k in name for k in ['endurance', 'anaerobic', 'aerobic', 'strength', 'speed', 'agility', 'flexibility', 'injury', 'rehabilitation', 'sports_med', 'fatigue', 'physiology', 'phv', 'growth', 'maturation', 'nutrition', 'hydration', 'electrolyte', 'burnout', 'overtraining', 'rice_protocol', 'sprain', 'tendinopathy', 'rotator', 'stability', 'spine_mobility', 'active_recovery', 'preconditioning', 'back_pain', 'jumper_knee', 'shoulder_pain', 'physiotherapy', 'caffeine', 'heart_rate', 'plyometric', 'conditioning', 'fitness', 'periodization', 'vo2', 'lactate', 'hydrotherapy', 'recovery', 'testing', 'sleep', 'cardio']):
        return '4_Physical_And_Sport_Science'
        
    # 2. Tactical and Match Play
    if any(k in name for k in ['tactical', 'tactic', 'match', 'singles', 'doubles', 'strategy', 'interval', 'scouting', 'analysis', 'rule', 'court_size', 'service_height', 'game', 'anticipation', 'tactics']):
        return '2_Tactical_And_Match_Play'
        
    # 1. Technical Skills
    if any(k in name for k in ['grip', 'clear', 'drop', 'serve', 'net', 'kill', 'lift', 'drive', 'block', 'smash', 'stroke', 'feed', 'wrist', 'forearm']):
        return '1_Technical_Skills'
        
    # 5. Coaching Methodology (pedagogy / feedback / philosophy / etc. as fallback)
    return '5_Coaching_Methodology'

# Jaccard similarity helpers
def get_words(text):
    text = re.sub(r'\[\[.*?\]\]', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'Category:.*', '', text)
    return set(re.findall(r'\w+', text.lower()))

def jaccard_similarity(set1, set2):
    if not set1 or not set2:
        return 0.0
    return len(set1.intersection(set2)) / len(set1.union(set2))

# Helper to extract drills from Plan tables
def extract_plan_outline(lines):
    drills = []
    for line in lines:
        if line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 3 and parts[0] != 'Drill Name' and not parts[0].startswith(':---'):
                drill_name = parts[0]
                drill_name = re.sub(r'\*\*|\[\[|\]\]', '', drill_name)
                drill_name = re.sub(r'^\d+[\.\)\s]+', '', drill_name)
                if drill_name:
                    drills.append(drill_name.strip())
    return drills

# Rich section generator
def generate_sections(filename, title, description, outline_points, category):
    # Core Purpose
    if category == '1_Technical_Skills':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to build consistent, biomechanically sound technical habits. In badminton, precise grip pressure adjustment, forearm pronation/supination, and hitting at the optimal contact point are foundational. Mastering this allows players to generate maximum racket head speed with minimum effort, manipulate the shuttle flight path effectively, and execute consistent patterns under match pressure while reducing joint fatigue."
    elif category == '2_Tactical_And_Match_Play':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to develop tactical intelligence and match play strategies. Coaches must train players to understand court coverage, doubles rotations, and singles patterns to exploit opponent weaknesses. This ensures players can make rapid decisions, dictate the rally's tempo, and execute tactical plans under competitive pressure."
    elif category == '3_Movement_And_Biomechanics':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to optimize movement efficiency and stroke biomechanics. Establishing correct footwork (chasse, crossover), split-step timing, and kinetic chain coordination allows players to cover the court quickly and strike from a stable base. This minimizes energy expenditure, improves reaction speed, and prevents chronic mechanical stress on the lower limbs."
    elif category == '4_Physical_And_Sport_Science':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to build the physical capabilities and physiological resilience required for high-performance badminton. Developing energy systems (aerobic/anaerobic endurance), explosive strength, speed-agility, and flexibility is critical. Incorporating sports medicine, hydration, PHV load monitoring, and active recovery prevents overtraining and sports injuries."
    else: # 5_Coaching_Methodology
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to establish structured pedagogical methods and coaching frameworks. Applying learning styles (VAK), stages of motor learning, and instructional progressions (shaping, chaining) helps coaches design effective practices. This ensures safe group management, inclusive training pathways, and precise feedback delivery."

    # Deep-Dive Synthesis
    p1_desc = outline_points[0] if len(outline_points) > 0 else "foundational patterns"
    p2_desc = outline_points[1] if len(outline_points) > 1 else "technical execution"
    p3_desc = outline_points[2] if len(outline_points) > 2 else "integration progression"
    
    if category == '1_Technical_Skills':
        p1 = f"A rigorous analysis of **{p1_desc}** reveals that precise finger placement and grip pressure are critical. Players must maintain a relaxed grip to allow for maximum wrist flexibility and rapid forearm rotation (pronation or supination). Rigid grip engagement limits the range of motion, reducing the potential racket head acceleration at contact."
        p2 = f"Furthermore, optimizing the contact point relative to the body, as outlined in **{p2_desc}**, ensures clean transfer of force. Contacting the shuttle too early or too late disrupts the kinetic chain. Players must align their body position to meet the shuttle slightly in front of the racket shoulder, maximizing reach and leverage."
        p3 = f"Lastly, the integration of **{p3_desc}** into feeding drills helps automate this technique. Transitioning from hand-fed multi-shuttle sequences to racket rallying allows players to refine their control under increasing pace. Coaches should focus on technical checkpoints rather than outcome metrics during early learning stages."
    elif category == '2_Tactical_And_Match_Play':
        p1 = f"Analyzing **{p1_desc}** highlights the importance of spatial awareness and court coverage. In singles or doubles match play, players must execute patterns that create empty spaces in the opponent's court. This requires consistent variation in shuttle speed and angle to force the opponent out of their recovery base."
        p2 = f"Under match stress, managing transitions, as detailed in **{p2_desc}**, dictates who controls the rally. Defensive block-to-counter transitions or offensive net-kill follow-ups must be executed automatically. Coaches should use representative match play constraints to build situational awareness in training."
        p3 = f"Additionally, coordinating tactics with **{p3_desc}** is key to sustaining performance. Analyzing opponent tendencies and adjusting server/receiver positioning during intervals can shift match momentum. Coaches should use video analysis tools to map tactical consistency during competitive cycles."
    elif category == '3_Movement_And_Biomechanics':
        p1 = f"Understanding the biomechanical parameters of **{p1_desc}** is essential for movement efficiency. The split-step mechanism must be timed perfectly with the opponent's strike, pre-tensioning the calf muscles to allow explosive lateral or forward acceleration. Incorrect split-step timing increases reaction time significantly."
        p2 = f"During court travel, managing decelerating forces, as seen in **{p2_desc}**, protects joints from high impact. The heel-to-toe lunge landing, with the knee aligned directly over the ankle, prevents patellar tendinopathy. Coaches must focus on correct foot alignment during rapid direction changes."
        p3 = f"Finally, the kinetic chain sequence of **{p3_desc}** dictates power output. Force generated from leg extension and hip rotation must transfer smoothly through the thoracic spine and shoulder girdle. Smooth energy transfer ensures high racket head speed without overloading the rotator cuff muscles."
    elif category == '4_Physical_And_Sport_Science':
        p1 = f"Physiological adaptation in badminton requires targeting **{p1_desc}**. High-intensity interval training (HIIT) activates the anaerobic lactic system, building tolerance to lactate accumulation. Concurrently, aerobic endurance training supports rapid recovery between rallies and matches."
        p2 = f"To prevent overtraining, managing the workload, as discussed in **{p2_desc}**, is critical. Tracking heart rate metrics and using subjective fatigue scales help coaches adjust training volume. Under PHV growth spurts, volume must be carefully scaled to protect growing bones and joints."
        p3 = f"Furthermore, combining rehabilitation protocols with **{p3_desc}** ensures safe return-to-play. Eccentric strengthening for ankle and shoulder joints stimulates tissue remodeling. Hydration loading and carbohydrate-caffeine protocols also play a vital role in preventing dehydration-induced fatigue."
    else: # 5_Coaching_Methodology
        p1 = f"Applying pedagogical principles to **{p1_desc}** accelerates motor skill acquisition. Coaches should align their instruction with the player's learning style (VAK). Visual learners benefit from clear demonstrations and whiteboard diagrams, while kinesthetic learners require immediate physical feedback."
        p2 = f"Designing progressive practices, as outlined in **{p2_desc}**, is fundamental to the coaching process. Session planning must detail duration, feed type, and safety measures. Coaches should use the shaping method—modifying rules or equipment—to gradually approximate the target technique."
        p3 = f"Lastly, establishing a coaching philosophy centered around **{p3_desc}** promotes inclusivity. Adjusting court sizes, service heights, and rackets allows players with physical or intellectual disabilities to participate fully. Safe group management and ethical boundaries build trust and encourage long-term participation."

    synthesis = f"{p1}\n\n{p2}\n\n{p3}"

    # Practical Coaching Application
    if category == '1_Technical_Skills':
        app = f"During a 90-minute technical session, the coach designs an on-court drill targeting this stroke. After a demonstration showing grip transitions, the coach groups players. Feeder A feeds 20 underarm shuttles to Player B's hitting zone. The coach observes Player B, focusing specifically on **{p1_desc}** (e.g. grip pressure). The coach provides immediate verbal cues (e.g. 'relax fingers') and uses target cones on court to measure consistency. If a player executes 15/20 successful shots, they progress to a racket-fed rally."
    elif category == '2_Tactical_And_Match_Play':
        app = f"The coach sets up a half-court singles game where Player A is constrained to play only drops and clears, while Player B can play any stroke but must target the backhand corner. This tactical scenario highlights **{p1_desc}**. The coach stands at the side, noting how players adjust their court coverage and base position. During the interval, the coach reviews tactical sheets to show players how their recovery positions affect the rally outcome."
    elif category == '3_Movement_And_Biomechanics':
        app = f"In a movement session, the coach sets up a shadow footwork circuit. Cones are placed at the four corners. Players perform a split-step at the center base and push off to a corner, focusing on **{p1_desc}** (e.g. heel-to-toe lunge landing). The coach uses a high-speed camera to record the movements, showing players their knee alignment and ankle angles during rest intervals to correct bad landing habits immediately."
    elif category == '4_Physical_And_Sport_Science':
        app = f"The coach runs a badminton-specific conditioning circuit consisting of 40-second high-intensity multi-shuttle movements followed by 20 seconds of rest. This drill targets **{p1_desc}** (e.g. anaerobic lactic tolerance). The coach monitors players' heart rates during the session. If a player's recovery heart rate does not drop below 130 bpm during rest, the coach scales down the feeding speed to ensure safety and prevent overtraining."
    else: # 5_Coaching_Methodology
        app = f"To teach a new tactical drill, the coach applies the whole-part-whole methodology. First, they let the players play a free match to see their natural response (whole). Next, they isolate the key movement transition, focusing on **{p1_desc}** using visual boards and shadow play (part). Finally, they integrate the movement back into a controlled match play scenario (whole). The coach delivers positive feedback using VAK cues to match individual player preferences."

    # Sample QA Pair
    question = f"How should a coach design a training progression and monitor key biomechanical/pedagogical checkpoints for **{title}**?"
    if category == '1_Technical_Skills':
        answer = f"To master **{title}**, coaches should structure their instruction around three technical phases:\n" \
                 f"1. **Grip and Wrist Mechanics**: Focus on **{p1_desc}**, ensuring players maintain a loose grip pressure for whip-like acceleration.\n" \
                 f"2. **Contact Point Alignment**: Align body positions to address **{p2_desc}**, ensuring contact is made in front of the body for maximum kinetic efficiency.\n" \
                 f"3. **Drill Progression**: Design feeds to build consistency, shifting from hand feed to racket rallying to integrate **{p3_desc}**."
    elif category == '2_Tactical_And_Match_Play':
        answer = f"To apply **{title}** tactically, coaches should design representative match scenarios:\n" \
                 f"1. **Court Positioning**: Guide players on **{p1_desc}** to maintain high court coverage and limit opponent angles.\n" \
                 f"2. **Transition Execution**: Focus on **{p2_desc}** to build automatic responses when switching between defense and offense under stress.\n" \
                 f"3. **Data-Driven Adjustments**: Incorporate **{p3_desc}** during matches and intervals, using scouting notes to adapt server/receiver strategy."
    elif category == '3_Movement_And_Biomechanics':
        answer = f"To optimize movement biomechanics for **{title}**, coaches should address the kinetic checkpoints:\n" \
                 f"1. **Acceleration & Timing**: Target **{p1_desc}** by optimizing split-step timing and initial footwork push-off force.\n" \
                 f"2. **Deceleration & Landing**: Align joints to handle **{p2_desc}**, ensuring knee-over-toe alignment to absorb landing forces.\n" \
                 f"3. **Kinetic Chain Efficiency**: Coordinate segments to address **{p3_desc}**, transferring force from lower limbs up to the racket head."
    elif category == '4_Physical_And_Sport_Science':
        answer = f"To build physiological capacity for **{title}**, coaches should apply sport science guidelines:\n" \
                 f"1. **Energy System Training**: Focus on **{p1_desc}** to develop the anaerobic lactic tolerance required for fast exchanges.\n" \
                 f"2. **Load Management**: Track player fatigue metrics and scale training volume according to **{p2_desc}**, especially during PHV growth spurts.\n" \
                 f"3. **Recovery & Injury Prevention**: Incorporate **{p3_desc}** (e.g. eccentric strengthening, hydration protocols) to maintain tissue health."
    else: # 5_Coaching_Methodology
        answer = f"To deliver effective coaching for **{title}**, coaches should apply pedagogical frameworks:\n" \
                 f"1. **Inclusive Communication**: Adapt instructions to player learning styles (VAK), focusing on **{p1_desc}** for clear cue delivery.\n" \
                 f"2. **Structured Lesson Design**: Write progressive practice schedules addressing **{p2_desc}**, maintaining clear risk assessments and safety limits.\n" \
                 f"3. **Inclusivity & Adaptation**: Incorporate **{p3_desc}** to modify rules, court sizes, or equipment for para-badminton classes."
                 
    qa_pair = f"**Question:** {question}\n\n**Response:** {answer}"
    
    return purpose, synthesis, app, qa_pair

# Main program
def main():
    root_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
    
    # 1. SCAN AND IDENTIFY ALL FILES
    all_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip BWF directories if they exist
        if any(sc in dirpath for sc in CATEGORIES):
            continue
        for f in filenames:
            if f.endswith('.md'):
                all_files.append(os.path.join(dirpath, f))
                
    print(f"Scanned {len(all_files)} total files.")
    
    # 2. DEDUPLICATION
    # Target Group: Plan_L3_155 to Plan_L3_166
    plan_l3_cluster = []
    for fp in all_files:
        name = os.path.basename(fp)
        # Check if it falls in the Plan_L3_155 to Plan_L3_166 range
        match = re.match(r'^Plan_L3_(\d+)_', name)
        if match:
            idx = int(match.group(1))
            if 155 <= idx <= 166:
                plan_l3_cluster.append(fp)
                
    print(f"Target cluster size: {len(plan_l3_cluster)} files.")
    
    # Run similarity checks and delete duplicates
    deleted_files = set()
    surviving_files = []
    
    # Load word sets
    file_words = {}
    for fp in all_files:
        try:
            with open(fp, 'r', encoding='utf-8') as f:
                file_words[fp] = get_words(f.read())
        except Exception as e:
            print(f"Error reading {fp}: {e}")
            file_words[fp] = set()

    # Greedy deduplication within the Plan L3 cluster
    # Sort them by name first
    plan_l3_cluster = sorted(plan_l3_cluster)
    cluster_survivors = []
    for fp in plan_l3_cluster:
        is_duplicate = False
        for sfp in cluster_survivors:
            sim = jaccard_similarity(file_words[fp], file_words[sfp])
            if sim >= 0.8:
                is_duplicate = True
                print(f"Duplicate found: {os.path.basename(fp)} is {sim:.2%} similar to {os.path.basename(sfp)}. Marking for deletion.")
                deleted_files.add(fp)
                break
        if not is_duplicate:
            cluster_survivors.append(fp)
            
    print(f"Deduplication results: {len(cluster_survivors)} files kept, {len(plan_l3_cluster) - len(cluster_survivors)} deleted.")
    
    # Physically delete duplicates
    for fp in deleted_files:
        if os.path.exists(fp):
            os.remove(fp)
            
    # Gather surviving files list
    for fp in all_files:
        if fp not in deleted_files:
            surviving_files.append(fp)
            
    print(f"Surviving files to process: {len(surviving_files)}")
    
    # 3. ROUTING AND ENRICHMENT
    # Ensure category folders exist
    for cat in CATEGORIES:
        os.makedirs(os.path.join(root_dir, cat), exist_ok=True)
        
    routed_files = [] # List of tuples (new_path, old_name)
    
    for filepath in surviving_files:
        filename = os.path.basename(filepath)
        category = classify(filename)
        dest_dir = os.path.join(root_dir, category)
        dest_path = os.path.join(dest_dir, filename)
        
        # Read content
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        lines = content.split('\n')
        
        # Extract elements
        title = ""
        for line in lines:
            if line.startswith('# '):
                title = line[2:].strip()
                break
        if not title:
            title = filename.replace('Topic_', '').replace('Plan_', '').replace('.md', '').replace('_', ' ')
            
        # Extract Description
        description = ""
        desc_started = False
        desc_lines = []
        for line in lines:
            if line.startswith('# '):
                desc_started = True
                continue
            if desc_started:
                if line.startswith('##') or line.startswith('---'):
                    break
                if line.strip():
                    desc_lines.append(line.strip())
        description = " ".join(desc_lines)
        
        # Extract Outline Points
        outline_points = []
        if filename.startswith('Plan_'):
            outline_points = extract_plan_outline(lines)
        else:
            outline_started = False
            for line in lines:
                if line.startswith('## Structural Outline') or line.startswith('## 3-point Detailed Outline'):
                    outline_started = True
                    continue
                if outline_started:
                    if line.startswith('##') or line.startswith('---') or line.strip() == '#llm-deep-backlog':
                        if len(outline_points) >= 3:
                            break
                    # Match list items
                    match = re.match(r'^\s*[\d\*\.\-\+]+\s*(.*)', line)
                    if match:
                        text = match.group(1).strip()
                        text = re.sub(r'\*\*|\[\[|\]\]', '', text)
                        if text and not text.startswith('---'):
                            outline_points.append(text)
                            
        # Fallbacks
        while len(outline_points) < 3:
            if filename.startswith('Plan_'):
                outline_points.append("Cooperative feeding drill sequencing.")
                outline_points.append("Representative match play simulation.")
                outline_points.append("Workload monitoring and load adjustments.")
            else:
                outline_points.append("Foundational technical coordination and movement.")
                outline_points.append("Progressive training practices and feedback.")
                outline_points.append("Tactical pattern adaptation and player safety.")
                
        outline_points = outline_points[:3]
        
        # Generate enriched content
        purpose, synthesis, app, qa_pair = generate_sections(filename, title, description, outline_points, category)
        
        # Filter original content: remove Level links, category tags, backlog tags
        filtered_lines = []
        for line in lines:
            if line.startswith('Category:') or line.startswith('[[Level_') or line.startswith('Source Manual:') or line.startswith('[[Training_Plans]]'):
                continue
            if line.strip() == '#llm-deep-backlog':
                continue
            filtered_lines.append(line)
            
        core_content = "\n".join(filtered_lines).strip()
        if core_content.startswith(f"# {title}"):
            core_content = core_content[len(f"# {title}"):].strip()
            
        # Rebuild enriched note
        new_content = f"Category: [[{category}]]\n\n"
        new_content += f"# {title}\n\n"
        if description and description not in core_content:
            new_content += f"{description}\n\n"
        if core_content:
            new_content += f"{core_content}\n\n"
            
        new_content += f"## Core Purpose & Objectives (ทำไปเพื่ออะไร)\n\n{purpose}\n\n"
        new_content += f"## Deep-Dive Synthesis\n\n{synthesis}\n\n"
        new_content += f"## Practical Coaching Application\n\n{app}\n\n"
        new_content += f"## Sample QA Pair\n\n{qa_pair}\n\n"
        
        # Extract related topics
        related = []
        related_started = False
        for line in lines:
            if line.startswith('## Related Topics'):
                related_started = True
                continue
            if related_started:
                if line.startswith('#') or line.strip() == '#llm-deep-backlog':
                    break
                match = re.findall(r'\[\[(.*?)\]\]', line)
                if match:
                    related.extend(match)
                    
        # Add related topics section
        if related:
            new_content += "## Related Topics\n\n"
            for r_topic in sorted(list(set(related))):
                new_content += f"* [[{r_topic}]]\n"
            new_content += "\n"
            
        new_content += "#llm-deep-backlog\n"
        
        # Write to destination category folder
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        # Remove original file if it is in another folder
        if os.path.abspath(filepath) != os.path.abspath(dest_path):
            if os.path.exists(filepath):
                os.remove(filepath)
                
        routed_files.append((dest_path, filename))
        
    print(f"Completed routing and enrichment of {len(routed_files)} files.")
    
    # 4. INDEX AND FILENAME STANDARDIZATION
    print("Starting filename and index standardization...")
    for cat in CATEGORIES:
        cat_dir = os.path.join(root_dir, cat)
        files_in_cat = [f for f in os.listdir(cat_dir) if f.endswith('.md')]
        
        # Group numbered plans by Level prefix
        # Prefix keys: 'Plan_L1', 'Plan_L2', 'Plan_L3'
        prefix_groups = {
            'Plan_L1': [],
            'Plan_L2': [],
            'Plan_L3': []
        }
        
        for f in files_in_cat:
            match = re.match(r'^(Plan_L[123])_(\d+)_(.*\.md)$', f)
            if match:
                prefix = match.group(1)
                suffix = match.group(3)
                prefix_groups[prefix].append((f, suffix))
                
        # Re-index each group sequentially
        for prefix, items in prefix_groups.items():
            if not items:
                continue
            # Sort items alphabetically by the descriptive suffix
            items = sorted(items, key=lambda x: x[1])
            
            for idx, (old_name, suffix) in enumerate(items, 1):
                new_name = f"{prefix}_{idx:03d}_{suffix}"
                old_path = os.path.join(cat_dir, old_name)
                new_path = os.path.join(cat_dir, new_name)
                
                if old_path != new_path:
                    # Rename the file on disk
                    print(f"Renaming: {old_name} -> {new_name}")
                    if os.path.exists(new_path):
                        # Safely overwrite if needed
                        os.remove(new_path)
                    shutil.move(old_path, new_path)
                    
    # 5. CLEAN UP EMPTY ORIGINAL FOLDERS
    for orig_dir in ['Level_1', 'Level_2', 'Level_3', 'Training_Plans']:
        path = os.path.join(root_dir, orig_dir)
        if os.path.exists(path):
            try:
                shutil.rmtree(path)
                print(f"Deleted original empty subdirectory: {orig_dir}")
            except Exception as e:
                print(f"Could not delete subdirectory {orig_dir}: {e}")
                
    print("Deduplication, Routing, Enrichment, and Re-indexing completed successfully!")

if __name__ == '__main__':
    main()
