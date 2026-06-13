import os

# Define the semantic groups of topics
groups = {
    "framework": [
        "Topic_BWF_Coaching_Framework_Levels",
        "Topic_Coaching_Philosophy_Development",
        "Topic_Autocratic_vs_Democratic_Coaching",
        "Topic_Role_and_Ethics_of_the_Coach",
        "Topic_Inclusivity_in_Badminton",
        "Topic_Ability_vs_Potential",
        "Topic_Youth_Development_Pathways",
        "Topic_Growth_Spurt_Maturation_Impact"
    ],
    "process": [
        "Topic_Coaching_Process_Overview",
        "Topic_Session_Planning_Basics",
        "Topic_Designing_Progressive_Practices",
        "Topic_Risk_Assessment_for_Badminton_Coaches",
        "Topic_Group_Management_and_Safety"
    ],
    "pedagogy": [
        "Topic_VAK_Learning_Styles_in_Badminton",
        "Topic_Methods_of_Developing_Skills",
        "Topic_Stages_of_Motor_Learning",
        "Topic_Face_to_Face_Communication",
        "Topic_Questioning_Techniques_for_Coaches",
        "Topic_Effective_Feedback_Delivery",
        "Topic_Demonstration_Best_Practices"
    ],
    "feeding": [
        "Topic_Racket_Feeding_Multi_Feed",
        "Topic_Racket_Feeding_Rallying",
        "Topic_Hand_Feeding_Underarm",
        "Topic_Hand_Feeding_Overarm",
        "Topic_Flat_Fast_Feeding"
    ],
    "grips_net": [
        "Topic_Badminton_V_Grip",
        "Topic_Thumb_Grip_for_Backhand",
        "Topic_Corner_Grip_Transition",
        "Topic_Panhandle_Grip_Applications",
        "Topic_Forehand_and_Backhand_Net_Shots",
        "Topic_Forehand_and_Backhand_Net_Lifts",
        "Topic_Forehand_and_Backhand_Net_Kills"
    ],
    "serves": [
        "Topic_Backhand_Low_Serve",
        "Topic_Forehand_High_Serve",
        "Topic_Backhand_Flick_Serve",
        "Topic_Forehand_Flick_Serve"
    ],
    "movement": [
        "Topic_The_Split_Step_Mechanism",
        "Topic_Footwork_Traveling_Movements",
        "Topic_Biomechanics_of_Lunging",
        "Topic_Base_Position_and_Recovery"
    ],
    "strokes": [
        "Topic_Forehand_Clear_Biomechanics",
        "Topic_Forehand_Dropshot_Slices",
        "Topic_Forehand_Smash_Angles",
        "Topic_Backhand_Clear_Struggles",
        "Topic_Backhand_Dropshot_Deceleration",
        "Topic_Forehand_Pulled_Dropshot",
        "Topic_Forearm_Pronation_and_Supination",
        "Topic_Kinetic_Chain_in_Overhead_Strokes",
        "Topic_Thoracic_Spine_Mobility"
    ],
    "conditioning": [
        "Topic_Aerobic_Endurance_for_Badminton",
        "Topic_Anaerobic_Lactic_System",
        "Topic_Anaerobic_Alactic_System",
        "Topic_Strength_Training_Periodization",
        "Topic_Speed_and_Agility_Drills",
        "Topic_Flexibility_and_Injury_Prevention",
        "Topic_Active_Recovery_Strategies",
        "Topic_Heart_Rate_Monitoring"
    ],
    "tactics": [
        "Topic_Tactical_Patterns_in_Singles",
        "Topic_Tactical_Patterns_in_Doubles",
        "Topic_Mixed_Doubles_Specific_Tactics",
        "Topic_Match_Analysis_and_Scouting",
        "Topic_Strategy_Formulation_in_Matches",
        "Topic_Coaching_in_Competition_Intervals"
    ],
    "sports_med": [
        "Topic_Overtraining_and_Burnout",
        "Topic_RICE_Protocol_for_Injuries",
        "Topic_Ankle_Sprains_Rehabilitation",
        "Topic_Patellar_Tendinopathy_Jumper_Knee",
        "Topic_Rotator_Cuff_Strengthening",
        "Topic_Core_Stability_for_Badminton",
        "Topic_Hydration_and_Electrolytes"
    ],
    "psychology": [
        "Topic_The_5_Cs_in_Sports_Psychology",
        "Topic_Motivational_Cues_in_Coaching",
        "Topic_Goal_Setting_for_Beginners",
        "Topic_Goal_Setting_for_Elites",
        "Topic_Psychology_of_Elite_Pressure"
    ],
    "high_performance": [
        "Topic_Elite_Player_Pathways",
        "Topic_Talent_Identification_Tests",
        "Topic_High_Performance_Planning",
        "Topic_Elite_Sports_Science_Physiology",
        "Topic_Elite_Match_Analysis_Software",
        "Topic_High_Performance_Athlete_Management"
    ],
    "para": [
        "Topic_Para_Badminton_Sport_Classes",
        "Topic_Wheelchair_Court_Size_Rules",
        "Topic_Wheelchair_Service_Height_Rule",
        "Topic_Standing_Para_Player_Adaptations",
        "Topic_Short_Stature_Class_SH6_Rules",
        "Topic_Coaching_Players_with_Intellectual_Disabilities",
        "Topic_Coaching_Deaf_Badminton_Players",
        "Topic_Para_Badminton_Equipment_Adaptations",
        "Topic_Risk_Assessment_for_Para_Badminton"
    ]
}

