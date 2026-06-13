import os
import re

def to_title_case(name):
    # Capitalize each word segment separated by underscores
    parts = name.split('_')
    cap_parts = [p.capitalize() for p in parts if p]
    return '_'.join(cap_parts)

def sanitize_filename(name):
    name = name.lower()
    name = re.sub(r'[^\w]', '_', name) # Replace non-alphanumeric with underscores
    name = re.sub(r'_+', '_', name) # Replace multiple underscores with a single one
    name = name.strip('_')
    return to_title_case(name)

# 1. Technical Skills (21 items)
techniques = [
    {"id": "v_grip", "name": "V-Grip", "desc": "The foundational V-grip used for forehand strokes, net play, and general racket control."},
    {"id": "thumb_grip", "name": "Thumb Grip", "desc": "The thumb grip, providing leverage and control for backhand strokes, low serves, and net lifts."},
    {"id": "corner_grip", "name": "Corner Grip", "desc": "The corner (or bevel) grip, used for backhand flick serves, late backhand clears, and backhand drop shots."},
    {"id": "panhandle_grip", "name": "Panhandle Grip", "desc": "The panhandle grip, used for forehand net kills, midcourt drives, and quick flat exchanges."},
    {"id": "short_grip", "name": "Short Grip", "desc": "The short grip (choking up on the handle), optimizing racket speed and control in the forecourt."},
    {"id": "long_grip", "name": "Long Grip", "desc": "The long grip (holding the racket end), maximizing power, leverage, and reach in the rearcourt."},
    {"id": "backhand_low_serve", "name": "Backhand Low Serve", "desc": "The backhand low serve, designed to cross the net low and land close to the short service line."},
    {"id": "backhand_flick_serve", "name": "Backhand Flick Serve", "desc": "The backhand flick serve, used to surprise opponents by flicking the shuttle deep into their rearcourt."},
    {"id": "forehand_low_serve", "name": "Forehand Low Serve", "desc": "The forehand low serve, a tactical variation to keep the shuttle low and disrupt the opponent's timing."},
    {"id": "forehand_flick_serve", "name": "Forehand Flick Serve", "desc": "The forehand flick serve, used to draw opponents forward before flicking the shuttle overhead."},
    {"id": "forehand_high_serve", "name": "Forehand High Serve", "desc": "The forehand high serve, delivering the shuttle high and deep to the opponent's back boundary line."},
    {"id": "net_shots", "name": "Net Shots", "desc": "Forehand and backhand net shots, played from the forecourt to drop vertically close to the opponent's side of the net."},
    {"id": "net_lifts", "name": "Net Lifts", "desc": "Forehand and backhand net lifts, clearing the shuttle high and deep from the net to the opponent's rearcourt."},
    {"id": "net_kills", "name": "Net Kills", "desc": "Forehand and backhand net kills, executing steep, downward strikes on loose shuttles near the net."},
    {"id": "drives", "name": "Drives", "desc": "Forehand and backhand drive shots, flat and fast midcourt exchanges hit parallel to the floor."},
    {"id": "body_blocks", "name": "Body Blocks", "desc": "Forehand and backhand body blocks, defensive wall-like blocks of fast-paced smashes targeted at the player's torso."},
    {"id": "forehand_clears", "name": "Forehand Clears", "desc": "Forehand overhead clears, hitting the shuttle high and deep from one rearcourt to the opponent's rearcourt."},
    {"id": "smashes", "name": "Smashes", "desc": "Forehand overhead smashes, powerful, steep, downward attacking strokes aimed at the opponent's midcourt."},
    {"id": "drops", "name": "Drops", "desc": "Forehand overhead drops, soft, slow strokes played from the rearcourt to drop close to the opponent's net."},
    {"id": "backhand_clears", "name": "Backhand Clears", "desc": "Backhand overhead clears, requiring correct kinetic chain and thumb/bevel grip to clear the shuttle deep."},
    {"id": "backhand_drops", "name": "Backhand Drops", "desc": "Backhand overhead drop shots, using decelerating racket head speed to place the shuttle softly over the net."}
]

