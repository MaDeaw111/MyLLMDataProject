import os
import re

# 18 new research topics based on BWF_Research project
research_topics = [
    {
        "filename": "Topic_Consecutive_Matches_Fatigue",
        "title": "Consecutive Matches Physical Fatigue",
        "description": "Analysis of performance decay, cardiovascular strain, and physiological stress when junior players play multiple matches in a single day.",
        "source": "BWF_Research project/Badminton Performance_Coaching/1.-Fernandez-Report_final.pdf",
        "outline": [
            "Cardiovascular demand adjustments and VO2 max changes over back-to-back competitive matches.",
            "Neuromuscular fatigue markers and velocity loss in jumping and lunging actions.",
            "Hydration and active recovery protocols to mitigate consecutive-match performance decay."
        ]
    },
    {
        "filename": "Topic_Anticipation_Under_Physiological_Stress",
        "title": "Anticipation Under Physiological Stress",
        "description": "Investigating how high heart rate, cognitive anxiety, and physical fatigue degrade visual search behaviors and perceptual-cognitive anticipation.",
        "source": "BWF_Research project/Badminton Performance_Coaching/4.-Alder-Report_final.pdf",
        "outline": [
            "Physiological fatigue limits: Thresholds where visual gaze fixation accuracy degrades.",
            "Cognitive load during matches: How stress narrows the attentional focus window on court.",
            "Stress-exposure training protocols (high-intensity cardiorespiratory stress combined with visual drills)."
        ]
    },
    {
        "filename": "Topic_Perceptual_Anticipation_Training",
        "title": "Perceptual Anticipation Training",
        "description": "Methods like video simulation training, temporal occlusion, and one-way mirror perception training to isolate and improve reaction speed.",
        "source": "BWF_Research project/Badminton Performance_Coaching/JOURNAL-CUH_Kumar.pdf",
        "outline": [
            "One-Way Mirror Perceptual Training: Blocking opponent visual body cues to force acoustic/racket angle focus.",
            "Temporal Occlusion: Video simulation training with clips cut off at racket-shuttle contact to build prediction habits.",
            "Agility and FCRT (Four Corner Run Test) improvements following perceptual-cognitive conditioning."
        ]
    },
    {
        "filename": "Topic_Speed_Accuracy_Tradeoff_Smash",
        "title": "Speed-Accuracy Trade-off in Forehand Smash",
        "description": "Determining optimal shuttlecock speed thresholds for international players to maintain high landing accuracy.",
        "source": "BWF_Research project/Badminton Performance_Coaching/SPATIAL-SPEED-ACCURACY-TRADE-OFF-IN-INTERNATIONAL-BADMINTON.pdf",
        "outline": [
            "Determining the optimal speed threshold (80-99% of maximum velocity) for spatial landing accuracy.",
            "Identifying Fitts' Law and alternate cluster models (FIR, NR, AIR) in overhead smashes.",
            "Biomechanical swing adaptations when transitioning from maximum power (MS) to high accuracy (TAR)."
        ]
    },
    {
        "filename": "Topic_Jump_Smash_Kinetic_Consistency",
        "title": "Jump Smash Kinetic Consistency",
        "description": "Kinematics of elite jump smashes, investigating kinematic parameters that yield high-velocity consistency.",
        "source": "BWF_Research project/Badminton Performance_Coaching/Final_Abdurrahman-et-al._Loughborough-University.pdf",
        "outline": [
            "Body joint angles and shoulder-pelvis rotation sequences that yield consistent shuttlecock flight paths.",
            "Comparing inter-individual biomechanical consistency between standing and jump smashes.",
            "Coaching progression to maintain smash accuracy while scaling jump smash power."
        ]
    },
    {
        "filename": "Topic_Multi_Feeding_vs_Match_Play_Load",
        "title": "Multi-Feeding vs. Match Play Mechanical Load",
        "description": "Comparing the tibial and lower back mechanical load differences between highly predictable feeding drills and competitive matches.",
        "source": "BWF_Research project/Badminton Performance_Coaching/Winchester_Smith-et-al.pdf",
        "outline": [
            "IMU sensor analytics: High shank and lower back G-force impacts on lunges during match play.",
            "Heavier vs. Lighter landers: Individual biomechanical traits and impact distribution patterns.",
            "Predictability constraints: Why closed multi-feed drills fail to simulate the loading variations of open match play."
        ]
    },
    {
        "filename": "Topic_Plyometric_Training_Jump_Height",
        "title": "Plyometric Training for Jump Height",
        "description": "Periodized high-impact bilateral plyometric programs to increase vertical jump parameters and overhead smash power.",
        "source": "BWF_Research project/Badminton Performance_Coaching/Final_Frohlich-et-al._Saarland-University-Institute-for-Sport-Science.pdf",
        "outline": [
            "Structuring an 8-week plyometric training macrocycle for junior national-tier players.",
            "Biomechanical diagnostics: Squat Jump (SJ), Countermovement Jump (CMJ), and Drop Jump (DJ) force plate variables.",
            "Rate of Force Development (RFD) transfer to badminton-specific vertical jumps."
        ]
    },
    {
        "filename": "Topic_Leg_Length_Discrepancy_Back_Pain",
        "title": "Leg Length Discrepancy and Back Pain",
        "description": "Examining how Leg Length Discrepancy (LLD) causes asymmetric gait, hip instability, and low back pain during repetitive training.",
        "source": "BWF_Research project/Injury prevention/CUH-Kumar-P.pdf",
        "outline": [
            "Measuring structural vs. functional LLD in junior players.",
            "Pelvic tilt, hip asymmetry, and lumbar loading patterns caused by LLD on court.",
            "Rehabilitation orthotics, balance boards, and core strengthening to mitigate LLD-related discomfort."
        ]
    },
    {
        "filename": "Topic_Shoulder_Pain_and_Physical_Fitness",
        "title": "Shoulder Pain and Physical Fitness",
        "description": "Assessing the correlations between shoulder range of motion (ROM), trunk rotation, handgrip strength, and shoulder pain risk.",
        "source": "BWF_Research project/Injury prevention/Assessing-the-Association-of-Shoulder-Pain-Risk-with-Physical-Fitness.pdf",
        "outline": [
            "Evaluating shoulder range of motion (ROM) parameters (internal/external rotation) in elite players.",
            "Correlating shoulder pain risk with physical fitness metrics (handgrip strength, trunk range of motion, Y-balance).",
            "Functional movement screens (FMS) to identify anatomical compensation patterns in the upper kinetic chain."
        ]
    },
    {
        "filename": "Topic_Landing_Instability_Overhead_Backhand",
        "title": "Landing Instability in Overhead Backhand Movements",
        "description": "Kinematics and kinetics of landing on the non-preferred leg during overhead movements, and its relationship to back pain.",
        "source": "BWF_Research project/Injury prevention/FINAL-ITB_Adiprawita.pdf",
        "outline": [
            "Kinematic monitoring of left clavicle (LCL), right clavicle (RCL), pelvis (PEL), and thorax (TRX) instability during landing.",
            "Asymmetric landing impacts on the non-preferred leg during backhand/around-the-head overhead clearances.",
            "Strengthening the gluteus medius and core muscles to stabilize pelvic tilt upon one-legged landing."
        ]
    },
    {
        "filename": "Topic_Swiss_Ball_Core_Functional_Movement",
        "title": "Swiss Ball Core and Functional Movement Training",
        "description": "8-week Swiss ball training protocols to improve functional movement screen (FMS) scores and dynamic balance.",
        "source": "BWF_Research project/Badminton Performance_Coaching/Research-paper.pdf",
        "outline": [
            "Integrating Swiss ball balance progressions prior to active badminton group training.",
            "Tracking changes in dynamic balance using the Y-Balance Test protocol.",
            "Core stability drills designed to prevent lower back shear stress during overhead stroke twists."
        ]
    },
    {
        "filename": "Topic_Shuttlecock_Aerodynamic_Deceleration",
        "title": "Shuttlecock Aerodynamic Deceleration",
        "description": "Analyzing the ballistic coefficient, drag force, and quadratic air resistance relationships that govern shuttlecock flight.",
        "source": "BWF_Research project/Badminton Performance_Coaching/Final_Naylor-et-al._Loughborough-University.pdf",
        "outline": [
            "Determining the ballistic coefficient and quadratic relationship between velocity and aerodynamic drag force.",
            "Mathematical models to calculate instantaneous pre-impact and post-impact shuttle velocities.",
            "Tracking shuttlecock flip, spin rotation, and deceleration patterns under tournament environments."
        ]
    },
    {
        "filename": "Topic_Ischemic_Preconditioning_Recovery",
        "title": "Ischemic Preconditioning for Match Recovery",
        "description": "Utilizing Ischemic Pre-conditioning (IPC) during the recovery interval between consecutive matches to preserve physical power.",
        "source": "BWF_Research project/Badminton Performance_Coaching/JOURNAL-UoWA_Olivier.pdf",
        "outline": [
            "Physiology of IPC: Cyclical blood flow occlusion (cuff pressure at 220 mmHg) to induce local muscular adaptation.",
            "Measuring IPC effects on Squat Jump (SJ), Countermovement Jump (CMJ), and L-test agility sprint times.",
            "Applications of IPC in multi-match tournament formats to preserve metabolic function."
        ]
    },
    {
        "filename": "Topic_Carbohydrate_Caffeine_Supplementation",
        "title": "Carbohydrate and Caffeine Supplementation",
        "description": "Investigating how carbohydrate and caffeine ingestion preserves shot accuracy and cognitive attention under fatigue.",
        "source": "BWF_Research project/Badminton Performance_Coaching/Final_Clarke-et-al._Coventry-University.pdf",
        "outline": [
            "Nutritional protocols: Optimal dosage (mg/kg body weight) of caffeine and carbohydrate concentration.",
            "Tracking shot accuracy and decision-making speed in fatigued players following supplementation.",
            "Glycogen sparing effects and central nervous system (CNS) arousal maintenance during extended tournament play."
        ]
    },
    {
        "filename": "Topic_Task_Constraint_Scaling_U11",
        "title": "Task Constraint Scaling for Under-11 Players",
        "description": "Effects of scaling court dimensions and net heights to match the physiological profile of youth players.",
        "source": "BWF_Research project/Badminton Performance_Coaching/JOURNAL-UJ_Gema-2.pdf",
        "outline": [
            "Impact of court scaling (reducing length and net height to 1.30m) on rally lengths and active playtime.",
            "Technical adaptations: Higher frequency of overhead smashes and net drops in scaled match-play.",
            "Designing optimal training game spaces to prevent early mechanical errors in youth badminton."
        ]
    },
    {
        "filename": "Topic_Wheelchair_Match_Play_Kinematics",
        "title": "Wheelchair Match Play Kinematics",
        "description": "Cardiorespiratory, metabolic, and temporal profile differences between WH1 and WH2 wheelchair categories.",
        "source": "BWF_Research project/Para Badminton/Oliveira-1.pdf",
        "outline": [
            "Physiological parameters: Heart rate zones, VO2 demand, and peak lactate levels in wheelchair singles.",
            "Temporal characteristics: Rally duration, play-to-rest ratio, and push frequency per rally.",
            "Influence of trunk stability (WH2) vs. lack of abdominal control (WH1) on court coverage speed."
        ]
    },
    {
        "filename": "Topic_Para_Badminton_Psychosocial_Impact",
        "title": "Para-Badminton Psychosocial Impact",
        "description": "Qualitative analysis of the psychophysical, emotional, and social health improvements in para-badminton players.",
        "source": "BWF_Research project/Para Badminton/Thesis-Dr.-Alberti-Stefano-Qualitative-analysis-of-ParaBadmintons-psycophysical-and-social-impact.pdf",
        "outline": [
            "Assessing changes in self-esteem, body image, and personal empowerment among wheelchair players.",
            "Social integration benefits: Building peer networks and community inclusion through sport.",
            "Cognitive and mental health benefits of regular competitive play for athletes with physical impairments."
        ]
    },
    {
        "filename": "Topic_Markerless_Motion_Analysis_Matchplay",
        "title": "Markerless Motion Analysis in Matchplay",
        "description": "Using markerless motion capture systems to quantify external mechanical work, sex differences, and discipline demands.",
        "source": "BWF_Research project/Badminton Performance_Coaching/Using-markerless-motion-analysis-to-quantify-sex-and-discipline-differences-in-external-mechanical-work-during-badminton-match-play.pdf",
        "outline": [
            "Comparing mechanical work output between singles, doubles, and mixed doubles play.",
            "Identifying sex-specific mechanical loading patterns on court using multi-camera capture.",
            "Markerless tracking validity: Transitioning biomechanical research from laboratory settings to live tournament matches."
        ]
    }
]