# Cross-group relations: map groups to related groups
related_group_map = {
    "framework": ["process", "pedagogy", "high_performance"],
    "process": ["framework", "pedagogy", "feeding"],
    "pedagogy": ["framework", "process", "feeding", "psychology"],
    "feeding": ["process", "pedagogy", "grips_net", "movement"],
    "grips_net": ["movement", "strokes", "tactics"],
    "serves": ["grips_net", "movement", "strokes", "tactics"],
    "movement": ["grips_net", "strokes", "conditioning", "sports_med"],
    "strokes": ["grips_net", "movement", "conditioning", "sports_med"],
    "conditioning": ["movement", "strokes", "sports_med", "high_performance"],
    "tactics": ["grips_net", "serves", "movement", "high_performance"],
    "sports_med": ["conditioning", "movement", "high_performance"],
    "psychology": ["framework", "pedagogy", "high_performance"],
    "high_performance": ["framework", "conditioning", "tactics", "psychology", "sports_med"],
    "para": ["framework", "process", "grips_net", "movement", "sports_med"]
}

# Source manual mapping
manuals = {
    "L1": "bwf_coach_education_coaches_manual_l1-2nd-edition-midres_clean.md",
    "L2": "BWF_Coach_Manual_Level_2_English_clean.md",
    "L3": "CE-Level-3_DIGITAL_clean.md"
}

# Map each topic to manual based on names
def get_source_manual(topic_name):
    # Para topics are Level 1 (Module 13)
    if topic_name in groups["para"]:
        return manuals["L1"]
    
    # High performance is Level 3
    if topic_name in groups["high_performance"] or topic_name in [
        "Topic_Strategy_Formulation_in_Matches", "Topic_Match_Analysis_and_Scouting", 
        "Topic_Coaching_in_Competition_Intervals", "Topic_Psychology_of_Elite_Pressure"
    ]:
        return manuals["L3"]
        
    # Level 2 focus
    if topic_name in groups["conditioning"] or topic_name in groups["sports_med"] or topic_name in [
        "Topic_Coaching_Process_Overview", "Topic_Macrocycles_in_Badminton", 
        "Topic_Mesocycles_for_Competition", "Topic_Microcycles_Weekly_Planning",
        "Topic_Goal_Setting_for_Elites", "Topic_Performance_Analysis_Tools"
    ]:
        return manuals["L2"]
        
    # Level 1 focus
    return manuals["L1"]

def get_related_topics(topic_name):
    # Find which group this topic belongs to
    owner_group = None
    for gname, gtopics in groups.items():
        if topic_name in gtopics:
            owner_group = gname
            break
            
    if not owner_group:
        return []
        
    related = []
    # 1. Add other topics in the same group
    for t in groups[owner_group]:
        if t != topic_name:
            related.append(t)
            
    # 2. Add some topics from related groups
    if owner_group in related_group_map:
        for rg in related_group_map[owner_group]:
            # Take the first 2 topics from each related group to avoid overwhelming
            related.extend(groups[rg][:2])
            
    # Remove duplicates and limit to top 6-8 related topics
    unique_related = []
    for r in related:
        if r not in unique_related and r != topic_name:
            unique_related.append(r)
            
    return unique_related[:6]

def update_files():
    topics_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
    for filename in os.listdir(topics_dir):
        if filename.endswith(".md"):
            topic_name = os.path.splitext(filename)[0]
            filepath = os.path.join(topics_dir, filename)
            
            # Get properties
            manual = get_source_manual(topic_name)
            related = get_related_topics(topic_name)
            
            # Read existing content
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # If manual link or related section already exists, clean them out
            lines = content.split('\n')
            
            # Filter out previous source manual headers, related topics, and backlog tags
            filtered_lines = []
            skip = False
            for line in lines:
                if line.startswith("Source Manual:") or line.startswith("Related Topics:") or line.startswith("[Source Manual]"):
                    continue
                if line.startswith("## Related Topics"):
                    skip = True
                    continue
                if skip and (line.startswith("#") and not line.startswith("## Related Topics")):
                    skip = False
                if skip:
                    continue
                if line.strip() == "#llm-deep-backlog":
                    continue
                filtered_lines.append(line)
                
            # Reconstruct the cleaned core content
            core_content = '\n'.join(filtered_lines).strip()
            
            # Build new content structure
            new_content = f"Source Manual: [{manual}](../RawNotes/{manual})\n\n"
            new_content += core_content + "\n\n"
            new_content += "## Related Topics\n\n"
            
            for rt in related:
                new_content += f"* [[{rt}]]\n"
                
            new_content += "\n#llm-deep-backlog\n"
            
            # Write back to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
                
    print("Successfully updated all 100 files with Obsidian links and source manual headers!")

if __name__ == "__main__":
    update_files()