# 8 dimensions for Technical Skills
tech_dimensions = [
    {
        "id": "biomechanics",
        "title": "Biomechanical Principles and Racket Work",
        "outline_template": [
            "Detailed analysis of the grip pressure, wrist articulation, and forearm rotation (pronation/supination) required for {name}.",
            "Optimizing the contact point relative to the body and racket head speed generation.",
            "The role of the non-racket arm in balancing the torso and kinetic chain efficiency."
        ]
    },
    {
        "id": "footwork",
        "title": "Footwork Integration and Body Positioning",
        "outline_template": [
            "Establishing the correct base position and split-step timing before executing the {name}.",
            "Footwork patterns (chassé, cross-over, lunges) required to reach the shuttle early.",
            "Center of gravity recovery and returning to the base position."
        ]
    },
    {
        "id": "singles_tactics",
        "title": "Tactical Utility in Singles Play",
        "outline_template": [
            "Positioning and target areas on the court to force weak replies using {name}.",
            "Setting up the rally and controlling the pace of the game in singles.",
            "Anticipating the opponent's recovery and counter-attacking options."
        ]
    },
    {
        "id": "doubles_tactics",
        "title": "Tactical Utility in Doubles Play",
        "outline_template": [
            "Midcourt and forecourt positioning adjustments when executing {name} in doubles.",
            "Promoting offensive pressure and rotational consistency between partners.",
            "Targeted placements to disrupt the opponent's defensive formation."
        ]
    },
    {
        "id": "common_errors",
        "title": "Common Errors, Diagnostic Indicators, and Corrective Actions",
        "outline_template": [
            "Identifying common kinematic errors (e.g., stiff wrist, poor timing, incorrect grip) during {name}.",
            "Coaching observations and diagnostic symptoms (e.g., net clipping, shuttle sailing long, lack of power).",
            "Implementing targeted corrective drills and mechanical adjustments to fix errors."
        ]
    },
    {
        "id": "feeding_drills",
        "title": "Feeder Feeding Drills and Skill Progression",
        "outline_template": [
            "Setting up static hand-feeding and racket-feeding drills to build confidence.",
            "Progressing to dynamic multi-feeding drills that incorporate lateral or forward-backward movement.",
            "Simulating pressure scenarios with variable feeding pace and placement."
        ]
    },
    {
        "id": "learning_stages",
        "title": "Skill Development and Learning Stages",
        "outline_template": [
            "Cognitive phase progressions, focusing on basic coordination and visual templates for {name}.",
            "Associative phase exercises, introducing random practice, pressure, and self-evaluation.",
            "Autonomous phase integration, where the movement is combined with tactical choices."
        ]
    },
    {
        "id": "sensory_cues",
        "title": "Visual, Auditory, and Kinesthetic Coaching Cues",
        "outline_template": [
            "Visual cues: Racket face orientation, target markers, and observation of the racket trajectory.",
            "Auditory cues: The rhythm of the footwork and the distinct hitting sound of {name} at impact.",
            "Kinesthetic cues: The feeling of grip tension release, joint angles, and weight transfer."
        ]
    }
]

# 2. Movements (8 items)
movements = [
    {"id": "split_step", "name": "Split-Step", "desc": "The split-step, a neutral pre-activation hop timed with the opponent's strike to prepare for rapid movement in any direction."},
    {"id": "chasse_footwork", "name": "Chassé Footwork", "desc": "The chassé (side-gallop) footwork, used for lateral and diagonal court travel without crossing the legs."},
    {"id": "crossover_footwork", "name": "Cross-Over Footwork", "desc": "The cross-over step footwork, used to cover longer distances rapidly by crossing one foot over the other."},
    {"id": "front_lunge", "name": "Front Lunge", "desc": "The front-hand and non-hand lunges, critical for reaching net shots while maintaining low center of gravity and stable trunk."},
    {"id": "front_back_lunge", "name": "Front-Back Lunge", "desc": "The forward and backward lunging movements, combining deceleration, lunging, and explosive push-off recovery."},
    {"id": "lateral_lunge", "name": "Lateral Lunge", "desc": "The lateral lunge, used to reach wide midcourt drives and blocks while protecting the knees and hips."},
    {"id": "recovery_base", "name": "Recovery Base", "desc": "The recovery base positioning, dynamic movement back to the optimal court-center base after hitting a stroke."},
    {"id": "traveling_movements", "name": "Traveling Movements", "desc": "General traveling movements including forward runs, backward steps, and lateral slides to cover the entire badminton court."}
]