# Path variables
generated_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
raw_notes_dir = r"C:\Users\usEr\MyLLMDataProject\RawNotes"

# 1. Create the new topic files
def create_research_topic_files():
    print("Creating 18 new research topic files...")
    for topic in research_topics:
        filename = f"{topic['filename']}.md"
        filepath = os.path.join(generated_dir, filename)
        
        # Build file content
        content = f"Source File: [{topic['source']}](../RawNotes/{topic['source']})\n\n"
        content += f"# {topic['title']}\n\n"
        content += f"{topic['description']}\n\n"
        content += "## Structural Outline\n\n"
        
        for i, item in enumerate(topic['outline'], 1):
            content += f"{i}. {item}\n"
            
        content += "\n## Related Topics\n\n"
        content += "\n#llm-deep-backlog\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {filename}")

# 2. Define cross-references dynamically
topic_associations = {
    # Hitting & Smash
    "Topic_Forehand_Smash_Angles": ["Topic_Speed_Accuracy_Tradeoff_Smash", "Topic_Jump_Smash_Kinetic_Consistency", "Topic_Shuttlecock_Aerodynamic_Deceleration"],
    "Topic_Speed_Accuracy_Tradeoff_Smash": ["Topic_Forehand_Smash_Angles", "Topic_Jump_Smash_Kinetic_Consistency", "Topic_Shuttlecock_Aerodynamic_Deceleration"],
    "Topic_Jump_Smash_Kinetic_Consistency": ["Topic_Forehand_Smash_Angles", "Topic_Speed_Accuracy_Tradeoff_Smash", "Topic_Kinetic_Chain_in_Overhead_Strokes"],
    "Topic_Shuttlecock_Aerodynamic_Deceleration": ["Topic_Forehand_Smash_Angles", "Topic_Speed_Accuracy_Tradeoff_Smash", "Topic_Forehand_Clear_Biomechanics"],
    
    # Footwork & Landing Loads
    "Topic_Biomechanics_of_Lunging": ["Topic_Multi_Feeding_vs_Match_Play_Load", "Topic_Leg_Length_Discrepancy_Back_Pain", "Topic_Landing_Instability_Overhead_Backhand", "Topic_Patellar_Tendinopathy_Jumper_Knee"],
    "Topic_Multi_Feeding_vs_Match_Play_Load": ["Topic_Biomechanics_of_Lunging", "Topic_Racket_Feeding_Multi_Feed", "Topic_Overtraining_and_Burnout", "Topic_Landing_Instability_Overhead_Backhand"],
    "Topic_Landing_Instability_Overhead_Backhand": ["Topic_Biomechanics_of_Lunging", "Topic_Backhand_Clear_Struggles", "Topic_Thoracic_Spine_Mobility", "Topic_Multi_Feeding_vs_Match_Play_Load"],
    "Topic_Leg_Length_Discrepancy_Back_Pain": ["Topic_Biomechanics_of_Lunging", "Topic_Ankle_Sprains_Rehabilitation", "Topic_Core_Stability_for_Badminton"],
    
    # Conditioning, Fatigue & Recovery
    "Topic_Aerobic_Endurance_for_Badminton": ["Topic_Consecutive_Matches_Fatigue", "Topic_Ischemic_Preconditioning_Recovery", "Topic_Heart_Rate_Monitoring"],
    "Topic_Consecutive_Matches_Fatigue": ["Topic_Aerobic_Endurance_for_Badminton", "Topic_Ischemic_Preconditioning_Recovery", "Topic_Active_Recovery_Strategies", "Topic_Hydration_and_Electrolytes"],
    "Topic_Ischemic_Preconditioning_Recovery": ["Topic_Consecutive_Matches_Fatigue", "Topic_Active_Recovery_Strategies", "Topic_Aerobic_Endurance_for_Badminton"],
    "Topic_Active_Recovery_Strategies": ["Topic_Consecutive_Matches_Fatigue", "Topic_Ischemic_Preconditioning_Recovery", "Topic_Overtraining_and_Burnout"],
    "Topic_Carbohydrate_Caffeine_Supplementation": ["Topic_Nutrition_for_Badminton_Players", "Topic_Consecutive_Matches_Fatigue", "Topic_Anticipation_Under_Physiological_Stress"],
    "Topic_Anticipation_Under_Physiological_Stress": ["Topic_Perceptual_Anticipation_Training", "Topic_Consecutive_Matches_Fatigue", "Topic_Psychology_of_Elite_Pressure"],
    "Topic_Perceptual_Anticipation_Training": ["Topic_Anticipation_Under_Physiological_Stress", "Topic_Observation_and_Analysis_Methodology", "Topic_Stages_of_Motor_Learning"],
    
    # Children & Task Constraint Scaling
    "Topic_Adapting_Equipment_for_Children": ["Topic_Task_Constraint_Scaling_U11", "Topic_Youth_Development_Pathways", "Topic_Growth_Spurt_Maturation_Impact"],
    "Topic_Task_Constraint_Scaling_U11": ["Topic_Adapting_Equipment_for_Children", "Topic_Youth_Development_Pathways", "Topic_Growth_Spurt_Maturation_Impact"],
    
    # Swiss Ball & FMS
    "Topic_Swiss_Ball_Core_Functional_Movement": ["Topic_Core_Stability_for_Badminton", "Topic_Session_Planning_Basics", "Topic_Flexibility_and_Injury_Prevention"],
    "Topic_Core_Stability_for_Badminton": ["Topic_Swiss_Ball_Core_Functional_Movement", "Topic_Thoracic_Spine_Mobility"],
    
    # Shoulder pain & Rotator Cuff
    "Topic_Shoulder_Pain_and_Physical_Fitness": ["Topic_Rotator_Cuff_Strengthening", "Topic_Flexibility_and_Injury_Prevention", "Topic_Thoracic_Spine_Mobility"],
    "Topic_Rotator_Cuff_Strengthening": ["Topic_Shoulder_Pain_and_Physical_Fitness"],
    
    # Para-badminton
    "Topic_Para_Badminton_Sport_Classes": ["Topic_Wheelchair_Match_Play_Kinematics", "Topic_Para_Badminton_Psychosocial_Impact", "Topic_Standing_Para_Player_Adaptations"],
    "Topic_Wheelchair_Match_Play_Kinematics": ["Topic_Para_Badminton_Sport_Classes", "Topic_Wheelchair_Court_Size_Rules", "Topic_Wheelchair_Service_Height_Rule"],
    "Topic_Para_Badminton_Psychosocial_Impact": ["Topic_Para_Badminton_Sport_Classes", "Topic_Coaching_Players_with_Intellectual_Disabilities"],
    "Topic_Wheelchair_Court_Size_Rules": ["Topic_Wheelchair_Match_Play_Kinematics"],
    "Topic_Wheelchair_Service_Height_Rule": ["Topic_Wheelchair_Match_Play_Kinematics"],
    
    # Markerless Motion
    "Topic_Markerless_Motion_Analysis_Matchplay": ["Topic_Performance_Analysis_Tools", "Topic_Match_Analysis_and_Scouting", "Topic_Elite_Match_Analysis_Software"]
}

