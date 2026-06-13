import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Helper to classify files
def classify(filename):
    name = filename.lower()
    
    # 5. Coaching Methodology
    if filename.startswith('Plan_') or 'plan' in name or 'coaching' in name or 'pedagogy' in name or 'learning' in name or 'feedback' in name or 'demonstration' in name or 'questioning' in name or 'philosophy' in name or 'ethics' in name or 'inclusivity' in name or 'talent' in name or 'management' in name or 'development' in name or 'framework' in name or 'psychology' in name or 'para_badminton' in name or 'disabled' in name or 'disabilit' in name or 'deaf' in name or 'v_g_r_i_p' in name or 'motor_learning' in name or 'method' in name or 'ability_vs_potential' in name or 'inclusivity' in name or 'educational' in name or 'philosophies' in name or 'vak_learning' in name or 'visual_learning' in name or 'auditory_learning' in name or 'kinesthetic_learning' in name:
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

def generate_sections(filename, title, description, outline_points, category):
    # Core Purpose
    if category == '1_Technical_Skills':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to establish consistent, high-quality execution of this technical skill. Developing precise control over finger placement, contact points, and forearm pronation/supination allows players to manipulate the shuttlecock's flight path with accuracy. In match conditions, technical mastery ensures shot consistency, reduces unforced errors, and enables players to execute complex tactical shots from any court position."
    elif category == '2_Tactical_And_Match_Play':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to build tactical awareness and court positioning to dominate match rallies. Understanding tactical patterns and match-play strategies allows players to systematically exploit opponent weaknesses, control the tempo of the game, and maintain optimal defensive or offensive positions under physiological stress. Strategic mastery is key to turning technical skill into competitive success."
    elif category == '3_Movement_And_Biomechanics':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to optimize movement efficiency and stroke biomechanics on the court. Establishing correct footwork patterns, split-step timing, and kinetic chain coordination ensures that players arrive at the shuttle early and strike from a stable base. This minimizes reaction times, conserves energy over long matches, and reduces joint strain by distributing impact forces throughout the body."
    elif category == '4_Physical_And_Sport_Science':
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to build the physical capacity and physiological resilience required for elite badminton play. Strengthening core muscle groups, optimizing energy systems (aerobic and anaerobic), and implementing structured active recovery, nutrition, and injury prevention protocols are critical. This ensures players can sustain high-intensity performance, prevent overtraining, and accelerate rehabilitation from common injuries."
    else: # 5_Coaching_Methodology
        purpose = f"The core purpose of mastering **{title}** (ทำไปเพื่ออะไร) is to equip coaches with systematic, evidence-based pedagogical frameworks and planning tools. Implementing structured lesson plans, progressive practice design, risk assessments, and diverse feedback styles (VAK) allows coaches to deliver safe, inclusive, and effective training. This optimizes player learning stages and guides them along the long-term player development pathway."

    # Deep-Dive Synthesis
    p1 = f"In-depth analysis of the first core area, **{outline_points[0]}**, shows that systematic technical progression is vital for long-term player adaptation. Under BWF coaching standards, candidates must ensure that players build a firm foundation in this area. Mechanically, this requires coordinating body segments in sequence, starting from the lower body to generate torque that travels up through the core and shoulder, and is finally released at shuttle contact. By focusing on specific grip pressure and racket face angles, players learn to self-correct during practice, transforming conscious coordination into automatic motor patterns."
    
    p2 = f"Furthermore, addressing the second key checkpoint, **{outline_points[1]}**, is critical to maintaining high performance under competitive stress. When players encounter unpredictable situations or fatigue, their movement recovery and timing are the first elements to degrade. Coaching intervention should focus on introducing progressive drills—such as transitioning from static shadow movements to cooperative hand feeding and finally to fast, open racket feeding. This progression forces players to adapt their body mechanics and maintain technical consistency when under time constraints and physiological fatigue."
    
    p3 = f"Finally, the integration of **{outline_points[2]}** completes the developmental module by connecting physical capabilities with tactical execution. Modern badminton requires players to perform rapid changes of direction and execute explosive strokes repeatedly. By integrating sport science principles—such as modeling workload constraints during growth spurts (PHV) and tracking recovery metrics—coaches can design safe sessions that push player boundaries without risking overtraining or injury. This ensures that the technical and physical foundation directly supports the player's tactical role on court."
    
    synthesis = f"{p1}\n\n{p2}\n\n{p3}"

    # Practical Coaching Application
    app = f"During a 90-minute training session, the coach designs an on-court scenario specifically targeting this concept. The coach starts with a structured 15-minute explanation and demonstration, highlighting key checkpoints. Players then break into pairs: Player A executes the target movement or stroke, while Player B feeds shuttles using a combination of hand feeding and racket feeding. The coach circulates, focusing on **{outline_points[0]}**. When the coach notices a player struggling with recovery or alignment, they halt the drill to provide immediate, specific feedback, using visual markers on the court to guide correct positioning. The session concludes with a competitive half-court game where players earn double points for successfully applying this concept."

    # Sample QA Pair
    question = f"How should a coach structure and apply the checkpoints of **{title}** to enhance player performance and safety?"
    answer = f"To effectively apply **{title}**, a coach must follow a structured, multi-dimensional progression based on BWF standards:\n" \
             f"1. **Biomechanical Foundation**: First, ensure the player understands and executes the primary mechanical checkpoints, specifically **{outline_points[0]}**. This involves adjusting grip pressure and body alignment during the preparation phase.\n" \
             f"2. **Progressive Drill Design**: Transition from closed drills to open, representative match play, focusing on **{outline_points[1]}**. Use cooperative feeding initially to build confidence before increasing speed and unpredictability.\n" \
             f"3. **Physical & Tactical Integration**: Finally, incorporate **{outline_points[2]}** to ensure the skill is tactically useful and physically sustainable. Monitor workload variables to prevent injuries and optimize motor learning stages."
    
    qa_pair = f"**Question:** {question}\n\n**Response:** {answer}"
    
    return purpose, synthesis, app, qa_pair