# 8 dimensions for Movements
mov_dimensions = [
    {
        "id": "biomechanics",
        "title": "Biomechanical Analysis and Kinematics",
        "outline_template": [
            "Center of gravity alignment and body posture during {name}.",
            "Lower extremity joint angles (ankle, knee, hip) and joint loading during execution.",
            "The role of push-off force and kinetic energy transfer in movement efficiency."
        ]
    },
    {
        "id": "tactics",
        "title": "Tactical Importance and Court Positioning",
        "outline_template": [
            "Strategic placement on court and timing of {name} relative to the opponent's strike.",
            "Minimizing recovery time and optimizing court coverage pathways.",
            "Adapting positioning based on singles versus doubles tactical requirements."
        ]
    },
    {
        "id": "errors",
        "title": "Common Movement Errors and Corrective Drills",
        "outline_template": [
            "Identifying common footwork errors (e.g., heel striking, flat-footedness, poor weight transfer).",
            "Diagnostic cues for coaches during match play and structured practices.",
            "Corrective drills and movement patterns to retrain the nervous system."
        ]
    },
    {
        "id": "pedagogy",
        "title": "Pedagogy: Teaching Progressions and Stages of Learning",
        "outline_template": [
            "Breaking down {name} using the whole-part-whole methodology.",
            "Cognitive phase coaching focus: static positioning and simple, repetitive footwork drills.",
            "Associative to autonomous phase: introducing variable feeding, reactiveness, and tactical decisions."
        ]
    },
    {
        "id": "conditioning",
        "title": "Physical Conditioning and Power Development",
        "outline_template": [
            "Strength and power development (e.g., plyometrics, resistance training) to enhance {name}.",
            "Developing speed, quickness, and change-of-direction agility on court.",
            "Core stability exercises to maintain balance during explosive push-offs."
        ]
    },
    {
        "id": "feedback",
        "title": "Feedback and Sensory Cueing",
        "outline_template": [
            "Visual coaching tools (e.g., floor markings, target cones) to guide foot placement.",
            "Auditory rhythms and feedback cues to establish smooth footwork timing.",
            "Kinesthetic focus points: weight distribution, balance, and sensory feeling of contact."
        ]
    },
    {
        "id": "planning",
        "title": "Session Planning and Integration in Group Practice",
        "outline_template": [
            "Incorporating {name} into warm-ups and progressive movement drills.",
            "Managing group sizes and court layout to maximize active movement repetitions.",
            "Design of high-frequency feeding drills for movement endurance."
        ]
    },
    {
        "id": "safety",
        "title": "Safety, Injury Prevention, and Joint Loading",
        "outline_template": [
            "Analyzing joint stress (specifically knees and ankles) during {name}.",
            "Proper shoe selection, orthotics, and court surfaces to minimize impact.",
            "Preventative strength exercises and dynamic stretching routines for lower limbs."
        ]
    }
]

