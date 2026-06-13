import os
import re
import sys
import argparse

sys.stdout.reconfigure(encoding='utf-8')

# Category mapping folders
CATEGORIES = [
    '1_Technical_Skills',
    '2_Tactical_And_Match_Play',
    '3_Movement_And_Biomechanics',
    '4_Physical_And_Sport_Science',
    '5_Coaching_Methodology'
]

# Classification function
def classify(filename):
    name = filename.lower()
    
    # 5. Coaching Methodology
    if filename.startswith('Plan_') or 'plan' in name or 'coaching' in name or 'pedagogy' in name or 'learning' in name or 'feedback' in name or 'demonstration' in name or 'questioning' in name or 'philosophy' in name or 'ethics' in name or 'inclusivity' in name or 'talent' in name or 'management' in name or 'development' in name or 'framework' in name or 'psychology' in name or 'para_badminton' in name or 'disabled' in name or 'disabilit' in name or 'deaf' in name or 'v_g_r_i_p' in name or 'motor_learning' in name or 'method' in name or 'ability_vs_potential' in name or 'educational' in name or 'philosophies' in name or 'vak_learning' in name or 'visual_learning' in name or 'auditory_learning' in name or 'kinesthetic_learning' in name or 'chaining' in name or 'shaping' in name or 'whole_part' in name:
        return '5_Coaching_Methodology'
        
    # 4. Physical and Sport Science
    if 'endurance' in name or 'anaerobic' in name or 'aerobic' in name or 'strength' in name or 'speed' in name or 'agility' in name or 'flexibility' in name or 'injury' in name or 'rehabilitation' in name or 'sports_med' in name or 'fatigue' in name or 'physiology' in name or 'phv' in name or 'growth' in name or 'maturation' in name or 'nutrition' in name or 'hydration' in name or 'electrolyte' in name or 'burnout' in name or 'overtraining' in name or 'rice_protocol' in name or 'sprain' in name or 'tendinopathy' in name or 'rotator' in name or 'stability' in name or 'spine_mobility' in name or 'active_recovery' in name or 'preconditioning' in name or 'back_pain' in name or 'jumper_knee' in name or 'shoulder_pain' in name or 'physiotherapy' in name or 'caffeine' in name or 'heart_rate' in name or 'plyometric' in name or 'conditioning' in name or 'fitness' in name or 'periodization' in name:
        return '4_Physical_And_Sport_Science'

    # 3. Movement and Biomechanics
    if 'movement' in name or 'footwork' in name or 'lunge' in name or 'split_step' in name or 'biomechanics' in name or 'kinetic' in name or 'kinematic' in name or 'traveling' in name or 'chasse' in name or 'crossover' in name or 'recovery' in name or 'base_position' in name or 'landing' in name or 'pronation' in name or 'supination' in name or 'deceleration' in name:
        return '3_Movement_And_Biomechanics'
        
    # 2. Tactical and Match Play
    if 'tactical' in name or 'tactic' in name or 'match' in name or 'singles' in name or 'doubles' in name or 'strategy' in name or 'interval' in name or 'scouting' in name or 'analysis' in name or 'rule' in name or 'court_size' in name or 'service_height' in name or 'game' in name or 'anticipation' in name or 'tactics' in name:
        return '2_Tactical_And_Match_Play'
        
    # 1. Technical Skills
    if 'grip' in name or 'clear' in name or 'drop' in name or 'serve' in name or 'net' in name or 'kill' in name or 'lift' in name or 'drive' in name or 'block' in name or 'smash' in name or 'stroke' in name or 'feed' in name or 'wrist' in name or 'forearm' in name:
        return '1_Technical_Skills'
        
    return '5_Coaching_Methodology'

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

    # Deep-Dive Synthesis (Category-specific technical elaboration)
    if category == '1_Technical_Skills':
        p1 = f"A rigorous analysis of **{outline_points[0]}** reveals that precise finger placement and grip pressure are critical. Players must maintain a relaxed grip to allow for maximum wrist flexibility and rapid forearm rotation (pronation or supination). Rigid grip engagement limits the range of motion, reducing the potential racket head acceleration at contact."
        p2 = f"Furthermore, optimizing the contact point relative to the body, as outlined in **{outline_points[1]}**, ensures clean transfer of force. Contacting the shuttle too early or too late disrupts the kinetic chain. Players must align their body position to meet the shuttle slightly in front of the racket shoulder, maximizing reach and leverage."
        p3 = f"Lastly, the integration of **{outline_points[2]}** into feeding drills helps automate this technique. Transitioning from hand-fed multi-shuttle sequences to racket rallying allows players to refine their control under increasing pace. Coaches should focus on technical checkpoints rather than outcome metrics during early learning stages."
    elif category == '2_Tactical_And_Match_Play':
        p1 = f"Analyzing **{outline_points[0]}** highlights the importance of spatial awareness and court coverage. In singles or doubles match play, players must execute patterns that create empty spaces in the opponent's court. This requires consistent variation in shuttle speed and angle to force the opponent out of their recovery base."
        p2 = f"Under match stress, managing transitions, as detailed in **{outline_points[1]}**, dictates who controls the rally. Defensive block-to-counter transitions or offensive net-kill follow-ups must be executed automatically. Coaches should use representative match play constraints to build situational awareness in training."
        p3 = f"Additionally, coordinating tactics with **{outline_points[2]}** is key to sustaining performance. Analyzing opponent tendencies and adjusting server/receiver positioning during intervals can shift match momentum. Coaches should use video analysis tools to map tactical consistency during competitive cycles."
    elif category == '3_Movement_And_Biomechanics':
        p1 = f"Understanding the biomechanical parameters of **{outline_points[0]}** is essential for movement efficiency. The split-step mechanism must be timed perfectly with the opponent's strike, pre-tensioning the calf muscles to allow explosive lateral or forward acceleration. Incorrect split-step timing increases reaction time significantly."
        p2 = f"During court travel, managing decelerating forces, as seen in **{outline_points[1]}**, protects joints from high impact. The heel-to-toe lunge landing, with the knee aligned directly over the ankle, prevents patellar tendinopathy. Coaches must focus on correct foot alignment during rapid direction changes."
        p3 = f"Finally, the kinetic chain sequence of **{outline_points[2]}** dictates power output. Force generated from leg extension and hip rotation must transfer smoothly through the thoracic spine and shoulder girdle. Smooth energy transfer ensures high racket head speed without overloading the rotator cuff muscles."
    elif category == '4_Physical_And_Sport_Science':
        p1 = f"Physiological adaptation in badminton requires targeting **{outline_points[0]}**. High-intensity interval training (HIIT) activates the anaerobic lactic system, building tolerance to lactate accumulation. Concurrently, aerobic endurance training supports rapid recovery between rallies and matches."
        p2 = f"To prevent overtraining, managing the workload, as discussed in **{outline_points[1]}**, is critical. Tracking heart rate metrics and using subjective fatigue scales help coaches adjust training volume. Under PHV growth spurts, volume must be carefully scaled to protect growing bones and joints."
        p3 = f"Furthermore, combining rehabilitation protocols with **{outline_points[2]}** ensures safe return-to-play. Eccentric strengthening for ankle and shoulder joints stimulates tissue remodeling. Hydration loading and carbohydrate-caffeine protocols also play a vital role in preventing dehydration-induced fatigue."
    else: # 5_Coaching_Methodology
        p1 = f"Applying pedagogical principles to **{outline_points[0]}** accelerates motor skill acquisition. Coaches should align their instruction with the player's learning style (VAK). Visual learners benefit from clear demonstrations and whiteboard diagrams, while kinesthetic learners require immediate physical feedback."
        p2 = f"Designing progressive practices, as outlined in **{outline_points[1]}**, is fundamental to the coaching process. Session planning must detail duration, feed type, and safety measures. Coaches should use the shaping method—modifying rules or equipment—to gradually approximate the target technique."
        p3 = f"Lastly, establishing a coaching philosophy centered around **{outline_points[2]}** promotes inclusivity. Adjusting court sizes, service heights, and rackets allows players with physical or intellectual disabilities to participate fully. Safe group management and ethical boundaries build trust and encourage long-term participation."

    synthesis = f"{p1}\n\n{p2}\n\n{p3}"

    # Practical Coaching Application
    if category == '1_Technical_Skills':
        app = f"During a 90-minute technical session, the coach designs an on-court drill targeting this stroke. After a demonstration showing grip transitions, the coach groups players. Feeder A feeds 20 underarm shuttles to Player B's hitting zone. The coach observes Player B, focusing specifically on **{outline_points[0]}** (e.g. grip pressure). The coach provides immediate verbal cues (e.g. 'relax fingers') and uses target cones on court to measure consistency. If a player executes 15/20 successful shots, they progress to a racket-fed rally."
    elif category == '2_Tactical_And_Match_Play':
        app = f"The coach sets up a half-court singles game where Player A is constrained to play only drops and clears, while Player B can play any stroke but must target the backhand corner. This tactical scenario highlights **{outline_points[0]}**. The coach stands at the side, noting how players adjust their court coverage and base position. During the interval, the coach reviews tactical sheets to show players how their recovery positions affect the rally outcome."
    elif category == '3_Movement_And_Biomechanics':
        app = f"In a movement session, the coach sets up a shadow footwork circuit. Cones are placed at the four corners. Players perform a split-step at the center base and push off to a corner, focusing on **{outline_points[0]}** (e.g. heel-to-toe lunge landing). The coach uses a high-speed camera to record the movements, showing players their knee alignment and ankle angles during rest intervals to correct bad landing habits immediately."
    elif category == '4_Physical_And_Sport_Science':
        app = f"The coach runs a badminton-specific conditioning circuit consisting of 40-second high-intensity multi-shuttle movements followed by 20 seconds of rest. This drill targets **{outline_points[0]}** (e.g. anaerobic lactic tolerance). The coach monitors players' heart rates during the session. If a player's recovery heart rate does not drop below 130 bpm during rest, the coach scales down the feeding speed to ensure safety and prevent overtraining."
    else: # 5_Coaching_Methodology
        app = f"To teach a new tactical drill, the coach applies the whole-part-whole methodology. First, they let the players play a free match to see their natural response (whole). Next, they isolate the key movement transition, focusing on **{outline_points[0]}** using visual boards and shadow play (part). Finally, they integrate the movement back into a controlled match play scenario (whole). The coach delivers positive feedback using VAK cues to match individual player preferences."

    # Sample QA Pair
    question = f"How should a coach design a training progression and monitor key biomechanical/pedagogical checkpoints for **{title}**?"
    if category == '1_Technical_Skills':
        answer = f"To master **{title}**, coaches should structure their instruction around three technical phases:\n" \
                 f"1. **Grip and Wrist Mechanics**: Focus on **{outline_points[0]}**, ensuring players maintain a loose grip pressure for whip-like acceleration.\n" \
                 f"2. **Contact Point Alignment**: Align body positions to address **{outline_points[1]}**, ensuring contact is made in front of the body for maximum kinetic efficiency.\n" \
                 f"3. **Drill Progression**: Design feeds to build consistency, shifting from hand feed to racket rallying to integrate **{outline_points[2]}**."
    elif category == '2_Tactical_And_Match_Play':
        answer = f"To apply **{title}** tactically, coaches should design representative match scenarios:\n" \
                 f"1. **Court Positioning**: Guide players on **{outline_points[0]}** to maintain high court coverage and limit opponent angles.\n" \
                 f"2. **Transition Execution**: Focus on **{outline_points[1]}** to build automatic responses when switching between defense and offense under stress.\n" \
                 f"3. **Data-Driven Adjustments**: Incorporate **{outline_points[2]}** during matches and intervals, using scouting notes to adapt server/receiver strategy."
    elif category == '3_Movement_And_Biomechanics':
        answer = f"To optimize movement biomechanics for **{title}**, coaches should address the kinetic checkpoints:\n" \
                 f"1. **Acceleration & Timing**: Target **{outline_points[0]}** by optimizing split-step timing and initial footwork push-off force.\n" \
                 f"2. **Deceleration & Landing**: Align joints to handle **{outline_points[1]}**, ensuring knee-over-toe alignment to absorb landing forces.\n" \
                 f"3. **Kinetic Chain Efficiency**: Coordinate segments to address **{outline_points[2]}**, transferring force from lower limbs up to the racket head."
    elif category == '4_Physical_And_Sport_Science':
        answer = f"To build physiological capacity for **{title}**, coaches should apply sport science guidelines:\n" \
                 f"1. **Energy System Training**: Focus on **{outline_points[0]}** to develop the anaerobic lactic tolerance required for fast exchanges.\n" \
                 f"2. **Load Management**: Track player fatigue metrics and scale training volume according to **{outline_points[1]}**, especially during PHV growth spurts.\n" \
                 f"3. **Recovery & Injury Prevention**: Incorporate **{outline_points[2]}** (e.g. eccentric strengthening, hydration protocols) to maintain tissue health."
    else: # 5_Coaching_Methodology
        answer = f"To deliver effective coaching for **{title}**, coaches should apply pedagogical frameworks:\n" \
                 f"1. **Inclusive Communication**: Adapt instructions to player learning styles (VAK), focusing on **{outline_points[0]}** for clear cue delivery.\n" \
                 f"2. **Structured Lesson Design**: Write progressive practice schedules addressing **{outline_points[1]}**, maintaining clear risk assessments and safety limits.\n" \
                 f"3. **Inclusivity & Adaptation**: Incorporate **{outline_points[2]}** to modify rules, court sizes, or equipment for para-badminton classes."
                 
    qa_pair = f"**Question:** {question}\n\n**Response:** {answer}"
    
    return purpose, synthesis, app, qa_pair