def scan_and_update_links():
    print("Scanning all topic files to establish links...")
    
    # Load all existing filenames (without extension)
    all_files = [os.path.splitext(f)[0] for f in os.listdir(generated_dir) if f.endswith(".md")]
    
    for filename in os.listdir(generated_dir):
        if filename.endswith(".md"):
            topic_name = os.path.splitext(filename)[0]
            filepath = os.path.join(generated_dir, filename)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Parse header, core, and previous related topics
            lines = content.split('\n')
            
            header_lines = []
            core_lines = []
            related_lines = []
            
            section = "header" # can be header, core, related
            for line in lines:
                # Identify header vs core
                if section == "header":
                    if line.startswith("Source Manual:") or line.startswith("Source File:"):
                        header_lines.append(line)
                        continue
                    elif line.strip() == "":
                        continue
                    else:
                        section = "core"
                
                # Check for related topics start
                if line.startswith("## Related Topics"):
                    section = "related"
                    continue
                    
                if line.strip() == "#llm-deep-backlog":
                    continue
                    
                if section == "core":
                    core_lines.append(line)
                elif section == "related":
                    # Collect existing links if any
                    m = re.match(r'^\*\s+\[\[(.*?)\]\]', line.strip())
                    if m:
                        related_lines.append(m.group(1))
            
            # Formulate the updated list of related links
            # Start with existing links
            updated_related = list(related_lines)
            
            # Check mapping for explicit additions
            if topic_name in topic_associations:
                for target in topic_associations[topic_name]:
                    if target in all_files and target not in updated_related:
                        updated_related.append(target)
            
            # Bidirectional: check if this topic is a target of another topic, then link them
            for source, targets in topic_associations.items():
                if topic_name in targets and source in all_files and source not in updated_related:
                    updated_related.append(source)
                    
            # Ensure unique, and limit list size to max 8
            unique_links = []
            for link in updated_related:
                if link != topic_name and link in all_files and link not in unique_links:
                    unique_links.append(link)
            unique_links = unique_links[:8]
            
            # Reconstruct content
            new_header = '\n'.join(header_lines).strip()
            new_core = '\n'.join(core_lines).strip()
            
            new_content = ""
            if new_header:
                new_content += new_header + "\n\n"
            new_content += new_core + "\n\n"
            new_content += "## Related Topics\n\n"
            
            for l in unique_links:
                new_content += f"* [[{l}]]\n"
                
            new_content += "\n#llm-deep-backlog\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
    print("Successfully completed the dynamic link cross-reference update across all files!")

if __name__ == "__main__":
    create_research_topic_files()
    scan_and_update_links()
