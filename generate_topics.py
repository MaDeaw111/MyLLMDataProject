import os

# Define the 100 topics with title, description, and 3-point outline/questions
topics = [
    # Level 1 Basic Coaching & Pedagogy
    {
        "filename": "Topic_BWF_Coaching_Framework_Levels",
        "title": "BWF Coaching Framework Levels",
        "description": "Structure, progression, and entry requirements of BWF Coaching Certification Levels 1 through 4.",
        "outline": [
            "Structure and core competencies required at each certificate tier.",
            "Progression pathways and experience requirements between certification levels.",
            "Fast-track entry options for elite national and international players."
        ]
    },
    {
        "filename": "Topic_Coaching_Philosophy_Development",
        "title": "Coaching Philosophy Development",
        "description": "Defining, establishing, and articulating a personal coaching philosophy centered around player welfare and positive experiences.",
        "outline": [
            "Identifying personal coaching values, ethics, and developmental priorities.",
            "Balancing performance outcomes with long-term athlete retention and enjoyment.",
            "Translating written philosophy into daily practice during group and individual sessions."
        ]
    },
    {
        "filename": "Topic_Autocratic_vs_Democratic_Coaching",
        "title": "Autocratic vs. Democratic Coaching Styles",
        "description": "Differences, advantages, and context-specific applications of autocratic, democratic, and laissez-faire coaching styles.",
        "outline": [
            "Defining autocratic coaching and situations requiring directive, quick decision-making (e.g., safety, rapid drills).",
            "Defining democratic coaching and methods for empowering player decision-making and autonomy.",
            "Assessing player maturity levels to select the most appropriate coaching style."
        ]
    },
    {
        "filename": "Topic_Risk_Assessment_for_Badminton_Coaches",
        "title": "Risk Assessment for Badminton Coaches",
        "description": "Conducting court-side, equipment, environmental, and player risk assessments to ensure safe group management.",
        "outline": [
            "Pre-session inspection of court surfaces, netting, posts, and perimeter safety zones.",
            "Equipment safety checks for rackets, grip wear, shuttle safety, and wheelchair/prosthetic integrity.",
            "Creating emergency action plans and procedures for managing sudden player injury or illness."
        ]
    },
    {
        "filename": "Topic_VAK_Learning_Styles_in_Badminton",
        "title": "VAK Learning Styles in Badminton Coaching",
        "description": "Applying Visual, Auditory, and Kinesthetic (VAK) learning styles to enhance instruction and speed up skill acquisition.",
        "outline": [
            "Visual methods: Demonstrations, video loops, and graphic diagrams of court movement.",
            "Auditory methods: Precise technical cues, verbal rhythms, and interactive questioning.",
            "Kinesthetic methods: Guided physical manipulation, target drills, and proprioceptive exercises."
        ]
    },
    {
        "filename": "Topic_Methods_of_Developing_Skills",
        "title": "Methods of Developing Skills",
        "description": "Syllabus guidelines on shaping, chaining, and whole-part-whole methodologies for skill progression.",
        "outline": [
            "Shaping: Modifying the rules or equipment to gradually approximate the target technique.",
            "Chaining: Breaking down complex skills into sequential links and teaching them in forward/backward order.",
            "Whole-Part-Whole: Demonstrating the full movement, isolating a single link to practice, and reintegrating it."
        ]
    },
    {
        "filename": "Topic_Stages_of_Motor_Learning",
        "title": "Stages of Motor Learning in Badminton",
        "description": "Identifying and coaching players through the Cognitive, Associative, and Autonomous phases of motor skill acquisition.",
        "outline": [
            "Cognitive Phase: High mental demand, error identification, and structured, simplified feedback.",
            "Associative Phase: Refining movement patterns, reducing errors, and shifting to self-analysis.",
            "Autonomous Phase: Executing skills automatically with minimal cognitive load, allowing focus on tactics."
        ]
    },
    {
        "filename": "Topic_Growth_Spurt_Maturation_Impact",
        "title": "Growth Spurt Maturation Impact on Youth Players",
        "description": "Adapting training volume, intensity, and biomechanics for children undergoing peak height velocity.",
        "outline": [
            "Tracking physiological indicators of growth spurts (peak height velocity) in young players.",
            "Managing coordination loss (adolescent awkwardness) and adjusting motor control expectations.",
            "Preventing overuse injuries (e.g., Osgood-Schlatter disease) through workload management."
        ]
    },
    {
        "filename": "Topic_Adapting_Equipment_for_Children",
        "title": "Adapting Equipment and Court Dimensions for Children",
        "description": "Modifications of racket lengths, net heights, court boundaries, and shuttle types to suit young learners.",
        "outline": [
            "Racket length selection based on child height to prevent shoulder and wrist strain.",
            "Lowering nets and narrowing court boundaries to encourage rally length and correct stroke trajectories.",
            "Using slower shuttles (e.g., plastic or sponge) to increase reaction time and stroke success."
        ]
    },
    {
        "filename": "Topic_Positive_Benefits_of_Participation",
        "title": "Positive Benefits of Badminton Participation",
        "description": "Psychological, social, cardiovascular, and coordination benefits of lifelong badminton participation.",
        "outline": [
            "Cardiorespiratory adaptations and metabolic demands of regular badminton play.",
            "Development of hand-eye coordination, spatial awareness, and agility.",
            "Social-emotional development: Teamwork, sportsmanship, and stress reduction."
        ]
    },
    {
        "filename": "Topic_Role_and_Ethics_of_the_Coach",
        "title": "Role and Ethics of the Badminton Coach",
        "description": "Code of conduct, duty of care, ethical boundaries, and role-modelling responsibilities of a coach.",
        "outline": [
            "Maintaining professional boundaries, confidentiality, and fair play standards.",
            "Ensuring equal opportunity and inclusivity across all skill levels and backgrounds.",
            "Implementing safeguarding procedures and child protection guidelines."
        ]
    },
    {
        "filename": "Topic_Observation_and_Analysis_Methodology",
        "title": "Observation and Analysis Methodology",
        "description": "Techniques for structured diagnostic observation to analyze and improve player technical biomechanics.",
        "outline": [
            "Positioning the coach relative to the player (side, front, back) for optimal viewing angle.",
            "Focusing on the movement sequence: Stance, preparation, hitting phase, and recovery.",
            "Isolating primary technical errors from secondary adaptation errors."
        ]
    },
    {
        "filename": "Topic_Session_Planning_Basics",
        "title": "Session Planning Basics",
        "description": "Structuring a single 60-to-90 minute session (warm-up, technical/tactical main body, cool-down) with clear objectives.",
        "outline": [
            "Formulating SMART session objectives aligned with player progression goals.",
            "Allocating time dynamically across activation, technique, tactical application, and recovery.",
            "Self-evaluating and documenting session outcomes to guide future planning."
        ]
    },
    {
        "filename": "Topic_Goal_Setting_for_Beginners",
        "title": "Goal Setting for Beginners",
        "description": "Introducing basic goal-setting strategies (process vs. outcome) to keep novice players motivated and focused.",
        "outline": [
            "Teaching beginners to focus on process goals (e.g., split-step timing) rather than match scores.",
            "Setting short-term, achievable technical benchmarks to build self-efficacy.",
            "Establishing collaborative coach-player goal agreements."
        ]
    },
    {
        "filename": "Topic_Face_to_Face_Communication",
        "title": "Face-to-Face Communication",
        "description": "Using verbal clarity, active listening, and body language to deliver instructions effectively on court.",
        "outline": [
            "Minimizing instruction time (keeping it under 2 minutes) to maximize active player movement.",
            "Using voice projection, pitch, and modulation to maintain player attention in noisy hall environments.",
            "Checking for understanding through body language observation and active listening."
        ]
    },
    {
        "filename": "Topic_Questioning_Techniques_for_Coaches",
        "title": "Questioning Techniques for Coaches",
        "description": "Using open, closed, and guided discovery questions to promote critical thinking and player autonomy.",
        "outline": [
            "Replacing directive feedback with open questions (e.g., 'Where was your weight balanced during that lunge?').",
            "Using closed questions for rapid verification of rules or safety rules.",
            "Encouraging players to self-diagnose technical mistakes through guided questioning."
        ]
    },
    {
        "filename": "Topic_Effective_Feedback_Delivery",
        "title": "Effective Feedback Delivery",
        "description": "Balancing intrinsic/extrinsic feedback, positive reinforcement, and corrective instruction.",
        "outline": [
            "Understanding the difference between intrinsic (felt by player) and extrinsic (provided by coach) feedback.",
            "Timing feedback: Intermittent vs. terminal feedback to avoid cognitive overload.",
            "Structuring corrective feedback: Praise-Correction-Praise (the feedback sandwich) technique."
        ]
    },
    {
        "filename": "Topic_Demonstration_Best_Practices",
        "title": "Demonstration Best Practices",
        "description": "Setting up, executing, and breaking down a demonstration so that key technical cues are visible and memorable.",
        "outline": [
            "Ensuring all players can see the demonstration clearly without looking into glare or background noise.",
            "Isolating 1-2 key technical checkpoints during the demo (e.g., 'Watch the racket head angle').",
            "Using full-speed and slow-motion variations of the movement to aid cognitive mapping."
        ]
    },
    {
        "filename": "Topic_Group_Management_and_Safety",
        "title": "Group Management and Safety on Court",
        "description": "Organizing player rotations, queue lines, and drills to maximize hits while maintaining court safety.",
        "outline": [
            "Designing safety spacing rules for players waiting off-court during high-speed drills.",
            "Using station-based training to keep large groups active with limited court space.",
            "Managing safety transitions between drills (e.g., shuttle clearing, water breaks)."
        ]
    },
    {
        "filename": "Topic_Designing_Progressive_Practices",
        "title": "Designing Progressive Practices",
        "description": "Structuring drills to move from closed, highly predictable settings to open, random, and game-like situations.",
        "outline": [
            "Closed drills: Developing technical consistency without environmental variation.",
            "Semi-open drills: Introducing choices or simple patterns (e.g., feed to net or deep).",
            "Open drills: Simulating match-like conditions with random feeding and tactical choices."
        ]
    },
    {
        "filename": "Topic_Racket_Feeding_Multi_Feed",
        "title": "Racket Feeding Multi-Feed Techniques",
        "description": "Mastering the grip, body position, speed, and accuracy needed for continuous multi-shuttle racket feeding.",
        "outline": [
            "Hand placement, grip variation, and body stance for high-volume racket feeding.",
            "Controlling shuttle height, speed, spin, and depth to isolate specific technical targets.",
            "Rhythm and timing of feeding to simulate specific match tempos."
        ]
    },
    {
        "filename": "Topic_Racket_Feeding_Rallying",
        "title": "Racket Feeding Rallying Techniques",
        "description": "Using cooperative rallies to feed shuttles, allowing players to practice in a continuous, realistic rhythm.",
        "outline": [
            "Controlling shot placement and pace during active rallies to match the player's development level.",
            "Using directional changes to transition players from static hitting to dynamic movement.",
            "Gradually shifting from cooperative rallying to competitive pressure within the drill."
        ]
    },
    {
        "filename": "Topic_Hand_Feeding_Underarm",
        "title": "Underarm Hand Feeding Techniques",
        "description": "Developing accuracy and correct ballistics for low, underarm hand feeds at the net.",
        "outline": [
            "Body stance, court position, and safety spacing relative to the hitting player.",
            "Flick action, release height, and targeting to simulate tight net shots.",
            "Modifying feed height and velocity to train forward lunging and racket acceleration."
        ]
    },
    {
        "filename": "Topic_Hand_Feeding_Overarm",
        "title": "Overarm Hand Feeding Techniques",
        "description": "Delivering high, deep, or flat overarm hand feeds to train rearcourt and midcourt strokes.",
        "outline": [
            "Throwing mechanics and release angles for deep, high-lob feeds.",
            "Feeding flat, high-speed overarm lobs to simulate attacking drives and smashes.",
            "Developing accuracy and consistency in landing zones to ensure repetitive, high-quality practice."
        ]
    },
    {
        "filename": "Topic_Flat_Fast_Feeding",
        "title": "Flat Fast Feeding Techniques",
        "description": "Feeding flat, high-speed shuttles to train defensive blocks, midcourt drives, and fast transitions.",
        "outline": [
            "Grip adjustments and racket angles to feed fast, flat drives continuously.",
            "Targeting the player's hip, shoulder, and center line to build defensive reaction speed.",
            "Varying feed intervals to challenge recovery footwork and grip transitions."
        ]
    },

    # Technical Skills / Hitting & Footwork (L1 & L2)
    {
        "filename": "Topic_The_Split_Step_Mechanism",
        "title": "The Split-Step Mechanism",
        "description": "Biomechanical analysis, timing relative to opponent contact, and stance parameters of the split-step.",
        "outline": [
            "Timing the split-step jump: Landing just after the opponent strikes the shuttle.",
            "Stance width, knee flexion angle, and vertical center-of-gravity displacement.",
            "The elastic energy storage phase (pre-stretch) and transition to directional acceleration."
        ]
    },
    {
        "filename": "Topic_Badminton_V_Grip",
        "title": "The Badminton V-Grip",
        "description": "Hand placement, finger spacing, bevel alignment, and usage of the default forehand V-grip.",
        "outline": [
            "Aligning the 'V' shape of the thumb and index finger with the handle bevels.",
            "Finger spacing and relaxation on the grip to allow maximum wrist snap and control.",
            "Transitioning from a relaxed grip during preparation to a tight squeeze at the point of impact."
        ]
    },
    {
        "filename": "Topic_Thumb_Grip_for_Backhand",
        "title": "The Thumb Grip for Backhand",
        "description": "Applying the thumb flat against the wide handle bevel for backhand serves, net shots, and midcourt defense.",
        "outline": [
            "Placing the thumb pad along the wide bevel of the racket handle.",
            "Using the thumb as a lever to create push force during short backhand swings.",
            "Modifying thumb placement for late backhand contacts or cross-court returns."
        ]
    },
    {
        "filename": "Topic_Corner_Grip_Transition",
        "title": "The Corner Grip Transition",
        "description": "Hand positioning and applications of the corner (bevel) grip for backhand overheads and angled slices.",
        "outline": [
            "Locating the bevels on the handle to position the thumb on the diagonal corner.",
            "Enabling arm pronation/supination comfort for overhead backhand clearances.",
            "Applying the corner grip to generate cross-court angles from the forecourt."
        ]
    },
    {
        "filename": "Topic_Panhandle_Grip_Applications",
        "title": "The Panhandle Grip",
        "description": "Hand placement and specific stroke contexts (net kills, late forehand drives) for the panhandle grip.",
        "outline": [
            "Rotating the handle 90 degrees to place the thumb pad on the narrow side bevel.",
            "Applying the panhandle grip for over-the-net kills to generate steep downward angles.",
            "Limitations of the panhandle grip for high-clearance overhead strokes."
        ]
    },
    {
        "filename": "Topic_Backhand_Low_Serve",
        "title": "The Backhand Low Serve",
        "description": "Stance, racket preparation, shuttle holding, push technique, and trajectory control.",
        "outline": [
            "Stance alignment, weight distribution, and forward lean at the service line.",
            "Holding the shuttle by a single feather between thumb and index finger to avoid feather deflection.",
            "The short, guided push stroke: Minimizing backswing and controlling height over the tape."
        ]
    },
    {
        "filename": "Topic_Forehand_High_Serve",
        "title": "The Forehand High Serve",
        "description": "Stance, backswing, kinetic sequence, release, and high, deep landing criteria.",
        "outline": [
            "Stance width, side-facing orientation, and weight transfer from back to front foot.",
            "Shuttle release timing and loop swing path of the racket.",
            "Forearm pronation and wrist snap to achieve deep, vertical landing trajectories."
        ]
    },
    {
        "filename": "Topic_Backhand_Flick_Serve",
        "title": "The Backhand Flick Serve",
        "description": "Maintaining identical setup to the low serve, with sudden acceleration to surprise the opponent.",
        "outline": [
            "Disguising the serve: Ensuring the backswing matches the low serve precisely.",
            "Rapid wrist and thumb acceleration at contact to push the shuttle deep.",
            "Tactical deployment: Exploiting opponent anticipation and forward weight bias."
        ]
    },
    {
        "filename": "Topic_Forehand_Flick_Serve",
        "title": "The Forehand Flick Serve",
        "description": "Swing modifications, wrist snap, and tactical usage of the forehand flick serve.",
        "outline": [
            "Establishing the forehand high-serve stance but decelerating the initial swing.",
            "Sudden wrist flick and racket acceleration to change trajectory from low to high-deep.",
            "Tactical target areas in singles and doubles play."
        ]
    },
    {
        "filename": "Topic_Forehand_and_Backhand_Net_Shots",
        "title": "Forehand and Backhand Net Shots",
        "description": "Biomechanics, racket angle, and rebound control for tight net play.",
        "outline": [
            "Lunge timing, racket leg stabilization, and extended-arm reach.",
            "Racket head tilt and grip pressure variation to generate tumble or clean spin.",
            "Tactical recovery stance and anticipation of net-retaliation patterns."
        ]
    },
    {
        "filename": "Topic_Forehand_and_Backhand_Net_Lifts",
        "title": "Forehand and Backhand Net Lifts",
        "description": "Biomechanical differences between defensive lifts and offensive flick lifts.",
        "outline": [
            "Under-shuttle racket path and follow-through variation for high defensive clearances.",
            "Offensive flick lifts: Short, sudden wrist acceleration to clear over a net-rushing opponent.",
            "Stabilizing the trunk to maintain lift accuracy under pressure."
        ]
    },
    {
        "filename": "Topic_Forehand_and_Backhand_Net_Kills",
        "title": "Forehand and Backhand Net Kills",
        "description": "Grip transitions, shortened swing arcs, and steep downward angles for net kills.",
        "outline": [
            "Panhandle (forehand) and thumb (backhand) grip adjustments for high net contacts.",
            "Shortening the swing path: Using index finger/thumb snap to avoid net touch violations.",
            "Footwork timing: Landing the racket foot simultaneously with racket contact."
        ]
    },
    {
        "filename": "Topic_Midcourt_Drives_FH_BH",
        "title": "Midcourt Drives (Forehand & Backhand)",
        "description": "Flat, high-speed midcourt exchanges: Grip, elbow lead, and body rotation.",
        "outline": [
            "Led by the elbow: Correct racket preparation and forearm rotation path.",
            "Stance parameters: Wide base, lowered center of gravity, and active footwork.",
            "Grip transitions: Switching between forehand V-grip and thumb-grip at high speed."
        ]
    },
    {
        "filename": "Topic_Forehand_Clear_Biomechanics",
        "title": "Forehand Clear Biomechanics",
        "description": "Kinetic sequence of overhead clearing, forearm pronation, and contact point alignment.",
        "outline": [
            "Kinetic chain: Leg push, hip rotation, trunk arch, shoulder rotation, and forearm pronation.",
            "Contact point: Hitting the shuttle slightly in front of the body at maximum extension.",
            "Pronation and follow-through: Pronating the forearm to generate clean power and recovery."
        ]
    },
    {
        "filename": "Topic_Forehand_Dropshot_Slices",
        "title": "Forehand Dropshot Slices",
        "description": "Racket angle adjustments, slicing contact, and deceleration mechanics for drop shots.",
        "outline": [
            "Creating technical disguise: Maintaining identical swing speeds to clears and smashes.",
            "Racket face angle modifications to slice (shear) the shuttle for cross-court control.",
            "Supination and wrist control to decelerate racket-to-shuttle impulse."
        ]
    },
    {
        "filename": "Topic_Forehand_Smash_Angles",
        "title": "Forehand Smash Angles and Power",
        "description": "Optimizing smash power through abdominal rotation, forearm pronation, and downward contact angles.",
        "outline": [
            "Maximizing vertical reach and forward jump to create steep downward angles.",
            "Shoulder-hip separation angle and core contraction to transfer elastic energy.",
            "Wrist and index finger snap at contact for maximum shuttle velocity."
        ]
    },
    {
        "filename": "Topic_Backhand_Clear_Struggles",
        "title": "Backhand Clear Technique and Mechanics",
        "description": "Common errors and correct biomechanical sequence for the overhead backhand clear.",
        "outline": [
            "Body positioning: Rotating the shoulders to face the back wall during preparation.",
            "Grip and arm alignment: Bevel/corner grip usage and elbow extension lead.",
            "Forearm supination: The critical speed-generating mechanism prior to contact."
        ]
    },
    {
        "filename": "Topic_Backhand_Dropshot_Deceleration",
        "title": "Backhand Dropshot Deceleration",
        "description": "Finesse, slicing angles, and racket control for overhead backhand drop shots.",
        "outline": [
            "Matching preparation to the backhand clear to maintain tactical disguise.",
            "Adjusting the racket face at contact to slice the shuttle, reducing forward velocity.",
            "Grip pressure release to absorb energy on contact."
        ]
    },
    {
        "filename": "Topic_Forehand_Pulled_Dropshot",
        "title": "Forehand Pulled Dropshot",
        "description": "Executing late angle changes (pulled drop shots) from the rear court.",
        "outline": [
            "Holding the shot: Delaying contact to freeze opponent split-step timing.",
            "Adjusting the racket face at the last millisecond to 'pull' the shuttle cross-court.",
            "Managing balance and recovery stance during late contact."
        ]
    },
    {
        "filename": "Topic_Base_Position_and_Recovery",
        "title": "Base Position and Recovery Dynamics",
        "description": "Concept of the 'center of probability' and footwork recovery paths after hitting.",
        "outline": [
            "Defining base position dynamically based on shot quality rather than physical court center.",
            "Recovery mechanics: Initial push-off and cross-over steps back to the active base.",
            "Anticipating opponent options to adjust the positioning of the base."
        ]
    },

    # Level 2 Training Planning & Sports Science
    {
        "filename": "Topic_Coaching_Process_Overview",
        "title": "The Coaching Process Cycle",
        "description": "Syllabus guidelines on the cycle of planning, delivering, reviewing, and evaluating coaching performance.",
        "outline": [
            "Integrating planning diagnostics with player-specific profile data.",
            "Methods of delivery: Adapting styles and drills dynamically based on real-time review.",
            "Review and evaluation: Methods of self-reflection, player feedback, and data logging."
        ]
    },
    {
        "filename": "Topic_Macrocycles_in_Badminton",
        "title": "Macrocycles in Badminton Periodization",
        "description": "Designing annual training plans, structuring preparatory, competitive, and transition macrocycles.",
        "outline": [
            "Establishing peak performance dates aligned with major tournaments.",
            "Distributing physical, technical, and tactical volumes across the annual cycle.",
            "Structuring macrocycle transition phases to ensure complete physical regeneration."
        ]
    },
    {
        "filename": "Topic_Mesocycles_for_Competition",
        "title": "Mesocycles for Competition Preparation",
        "description": "Structuring 4-to-6 week mesocycles to transition players from general fitness to tournament-specific sharpness.",
        "outline": [
            "General preparatory mesocycles: High volume, low intensity, focus on base fitness.",
            "Specific preparatory mesocycles: Transitioning to sport-specific movements and tactics.",
            "Competitive mesocycles: Low volume, high intensity, prioritizing speed, tactics, and recovery."
        ]
    },
    {
        "filename": "Topic_Microcycles_Weekly_Planning",
        "title": "Microcycles and Weekly Training Load",
        "description": "Structuring daily training volumes, intensities, recovery protocols, and tapering methods within a 7-day cycle.",
        "outline": [
            "Planning training load distribution (peaks and troughs) to avoid overreaching.",
            "Integrating technical sessions, weight training, cardiorespiratory workouts, and active recovery.",
            "Tapering microcycles: Reducing volume while maintaining intensity prior to match days."
        ]
    },
    {
        "filename": "Topic_Aerobic_Endurance_for_Badminton",
        "title": "Aerobic Endurance for Badminton",
        "description": "Developing cardiorespiratory base fitness, aerobic threshold, and long-term energy pathways.",
        "outline": [
            "The role of aerobic base fitness in accelerating recovery between high-intensity rallies.",
            "Methods: Continuous low-intensity training vs. extensive aerobic intervals on and off court.",
            "Monitoring adaptations using resting heart rate and submaximal exercise parameters."
        ]
    },
    {
        "filename": "Topic_Anaerobic_Lactic_System",
        "title": "Anaerobic Lactic System Conditioning",
        "description": "Conditioning players to tolerate lactate accumulation and maintain speed during long, high-intensity rallies.",
        "outline": [
            "Physiology of anaerobic glycolysis and lactate accumulation in working muscles.",
            "Training protocols: Multi-shuttle drills at maximum speed lasting 30-90 seconds with incomplete recovery.",
            "Developing psychological tolerance and movement efficiency under high acidosis."
        ]
    },
    {
        "filename": "Topic_Anaerobic_Alactic_System",
        "title": "Anaerobic Alactic System Development",
        "description": "Developing explosive power, maximum acceleration, and ATP-CP recovery mechanisms.",
        "outline": [
            "Physiology of the ATP-CP (phosphagen) energy pathway during short bursts under 10 seconds.",
            "Training protocols: High-speed agility starts, maximum-effort jumps, and short multi-shuttle bursts.",
            "Ensuring complete recovery (work-to-rest ratio of 1:6 or higher) to target alactic power."
        ]
    },
    {
        "filename": "Topic_Strength_Training_Periodization",
        "title": "Strength Training Periodization",
        "description": "Structuring strength development from hypertrophy and basic strength to explosive power and court agility.",
        "outline": [
            "Hypertrophy/anatomical adaptation phase: Building tendon stiffness and muscular balance.",
            "Maximum strength phase: Developing absolute force production using compound multi-joint movements.",
            "Power/conversion phase: Translating maximum strength into rate of force development (RFD) using plyometrics."
        ]
    },
    {
        "filename": "Topic_Speed_and_Agility_Drills",
        "title": "Speed and Agility Development",
        "description": "Drill design, acceleration/deceleration biomechanics, and reactive agility drills.",
        "outline": [
            "Deceleration mechanics: Lowering center of gravity, foot angle, and eccentric quadriceps strength.",
            "Closed agility drills (e.g., star footwork patterns) vs. open reactive agility (responding to visual feeds).",
            "Linear speed vs. multidirectional court speed adaptations."
        ]
    },
    {
        "filename": "Topic_Flexibility_and_Injury_Prevention",
        "title": "Flexibility and Range of Motion Training",
        "description": "Applying static, dynamic, and Proprioceptive Neuromuscular Facilitation (PNF) stretching protocols.",
        "outline": [
            "Dynamic stretching protocols during warm-ups to optimize muscle temperature and joint lubrication.",
            "Static and PNF stretching post-session to develop long-term joint flexibility and muscle length.",
            "Targeting key areas: Shoulder joint capsule, hip flexors, hamstrings, and gastrocnemius."
        ]
    },
    {
        "filename": "Topic_Nutrition_for_Badminton_Players",
        "title": "Nutrition for Badminton Players",
        "description": "Pre-competition carbohydrate loading, hydration, electrolyte balance, and post-match recovery nutrition.",
        "outline": [
            "Macronutrient ratios for high-volume training: Prioritizing glycogen replenishment.",
            "Pre-, during-, and post-match hydration schedules: Calculating fluid loss and electrolyte needs.",
            "Post-match nutrition window: Protein-carbohydrate co-ingestion for muscle tissue repair."
        ]
    },
    {
        "filename": "Topic_RICE_Protocol_for_Injuries",
        "title": "Acute Injury Management (R.I.C.E. Protocol)",
        "description": "Immediate court-side management of soft tissue injuries (sprains, strains) using the Rest, Ice, Compression, Elevation protocol.",
        "outline": [
            "Rest: Safely removing the player from court and immobilization of the injured joint/limb.",
            "Ice & Compression: Application criteria, duration, and safety limits to control localized swelling.",
            "Elevation: Proper height relative to heart level to assist lymphatic drainage."
        ]
    },
    {
        "filename": "Topic_The_5_Cs_in_Sports_Psychology",
        "title": "The 5 Cs in Sports Psychology",
        "description": "Applying Commitment, Communication, Concentration, Control, and Confidence to player development.",
        "outline": [
            "Commitment: Setting process-oriented milestones and maintaining intrinsic motivation.",
            "Concentration & Control: Techniques for visual focus, cue filtering, and regulating emotional arousal.",
            "Confidence: Building self-efficacy through technical mastery and structured mental rehearsal."
        ]
    },
    {
        "filename": "Topic_Motivational_Cues_in_Coaching",
        "title": "Motivational Cues in Coaching",
        "description": "Using positive reinforcement, autonomy support, and task-oriented climate cues.",
        "outline": [
            "Establishing a task-oriented motivational climate (valuing effort and learning) vs. ego-oriented climate.",
            "Providing autonomy support: Involving players in session decision-making and goal reviews.",
            "Selecting verbal and non-verbal cues that build player self-determination."
        ]
    },
    {
        "filename": "Topic_Goal_Setting_for_Elites",
        "title": "Goal Setting for Elite Players",
        "description": "Structuring outcome, performance, and process goals for national and international competition prep.",
        "outline": [
            "Aligning long-term outcome goals (e.g., tournament ranking) with medium-term performance benchmarks.",
            "Isolating micro-process goals during match play to reduce cognitive anxiety and maintain tactical focus.",
            "Systematic review, adjustment, and documentation of elite goal profiles."
        ]
    },
    {
        "filename": "Topic_Performance_Analysis_Tools",
        "title": "Performance Analysis Tools",
        "description": "Using video analysis, notation templates, and physical metrics to track player development.",
        "outline": [
            "Designing notation templates to track unforced error types, serve return patterns, and rally length.",
            "Using video analysis to diagnose biomechanical faults in slow motion.",
            "Correlating technical-tactical statistics with physical data (heart rate, movement speed)."
        ]
    },
    {
        "filename": "Topic_Inclusivity_in_Badminton",
        "title": "Inclusivity in Badminton",
        "description": "Designing coaching sessions that accommodate diverse ages, genders, skill levels, and physical profiles.",
        "outline": [
            "Differentiating exercises within the same session using progression and regression steps.",
            "Overcoming gender bias and promoting equal access in squad training setups.",
            "Building social cohesion through cooperative group challenges on court."
        ]
    },
    {
        "filename": "Topic_Motor_Skills_Classification",
        "title": "Motor Skills Classification",
        "description": "Syllabus guidelines on open, closed, discrete, continuous, and serial motor skills.",
        "outline": [
            "Classifying badminton technical movements: Closed skills (high serve) vs. open skills (defensive block).",
            "Analyzing serial skills (e.g., split-step to lunge to hit to recovery) as linked discrete elements.",
            "Structuring practice progressions based on skill classification."
        ]
    },
    {
        "filename": "Topic_Ability_vs_Potential",
        "title": "Ability vs. Potential",
        "description": "Distinguishing current motor skill ability from long-term developmental potential in talent identification.",
        "outline": [
            "Defining current ability as current performance metrics influenced by past training volume.",
            "Identifying indicators of potential: Coordination adaptability, kinesthetic awareness, and trainability.",
            "Avoiding selection bias toward early-maturing youth players."
        ]
    },
    {
        "filename": "Topic_Youth_Development_Pathways",
        "title": "Youth Development Pathways",
        "description": "Long-Term Athlete Development (LTAD) frameworks applied specifically to badminton.",
        "outline": [
            "Stages of LTAD: Active Start, FUNdamentals, Learning to Train, and Training to Train.",
            "Prioritizing multilateral physical development (agility, balance, coordination) in early childhood.",
            "Determining transition ages for technical specialization and high-volume training."
        ]
    },

    # Biomechanics & Sports Medicine (L2 & L3)
    {
        "filename": "Topic_Biomechanics_of_Lunging",
        "title": "Biomechanics of Lunging",
        "description": "Kinematics and kinetics of forward and lateral lunging: Ankle alignment, knee angle, and deceleration forces.",
        "outline": [
            "Analyzing heel-strike landing, knee angle alignment (avoiding valgus collapse), and ankle stability.",
            "Pelvic tilt control and core engagement to maintain center of gravity within the base of support.",
            "Eccentric muscle force requirements of the quadriceps and gluteals during the braking phase."
        ]
    },
    {
        "filename": "Topic_Forearm_Pronation_and_Supination",
        "title": "Forearm Pronation and Supination",
        "description": "Biomechanical analysis of forearm rotation in generating racket head speed for smashes and backhand clearances.",
        "outline": [
            "Pronation mechanics: Rapid inward rotation of the forearm to drive forehand smashes and clears.",
            "Supination mechanics: Outward rotation of the forearm to generate power for backhand clears and drives.",
            "Timing the grip squeeze at the end-range of rotation to transfer maximum velocity."
        ]
    },
    {
        "filename": "Topic_Kinetic_Chain_in_Overhead_Strokes",
        "title": "Kinetic Chain in Overhead Strokes",
        "description": "The sequential transfer of force from ground contact, through the lower limbs, hips, core, shoulder, to the racket.",
        "outline": [
            "Ground reaction force generation: The leg push phase off the rear foot.",
            "Rotational torque transfer: Hip rotation leading thoracic rotation, leading shoulder elevation.",
            "Proximal-to-distal sequencing: Unleashing the shoulder, elbow, forearm, and wrist in a whip-like motion."
        ]
    },
    {
        "filename": "Topic_Footwork_Traveling_Movements",
        "title": "Footwork Traveling Movements",
        "description": "Biomechanical parameters of the chassé step, running step, and cross-over footwork.",
        "outline": [
            "Chassé step: Stride parameters, lateral movement efficiency, and maintaining a level head height.",
            "Cross-over step: Fast recovery and deep corner coverage biomechanics.",
            "Running step: Application in forward net rushes and diving recoveries."
        ]
    },
    {
        "filename": "Topic_Tactical_Patterns_in_Singles",
        "title": "Tactical Patterns in Singles",
        "description": "Exploiting space, using the four corners, change of pace, and targeting player weaknesses.",
        "outline": [
            "Using deep, high clears and tight net drops to maximize opponent court coverage distance.",
            "Attacking tactics: Using half-smashes and sliced drop shots to draw weak returns.",
            "Defensive tactics: Flat counter-clears and cross-court lifts to neutralize attacking pressure."
        ]
    },
    {
        "filename": "Topic_Tactical_Patterns_in_Doubles",
        "title": "Tactical Patterns in Doubles",
        "description": "Attacking and defending rotations, communication, side-by-side defense, and front-and-back attack.",
        "outline": [
            "Transitioning from side-by-side (defensive) to front-and-back (offensive) formations.",
            "Attacking zones: Targeting the midcourt area and the seam between defenders.",
            "Defensive adjustments: Using low blocks and drives to counter aggressive smashes."
        ]
    },
    {
        "filename": "Topic_Mixed_Doubles_Specific_Tactics",
        "title": "Mixed Doubles Specific Tactics",
        "description": "Formations, male player court coverage, female player net dominance, and tactical target zones.",
        "outline": [
            "Female player positioning: Domination of the T-line, hunting net kills, and intercepting drives.",
            "Male player positioning: Deep court coverage, continuous smash generation, and court movement.",
            "Tactical matchups: Attacking the opponent's female player in the rear court or pushing the male player wide."
        ]
    },
    {
        "filename": "Topic_Heart_Rate_Monitoring",
        "title": "Heart Rate Monitoring in Training",
        "description": "Using heart rate zones to monitor training intensity, aerobic conditioning, and player recovery.",
        "outline": [
            "Determining individual maximum and resting heart rates for cardiorespiratory zone calculations.",
            "Designing specific conditioning drills targeting anaerobic threshold zones.",
            "Using heart rate recovery (HRR) times after high-intensity intervals to assess fitness levels."
        ]
    },
    {
        "filename": "Topic_Overtraining_and_Burnout",
        "title": "Overtraining and Burnout Prevention",
        "description": "Identifying physiological, psychological, and performance markers of chronic fatigue in competitive players.",
        "outline": [
            "Physiological indicators: Elevated resting heart rate, sleep disruption, and chronic muscle soreness.",
            "Psychological markers: Loss of motivation, mood changes, and decreased concentration.",
            "Implementing recovery microcycles and workload monitoring (acute-to-chronic workload ratio)."
        ]
    },
    {
        "filename": "Topic_Thoracic_Spine_Mobility",
        "title": "Thoracic Spine Mobility",
        "description": "Relevance of thoracic rotation and extension for generating overhead power and preventing shoulder/lower back injuries.",
        "outline": [
            "Anatomy of thoracic rotation vs. lumbar stability during high-speed twists.",
            "Assessment protocols (e.g., Seated Trunk Rotation) and identifying mobility blocks.",
            "Mobility exercises: Foam rolling, thread-the-needle, and open-book stretches."
        ]
    },
    {
        "filename": "Topic_Ankle_Sprains_Rehabilitation",
        "title": "Ankle Sprains Rehabilitation",
        "description": "Rehabilitation phases, progressive balance, proprioceptive training, and lateral stability exercises.",
        "outline": [
            "Phase 1: Pain management, inflammation reduction, and gentle range-of-motion drills.",
            "Phase 2: Proprioceptive retraining using wobble boards, balance pads, and single-leg stances.",
            "Phase 3: Returning to court: Agility work, jump landings, and lunging control."
        ]
    },
    {
        "filename": "Topic_Patellar_Tendinopathy_Jumper_Knee",
        "title": "Patellar Tendinopathy (Jumper's Knee)",
        "description": "Biomechanics, prevention, eccentric quadriceps loading, and landing stabilization.",
        "outline": [
            "Analyzing patellar tendon loading during deep landing lunges and jumps.",
            "Eccentric rehabilitation: Decline squats and leg press protocols to stimulate tendon remodeling.",
            "Landing mechanics: Soft knee bend, pelvic alignment, and core bracing."
        ]
    },
    {
        "filename": "Topic_Rotator_Cuff_Strengthening",
        "title": "Rotator Cuff Strengthening",
        "description": "Shoulder stability biomechanics, strengthening internal/external rotators, and preventing impingement.",
        "outline": [
            "Anatomy of the rotator cuff muscles (SITS) in stabilizing the humeral head during smashes.",
            "Identifying shoulder impingement risks from repetitive, high-speed overhead swings.",
            "Rehab exercises: Band-resisted external rotation, internal rotation, and scapular control drills."
        ]
    },
    {
        "filename": "Topic_Core_Stability_for_Badminton",
        "title": "Core Stability for Badminton",
        "description": "Pelvic alignment, anti-rotation core strength, and power transfer during airborne jumps.",
        "outline": [
            "Developing anti-rotation and anti-extension core strength to protect the lower back.",
            "Core activation during jumps: Transferring force from lower to upper body during the smash.",
            "Practical exercises: Planks, bird-dogs, Pallof presses, and medicine ball throws."
        ]
    },
    {
        "filename": "Topic_Hydration_and_Electrolytes",
        "title": "Hydration and Electrolyte Replacement",
        "description": "Calculating sweat rate, fluid replacement guidelines, and managing sodium/potassium balance.",
        "outline": [
            "Conducting sweat-rate testing: Weighing players before and after high-intensity sessions.",
            "Electrolyte concentration: The importance of sodium in preventing cramping and dehydration.",
            "Formulating pre-match, match-day, and post-match fluid replacement plans."
        ]
    },

    # Level 3 High Performance & Elite Preparation
    {
        "filename": "Topic_Elite_Player_Pathways",
        "title": "Elite Player Pathways",
        "description": "Talent identification frameworks, national development pipelines, and transitioning to professional squads.",
        "outline": [
            "Designing national and regional talent identification and development models.",
            "Managing key transitions: Moving from youth to senior elite performance settings.",
            "Collaborating across multi-disciplinary teams (coaches, sports scientists, medical staff)."
        ]
    },
    {
        "filename": "Topic_Talent_Identification_Tests",
        "title": "Talent Identification Testing Batteries",
        "description": "Testing physical, psychological, and technical attributes of prospective elite youth players.",
        "outline": [
            "Physical tests: Assessing agility (T-test), anaerobic capacity, and sprint speed.",
            "Technical evaluation: Assessing motor adaptability, hand-eye coordination, and spatial awareness.",
            "Psychological screening: Evaluating mental toughness, motivation, and coachability."
        ]
    },
    {
        "filename": "Topic_High_Performance_Planning",
        "title": "High Performance Planning",
        "description": "Designing multi-year plans, managing Olympic/Paralympic cycles, and peaking strategies.",
        "outline": [
            "Structuring quadrennial plans for Olympic and World Championship cycles.",
            "Managing travel, acclimatization, and competition schedules to avoid player fatigue.",
            "Double-periodization strategies: Peaking twice in a single calendar year."
        ]
    },
    {
        "filename": "Topic_Match_Analysis_and_Scouting",
        "title": "Match Analysis and Scouting Reports",
        "description": "Conducting opponent video analysis, tagging shots, mapping court movements, and formulating game plans.",
        "outline": [
            "Systematic video coding: Recording serve placement, return preferences, and unforced error zones.",
            "Synthesizing opponent profiles: Identifying movement limitations and tactical weaknesses.",
            "Creating clear, actionable scout reports for elite players."
        ]
    },
    {
        "filename": "Topic_Strategy_Formulation_in_Matches",
        "title": "Strategy Formulation in Matches",
        "description": "Adapting game plans during high-pressure matches based on tactical observation.",
        "outline": [
            "Identifying opponent pattern changes (e.g., shifting service targets) early in the match.",
            "Formulating mid-match adjustments: Modifying speed, shot height, and rally length.",
            "Mentally preparing the player to execute tactical changes under pressure."
        ]
    },
    {
        "filename": "Topic_Coaching_in_Competition_Intervals",
        "title": "Coaching in Competition Intervals",
        "description": "Delivering high-impact, concise, 1-minute tactical advice during the 11-point and 21-point intervals.",
        "outline": [
            "Structuring the 60-second coaching window: Calm down, deliver 1 technical cue, and 1 tactical adjustment.",
            "Using visual cues and diagrams to explain spatial/tactical changes quickly.",
            "Managing player emotional state and focus during intervals."
        ]
    },
    {
        "filename": "Topic_Psychology_of_Elite_Pressure",
        "title": "Psychology of Elite Pressure",
        "description": "Coping with high-pressure situations, managing choke tendencies, and pre-performance routines.",
        "outline": [
            "Understanding the mechanisms of choking under pressure: Cognitive anxiety and self-focus.",
            "Implementing pre-performance routines (breathing, visualization, cue words) to regulate arousal.",
            "Developing resilience and mindfulness techniques for high-stakes competition."
        ]
    },
    {
        "filename": "Topic_Elite_Sports_Science_Physiology",
        "title": "Elite Sports Science Physiology",
        "description": "VO2 Max testing, blood lactate threshold, and metabolic demand analysis of elite players.",
        "outline": [
            "Conducting sport-specific aerobic/anaerobic field tests (e.g., continuous court-movement protocols).",
            "Determining blood lactate thresholds to design individualized training intensities.",
            "Analyzing metabolic demands of elite singles vs. doubles rallies."
        ]
    },
    {
        "filename": "Topic_Elite_Match_Analysis_Software",
        "title": "Elite Match Analysis Software Usage",
        "description": "Applying specialized analysis systems (e.g., Dartfish, Hudl) to tag, slice, and review performance video.",
        "outline": [
            "Designing tagging panels to log shot types, coordinates, and rally outcomes.",
            "Using video tagging to identify technical flaws in shot preparation.",
            "Creating video playlists to review game play with the athlete."
        ]
    },
    {
        "filename": "Topic_High_Performance_Athlete_Management",
        "title": "High Performance Athlete Management",
        "description": "Balancing elite training, sponsor/media commitments, travel load, and career transitions.",
        "outline": [
            "Designing lifestyle profiles to balance training, sleep, academic, and commercial commitments.",
            "Monitoring travel fatigue, jet lag protocols, and nutritional adaptation during international tournaments.",
            "Managing dual-career pathways and post-retirement transitions."
        ]
    },

    # Para-Badminton & Special Populations
    {
        "filename": "Topic_Para_Badminton_Sport_Classes",
        "title": "Para-Badminton Sport Classes",
        "description": "BWF classification criteria and physical impairment standards for WH1, WH2, SL3, SL4, SU5, and SH6 classes.",
        "outline": [
            "Wheelchair classes (WH1, WH2): Assessing trunk function, core stability, and upper limb control.",
            "Standing classes (SL3, SL4, SU5): Distinguishing lower limb impairments (SL3/SL4) and upper limb limitations (SU5).",
            "Short Stature class (SH6): Classification criteria and eligibility boundaries."
        ]
    },
    {
        "filename": "Topic_Wheelchair_Court_Size_Rules",
        "title": "Wheelchair Court Size Rules",
        "description": "Rule-book variations in singles and doubles court dimensions for WH1 and WH2 players.",
        "outline": [
            "Wheelchair Singles: The court consists of the half-court (long, narrow), excluding the forecourt area.",
            "Wheelchair Doubles: The court utilizes the full width, excluding the forecourt area.",
            "Tactical positioning: Managing the open space and recovering to base under wheelchair constraints."
        ]
    },
    {
        "filename": "Topic_Wheelchair_Service_Height_Rule",
        "title": "Wheelchair Service Height and Position Rules",
        "description": "Service laws, hand/wheel positioning, and racket contact rules for wheelchair categories.",
        "outline": [
            "The serve must be hit from a stationary wheelchair position relative to the court lines.",
            "The wheelchair wheels must be positioned entirely within the correct service box.",
            "Height of contact: Hand, racket, and shuttle position restrictions at impact."
        ]
    },
    {
        "filename": "Topic_Standing_Para_Player_Adaptations",
        "title": "Standing Para-Player Adaptations",
        "description": "Adapting movement patterns, lunging, and balance recovery for SL3, SL4, and SU5 players.",
        "outline": [
            "SL3/SL4 adaptations: Modifying footwork patterns (e.g., hopping, step-close-step) to compensate for lower limb impairments.",
            "SU5 adaptations: Balancing the body and counterweight during lunges without full use of both arms.",
            "Optimizing racket grip and swing trajectories to maximize range of motion."
        ]
    },
    {
        "filename": "Topic_Short_Stature_Class_SH6_Rules",
        "title": "Short Stature Class (SH6) Rules and Adaptations",
        "description": "Rules, technical adjustments, and training focus for SH6 athletes.",
        "outline": [
            "Understanding the biomechanical differences of short limbs on court speed and reach.",
            "Adapting high serves and clears to account for lower contact points.",
            "Tactical positioning: Compensating for height limitations by dominating the midcourt."
        ]
    },
    {
        "filename": "Topic_Coaching_Players_with_Intellectual_Disabilities",
        "title": "Coaching Players with Intellectual Disabilities",
        "description": "Pedagogical adaptations, simplifying instructions, using visual aids, and structuring sessions.",
        "outline": [
            "Using concrete, single-step instructions and repetitive, structured drill patterns.",
            "Applying visual color-coded markings on court and rackets to simplify spatial concepts.",
            "Managing emotional regulation, session routine, and praise reinforcement."
        ]
    },
    {
        "filename": "Topic_Coaching_Deaf_Badminton_Players",
        "title": "Coaching Deaf Badminton Players",
        "description": "Communication methods, visual feedback loop, and positioning strategies on court.",
        "outline": [
            "Establishing visual sign signals and non-verbal cues for immediate court-side instruction.",
            "Ensuring visual line of sight before speaking or demonstrating techniques.",
            "Using mirrors and video playback to provide clear, visual feedback."
        ]
    },
    {
        "filename": "Topic_Para_Badminton_Equipment_Adaptations",
        "title": "Para-Badminton Equipment Adaptations",
        "description": "Adjusting wheelchair wheel camber, backrest height, chest strapping, and specialized racket grips.",
        "outline": [
            "Modifying wheelchair camber angles to optimize turning speed and lateral stability.",
            "Selecting chest and waist straps to compensate for weak core/abdominal control.",
            "Designing custom racket grips and wrist straps for players with hand or finger amputations."
        ]
    },
    {
        "filename": "Topic_Risk_Assessment_for_Para_Badminton",
        "title": "Risk Assessment for Para-Badminton",
        "description": "Wheelchair integrity checks, court clearance rules, and safe assistant positioning.",
        "outline": [
            "Inspecting wheelchairs for anti-tip wheel function, wheel integrity, and secure strap buckles.",
            "Ensuring wide court clearance margins to prevent collision with walls, posts, or nearby equipment.",
            "Establishing safety protocols for assistants/feeders standing near wheelchair courts."
        ]
    },
    {
        "filename": "Topic_Active_Recovery_Strategies",
        "title": "Active Recovery Strategies",
        "description": "Optimizing player recovery through active cool-downs, hydrotherapy, compression garments, and sleep hygiene.",
        "outline": [
            "Designing progressive cool-down protocols (static stretching, low-intensity cycling) to reduce muscle soreness.",
            "Using contrast hydrotherapy (hot/cold water immersion) and active compression to promote circulation.",
            "Sleep hygiene guidelines for elite players: Optimizing recovery and muscle repair windows."
        ]
    }
]

def generate_topic_files():
    output_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created directory: {output_dir}")
        
    for index, topic in enumerate(topics, 1):
        filename = f"{topic['filename']}.md"
        filepath = os.path.join(output_dir, filename)
        
        content = f"# {topic['title']}\n\n"
        content += f"{topic['description']}\n\n"
        content += "## Structural Outline\n\n"
        
        for i, item in enumerate(topic['outline'], 1):
            content += f"{i}. {item}\n"
            
        content += "\n#llm-deep-backlog\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
        if index % 20 == 0 or index == len(topics):
            print(f"Generated {index}/{len(topics)} files...")
            
    print(f"All {len(topics)} topic files generated successfully in {output_dir}!")

if __name__ == "__main__":
    generate_topic_files()