# 3. Pedagogy (18 items)
pedagogy = [
    {"id": "visual_learning", "name": "Visual Learning Style", "desc": "Instructional delivery catering to visual learners through demonstrations, whiteboard diagrams, and video feedback."},
    {"id": "auditory_learning", "name": "Auditory Learning Style", "desc": "Instructional delivery catering to auditory learners through verbal explanations, rhythmic hitting sounds, and keywords."},
    {"id": "kinesthetic_learning", "name": "Kinesthetic Learning Style", "desc": "Instructional delivery catering to kinesthetic learners through physical guidance, target challenges, and feeling joint positions."},
    {"id": "shaping_method", "name": "Shaping Method", "desc": "Shaping technique in skill development, modifying target tasks and parameters to guide progressive skill acquisition."},
    {"id": "chaining_method", "name": "Chaining Method", "desc": "Chaining technique in skill development, breaking down complex strokes into links and teaching them sequentially."},
    {"id": "whole_part_whole", "name": "Whole-Part-Whole Method", "desc": "Whole-part-whole coaching method, demonstrating the full stroke, breaking out a component to practice, and reintegrating it."},
    {"id": "cognitive_stage", "name": "Cognitive Learning Stage", "desc": "Characteristics and coaching adjustments for players in the first, high-cognitive-load stage of motor learning."},
    {"id": "associative_stage", "name": "Associative Learning Stage", "desc": "Characteristics and coaching adjustments for players in the associative stage, refining movement patterns with fewer errors."},
    {"id": "autonomous_stage", "name": "Autonomous Learning Stage", "desc": "Characteristics and coaching adjustments for players in the autonomous stage, executing motor skills with high automaticity."},
    {"id": "session_planning", "name": "Session Planning", "desc": "Structuring, scheduling, and sequencing coaching sessions with clear warm-up, core, and cool-down blocks."},
    {"id": "risk_assessment", "name": "Risk Assessment", "desc": "Safety planning, hazard identification, court inspection, and medical readiness protocols for badminton sessions."},
    {"id": "group_management", "name": "Group Management", "desc": "Organizing groups, court assignments, maximizing active time, and maintaining discipline during group coaching."},
    {"id": "coaching_delivery", "name": "Coaching Delivery", "desc": "Tone, position on court, clarity, and pacing when presenting instructions and managing the training space."},
    {"id": "coaching_feedback", "name": "Coaching Feedback", "desc": "Delivering constructive, immediate, delayed, intrinsic, and extrinsic feedback to support learning without overload."},
    {"id": "demonstration_techniques", "name": "Demonstration Techniques", "desc": "Best practices for demonstrating strokes: camera angles, body positioning, using assistant coaches, and highlight points."},
    {"id": "multi_feeding_racket", "name": "Multi-Feeding Racket", "desc": "Racket-based multi-feeding, controlling speed, spin, and trajectory to feed multiple players in sequence."},
    {"id": "hand_feeding_underarm", "name": "Hand-Feeding Underarm", "desc": "Underarm hand-feeding, providing precise, consistent trajectories to build player confidence in net play and drives."},
    {"id": "hand_feeding_overarm", "name": "Hand-Feeding Overarm", "desc": "Overarm hand-feeding, throwing shuttles downward to simulate smashes and defensive block situations."}
]

# 4 dimensions for Pedagogy
ped_dimensions = [
    {
        "id": "planning",
        "title": "Coaching Application and Session Planning",
        "outline_template": [
            "Incorporating {name} into lesson plans and curriculum development.",
            "Setting clear behavioral and learning objectives aligned with this pedagogical approach.",
            "Resource allocation, time management, and group organization considerations."
        ]
    },
    {
        "id": "practice",
        "title": "Practical Examples in Stroke and Movement Training",
        "outline_template": [
            "Practical application of {name} during grip and serve introductions.",
            "Using {name} to improve footwork speed and court movement patterns.",
            "Real-world case studies of player improvement using this specific approach."
        ]
    },
    {
        "id": "troubleshooting",
        "title": "Troubleshooting, Common Coaching Mistakes, and Solutions",
        "outline_template": [
            "Identifying mistakes coaches make when applying {name} (e.g., information overload, poor timing).",
            "Diagnostic signs that the pedagogical method is not working (e.g., player confusion, lack of progress).",
            "Strategic adjustments and alternative coaching strategies to restore learning efficiency."
        ]
    },
    {
        "id": "inclusivity",
        "title": "Integration with Special Populations and Inclusivity",
        "outline_template": [
            "Adapting {name} for wheelchair (WH1/WH2) and standing (SL3/SL4/SU5) para-badminton players.",
            "Modifying communication and teaching techniques for players with intellectual disabilities (ID) or deaf players.",
            "Creating an inclusive environment that respects diverse learning speeds and physical abilities."
        ]
    }
]