def process_file(filepath):
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
    outline_started = False
    for line in lines:
        if line.startswith('## Structural Outline') or line.startswith('## Structured Drill Schedule') or line.startswith('## Focus Summary') or line.startswith('## 3-point Detailed Outline'):
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
                # Clean up markdown formatting like bolding or table formatting
                text = re.sub(r'\*\*|\[\[|\]\]', '', text)
                text = text.split('|')[1].strip() if '|' in text else text
                if text and not text.startswith('Drill Name') and not text.startswith(':---') and not text.startswith('---'):
                    outline_points.append(text)
                    
    # Fallback outline points if not found
    while len(outline_points) < 3:
        outline_points.append(f"Essential movement coordination and position recovery.")
        outline_points.append(f"Progressive practices and workload adjustment.")
        outline_points.append(f"Integration with tactical scenarios and safety guidelines.")
        
    outline_points = outline_points[:3]
    
    # Generate enriched sections
    purpose, synthesis, app, qa_pair = generate_sections(filename, title, description, outline_points, category)
    
    # Reconstruct Content
    # We need to retain existing links and hashtags, and add Category: [[Category]] at the top
    # We will filter out old headers like Related Topics and the backlog tag so we can clean-reconstruct
    filtered_lines = []
    skip = False
    for line in lines:
        if line.startswith('Category:') or line.startswith('[[Level_') or line.startswith('Source Manual:'):
            continue
        if line.startswith('## Related Topics') or line.startswith('## Structural Outline') or line.startswith('## Focus Summary') or line.startswith('## Structured Drill Schedule') or line.startswith('## Target Metrics') or line.startswith('## Sports Science') or line.startswith('---'):
            skip = True
            continue
        if skip and line.startswith('#') and not line.startswith('##'):
            skip = False
        if skip:
            # We want to stop skipping if we find headers we don't want to skip, but we want to skip all sections we are replacing
            # Actually, let's keep it simple: we skip everything except the title and description, and we will rebuild the rest!
            continue
        if line.strip() == '#llm-deep-backlog':
            continue
        filtered_lines.append(line)
        
    core_content = "\n".join(filtered_lines).strip()
    # Remove title if it's already there to avoid duplicates
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
    
    return new_content

# Test with samples
sample_topic = r"GeneratedTopics/Topic_Ability_vs_Potential.md"
sample_plan = r"GeneratedTopics/Training_Plans/Plan_L1_001_V_Grip_Visual_Learning.md"

print("--- TOPIC ENRICHMENT TEST ---")
print(process_file(sample_topic)[:1500])
print("\n--- PLAN ENRICHMENT TEST ---")
print(process_file(sample_plan)[:1500])