# Process a single file
def process_file(filepath, dest_dir):
    filename = os.path.basename(filepath)
    category = classify(filename)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    lines = content.split('\n')
    
    # Extract Title
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
                # Match list items like "1. ...", "* **1. ...**", etc.
                match = re.match(r'^\s*[\d\*\.\-\+]+\s*(.*)', line)
                if match:
                    text = match.group(1).strip()
                    # Clean up markdown formatting
                    text = re.sub(r'\*\*|\[\[|\]\]', '', text)
                    if text and not text.startswith('---'):
                        outline_points.append(text)
                        
    # Fallback outline points if not found
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
    
    # Generate enriched sections
    purpose, synthesis, app, qa_pair = generate_sections(filename, title, description, outline_points, category)
    
    # Reconstruct Content
    # We strip out old headers and the backlog tag
    filtered_lines = []
    skip = False
    for line in lines:
        if line.startswith('Category:') or line.startswith('[[Level_') or line.startswith('Source Manual:') or line.startswith('[[Training_Plans]]'):
            continue
        if line.startswith('## Related Topics') or line.startswith('## Structural Outline') or line.startswith('## Focus Summary') or line.startswith('## Structured Drill Schedule') or line.startswith('## Target Metrics') or line.startswith('## Sports Science') or line.startswith('---'):
            skip = True
            continue
        if skip and line.startswith('#') and not line.startswith('##'):
            skip = False
        if skip:
            continue
        if line.strip() == '#llm-deep-backlog':
            continue
        filtered_lines.append(line)
        
    core_content = "\n".join(filtered_lines).strip()
    if core_content.startswith(f"# {title}"):
        core_content = core_content[len(f"# {title}"):].strip()
    
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
    
    # Related Topics (Retain old related topics if possible)
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
                
    if related:
        new_content += "## Related Topics\n\n"
        for r_topic in sorted(list(set(related))):
            new_content += f"* [[{r_topic}]]\n"
        new_content += "\n"
        
    new_content += "#llm-deep-backlog\n"
    
    # Write to destination
    dest_path = os.path.join(dest_dir, filename)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    # Delete original if different
    if os.path.abspath(filepath) != os.path.abspath(dest_path):
        os.remove(filepath)

def main():
    parser = argparse.ArgumentParser(description="Process and enrich GeneratedTopics files")
    parser.add_argument("--category", type=str, required=True, help="Category name to process")
    args = parser.parse_args()
    
    target_category = args.category
    if target_category not in CATEGORIES:
        print(f"Error: Invalid category '{target_category}'")
        sys.exit(1)
        
    topics_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
    dest_dir = os.path.join(topics_dir, target_category)
    os.makedirs(dest_dir, exist_ok=True)
    
    processed_count = 0
    # Walk all files recursively
    for root, dirs, files in os.walk(topics_dir):
        # Skip BWF category directories to avoid visiting already moved files
        if os.path.basename(root) in CATEGORIES:
            continue
            
        for f in files:
            if f.endswith('.md'):
                filepath = os.path.join(root, f)
                file_cat = classify(f)
                if file_cat == target_category:
                    process_file(filepath, dest_dir)
                    processed_count += 1
                    
    print(f"Category '{target_category}': Successfully processed and moved {processed_count} files.")

if __name__ == '__main__':
    main()