# 4. Special Populations (8 items)
special_populations = [
    {"id": "wheelchair_wh1", "name": "Wheelchair WH1 Class", "desc": "Para-badminton wheelchair WH1 classification, for players with severe impairment in trunk and lower limbs."},
    {"id": "wheelchair_wh2", "name": "Wheelchair WH2 Class", "desc": "Para-badminton wheelchair WH2 classification, for players with minor trunk impairment and lower limb limitations."},
    {"id": "standing_sl3", "name": "Standing SL3 Class", "desc": "Para-badminton standing SL3 classification, for players with impairment in one or both lower limbs and poor walking balance."},
    {"id": "standing_sl4", "name": "Standing SL4 Class", "desc": "Para-badminton standing SL4 classification, for players with minor impairment in lower limbs and better balance/mobility."},
    {"id": "standing_su5", "name": "Standing SU5 Class", "desc": "Para-badminton standing SU5 classification, for players with impairment of the upper limbs (racket or non-racket arm)."},
    {"id": "short_stature_sh6", "name": "Short Stature SH6 Class", "desc": "Para-badminton short stature SH6 classification, for players with dwarfism or standing height restrictions."},
    {"id": "intellectual_disability", "name": "ID Players", "desc": "Coaching strategies for badminton players with intellectual disabilities, focusing on inclusion and skill acquisition."},
    {"id": "deaf_players", "name": "Deaf Players", "desc": "Coaching strategies and visual adaptation methods for deaf or hard-of-hearing badminton players."}
]

# 3 dimensions for Special Populations
spec_dimensions = [
    {
        "id": "rules",
        "title": "Classification, Rules, and Court Adaptation",
        "outline_template": [
            "Understanding the official classification criteria and functional profiles of {name} players.",
            "Court boundaries, service height rules, and competition format adjustments.",
            "Equipment specifications (e.g., wheelchair camber, straps, prosthetics) and safety guidelines."
        ]
    },
    {
        "id": "strokes",
        "title": "Technical Stroke and Grip Modifications",
        "outline_template": [
            "Modifying grips (V-grip, thumb grip, short grip) to suit the physical capabilities of {name}.",
            "Adjusting contact points, swing trajectories, and biomechanics of overarm and underarm strokes.",
            "The role of the torso and non-racket arm in balancing and generating power."
        ]
    },
    {
        "id": "mobility",
        "title": "Footwork, Mobility, and Recovery Strategies",
        "outline_template": [
            "Adapting footwork, push-off, and movement patterns (e.g., wheelchair movement, hopping, step-close-step) for {name}.",
            "Base positioning, recovery pathways, and court coverage strategies on a modified court.",
            "Cardio-respiratory and muscular endurance conditioning tailored to mobility limitations."
        ]
    }
]

# 5. Children Maturation (7 specific topics)
children_maturation_topics = [
    {
        "id": "growth_spurts_physiology",
        "title": "Growth Spurts: Physiological Impact and Coordination Changes",
        "desc": "How children's physiological growth, skeletal changes, and muscle-tendon elongation during growth spurts impact motor control and coordination.",
        "outline": [
            "Understanding the physiological changes, bone growth, and muscle-tendon elongation during growth spurts.",
            "Managing the temporary loss of motor control and coordination (adolescent awkwardness).",
            "Adapting coaching expectations and feedback styles to maintain self-esteem and motivation."
        ]
    },
    {
        "id": "growth_spurts_injury",
        "title": "Growth Spurts: Injury Prevention and Training Load Management",
        "desc": "Preventing overuse injuries and managing physical stress in children undergoing rapid skeletal growth.",
        "outline": [
            "Identifying risks of overuse injuries (e.g., Osgood-Schlatter disease, Sever's disease) during rapid growth.",
            "Monitoring training volume, intensity, and active recovery periods.",
            "Implementing mobility, flexibility, and core stability exercises to support growing joints."
        ]
    },
    {
        "id": "phv_monitoring",
        "title": "PHV Adjustments: Peak Height Velocity Monitoring and Assessment",
        "desc": "Methods for measuring, calculating, and tracking Peak Height Velocity (PHV) to predict growth spurts in young players.",
        "outline": [
            "Methods for measuring and tracking standing height, sitting height, and arm span to estimate PHV.",
            "Establishing a systematic database for youth player growth monitoring.",
            "Communicating growth trends and physical adjustments to parents and athletic trainers."
        ]
    },
    {
        "id": "phv_training",
        "title": "PHV Adjustments: Designing Training Programs During Peak Height Velocity",
        "desc": "Designing training blocks and drills that match physical development during peak height velocity (PHV).",
        "outline": [
            "Adjusting coaching drills to prioritize agility, balance, and coordination over raw strength during PHV.",
            "Modifying shock-absorption training (e.g., lower jump landing heights) to protect developing skeletons.",
            "Periodization adjustments: shifting focus to technical refinement and tactical awareness during growth peaks."
        ]
    },
    {
        "id": "modified_rules_adaptation",
        "title": "Modified Rules: Adapting Game Structures and Match Play Rules for Children",
        "desc": "Adapting scoring systems, court layouts, and match formats for junior players to encourage participation.",
        "outline": [
            "Simplifying scoring systems (e.g., shorter games, play to 11 points) to match children's shorter attention spans.",
            "Adapting court dimensions (e.g., using half-courts or short lines) to make rallies achievable.",
            "Implementing team formats and collaborative games to foster a positive, social training atmosphere."
        ]
    },
    {
        "id": "modified_rules_benefits",
        "title": "Modified Rules: Educational and Tactical Benefits of Simplified Children's Rules",
        "desc": "How scaling down rules helps children develop spatial awareness, tactics, and long-term interest in the sport.",
        "outline": [
            "How modified rules accelerate the development of tactical awareness and court positioning in kids.",
            "Promoting cooperative rally-building over immediate winners to build baseline consistency.",
            "Psychological benefits: reducing competition-related anxiety and increasing confidence in basic skills."
        ]
    },
    {
        "id": "modified_equipment",
        "title": "Modified Equipment: Scaling Racket Size, Shuttle Speed, and Net Height for Youth Players",
        "desc": "Using child-appropriate racket weights, slower shuttles, and lower nets to establish correct habits.",
        "outline": [
            "Selecting racket lengths (e.g., 21 to 25 inches) based on a child's height and physical strength.",
            "Adjusting net heights to encourage flat and high trajectories suitable for smaller players.",
            "Utilizing slower plastic or sponge shuttlecocks to increase reaction time and success rates."
        ]
    }
]

def generate_all_topics():
    target_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics\Level_1"
    os.makedirs(target_dir, exist_ok=True)
    
    count = 0
    generated_names = set()
    
    # 1. Technical Skills (168 files)
    for tech in techniques:
        for dim in tech_dimensions:
            title = f"{tech['name']} - {dim['title']}"
            desc = f"An in-depth guide on the {dim['title'].lower()} of {tech['name'].lower()}. {tech['desc']}"
            outline = [line.format(name=tech['name']) for line in dim['outline_template']]
            
            short_name = f"{tech['id']}_{dim['id']}"
            short_name = sanitize_filename(short_name)
            filename = f"Topic_L1_{short_name}.md"
            
            filepath = os.path.join(target_dir, filename)
            
            content = f"[[Level_1]]\n\n"
            content += f"# {title}\n\n"
            content += f"{desc}\n\n"
            content += "## Structural Outline\n\n"
            for idx, pt in enumerate(outline, 1):
                content += f"{idx}. {pt}\n"
            content += "\n#llm-deep-backlog\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            generated_names.add(filename)
            count += 1

    # 2. Movements (64 files)
    for mov in movements:
        for dim in mov_dimensions:
            title = f"{mov['name']} - {dim['title']}"
            desc = f"An in-depth guide on the {dim['title'].lower()} of {mov['name'].lower()}. {mov['desc']}"
            outline = [line.format(name=mov['name']) for line in dim['outline_template']]
            
            short_name = f"{mov['id']}_{dim['id']}"
            short_name = sanitize_filename(short_name)
            filename = f"Topic_L1_{short_name}.md"
            
            filepath = os.path.join(target_dir, filename)
            
            content = f"[[Level_1]]\n\n"
            content += f"# {title}\n\n"
            content += f"{desc}\n\n"
            content += "## Structural Outline\n\n"
            for idx, pt in enumerate(outline, 1):
                content += f"{idx}. {pt}\n"
            content += "\n#llm-deep-backlog\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            generated_names.add(filename)
            count += 1

    # 3. Pedagogy (72 files)
    for ped_item in pedagogy:
        for dim in ped_dimensions:
            title = f"{ped_item['name']} - {dim['title']}"
            desc = f"An in-depth guide on the {dim['title'].lower()} of {ped_item['name'].lower()}. {ped_item['desc']}"
            outline = [line.format(name=ped_item['name']) for line in dim['outline_template']]
            
            short_name = f"{ped_item['id']}_{dim['id']}"
            short_name = sanitize_filename(short_name)
            filename = f"Topic_L1_{short_name}.md"
            
            filepath = os.path.join(target_dir, filename)
            
            content = f"[[Level_1]]\n\n"
            content += f"# {title}\n\n"
            content += f"{desc}\n\n"
            content += "## Structural Outline\n\n"
            for idx, pt in enumerate(outline, 1):
                content += f"{idx}. {pt}\n"
            content += "\n#llm-deep-backlog\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            generated_names.add(filename)
            count += 1

    # 4. Special Populations (24 files)
    for spec in special_populations:
        for dim in spec_dimensions:
            title = f"{spec['name']} - {dim['title']}"
            desc = f"An in-depth guide on the {dim['title'].lower()} of {spec['name'].lower()}. {spec['desc']}"
            outline = [line.format(name=spec['name']) for line in dim['outline_template']]
            
            short_name = f"{spec['id']}_{dim['id']}"
            short_name = sanitize_filename(short_name)
            filename = f"Topic_L1_{short_name}.md"
            
            filepath = os.path.join(target_dir, filename)
            
            content = f"[[Level_1]]\n\n"
            content += f"# {title}\n\n"
            content += f"{desc}\n\n"
            content += "## Structural Outline\n\n"
            for idx, pt in enumerate(outline, 1):
                content += f"{idx}. {pt}\n"
            content += "\n#llm-deep-backlog\n"
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            generated_names.add(filename)
            count += 1

    # 5. Children Maturation (7 files)
    for ch in children_maturation_topics:
        title = ch['title']
        desc = ch['desc']
        outline = ch['outline']
        
        short_name = ch['id']
        short_name = sanitize_filename(short_name)
        filename = f"Topic_L1_{short_name}.md"
        
        filepath = os.path.join(target_dir, filename)
        
        content = f"[[Level_1]]\n\n"
        content += f"# {title}\n\n"
        content += f"{desc}\n\n"
        content += "## Structural Outline\n\n"
        for idx, pt in enumerate(outline, 1):
            content += f"{idx}. {pt}\n"
        content += "\n#llm-deep-backlog\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        generated_names.add(filename)
        count += 1

    print(f"Total topics generated programmatically: {count}")
    print(f"Unique files written: {len(generated_names)}")
    
    # Assert check
    assert len(generated_names) == 335, f"Expected 335 files, but generated {len(generated_names)}"
    print("Verification passed! Exactly 335 unique files have been created.")

if __name__ == "__main__":
    generate_all_topics()
