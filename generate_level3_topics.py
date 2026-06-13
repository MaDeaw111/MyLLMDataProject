import os
import json

output_dir = "C:/Users/usEr/MyLLMDataProject/GeneratedTopics/Level_3"
os.makedirs(output_dir, exist_ok=True)

# List of 330 topics
topics = [
    # --- Category 1: High Performance Pathways (HPP) ---
    {
        "filename": "Topic_L3_Talent_ID_Anthropometric_Profiling",
        "title": "Anthropometric Profiling for Elite Badminton Players",
        "outline": [
            "Wing-span and standing reach correlation with defensive coverage efficiency.",
            "Lower-limb length ratios as predictors of deep lunging displacement speed.",
            "Longitudinal monitoring of skeletal changes during adolescent maturation."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Physiological_Screening",
        "title": "Physiological Screening Batteries for Elite Selection",
        "outline": [
            "Standardizing explosive jump power tests for national pathway entrance.",
            "Utilizing incremental shuttle run tests to benchmark aerobic capacity.",
            "Evaluating upper body pull-to-push ratios for overhead power potential."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Cognitive_Decision_Speed",
        "title": "Cognitive Decision-Making Speed in Youth Talent Identification",
        "outline": [
            "Reactive agility tests under complex visual stimulation.",
            "Assessing stroke selection speed under high cognitive pressure.",
            "Tracking anticipation accuracy using occlusion video testing."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Visual_Gaze_Tracking",
        "title": "Visual Gaze Tracking and Anticipation in Selection",
        "outline": [
            "Measuring fixation duration on racket face vs. opponent torso.",
            "Correlating visual search efficiency with baseline reaction times.",
            "Training peripheral vision sensitivity to detect early shuttle launch angles."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Functional_Movement_Screen",
        "title": "Functional Movement Screening in Junior Academies",
        "outline": [
            "Screening overhead deep squat mechanics to check ankle/hip mobility.",
            "Identifying unilateral imbalances in single-leg landing control.",
            "Tracking thoracic spine rotation symmetry to prevent compensation injuries."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Reactive_Agility_Testing",
        "title": "Reactive Agility Assessment Under Dual-Task Conditions",
        "outline": [
            "Measuring time delay in direction change when given late auditory cues.",
            "Evaluating cognitive interference during footwork execution.",
            "Correlating reactive agility times with defensive return efficiency."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Heart_Rate_Recovery_Metrics",
        "title": "Heart Rate Recovery Capacity as a Selection Metric",
        "outline": [
            "Benchmarking 60-second post-exercise heart rate drop in elite juniors.",
            "Correlating fast parasympathetic reactivation with training tolerance.",
            "Tracking recovery index variations during multi-day trial simulations."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Upper_Limb_Power_Assessment",
        "title": "Upper Limb Explosive Power Assessment for Smash Potential",
        "outline": [
            "Medicine ball throw tests (overhead and rotational) for power profiling.",
            "Isokinetic dynamometry of shoulder external/internal rotation torque.",
            "Velocity tracking of hand-speed using high-frequency accelerometers."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Ankle_Stability_Plantarflexion",
        "title": "Ankle Joint Stability and Plantarflexion Strength in Talent ID",
        "outline": [
            "Dynamic balance testing on unstable surfaces to measure ankle control.",
            "Eccentric plantarflexion strength benchmarks for explosive push-offs.",
            "Screening ankle joint range of motion (dorsiflexion) for deep lunge safety."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Psychological_Resilience_Grit",
        "title": "Psychological Resilience and Grit Inventories for Elite Entry",
        "outline": [
            "Standardized sports-specific resilience scale applications in trial phases.",
            "Assessing athlete coping strategies under structured failure scenarios.",
            "Long-term tracking of goal-directed grit and coachability parameters."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Dynamic_Postural_Stability",
        "title": "Dynamic Balance and Postural Stability in Badminton Talents",
        "outline": [
            "Y-Balance Test protocols to assess unilateral reach boundaries.",
            "Postural sway analysis during landing from maximum vertical jumps.",
            "Core activation response to sudden perturbations in stance."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Peak_Height_Velocity_PHV",
        "title": "Peak Height Velocity Modeling in Long-Term Development",
        "outline": [
            "Calculating somatic maturation age using standing height and sitting height.",
            "Adjusting training volume to match peak bone growth vulnerability windows.",
            "Re-educating coordination patterns during adolescent growth-related awkwardness."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Grip_Strength_Dynamics",
        "title": "Finger and Grip Strength Dynamics in Grip Change Speed",
        "outline": [
            "Dynamometer testing of thumb and forefinger pinch force profiles.",
            "Correlation between forearm muscle endurance and grip change speed.",
            "Diagnostic screening for hand-grip stabilization during off-center hits."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Rotational_Trunk_Power",
        "title": "Rotational Trunk Power Assessment in Talent ID",
        "outline": [
            "Measuring pelvic-thoracic separation angle velocity during core rotation.",
            "Dynamic medicine ball rotational throws for distance and speed.",
            "Assessing core muscle activation symmetry during multi-directional twists."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Spatial_Orientation_Testing",
        "title": "Spatial Orientation and Court Awareness Testing",
        "outline": [
            "Blended reality tests to assess blind-spot recovery and awareness.",
            "Measuring tracking error rates when returning to base post-rotation.",
            "Dynamic adjustment of movement pathways under fluctuating court boundaries."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Neuromuscular_Control_Complexity",
        "title": "Neuromuscular Control and Coordination Complexity Metrics",
        "outline": [
            "Dual-task coordinative testing involving racket control and footwork variations.",
            "Electromyographical (EMG) latency analysis of core stabilizing muscle activation.",
            "Dynamic tracking of coordination adaptability in novel motor tasks."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Genetic_Fiber_Composition",
        "title": "Genetic and Muscle Fiber Considerations in Talent Selection",
        "outline": [
            "Non-invasive estimation of muscle fiber composition in elite youth.",
            "Assessing genetic predispositions for explosive power vs. fatigue resistance.",
            "Balancing genotypic indicators with phenotypic adaptation capabilities in selection."
        ]
    },
    {
        "filename": "Topic_L3_Talent_ID_Biological_Age_Assessment",
        "title": "Biological vs. Chronological Age Assessment in High Performance",
        "outline": [
            "Utilizing skeletal age estimators and secondary sex characteristics safely.",
            "Grouping young athletes based on biological maturity (bio-banding) in tournaments.",
            "Adjusting physiological training loads to biological age rather than age groups."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Regional_Transition",
        "title": "Transitioning Players from Regional to National Squads",
        "outline": [
            "Alignment of technical terms and coaching philosophies between regions and center.",
            "Standardizing physical conditioning baselines before transition entry.",
            "Managing psychosocial stress of relocation to centralized dormitories."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Curriculum_Integration",
        "title": "Curriculum Integration Across National Junior Centers",
        "outline": [
            "Shared technical syllabus database accessible to all regional coaches.",
            "Video analysis sharing and technical benchmarking across centers.",
            "Annual training program auditing to ensure baseline skills development."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Multi_Disciplinary_Teams",
        "title": "Multi-Disciplinary Support Teams in Youth Pipelines",
        "outline": [
            "Coordinating physiotherapy, psychology, nutrition, and strength coaches.",
            "Standardized weekly monitoring meetings to discuss individual player progress.",
            "Balancing clinical advice with daily coaching demands and performance targets."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_U15_Periodization",
        "title": "Periodization Standardization for Under-15 Elite Groups",
        "outline": [
            "Focus on multi-lateral physical preparation rather than extreme specialization.",
            "Structural distribution of competition blocks within academic calendars.",
            "Balancing skill acquisition phases with moderate aerobic-anaerobic base building."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_U17_Load_Monitoring",
        "title": "Periodized Training Load Monitoring in U17 National Pipelines",
        "outline": [
            "Daily collection of Session RPE (Rate of Perceived Exertion) and training duration.",
            "Tracking Acute-to-Chronic Workload Ratios (ACWR) to prevent overuse injuries.",
            "Adjusting individual loads during key physical maturation spurts."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_U19_Benchmarking",
        "title": "Technical Benchmarking for National Under-19 Squads",
        "outline": [
            "Target velocity expectations for overhead forehand jump smashes.",
            "Footwork efficiency parameters during multi-directional defensive sweeps.",
            "Tactical literacy standards in court positioning and recovery choices."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Competitive_Scheduling",
        "title": "Competitive Scheduling and Travel Management for Junior Teams",
        "outline": [
            "Limiting international travel to prevent school and training disruption.",
            "Selecting tournaments based on ranking point strategy and exposure value.",
            "Incorporating dedicated recovery phases post-competition block."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Dual_Career_Academies",
        "title": "Dual-Career Management for Student-Athletes in National Academies",
        "outline": [
            "Collaborating with educational institutions for flexible class schedules.",
            "Academic tutoring integration within the national training center.",
            "Psychological support to manage academic stress alongside sport demands."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Parent_Education",
        "title": "Parent Education Programs in Elite Sports Pathways",
        "outline": [
            "Informing parents about long-term development stages and performance expectations.",
            "Guidance on sports nutrition, sleep environment, and recovery support at home.",
            "Directing parental support toward emotional stability rather than technical coaching."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Injury_Prevention",
        "title": "Injury Prevention Integration in Daily Academy Training",
        "outline": [
            "Pre-session neuromuscular activation routines (15-20 minutes).",
            "Weekly strength profiling to identify muscle imbalances early.",
            "Restricting racket volume for athletes returning from shoulder or knee injuries."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Selection_Policies",
        "title": "Selection Policy Transparency and Appeals Procedures",
        "outline": [
            "Formulating objective, measurable physical and technical selection criteria.",
            "Establishing independent selection panels for national team representation.",
            "Creating clear communication pathways and legal structures for appeals."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Quality_Assurance",
        "title": "Quality Assurance of National High-Performance Centers",
        "outline": [
            "Continuous facility auditing (e.g., lighting, flooring, medical rooms).",
            "Coach performance evaluation and professional development tracking.",
            "Athlete feedback collection systems regarding training quality and culture."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Tactical_Literacy",
        "title": "Tactical Literacy Curriculum for Emerging Elites",
        "outline": [
            "Video analysis workshops to teach structural pattern recognition.",
            "Tactical simulations during training with strict matchplay constraints.",
            "Scenario-based training (e.g., playing at 19-19 in the final set)."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Nutrition_Education",
        "title": "Nutrition and Hydration Education Protocols in Pipelines",
        "outline": [
            "Interactive workshops on meal preparation, macronutrients, and hydration.",
            "Dispelling myths around sports supplements and educating on anti-doping.",
            "Monitoring hydration via urine specific gravity during intensive camps."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Mental_Skills",
        "title": "Mental Skills Integration for High-Performance Pipelines",
        "outline": [
            "Teaching self-talk, visualization, and arousal regulation from age 14.",
            "Integrating mindfulness practices within the weekly training schedule.",
            "Simulating pressure environments in daily practice matches."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Sleep_Hygiene",
        "title": "Sleep Hygiene Standards for National Academy Athletes",
        "outline": [
            "Educating athletes on sleep cycles, blue-light exposure, and bedroom environment.",
            "Tracking sleep duration and subjective quality using athlete diaries.",
            "Strategic napping protocols during double-session training days."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Physiological_Database",
        "title": "Standardized Physiological Profiling Database Management",
        "outline": [
            "Centralizing physical test results (e.g., VO2 max, sprint times, jump heights).",
            "Tracking historical progression of individual elite players.",
            "Utilizing cohort benchmarks to refine development standards."
        ]
    },
    {
        "filename": "Topic_L3_National_Pipeline_Cross_Training",
        "title": "Cross-Training Integration in Youth Badminton Development",
        "outline": [
            "Integrating swimming or gymnastics for multi-lateral movement capacity.",
            "Utilizing non-racket cardiovascular training during recovery blocks.",
            "Risk management and safety considerations of cross-training options."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Junior_Senior_Move",
        "title": "Managing Transition from Junior Elite to Senior International",
        "outline": [
            "Preparing athletes for increased match intensity and physical contact.",
            "Managing expectations during early career losses in senior draws.",
            "Re-evaluating tactical roles and specific styles for senior court play."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Deescalation_Retirement",
        "title": "Career De-escalation and Post-Retirement Program Integration",
        "outline": [
            "Structured step-down of physical training volume to prevent health issues.",
            "Psychological transition planning for identity change post-sport.",
            "Relocating elite retired athletes into administrative or coaching roles."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Injury_Rehab_Psychology",
        "title": "Psychological Adjustments During Long-Term Injury Rehab",
        "outline": [
            "Managing identity loss when away from active training and competition.",
            "Goal setting focused on physical recovery milestones.",
            "Cognitive-behavioral strategies to reduce re-injury anxiety on return."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Financial_Literacy",
        "title": "Financial Literacy and Sponsor Relations for Senior Athletes",
        "outline": [
            "Educating players on tax management, contract negotiation, and savings.",
            "Balancing sponsor duties with training and match schedules.",
            "Ethical considerations and anti-doping responsibilities in endorsements."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Mid_Career_Planning",
        "title": "Career Transition Plans for Mid-Career Elite Players",
        "outline": [
            "Assessing vocational interests and skill transferability to other sectors.",
            "Incorporating part-time educational programs without training conflicts.",
            "Building professional networks during high-performance active periods."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Academic_Vocational_Support",
        "title": "Academic and Vocational Support Programs During Active Careers",
        "outline": [
            "Creating structured partnerships with universities offering online courses.",
            "Flexible exam scheduling and extensions during international tournaments.",
            "Career advisory services specific to high-performance athletes."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Dual_Career_Pathways",
        "title": "Dual-Career Pathways (Badminton and Higher Education)",
        "outline": [
            "Optimizing daily time management templates for study and training.",
            "Setting long-term academic targets that match athletic macrocycles.",
            "Managing stress markers during university exams and key tournaments."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Post_Olympic_Decompression",
        "title": "Post-Olympic Transition and Decompression Protocols",
        "outline": [
            "Mandatory psychological downtime and detachment post-Games.",
            "Medical evaluation and physical screening for accumulated fatigue.",
            "Phased re-integration plan to active competition and training."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Active_Player_Mentoring",
        "title": "Preparing Active Players for Coaching and Mentorship Roles",
        "outline": [
            "Integrating basic coaching modules in senior player training programs.",
            "Mentoring opportunities with academy junior squads.",
            "Establishing formal certification pathways for retiring players."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Identity_Management",
        "title": "Retirement Identity Management and Mental Health Support",
        "outline": [
            "Separating personal identity from athletic outcomes.",
            "Regular mental health check-ins with clinical psychologists.",
            "Developing hobby and non-sport interests during active career phases."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Relocation_Management",
        "title": "Relocation and Adaptation Management for International Academies",
        "outline": [
            "Language and cultural acclimatization support for foreign players.",
            "Logistic support including visas, housing, and integration.",
            "Fostering inclusive community environments within national academies."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Women_Athlete_Return",
        "title": "Support Systems for Women Athletes Re-entering Elite Competition",
        "outline": [
            "Physiological rebuild post-pregnancy or long-term career breaks.",
            "Travel logistics and child support integration at tournaments.",
            "Flexible training schedules and gradual intensity ramp-up."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Para_Badminton_Pathways",
        "title": "Athlete Transition Programs for Para-Badminton Players",
        "outline": [
            "Addressing specific accessibility needs during career transitions.",
            "Vocational retraining and equipment transfer post-competition.",
            "Advancing opportunities within the IPC and national committees."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Leadership_Development",
        "title": "Developing Leadership and Communication Skills in Transitioning Players",
        "outline": [
            "Providing public speaking and leadership workshops for elite seniors.",
            "Athlete representative roles in national federation committees.",
            "Organizing community outreach and junior camp leadership opportunities."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Media_Training",
        "title": "Media Training and Public Relations for High-Performance Athletes",
        "outline": [
            "Interactive mock interview training for television and print media.",
            "Developing crisis communication and social media safety guidelines.",
            "Formulating clear, professional messaging under high-stress press events."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Athlete_Branding",
        "title": "Athlete Branding and Digital Presence Management",
        "outline": [
            "Crafting a cohesive personal brand aligned with sporting values.",
            "Guidelines for managing sponsor integration on digital channels.",
            "Protecting mental health from negative social media interactions."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Post_Career_Administration",
        "title": "Post-Career Placement in National Governing Bodies",
        "outline": [
            "Trainee administrative positions in national badminton federations.",
            "Utilizing sport-specific knowledge for tournament management roles.",
            "Developing pathway leadership and selection committee representation."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Alumni_Networks",
        "title": "Integrating Player Alumni Networks for Youth Mentoring",
        "outline": [
            "Creating connection points between past champions and academy juniors.",
            "Organizing regular discussions on elite lifestyle and training pressure.",
            "Facilitating career networking opportunities outside the sport."
        ]
    },
    {
        "filename": "Topic_L3_Career_Transition_Sudden_Termination_Plan",
        "title": "Sudden Career Termination Planning (Injury/Health Reasons)",
        "outline": [
            "Creating immediate psychological protocols for sudden retirement.",
            "Financial backup planning and insurance coverage management.",
            "Rapid enrollment in vocational rehabilitation and transition programs."
        ]
    },

    # --- Category 2: High Performance Planning (HPPl) ---
    {
        "filename": "Topic_L3_HPPl_Macro_Quadrennial_Periodization",
        "title": "Macro-level Quadrennial Periodization for Olympic Cycles",
        "outline": [
            "Mapping the four-year progression from baseline accumulation to Olympic peaking.",
            "Adjusting yearly volumes and recovery cycles across the quadrennial.",
            "Integrating secondary target events (World Cups, Continental Games) without disrupting the main peak."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Phase_Specific_Volume_Adjustments",
        "title": "Phase-Specific Training Volume Adjustments in a Four-Year Cycle",
        "outline": [
            "Structuring general physical preparation blocks at the start of the quadrennial.",
            "Gradual shifting to high-intensity, sport-specific tactical training in years three and four.",
            "Tapering strategies and maintenance volumes during the qualification year."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Peak_Performance_Targeting",
        "title": "Peak Performance Targeting for World Championships Within Quadrennial",
        "outline": [
            "Designing 8-to-12 week specific prep phases prior to each annual World Championships.",
            "Utilizing performance feedback from majors to adjust the Olympic timeline.",
            "Balancing qualification point accumulation with physical preservation for peak performance."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Mid_Cycle_Performance_Auditing",
        "title": "Mid-Cycle Performance Auditing and Route Correction Protocols",
        "outline": [
            "Conducting comprehensive physical and tactical tests at the two-year mark.",
            "Adjusting individual athlete timelines based on maturation and performance markers.",
            "Reallocating support staff resources to address identified performance gaps."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Budgetary_Allocation_Optimization",
        "title": "Budgetary Allocation and Resource Optimization for Quadrennials",
        "outline": [
            "Cost-benefit analysis of training camps, international tournaments, and support staff.",
            "Prioritizing funding for medal-potential athletes while maintaining developmental pathways.",
            "Securing emergency contingency funds for medical and equipment needs."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Long_Term_Athlete_Retention_Rotation",
        "title": "Long-Term Athlete Retention and Rotation Strategies in Quadrennial Plans",
        "outline": [
            "Managing mental fatigue by incorporating extended off-season breaks in years one and two.",
            "Utilizing squad rotation in minor team events to blood emerging talent.",
            "Structuring longevity-focused conditioning programs for veteran athletes."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Facility_Infrastructure_Planning",
        "title": "Training Facility and Infrastructure Planning for Olympic Preparation",
        "outline": [
            "Selecting training venues that match Olympic host conditions (altitude, surface, temperature).",
            "Ensuring access to high-performance medical and recovery equipment.",
            "Coordinating housing and transport logistics to minimize daily travel stress."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Technical_Staffing_Contracting",
        "title": "Technical Staffing and Support Team Contracting in Four-Year Cycles",
        "outline": [
            "Securing long-term contracts with key coaching, physiotherapy, and analytics staff.",
            "Establishing performance-based key performance indicators (KPIs) for coaching staff.",
            "Structuring communication and alignment protocols across the multi-disciplinary team."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Longitudinal_Biomarker_Monitoring",
        "title": "Monitoring Longitudinal Biomarkers Over a Four-Year Plan",
        "outline": [
            "Tracking blood markers (ferritin, cortisol, testosterone) to detect systemic overtraining.",
            "Establishing baseline physiological values during early quadrennial phases.",
            "Adjusting training intensities based on individual recovery profiles."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Junior_Senior_Integration",
        "title": "Integrating Junior Talents into Quadrennial Senior Prep Plans",
        "outline": [
            "Selecting elite juniors to act as sparring partners for senior Olympic prospects.",
            "Phasing junior exposure to senior international training camps.",
            "Managing training loads during transition to prevent premature burnout."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Olympic_Qualification_Strategy",
        "title": "Olympic Qualification Point Accumulation Strategy",
        "outline": [
            "Selecting tournaments to maximize points while avoiding unnecessary travel.",
            "Monitoring qualification rankings and adjusting travel schedules dynamically.",
            "Balancing performance requirements with injury prevention during peak density."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Paralympic_Qualification_Classification",
        "title": "Paralympic Qualification Classification Review and Planning",
        "outline": [
            "Navigating international classification systems and tracking status updates.",
            "Tactical selection of tournaments with high classification panel presence.",
            "Managing documentation and medical evidence for athlete categorization."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Qualification_Fatigue_Management",
        "title": "Managing Qualification Travel Fatigue and Tournament Density",
        "outline": [
            "Implementing active recovery protocols during short tournament intervals.",
            "Optimizing flight and rest schedules during multi-tournament swings.",
            "Modifying training intensity during qualification weeks to prioritize matchplay."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Olympic_Village_Simulation",
        "title": "Simulating Olympic Village Environments and Schedule Protocols",
        "outline": [
            "Replicating early morning match schedules and shared living quarters in camp.",
            "Implementing strict device and distraction-management protocols.",
            "Adapting to dining hall nutrition choices and travel distances to courts."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Security_Media_Management",
        "title": "Security and Media Management Plans for Olympic Games",
        "outline": [
            "Establishing guidelines for press interactions and social media blackout periods.",
            "Ensuring physical safety and transport security during international travel.",
            "Coaching athletes on managing press pressure and distraction."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Coach_Player_Relations_Pressure",
        "title": "Managing Coach-Player Relations Under Olympic Pressure",
        "outline": [
            "Resolving interpersonal conflicts quickly in high-stakes training camps.",
            "Establishing boundaries and communication guidelines during competition weeks.",
            "Providing psychological support for coaches managing high expectations."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Post_Qualification_Peak_Design",
        "title": "Post-Qualification Peak Training Block Design",
        "outline": [
            "Designing a 6-to-8 week intensive camp post-qualification confirmation.",
            "Re-establishing physical strength baselines post-heavy travel phases.",
            "Fine-tuning tactical combinations and tournament-specific game plans."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Paralympic_Court_Logistics",
        "title": "Paralympic-Specific Court Familiarization and Logistics Management",
        "outline": [
            "Checking wheelchair accessibility and configuration at host venues.",
            "Familiarizing athletes with lighting, drift patterns, and floor surface.",
            "Coordinating medical and prosthetic support logistics near the field of play."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Athlete_Entourage_Boundaries",
        "title": "Managing Athlete Entourages and Family Boundaries During Games",
        "outline": [
            "Establishing guidelines for family visits and agent contact.",
            "Protecting athletes' schedules from non-performance commitments.",
            "Clarifying roles of external advisors vs. official team coaches."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Pre_Games_Camps_Selection",
        "title": "Pre-Games Training Camps Selection and Acclimatization",
        "outline": [
            "Choosing locations with similar climate, altitude, and time zones to host city.",
            "Simulating tournament conditions (shuttles, schedules, lighting) at camp.",
            "Minimizing external stress through private and secure training facilities."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Team_Selection_Policies",
        "title": "Team Selection Policies and Criteria Management",
        "outline": [
            "Establishing clear, objective, and legally sound selection procedures.",
            "Communicating policies to athletes and support staff early in the cycle.",
            "Handling selection disputes through transparent and fair review boards."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Equipment_Customization_Logistics",
        "title": "Equipment Customization and Racket Stringing Logistics for Games",
        "outline": [
            "Selecting and testing racket models, weights, and grips for tournament conditions.",
            "Coordinating with official tournament stringers for consistent tension.",
            "Secure shipping and management of backup rackets, strings, and grips."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Last_Minute_Roster_Replacements",
        "title": "Dynamic Adjustments for Last-Minute Roster Replacements",
        "outline": [
            "Managing the psychological impact of teammate injuries on the squad.",
            "Integrating reserve players into starting tactical systems.",
            "Adjusting training schedules and rooming assignments post-change."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Host_Nation_Media_Pressure",
        "title": "Handling Pressures of Host Nation Media and Fan Base",
        "outline": [
            "Preparing athletes for local media focus and spectator noise.",
            "Simulating hostile or loud crowd noise during training matches.",
            "Developing focus cues to keep players centered on court action."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Medical_AntiDoping_Compliance",
        "title": "Medical Support Coordination and Anti-Doping Compliance",
        "outline": [
            "Managing therapeutic use exemptions (TUEs) for required medications.",
            "Education on WADA anti-doping updates and testing procedures.",
            "Coordinating medical staff access to training and competition venues."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Jet_Lag_East_West",
        "title": "Jet Lag Mitigation Protocols for East-to-West Travel",
        "outline": [
            "Gradually shifting sleep schedules later in the days before travel.",
            "Strategic exposure to evening light and avoiding morning light post-arrival.",
            "Timing light workouts and meals to align with the new time zone."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Jet_Lag_West_East",
        "title": "Jet Lag Mitigation Protocols for West-to-East Travel",
        "outline": [
            "Shifting sleep and wake times earlier in the days before departure.",
            "Utilizing bright light in the morning and avoiding light in the evening post-travel.",
            "Short-term melatonin supplementation to ease early sleep onset."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Altitude_Acclimatization_Profiles",
        "title": "Altitude Acclimatization Profiles for High-Altitude Venues",
        "outline": [
            "Initial arrival protocols: Lower training volume to adapt to thin air.",
            "Monitoring heart rate, hydration, and oxygen saturation levels daily.",
            "Adjusting tactical game plans (faster shuttle travel, shorter rallies)."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Humidity_Heat_Acclimatization",
        "title": "Humidity and Heat Acclimatization Protocols",
        "outline": [
            "Conducting training in climate-controlled chambers (thermal training).",
            "Gradual increase of workout duration in hot and humid conditions.",
            "Implementing cooling strategies (ice vests, cold drinks) post-session."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Travel_Nutrition_Food_Safety",
        "title": "Travel Nutrition and Food Safety Standards on International Tours",
        "outline": [
            "Securing safe food and bottled water sources in challenging travel locations.",
            "Carrying pre-packaged, high-quality carbohydrate and protein snacks.",
            "Educating players on avoiding local high-risk foods before matches."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Compression_Garments_Flights",
        "title": "Compression Garment Protocols During Long-Haul Flights",
        "outline": [
            "Proper sizing and pressure grade selection for travel compression socks.",
            "Guidelines on wear duration and removal during transit.",
            "Combining compression with light mobility exercises in the cabin."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_InFlight_Mobility_Hydration",
        "title": "In-Flight Mobility and Hydration Schedule Management",
        "outline": [
            "Setting timers for hourly in-seat stretches and ankle rotations.",
            "Structuring water intake guidelines (e.g., 250ml per hour of flight).",
            "Avoiding caffeine and alcohol to preserve natural sleep rhythms."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Sleep_Hygiene_Time_Zones",
        "title": "Sleep Hygiene Adaptations for Varying Time Zones",
        "outline": [
            "Restricting device screen time post-arrival to align with local night.",
            "Optimizing room temperature and darkness in transition hotels.",
            "Utilizing relaxation techniques and white noise to ease adaptation."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Circadian_Rhythm_Shifts",
        "title": "Managing Circadian Rhythm Shifts with Melatonin and Light",
        "outline": [
            "Planning precise timings for melatonin use based on travel direction.",
            "Utilizing blue-light blocking glasses during inappropriate light periods.",
            "Adjusting training times gradually to match local match schedules."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Rapid_Acclimatization_Late_Travel",
        "title": "Rapid Acclimatization Protocols for Late-Notice Travel",
        "outline": [
            "Prioritizing light, active recovery sessions immediately on arrival.",
            "Rapid hydration loading and high-carbohydrate meals.",
            "Adjusting court expectations for the first 48 hours of practice."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Travel_Recovery_Modalities",
        "title": "Travel Recovery Modalities: Contrast Baths and Soft Tissue Work",
        "outline": [
            "Standardizing contrast bath routines (hot-cold water intervals) post-arrival.",
            "Utilizing light foam rolling and trigger point therapy to restore mobility.",
            "Scheduling light active mobility walks to promote lower body circulation."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Shuttlecock_Speed_Venue_Acclimatization",
        "title": "Acclimatizing to Varying Shuttlecock Speeds in Hot/Cold Venues",
        "outline": [
            "Testing different speed ratings (76 to 79) under venue-specific heat.",
            "Modifying racket string tension to control fast shuttles in hot environments.",
            "Adapting tactical stroke choices (drops and clears) to shuttle speeds."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Continental_Swings_Scheduling",
        "title": "Adjusting Travel Schedules for Multi-Stop Continental Swings",
        "outline": [
            "Structuring mid-swing rest days at centralized training hubs.",
            "Managing laundry, equipment prep, and nutrition logistics during transitions.",
            "Monitoring athlete fatigue markers across a 4-to-6 week tour."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Travel_Logistics_Equipment_Integrity",
        "title": "Travel Logistics and Equipment Integrity Preservation",
        "outline": [
            "Packing rackets in thermal bags to shield from cargo hold temperatures.",
            "Hand-carrying essential match kit (rackets, shoes, orthotics) on flights.",
            "Pre-arranging local transport that fits large gear and wheelchair bags."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Team_Mental_Wellness_Extended_Tours",
        "title": "Managing Team Mental Wellness During Extended Tours",
        "outline": [
            "Creating opportunities for group activities outside of court environments.",
            "Providing individual quiet times and respecting personal space on tour.",
            "Regular check-ins with team psychologists via video conferences."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Immediate_Training_Resumption_PostTravel",
        "title": "Protocol for Immediate Training Resumption Post-Travel",
        "outline": [
            "First 24 hours: Non-impact mobility and light footwork drills.",
            "48 hours: Gradual increase in rally length and basic tactical drills.",
            "72 hours: Full-intensity match play and power training."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Cold_Weather_Travel_Warmups",
        "title": "Cold Weather Travel Adaptation and Warm-up Adjustments",
        "outline": [
            "Extending off-court dynamic warm-ups by 10-15 minutes in cold halls.",
            "Wearing layered thermal clothing during early practice stages.",
            "Adjusting string tension down to prevent premature string breakage."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Hydration_Air_Travel",
        "title": "Managing Athlete Hydration Status During Air Travel",
        "outline": [
            "Pre-travel hydration loading protocols (water and electrolyte drinks).",
            "Monitoring hydration levels via urine color cards during transit.",
            "Post-flight rehydration schedules to restore cellular fluid balance."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_PostTravel_Active_Recovery",
        "title": "Post-Travel Active Recovery Session Design",
        "outline": [
            "Combining dynamic stretching, breathing exercises, and light walking.",
            "Joint mobilization focus: Ankle, hip, and thoracic spine.",
            "Restricting heavy resistance training for 24-48 hours post-long flight."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Environmental_Stress_Monitoring",
        "title": "Environmental Stress Index Monitoring for Safe Competition",
        "outline": [
            "Using Wet Bulb Globe Temperature (WBGT) to assess heat strain.",
            "Implementing safety pauses and cooling breaks during extreme humidity.",
            "Guidelines for canceling outdoor or high-heat practices."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Recovery_Drips_Saline_Hydration",
        "title": "Strategic Use of Recovery Drips and Saline Hydration",
        "outline": [
            "Medical guidelines and legal constraints under anti-doping regulations.",
            "Timing IV hydration for severe dehydration recovery situations.",
            "Safe alternatives: High-electrolyte oral rehydration solutions."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_PreTravel_Immune_Support",
        "title": "Pre-Travel Immune Support and Health Protocols",
        "outline": [
            "Supplementation with Vitamin C, Zinc, and Probiotics before departure.",
            "Hygiene protocols: Hand sanitizing, mask-wearing in crowded terminals.",
            "Pre-travel health screenings and vaccinations for high-risk zones."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Jet_Lag_Wheelchair_Athletes",
        "title": "Managing Jet Lag in Wheelchair Para-Badminton Athletes",
        "outline": [
            "Adapting sleep shift schedules to physical mobility constraints.",
            "Managing hydration and pressure relief during extended sitting on flights.",
            "Coordinating accessible transport and hotel rooms post-arrival."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Court_Air_Conditioning_Drift",
        "title": "Adaptations for Varying Court Air Conditioning Flow Profiles",
        "outline": [
            "Mapping drift directions and strengths at the host venue.",
            "Strategic adjustment of shot selection (clears vs. drops) based on wind.",
            "Adapting defense positioning when playing against or with the drift."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_PostArrival_Musculoskeletal_Screening",
        "title": "Post-Arrival Musculoskeletal Screenings and Mobilization",
        "outline": [
            "Standardized 10-minute assessment of hip flexor and lower back tightness.",
            "Targeted manual therapy to address flight-induced stiffness.",
            "Dynamic mobilization sequences before the first on-court session."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Racket_Tension_Temperature_Adjustments",
        "title": "Adjusting Racket String Tension Based on Venue Temperature",
        "outline": [
            "Lowering tension (1-2 lbs) in cold halls to maintain repulsion power.",
            "Increasing tension (1-2 lbs) in hot, humid halls to keep control.",
            "Calibrating tension adjustments based on specific string types used."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Match_Scheduling_Rest_Profiles",
        "title": "Strategic Match Scheduling and Rest Profiles in Group Stages",
        "outline": [
            "Organizing daily recovery timelines (ice, food, massage) post-match.",
            "Balancing sleep schedules when transitioning from night to day sessions.",
            "Managing light activation workouts on rest days between matches."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Emergency_Medical_Evacuation",
        "title": "Emergency Medical and Evacuation Planning During Travel",
        "outline": [
            "Identifying local high-quality medical facilities near the venue.",
            "Securing international sports-medical travel insurance policies.",
            "Developing protocols for transferring injured athletes back home."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_High_Performance_Recovery_Centers",
        "title": "High Performance Recovery Centers Setup at Major Venues",
        "outline": [
            "Setting up temporary team rooms with ice baths and massage tables.",
            "Ensuring access to clean, high-carb nutrition and recovery shakes.",
            "Managing entry access to protect players' recovery space."
        ]
    },
    {
        "filename": "Topic_L3_HPPl_Local_Liaison_Officers",
        "title": "Integrating Local Liaison Officers for Optimal Accommodation",
        "outline": [
            "Selecting local support staff for language translation and transport.",
            "Coordinating food preparation with hotel chefs to meet dietary needs.",
            "Resolving venue credentialing and logistic hurdles quickly."
        ]
    },

    # --- Category 3: Match Analysis & Tech (MAT) ---
    {
        "filename": "Topic_L3_MAT_Opponent_Service_Return_Patterns",
        "title": "Profiling Opponent Service and Return Patterns",
        "outline": [
            "Coding opponent serve choices (short vs. flick) under pressure.",
            "Mapping return trajectories to locate forehand/backhand vulnerabilities.",
            "Developing tactics to exploit predictable service return habits."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Court_Coverage_Weak_Zones",
        "title": "Analyzing Court Coverage and Weak Zones Under Pressure",
        "outline": [
            "Identifying slow recovery corners using heat maps of movement.",
            "Forcing transitions to weak defensive zones under fast pressure.",
            "Exploiting movement delays after deep backhand overhead corners."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Smash_Vector_Recovery_Habits",
        "title": "Mapping Opponent Smash Vector and Recovery Habits",
        "outline": [
            "Tracking straight vs. cross smash percentages from rear court.",
            "Correlating opponent smash direction with their net follow-up speed.",
            "Positioning defenders based on opponent smash vector trends."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Tactical_Triggers_Critical_Points",
        "title": "Deciphering Opponent Tactical Triggers in Critical Points",
        "outline": [
            "Analysis of shot selection choices at 11-point and 21-point intervals.",
            "Identifying go-to serves or returns during tight match scores.",
            "Exploiting anxiety-driven structural changes in opponent game plan."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Defensive_Blocks_Deconstruction",
        "title": "Structural Deconstruction of Opponent Defensive Blocks",
        "outline": [
            "Mapping the frequency of cross vs. straight net blocks.",
            "Identifying forearm and wrist positioning markers during block contact.",
            "Targeting areas behind weak blocks for quick net interceptions."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Doubles_Rotational_Transitions",
        "title": "Analyzing Doubles Rotational Transitions and Gaps",
        "outline": [
            "Coding transition phases from attacking front-back to defensive side-side.",
            "Pinpointing defensive coverage holes in mid-court doubles rotations.",
            "Exploiting communication issues during high-speed rotational switches."
        ]
    },
    {
        "filename": "Topic_L3_MAT_LeftHanded_Players_Angles",
        "title": "Profiling Left-Handed Players: Angles and Strategy",
        "outline": [
            "Mapping the distinct slice angles of left-handed forehand dropshots.",
            "Targeting the deep backhand corner of left-handed players.",
            "Adjusting doubles receiver positioning for left-handed serves."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Opponent_Psychological_Triggers",
        "title": "Scouting Opponent Psychological Triggers and De-escalation",
        "outline": [
            "Identifying body language indicators of frustration or fatigue.",
            "Exploiting opponent emotional drops through strategic delays.",
            "Directing tactical play to force errors from anxious opponents."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Net_Play_Trajectories",
        "title": "Mapping Opponent Net Play Trajectories and Spinner Frequency",
        "outline": [
            "Coding tumbling net shot success rates and release height.",
            "Identifying telltale signs of cross-court net shot variations.",
            "Developing counter-positioning for early net-kill interceptions."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Serve_Flick_Patterns",
        "title": "Identification of Opponent Serve Flick Patterns",
        "outline": [
            "Tracking preparation time differences between short and flick serves.",
            "Identifying look-away cues and body alignment before a flick.",
            "Positioning weight back when flick probability markers increase."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Grip_Shifts_Fatigue_Markers",
        "title": "Scouting Opponent Grip Shifts and Forearm Fatigue Markers",
        "outline": [
            "Tracking errors in backhand-to-forehand transitions under speed.",
            "Identifying drop-offs in racket-head speed due to forearm fatigue.",
            "Forcing late grip transitions in the rear court via flat drives."
        ]
    },
    {
        "filename": "Topic_L3_MAT_PreMatch_Video_Briefings",
        "title": "Pre-Match Video Briefings: Distilling Scouting Data",
        "outline": [
            "Selecting three key video clips demonstrating opponent weaknesses.",
            "Presenting clear tactical responses to opponent patterns.",
            "Avoiding cognitive overload by keeping briefings under 10 minutes."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Video_Tagging_Taxonomies",
        "title": "Developing Standardized Video Tagging Taxonomies",
        "outline": [
            "Defining consistent code structures for strokes, zones, and outcomes.",
            "Setting up key-binding shortcuts for fast live match tagging.",
            "Aligning national coaching vocabulary with tagging labels."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Rally_Length_Shot_Sequences",
        "title": "Coding Rally Length and Shot Progression Sequences",
        "outline": [
            "Analyzing percentage of points won in short (1-4 shots) vs. long rallies.",
            "Identifying common 3-shot sequences leading to point outcomes.",
            "Optimizing tactical serve-and-return sequences based on length trends."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Unforced_vs_Forced_Errors",
        "title": "Tagging Unforced Errors vs. Forced Errors in Matchplay",
        "outline": [
            "Standardizing definitions of unforced errors (no-pressure misses).",
            "Analyzing tactical choices leading to forced error situations.",
            "Correlating error ratios with player movement fatigue indices."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Winning_Shot_Distribution",
        "title": "Analysis of Winning Shot Distribution and Court Locations",
        "outline": [
            "Mapping winning shots (smashes, drops, net kills) on court diagrams.",
            "Correlating winning locations with prior shot placement setups.",
            "Developing tactical guidelines to target high-probability zones."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Net_Play_Outcomes",
        "title": "Video Coding of Net Play Outcomes: Net Shot vs. Lift",
        "outline": [
            "Coding net-play decisions under varying contact heights.",
            "Measuring success rates of tumbling net shots vs. flat pushes.",
            "Directing training focus based on net-decision coding results."
        ]
    },
    {
        "filename": "Topic_L3_MAT_InterPoint_Time_Recovery",
        "title": "Temporal Analysis of Inter-Point Time and Player Recovery",
        "outline": [
            "Coding seconds elapsed between rallies to monitor pace manipulation.",
            "Tracking warnings for delay of game and umpire interactions.",
            "Optimizing player recovery behavior in the allowed 20-second break."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Defensive_Recovery_Footwork_Tagging",
        "title": "Tagging Defensive Recovery Footwork Configurations",
        "outline": [
            "Coding step frequency and stance width during deep lunges.",
            "Identifying foot-slip events and correlation with shoe/floor clean.",
            "Assessing recovery time differences between standard and slide lunges."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Return_of_Serve_Mixed_Doubles",
        "title": "Coding Return of Serve Trajectories in Mixed Doubles",
        "outline": [
            "Mapping female vs. male server returns in mixed matches.",
            "Identifying target zones that force mixed partners to cross over.",
            "Designing return routines that neutralize the male player's attack."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Smash_Angles_Jump_Heights",
        "title": "Video Analysis of Overhead Smash Angles and Jump Heights",
        "outline": [
            "Estimating contact height and angle from video footage frames.",
            "Correlating jump heights with smash speed and floor landing.",
            "Analyzing mechanical breakdown in overhead smashes during late sets."
        ]
    },
    {
        "filename": "Topic_L3_MAT_SemiAutomated_Video_Coding",
        "title": "Semi-Automated Video Coding Systems Integration",
        "outline": [
            "Utilizing computer-vision tools for automatic court line detection.",
            "Integrating racket and shuttle tracking systems with video coding.",
            "Managing real-time data output during match-play intervals."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Rotational_Efficiency_Mens_Doubles",
        "title": "Tracking Rotational Efficiency in Men's Doubles Video Coding",
        "outline": [
            "Coding time gaps during player rotations from back to front.",
            "Identifying coordination errors during side-by-side defense switches.",
            "Assessing rotation choices under fast, flat drive attacks."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Player_Positioning_Shuttle_Impact",
        "title": "Coding Player Positioning Relative to Shuttle Impact Point",
        "outline": [
            "Measuring player distance from center base at shuttle contact.",
            "Coding balance state (on-balance vs. off-balance) during strokes.",
            "Correlating contact distance with subsequent rally control outcomes."
        ]
    },
    {
        "filename": "Topic_L3_MAT_RealTime_HR_Telemetry",
        "title": "Real-Time Heart Rate Telemetry During Practice Matches",
        "outline": [
            "Setting up reliable on-court wireless telemetry transmitters.",
            "Monitoring live heart rate fluctuations during intensive sparring.",
            "Adjusting player rest times based on real-time heart rate drop."
        ]
    },
    {
        "filename": "Topic_L3_MAT_HR_Spikes_Rally_Intensity",
        "title": "Correlating Heart Rate Spikes with Rally Intensity Metrics",
        "outline": [
            "Matching telemetry timecodes with video-coded rally durations.",
            "Quantifying metabolic demand of long rallies (>15 shots) via HR.",
            "Establishing individual cardiovascular load profiles."
        ]
    },
    {
        "filename": "Topic_L3_MAT_HR_Recovery_PostRally",
        "title": "Heart Rate Recovery Curves Post-Rally Analysis",
        "outline": [
            "Measuring rate of heart rate drop in the first 15 seconds post-rally.",
            "Correlating recovery speed with systemic aerobic fitness levels.",
            "Utilizing recovery curves to identify cardiovascular fatigue states."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Cardiovascular_Load_Singles_Doubles",
        "title": "Cardiovascular Load of Singles vs. Doubles Matchplay",
        "outline": [
            "Comparative analysis of peak and average heart rates in matches.",
            "Tracking work-to-rest ratios and heart rate zones in both disciplines.",
            "Designing discipline-specific cardiovascular conditioning programs."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Telemetry_RPE_Correlation",
        "title": "Correlating Telemetry Data with Player Rated Perceived Exertion",
        "outline": [
            "Collecting RPE scores 30 minutes post-session and comparing to HR data.",
            "Identifying discrepancies between objective HR loads and subjective RPE.",
            "Utilizing composite scores to adjust weekly training plans."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Anaerobic_Threshold_Telemetry",
        "title": "Identifying Anaerobic Threshold Crossings via Telemetry",
        "outline": [
            "Mapping individual anaerobic heart rate thresholds in training.",
            "Tracking time spent above the anaerobic threshold during matchplay.",
            "Designing training drills to extend time before threshold crossing."
        ]
    },
    {
        "filename": "Topic_L3_MAT_HRV_Readiness_Indicator",
        "title": "Heart Rate Variability as a Daily Readiness Indicator",
        "outline": [
            "Standardized morning HRV measurement protocols for elite players.",
            "Correlating autonomic nervous system balance with training readiness.",
            "Adjusting daily load plans based on weekly HRV deviations."
        ]
    },
    {
        "filename": "Topic_L3_MAT_HR_Response_HighPressure",
        "title": "Heart Rate Response to High-Pressure Game Situations",
        "outline": [
            "Telemetry monitoring during simulated sudden-death points (e.g., 20-20).",
            "Correlating heart rate spikes with cognitive focus and error rates.",
            "Implementing biofeedback training to control HR spikes."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Telemetry_Multifeeder_Conditioning",
        "title": "Telemetry-Guided Recovery Protocols Between Sets",
        "outline": [
            "Monitoring heart rate drop during the 120-second interval between sets.",
            "Selecting recovery activities (sitting, walking, deep breathing) based on HR.",
            "Adapting tactical coaching instructions to the player's physiological state."
        ]
    },
    {
        "filename": "Topic_L3_MAT_OnCourt_Multifeeder_Telemetry",
        "title": "Telemetry Integration in On-Court Multifeeder Conditioning",
        "outline": [
            "Structuring feeding frequency (shots per minute) to target specific HR zones.",
            "Adjusting drill intensity dynamically based on live telemetry feedback.",
            "Benchmarking anaerobic capacity during exhausting multifeeder sets."
        ]
    },
    {
        "filename": "Topic_L3_MAT_LongTerm_Cardiovascular_Profiling",
        "title": "Long-Term Cardiovascular Profiling of Elite Badminton Players",
        "outline": [
            "Tracking resting heart rate and VO2 max changes over consecutive years.",
            "Monitoring changes in submaximal heart rate indices during standardized runs.",
            "Adjusting training intensities to maintain career aerobic foundations."
        ]
    },
    {
        "filename": "Topic_L3_MAT_HR_Telemetry_Wheelchair_Para",
        "title": "Heart Rate Telemetry Challenges in Wheelchair Para-Badminton",
        "outline": [
            "Addressing sensor displacement issues during intensive wheeling.",
            "Calibrating heart rate zones to match upper-body muscular demand.",
            "Utilizing custom telemetry setups for athletes with spinal cord injuries."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Jump_Smash",
        "title": "Kinematic Profiling of the Jump Smash via Markerless Mocap",
        "outline": [
            "Tracking coordinate velocity of the ankle, knee, hip, shoulder, and wrist.",
            "Measuring vertical displacement and launch angle during takeoff.",
            "Correlating peak joint angular velocities with shuttle exit speed."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Lunge_Knee_Alignment",
        "title": "Analyzing Lunge Depth and Knee Alignment in Defense",
        "outline": [
            "Measuring peak knee flexion angle and lateral translation during lunges.",
            "Identifying knee valgus markers that increase ACL injury risk.",
            "Tracking recovery speed from deep forehand vs. backhand lunges."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Thoracic_Spine",
        "title": "Thoracic Spine Rotation Tracking in Overhead Strokes",
        "outline": [
            "Measuring axial rotation angles of the torso relative to the pelvis.",
            "Correlating thoracic mobility with shoulder draw distance during smashes.",
            "Identifying restrictions in thoracic rotation that lead to lower back strain."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Shoulder_Angles",
        "title": "Tracking Shoulder Rotation Angles in Forehand Clears",
        "outline": [
            "Tracking glenohumeral joint elevation and abduction angles.",
            "Measuring internal rotation velocity during the deceleration phase.",
            "Identifying compensation patterns in shoulder movement due to fatigue."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Forearm_Pronation",
        "title": "Measuring Forearm Pronation Velocity in Smash Sequences",
        "outline": [
            "Capturing rotation speed of the radioulnar joint before shuttle contact.",
            "Correlating pronation velocity with racket head acceleration.",
            "Tracking timing synchronization between forearm pronation and wrist flexion."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Footwork_Movement",
        "title": "Markerless Motion Capture of Court Movement Footwork",
        "outline": [
            "Tracking stance width, foot contact time, and center of mass shift.",
            "Analyzing step frequency during recovery from rear to front court.",
            "Comparing kinematic profiles of slide lunges vs. step lunges."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Hip_Rotation",
        "title": "Analyzing Hip Rotation and Power Generation in Smash Returns",
        "outline": [
            "Measuring pelvic rotation velocity during defensive court positioning.",
            "Correlating hip extension power with rapid directional recovery.",
            "Identifying core-to-hip coordination issues that slow footwork."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Grip_Transitions",
        "title": "Joint Angle Velocity Profiles in Rapid Grip Transitions",
        "outline": [
            "Capturing wrist and finger flexion angles during backhand-to-forehand shifts.",
            "Measuring time delay in grip changes under high shuttlecock speed.",
            "Profiling finger coordinate positioning for clean racket face control."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Spine_Biomechanics",
        "title": "Assessing Spine Biomechanics in Backhand Clear Movements",
        "outline": [
            "Measuring lumbar and thoracic spine flex-extension under deep reaches.",
            "Tracking lateral trunk lean during off-balance backhand overhead shots.",
            "Developing corrective exercise plans based on spine rotation metrics."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Lower_Limb_Split_Step",
        "title": "Evaluating Lower Limb Kinematics During the Split Step",
        "outline": [
            "Measuring flight time and landing stance width of the split step.",
            "Tracking joint angles (hip, knee, ankle) during initial push-off.",
            "Correlating split-step timing with opponent shuttle contact time."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Ankle_Instability",
        "title": "Markerless Tracking of Ankle Instability During Lateral Lunges",
        "outline": [
            "Measuring peak inversion and eversion angles during lateral cuts.",
            "Identifying biomechanical indicators of ankle joint vulnerability.",
            "Developing ankle strengthening programs using motion capture diagnostics."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Wrist_Torque",
        "title": "Wrist and Forearm Supination Torque Mapping in Dropshots",
        "outline": [
            "Capturing coordinate rotation profiles of the hand during slice drops.",
            "Measuring torque output variations in standard vs. reverse slices.",
            "Optimizing racket face control through precise wrist-forearm tracking."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Standing_vs_Wheelchair",
        "title": "Comparative Motion Capture of Standing vs. Wheelchair Players",
        "outline": [
            "Tracking coordinate velocity of the upper body during overhead shots.",
            "Measuring differences in trunk lean angles and balance control.",
            "Adapting training programs to match wheelchair-specific kinematics."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Daily_Training",
        "title": "Integrating Markerless Mocap into Daily Training Environments",
        "outline": [
            "Setting up multi-camera arrays around training courts for daily use.",
            "Automating data processing pipelines to deliver immediate feedback.",
            "Training coaching staff on interpreting daily kinematic reports."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_RealTime_Feedback",
        "title": "Real-time Feedback Systems Using Motion Capture Arrays",
        "outline": [
            "Providing immediate audio-visual cues on joint angles during drills.",
            "Setting up virtual boundaries for knee alignment during lunges.",
            "Measuring rate of motor learning using real-time feedback systems."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Rotator_Cuff_Injury_Risk",
        "title": "Identifying Biomechanical Risk Factors for Rotator Cuff Tears",
        "outline": [
            "Tracking abnormal shoulder translation during overhead shots.",
            "Identifying imbalance in internal/external shoulder rotation ranges.",
            "Designing rotator cuff stabilization plans based on mocap diagnostics."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Center_of_Mass",
        "title": "Tracking Center of Mass Trajectory During Multi-Directional Footwork",
        "outline": [
            "Measuring horizontal and vertical shifts of center of mass.",
            "Correlating center of mass control with agility performance.",
            "Developing footwork drills to optimize center of mass positioning."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Inertial_Sensors_Validation",
        "title": "Markerless Mocap Validation Against Gold-Standard Inertial Sensors",
        "outline": [
            "Designing comparative trials with IMUs and optical motion capture.",
            "Quantifying error rates in tracking joint angles during fast rallies.",
            "Setting calibration guidelines for markerless optical setups."
        ]
    },
    {
        "filename": "Topic_L3_MAT_Markerless_Mocap_Standardized_Testing",
        "title": "Standardized Motion Capture Testing Protocols for Elite Academies",
        "outline": [
            "Establishing baseline testing batteries for national squad entrants.",
            "Scheduling quarterly kinematic audits to track developmental progress.",
            "Centralizing joint kinematic data in national athlete profiles."
        ]
    },

    # --- Category 4: Advanced Biomechanics (AB) ---
    {
        "filename": "Topic_L3_AB_Kinetic_Chain_Jump_Smash",
        "title": "Kinetic Chain Optimization in the Forehand Jump Smash",
        "outline": [
            "Analyzing dynamic force transfer from feet to core to forearm.",
            "Optimizing segment delays to maximize racket speed at contact.",
            "Identifying kinetic chain energy leaks that cause early fatigue."
        ]
    },
    {
        "filename": "Topic_L3_AB_Proximal_Distal_Sequencing",
        "title": "Proximal-to-Distal Sequencing in Overhead Badminton Strokes",
        "outline": [
            "Quantifying the rotational delay between pelvis and thoracic segments.",
            "Optimizing shoulder, elbow, and wrist extension sequence timings.",
            "Correcting early forearm activation to prevent muscle strain."
        ]
    },
    {
        "filename": "Topic_L3_AB_GRF_Split_Step",
        "title": "Ground Reaction Force Generation in the Split Step",
        "outline": [
            "Measuring bilateral ground reaction forces using pressure plates.",
            "Correlating foot angle and center of mass shift with jump speed.",
            "Optimizing ankle stiffness to enhance energy return on push-off."
        ]
    },
    {
        "filename": "Topic_L3_AB_Energy_Transfer_Clears",
        "title": "Energy Transfer from Lower Limb to Upper Limb in Overhead Clears",
        "outline": [
            "Tracking forces through the knee, hip, and spine to the shoulder.",
            "Optimizing axial rotation to increase deep clear depth consistency.",
            "Identifying torque constraints in the abdominal core during clears."
        ]
    },
    {
        "filename": "Topic_L3_AB_Core_Stability_Off_Balance",
        "title": "Core Stability and Force Transmission in Off-Balance Hits",
        "outline": [
            "Evaluating rectus abdominis and obliques activation during reach shots.",
            "Stabilizing the pelvis to support accurate racket control off-balance.",
            "Training lumbar-thoracic core stiffness to preserve recovery speed."
        ]
    },
    {
        "filename": "Topic_L3_AB_Hip_Rotation_Power",
        "title": "Dynamic Hip Rotation for Power Enhancement in Overhead Strokes",
        "outline": [
            "Measuring hip separation angle velocity in deep forehand overheads.",
            "Optimizing hip extension to assist shoulder draw acceleration.",
            "Identifying biomechanical limits of hip rotation under fatigue."
        ]
    },
    {
        "filename": "Topic_L3_AB_Kinetic_Chain_Interruption",
        "title": "Kinetic Chain Interruption: Causes and Injury Risks",
        "outline": [
            "Analyzing structural causes of energy leaks in overhead motions.",
            "Correlating kinetic interruptions with shoulder impingement risks.",
            "Designing drills to re-establish sequential joint rotation."
        ]
    },
    {
        "filename": "Topic_L3_AB_Kinetic_Chain_Backhand_Overhead",
        "title": "Kinetic Chain Activation in Backhand Overhead Shots",
        "outline": [
            "Sequencing backhand clear movements from ankle push to wrist snap.",
            "Optimizing thoracic spine extension during deep backhand overheads.",
            "Correcting elbow hyper-extension issues through proper recovery."
        ]
    },
    {
        "filename": "Topic_L3_AB_GRF_Forehand_Lunges",
        "title": "Ground Reaction Forces in Deep Forehand Lunges",
        "outline": [
            "Measuring landing impact forces on the front heel during lunges.",
            "Analyzing forces during recovery push-back to the base position.",
            "Optimizing shoe grip friction to reduce knee shear forces."
        ]
    },
    {
        "filename": "Topic_L3_AB_Force_Transmission_Drives",
        "title": "Optimizing Force Transmission in Midcourt Drive Rallies",
        "outline": [
            "Tracking kinetic pathways under minimal lower limb displacement.",
            "Optimizing forearm pronation/supination torque for drive speed.",
            "Analyzing wrist stabilization requirements during fast exchanges."
        ]
    },
    {
        "filename": "Topic_L3_AB_Segmental_Deceleration_Impact",
        "title": "Segmental Deceleration Mechanics Post-Impact",
        "outline": [
            "Quantifying eccentric muscle work required to slow the racket arm.",
            "Analyzing rotator cuff stabilization load during follow-through.",
            "Designing deceleration drills to protect shoulder and elbow joints."
        ]
    },
    {
        "filename": "Topic_L3_AB_Shoulder_Rotation_Angles",
        "title": "Analyzing Shoulder Internal and External Rotation Angles",
        "outline": [
            "Tracking peak shoulder external rotation during backswing.",
            "Measuring internal rotation velocity at shuttle contact point.",
            "Analyzing shoulder range of motion adaptations in elite players."
        ]
    },
    {
        "filename": "Topic_L3_AB_Glenohumeral_Joint_Alignment",
        "title": "Glenohumeral Joint Alignment During the Smash Backswing",
        "outline": [
            "Identifying optimal glenohumeral angles to maximize arm reach.",
            "Screening for joint instability during extreme overhead draws.",
            "Preventing subacromial impingement via proper posture alignment."
        ]
    },
    {
        "filename": "Topic_L3_AB_Shoulder_Abduction_Inju_Prev",
        "title": "Shoulder Abduction Angle and Injury Prevention in Overhead Smashes",
        "outline": [
            "Measuring abduction angles relative to the trunk during execution.",
            "Identifying unsafe abduction angles (>90 degrees) under load.",
            "Correcting overhead reach pathways to protect soft tissues."
        ]
    },
    {
        "filename": "Topic_L3_AB_Rotator_Cuff_Activation_Angles",
        "title": "Dynamic Rotator Cuff Activation Angles for Shoulder Stability",
        "outline": [
            "Tracking supraspinatus and infraspinatus activation timing.",
            "Analyzing rotator cuff muscle balance under speed and fatigue.",
            "Designing angle-specific strengthening routines for rehabilitation."
        ]
    },
    {
        "filename": "Topic_L3_AB_Scapular_Dyskinesis_Angles",
        "title": "Scapular Dyskinesis and Shoulder Joint Angles in Elite Players",
        "outline": [
            "Screening for winging scapula during active overhead movements.",
            "Evaluating impact of abnormal scapular rhythm on shoulder reach.",
            "Corrective exercises to restore scapular stability and rotation."
        ]
    },
    {
        "filename": "Topic_L3_AB_Rotator_Cuff_Deep_Clears",
        "title": "Biomechanical Mapping of Rotator Cuff Loading in Deep Clears",
        "outline": [
            "Quantifying joint load differences in forehand vs. backhand clears.",
            "Identifying peak load points during late-release overhead reaches.",
            "Developing recovery protocols for chronic rotator cuff irritation."
        ]
    },
    {
        "filename": "Topic_L3_AB_Shoulder_ROM_Extreme_Reach",
        "title": "Shoulder Joint Range of Motion in Extreme Reach Shots",
        "outline": [
            "Measuring passive and active range of motion under reach stress.",
            "Correlating shoulder flexibility with defensive block coverage.",
            "Safeguarding loose joints through specialized stabilizing drills."
        ]
    },
    {
        "filename": "Topic_L3_AB_Shoulder_Rotation_Drives",
        "title": "Shoulder Rotation Angles in Forehand vs. Backhand Drives",
        "outline": [
            "Comparing scapular translation during forehand and backhand drives.",
            "Measuring internal/external shoulder rotation ranges during drive play.",
            "Adjusting stroke preparation based on shoulder angle metrics."
        ]
    },
    {
        "filename": "Topic_L3_AB_Shoulder_Fatigue_Kinematics",
        "title": "Effect of Shoulder Muscle Fatigue on Stroke Kinematics",
        "outline": [
            "Tracking joint angle changes during late-set match simulations.",
            "Identifying loss of shoulder elevation due to muscle fatigue.",
            "Designing endurance routines to preserve overhead form."
        ]
    },
    {
        "filename": "Topic_L3_AB_Shoulder_Draw_Max_Velocity",
        "title": "Optimizing the Shoulder Draw for Maximal Smash Velocity",
        "outline": [
            "Measuring backswing draw distance and shoulder abduction angles.",
            "Correlating draw speed with subsequent racket exit velocity.",
            "Correcting short backswings that limit smash acceleration."
        ]
    },
    {
        "filename": "Topic_L3_AB_Shoulder_Mechanics_Wheelchair",
        "title": "Shoulder Joint Mechanics in Wheelchair Court Movements",
        "outline": [
            "Tracking shoulder loads during combined wheeling and hitting.",
            "Evaluating risk of shoulder impingement in low-seated players.",
            "Optimizing seat height and backrest angles to protect shoulders."
        ]
    },
    {
        "filename": "Topic_L3_AB_Forearm_Pronation_Torque",
        "title": "Generating Forearm Pronation Torque in the Jump Smash",
        "outline": [
            "Measuring pronation speed of the radioulnar joint during smashes.",
            "Correlating pronation torque with racket head exit velocity.",
            "Optimizing timing of forearm pronation post-elbow extension."
        ]
    },
    {
        "filename": "Topic_L3_AB_Forearm_Supination_Backhand_Clears",
        "title": "Forearm Supination and Grip Tension in Backhand Clears",
        "outline": [
            "Tracking forearm supination torque during backhand preparations.",
            "Managing grip tension transition (loose to tight) at contact.",
            "Reducing stress on the lateral epicondyle during supination."
        ]
    },
    {
        "filename": "Topic_L3_AB_Forearm_Pronation_Supination_Net_Kills",
        "title": "Forearm Pronation-Supination Velocity in Net Kills",
        "outline": [
            "Measuring rapid rotational changes during short net attacks.",
            "Optimizing racket face angle control using finger adjustments.",
            "Designing net multifeeder drills to build forearm speed."
        ]
    },
    {
        "filename": "Topic_L3_AB_Grip_Force_Torque_Impact",
        "title": "Grip Force Profiling and Torque Generation During Impact",
        "outline": [
            "Measuring dynamic finger pressure during overhead smashes.",
            "Correlating grip tightness timings with torque outputs.",
            "Correcting premature grip tightening that limits joint speed."
        ]
    },
    {
        "filename": "Topic_L3_AB_Forearm_EMG_Flat_Exchanges",
        "title": "Forearm Muscle Activity in High-Frequency Flat Exchanges",
        "outline": [
            "Electromyographical (EMG) tracking of flexor/extensor activation.",
            "Evaluating muscle fatigue rates during extended drive rallies.",
            "Designing forearm conditioning programs for doubles specialists."
        ]
    },
    {
        "filename": "Topic_L3_AB_Forearm_Torque_Wrist_Flexion",
        "title": "Forearm Torque and Wrist Flexion Coordination in Trick Shots",
        "outline": [
            "Analyzing sequential coordination of wrist snap and forearm turn.",
            "Optimizing deception angles using late wrist adjustments.",
            "Preventing tendon strain during high-torque wrist movements."
        ]
    },
    {
        "filename": "Topic_L3_AB_Medial_Epicondylitis_Prevention",
        "title": "Preventing Medial Epicondylitis via Forearm Torque Optimization",
        "outline": [
            "Identifying mechanical errors in forearm pronation causing golfer's elbow.",
            "Strengthening pronator teres and flexor muscles eccentrically.",
            "Adjusting racket grip diameter to reduce elbow muscle load."
        ]
    },
    {
        "filename": "Topic_L3_AB_Forearm_Torque_Cross_Drops",
        "title": "Forearm Torque Mechanics in Cross-court Dropshots",
        "outline": [
            "Measuring forearm supination speed during slice drops.",
            "Controlling racket face angles to alter shuttle paths.",
            "Minimizing arm movement markers to keep dropshots deceptive."
        ]
    },
    {
        "filename": "Topic_L3_AB_Forearm_Supination_Backhand_Defense",
        "title": "Forearm Supination and Pronation Timing in Backhand Defenses",
        "outline": [
            "Tracking joint rotation sequences under fast smash returns.",
            "Optimizing forearm angles to direct defense blocks cross-court.",
            "Correcting late forearm rotation that leads to defensive errors."
        ]
    },
    {
        "filename": "Topic_L3_AB_Torque_Feather_vs_Synthetic",
        "title": "Torque Output Differences: Feather vs. Synthetic Shuttles",
        "outline": [
            "Measuring impact force differences on the wrist and forearm.",
            "Analyzing joint torque changes due to synthetic shuttle drag.",
            "Adjusting player stroke mechanics when training with synthetics."
        ]
    },
    {
        "filename": "Topic_L3_AB_Racket_Mass_Forearm_Torque",
        "title": "Racket Mass Distribution and Forearm Torque Requirements",
        "outline": [
            "Evaluating head-heavy vs. head-light racket torque demands.",
            "Correlating racket swingweight with forearm muscle fatigue.",
            "Selecting equipment based on individual forearm strength."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Spine_Rotation_Power",
        "title": "Thoracic Spine Axial Rotation Power in Overhead Smashes",
        "outline": [
            "Measuring axial rotation speed of the thoracic spine in jumps.",
            "Optimizing torso coil-to-uncoil timings for smash power.",
            "Correcting lumbar compensation caused by stiff thoracic joints."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Mobility_Smash_Recovery",
        "title": "Thoracic Spine Mobility for Steep Smash Recovery Angles",
        "outline": [
            "Measuring spine flex-extension and rotation ranges of motion.",
            "Analyzing body recovery speed post-overhead smash execution.",
            "Designing stretching programs to enhance thoracic flexibility."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Biomechanics_Backhand_Clear",
        "title": "Thoracic Spine Biomechanics in Late Backhand Off-balance Clears",
        "outline": [
            "Tracking spinal rotation angles in deep backhand corners.",
            "Evaluating thoracic reach capacity during late shuttle contacts.",
            "Strengthening core obliques to support off-balance rotation."
        ]
    },
    {
        "filename": "Topic_L3_AB_Lumbar_Thoracic_Splinting",
        "title": "Lumbar-Thoracic Core Splinting Under High Acceleration",
        "outline": [
            "Evaluating core muscle co-contraction to stabilize the spine.",
            "Preventing dynamic spine shear forces during fast lunges.",
            "Training athletic core stability using target weight exercises."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Extension_Steep_Angles",
        "title": "Thoracic Spine Extension and Rotation for Steep Smash Angles",
        "outline": [
            "Measuring spine extension angles during high overhead smashes.",
            "Correlating spine extension with steep shuttle downward angles.",
            "Safeguarding lower back health through thoracic extension mobility."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Mobility_Back_Strain",
        "title": "Preventing Lower Back Strain via Thoracic Mobility Exercises",
        "outline": [
            "Screening thoracic hypomobility as a cause of lumbar strain.",
            "Implementing rotational mobility drills in daily warm-ups.",
            "Managing training volumes to protect tired core muscles."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Kinematics_Deep_Lifts",
        "title": "Thoracic Spine Kinematics in Return of Deep Overhead Lifts",
        "outline": [
            "Tracking spine adjustments under deep, defensive rear-court hits.",
            "Optimizing back-arch angles to maintain high clear returns.",
            "Correcting head tilt issues that affect visual tracking."
        ]
    },
    {
        "filename": "Topic_L3_AB_Axial_Twist_Velocity_Stiffness",
        "title": "Axial Twist Velocity and Core Stiffness at Shuttle Contact",
        "outline": [
            "Measuring pelvic-thoracic separation rotation speed at impact.",
            "Evaluating core bracing stiffness timings during smashes.",
            "Designing dynamic core drills to enhance axial twist power."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Power_Court_Reaches",
        "title": "Thoracic Power Generation in Forehand Court-Corner Reaches",
        "outline": [
            "Tracking trunk lateral rotation speed during wide forehand lunges.",
            "Optimizing body posture to support fast recovery footwork.",
            "Correcting balance loss via targeted core-oblique training."
        ]
    },
    {
        "filename": "Topic_L3_AB_Thoracic_Rotation_Wheelchair",
        "title": "Thoracic Rotation Demands in Wheelchair Badminton Strokes",
        "outline": [
            "Measuring spinal rotation restrictions due to wheelchair strapping.",
            "Optimizing upper body twist to generate stroke power without legs.",
            "Strengthening latissimus dorsi and obliques for wheelchair players."
        ]
    },
    {
        "filename": "Topic_L3_AB_Postural_Alignment_Thoracic_Rotation",
        "title": "Postural Alignment and Thoracic Rotation Efficiency",
        "outline": [
            "Evaluating impact of head posture on thoracic rotation speed.",
            "Correcting round-shoulder postures to expand chest draw capacity.",
            "Tracking alignment changes during long endurance practices."
        ]
    },
    {
        "filename": "Topic_L3_AB_Wrist_Flexion_Velocity",
        "title": "Wrist Flexion Velocity and Dynamic Racket Face Angle control",
        "outline": [
            "Measuring wrist flexion speed at high-frequency racket impacts.",
            "Controlling racket face angles to alter shuttle flight paths.",
            "Designing strength drills for wrist flexor and extensor muscles."
        ]
    },
    {
        "filename": "Topic_L3_AB_Knee_Joint_Flexion_Angles",
        "title": "Knee Joint Flexion Angles in Defensive Lunge Recovery",
        "outline": [
            "Tracking knee flexion angles during deep defensive lunges.",
            "Identifying optimal knee flexion angles to support fast recovery.",
            "Correcting over-flexion (knee past toe) that increases patellar stress."
        ]
    },
    {
        "filename": "Topic_L3_AB_Hip_Extension_Power",
        "title": "Hip Extension Power in Rebounding After Deep Lunges",
        "outline": [
            "Measuring gluteus maximus force generation during lunge recovery.",
            "Optimizing step push-off sequences to speed up baseline returns.",
            "Designing plyometric exercises to build explosive hip power."
        ]
    },
    {
        "filename": "Topic_L3_AB_Plantarflexion_Achilles_Energy",
        "title": "Plantarflexion and Achilles Tendon Energy Storage in Jump Smashes",
        "outline": [
            "Evaluating calf activation and ankle plantarflexion speed.",
            "Utilizing Achilles tendon elasticity for vertical jump height.",
            "Preventing tendon strain through eccentric ankle strengthening."
        ]
    },
    {
        "filename": "Topic_L3_AB_Aerodynamic_Drag_Constraints",
        "title": "Aerodynamic Drag and Torque Constraints of the Badminton Racket",
        "outline": [
            "Analyzing drag force profiles of racket frame profiles under speed.",
            "Measuring air resistance effects on racket head acceleration.",
            "Selecting racket frame geometries that minimize swing drag."
        ]
    },
    {
        "filename": "Topic_L3_AB_Grip_Diameter_Torque_Flexion",
        "title": "Grip Diameter Effects on Wrist Torque and Flexion Speed",
        "outline": [
            "Comparing hand muscle activation levels across various grip sizes.",
            "Correlating grip diameter with wrist flexion range of motion.",
            "Optimizing grip setups to support finger-control adjustments."
        ]
    },
    {
        "filename": "Topic_L3_AB_Tibial_Rotation_Torque",
        "title": "Tibial Rotation Torque in High-Friction Lateral Cuts",
        "outline": [
            "Measuring knee rotation stress during fast, lateral changes of direction.",
            "Evaluating shoes and court surfaces for safe traction balance.",
            "Preventing meniscus injuries via lateral knee control training."
        ]
    },
    {
        "filename": "Topic_L3_AB_Patellofemoral_Joint_Stress",
        "title": "Patellofemoral Joint Stress in Forward Lunge Biomechanics",
        "outline": [
            "Tracking kneecap pressure paths under high deceleration lunges.",
            "Evaluating patellar tracking stability during unilateral landings.",
            "Designing quadriceps strengthening protocols for knee safety."
        ]
    },
    {
        "filename": "Topic_L3_AB_Ankle_Inversion_Angles",
        "title": "Ankle Inversion Angles and Sprain Prevention in Court Footwork",
        "outline": [
            "Measuring lateral ankle roll angles during fast direction changes.",
            "Strengthening peroneal muscles to prevent inversion sprains.",
            "Evaluating brace and taping effects on ankle mobility and safety."
        ]
    },
    {
        "filename": "Topic_L3_AB_Head_Neck_Stabilization",
        "title": "Head and Neck Stabilization Kinematics During Fast Rallies",
        "outline": [
            "Tracking head position stability during fast lateral movements.",
            "Analyzing visual stabilization efficiency post-split step landing.",
            "Strengthening neck muscles to prevent fatigue-related coordination loss."
        ]
    },
    {
        "filename": "Topic_L3_AB_Elbow_Extension_Velocity",
        "title": "Elbow Extension Velocity and Joint Laxity in Defensive Blocks",
        "outline": [
            "Tracking elbow extension acceleration under fast smash defense.",
            "Identifying risk of joint hyper-extension during late block contacts.",
            "Strengthening triceps and biceps for joint protection."
        ]
    },

    # --- Category 5: Competition Coaching (CC) ---
    {
        "filename": "Topic_L3_CC_Interval_Communication_11_Point",
        "title": "Structural Communication Protocols for the 11-Point Interval",
        "outline": [
            "Allocating the 60-second break: Hydration, tactical review, mental check.",
            "Delivering concise feedback: One positive observation and one adjust.",
            "Managing communication tone based on athlete's anxiety levels."
        ]
    },
    {
        "filename": "Topic_L3_CC_Maximizing_Break_Time",
        "title": "Maximizing Information Delivery in 60-Second Breaks",
        "outline": [
            "Preparing key tactical messages before the interval begins.",
            "Using whiteboard visuals or tablet clips to clarify court targets.",
            "Ensuring player hydration and physical cooling are completed first."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidGame_Reframing_21_Point",
        "title": "21-Point Mid-Game Psychological Reframing Strategies",
        "outline": [
            "Helping players let go of previous set errors during the 120-second break.",
            "Re-focusing athlete attention on process goals for the next game.",
            "Implementing tactical resets to address opponent adjustments."
        ]
    },
    {
        "filename": "Topic_L3_CC_NonVerbal_Body_Language",
        "title": "Non-Verbal Cues and Body Language Management During Intervals",
        "outline": [
            "Maintaining calm, confident posture to stabilize the athlete's mood.",
            "Reading player body language to gauge exhaustion or panic.",
            "Using physical contact (e.g., shoulder pat) to reassure the player."
        ]
    },
    {
        "filename": "Topic_L3_CC_Three_Actionable_Directives",
        "title": "Delivery of Three Actionable Tactical Directives in Intervals",
        "outline": [
            "Filtering complex match analysis into three clear instructions.",
            "Structuring instructions with actionable verbs (e.g., lift, attack, drop).",
            "Checking player understanding via quick questions before court return."
        ]
    },
    {
        "filename": "Topic_L3_CC_Interval_Singles_vs_Doubles",
        "title": "Tailoring Interval Communication: Singles vs. Doubles",
        "outline": [
            "Managing communication split between doubles partners to avoid confusion.",
            "Addressing individual singles focus vs. doubles partner chemistry.",
            "Resolving team disagreements on tactical execution in intervals."
        ]
    },
    {
        "filename": "Topic_L3_CC_Deescalating_Player_Anxiety",
        "title": "De-escalating Player Anxiety and Panicked States in Intervals",
        "outline": [
            "Using slow, controlled vocal delivery to soothe anxious players.",
            "Directing player focus to slow diaphragmatic breathing.",
            "Reframing high stakes into simple, manageable technical steps."
        ]
    },
    {
        "filename": "Topic_L3_CC_Strategic_Hydration_Reinforcement",
        "title": "Strategic Use of Hydration and Toweling Time for Tactical Reinforcement",
        "outline": [
            "Integrating tactical advice during quick court cleaning breaks.",
            "Teaching players to use towel-wiping pauses to slow match tempo.",
            "Establishing non-verbal signaling protocols for mid-game breaks."
        ]
    },
    {
        "filename": "Topic_L3_CC_Interval_Coaching_Para",
        "title": "Communication Adaptations for Para-Badminton Interval Coaching",
        "outline": [
            "Addressing wheelchair positioning and strapping adjustments during breaks.",
            "Vocal and visual adaptations for athletes with sensory challenges.",
            "Managing recovery times for athletes with different physical needs."
        ]
    },
    {
        "filename": "Topic_L3_CC_Feedback_Timing_Intervals",
        "title": "Feedback Timing: Immediate vs. Delayed Correction in Intervals",
        "outline": [
            "Deciding when to give immediate feedback vs. letting players rest.",
            "Avoiding overload by holding technical corrections for post-match reviews.",
            "Prioritizing tactical and emotional adjustments in intervals."
        ]
    },
    {
        "filename": "Topic_L3_CC_Player_Focus_External_Factors",
        "title": "Managing Player Focus on External Factors During Intervals",
        "outline": [
            "Redirecting player attention away from poor referee calls.",
            "Addressing distractions from court drift, lighting, or spectator noise.",
            "Re-focusing players on variables they can control (tactics, effort)."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Defensive_Gaps",
        "title": "Identifying and Exploiting Mid-Match Defensive Gaps",
        "outline": [
            "Spotting shifts in opponent court positioning during match play.",
            "Directing attacks to newly exposed defensive areas (e.g., body shots).",
            "Adjusting player position to anticipate opponent defensive blocks."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Tempo_Speed_Profiles",
        "title": "Adjusting Rally Tempo and Speed Profiles Mid-Match",
        "outline": [
            "Instructing players to slow rallies down using high clears and slow drops.",
            "Accelerating match pace via flat drives and early net-kill attacks.",
            "Managing match tempo to counter or exploit player fatigue."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Service_Variation",
        "title": "Countering Opponent Service Variation Adjustments",
        "outline": [
            "Spotting patterns in opponent serve variations mid-match.",
            "Adjusting return stance width and racket height to counter serves.",
            "Using deceptive returns to neutralize opponent server advantage."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Doubles_Rotations",
        "title": "Modifying Doubles Rotations Based on Opponent Target Shift",
        "outline": [
            "Adjusting front-back rotations if opponents target a single partner.",
            "Implementing side-by-side defensive shifts to cover wide gaps.",
            "Improving communication protocols between partners mid-match."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Environmental_Conditions",
        "title": "Adjusting Tactical Plans Under Extreme Environmental Conditions",
        "outline": [
            "Modifying clear depth to account for changing draft strengths.",
            "Adapting court placement strategies for hot vs. cold halls.",
            "Selecting appropriate shuttle speeds during environmental shifts."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Attacking_Defensive_Drift",
        "title": "Mid-Match Transitions from Offensive to Defensive Drift Play",
        "outline": [
            "Adjusting smash intensity when playing with a strong tailwind.",
            "Transitioning to tight drops and blocks when attacking is difficult.",
            "Using high, defensive clears to manage drift when defending."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_LeftHanded_Adjustments",
        "title": "Tactical Shifts for Left-Handed Opponent Adjustments",
        "outline": [
            "Directing lifts and clears to the left-hander's backhand corner.",
            "Adjusting defensive block angles to counter left-handed smash spins.",
            "Modifying doubles rotation positions for left-handed opponents."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_GameTwo_Loss_Shifts",
        "title": "Modifying Shot Selection Patterns in Game Two After Loss",
        "outline": [
            "Analyzing why game one was lost (errors, pace, tactics).",
            "Implementing game plan shifts (e.g., moving from drives to drops).",
            "Managing player focus during early stages of the second game."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_JumpSmash_Dominant",
        "title": "Defending Against the Jump-Smash Dominant Player Mid-Match",
        "outline": [
            "Restricting lift depth and heights to prevent comfortable smashes.",
            "Positioning defenders deeper to manage high-speed smashes.",
            "Using flat, fast drives to jam the attacker's shoulder movement."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Return_Positioning",
        "title": "Strategic Shifts in Service Return Positioning",
        "outline": [
            "Moving forward to intercept short serves early.",
            "Adjusting stance back to handle high flick serve frequency.",
            "Altering weight distribution to counter deceptive serve angles."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Net_Trickery",
        "title": "Countering Opponent Net Trickery and Spin Play",
        "outline": [
            "Avoiding low, tumbling net exchanges; lifting to safety.",
            "Anticipating cross-court net spins by reading racket face angles.",
            "Using early racket prep to challenge opponent net domination."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Fatigue_Mobility_Loss",
        "title": "Tactical Adaptations for Fatigue-Induced Mobility Loss",
        "outline": [
            "Transitioning to high-efficiency, low-energy recovery paths.",
            "Using deceptive drops and clears to move opponents without sprinting.",
            "Managing match tempo to maximize player recovery times."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_High_Drift_Halls",
        "title": "Adjusting Shot Heights and Depth in High-Drift Halls",
        "outline": [
            "Using low, flat trajectories to bypass strong crosswinds.",
            "Restricting lift heights to prevent shuttle drift out of bounds.",
            "Exploiting drift-induced errors by forcing opponent lifts."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Mens_Doubles_Flat",
        "title": "Mid-Match Counter-Strategies for Men's Doubles Flat Rallies",
        "outline": [
            "Slowing flat exchanges using soft, drop-like block adjustments.",
            "Lifting high to reset rally when flat speed becomes unmanageable.",
            "Intercepting mid-court drives to take offensive control."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_String_Changes",
        "title": "Adapting Match Tactics to Sudden Racket/String Changes",
        "outline": [
            "Adapting to tension differences when using backup rackets.",
            "Adjusting drop shot force to match new string repulsion profiles.",
            "Restoring player confidence after sudden mid-rally string breaks."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Pacing_Delays",
        "title": "Psychological Play: Initiating Delays and Tempo Shifts Legally",
        "outline": [
            "Asking to wipe court or check shuttle to break opponent run.",
            "Taking full allowed time (20 seconds) between points to slow play.",
            "Communicating with partner in doubles to break opponent momentum."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Interceptions",
        "title": "Disrupting Opponent Rhythm via Mid-Court Interceptions",
        "outline": [
            "Positioning players forward to cut off slow cross drives.",
            "Using aggressive racket positioning to pressure opponent clears.",
            "Training quick reflexes for mid-court flat exchanges."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Wheelchair_NetPlay",
        "title": "Mid-Match Adjustments for Wheelchair Net Play Domination",
        "outline": [
            "Using short, tight spinning net shots to limit wheelchair reach.",
            "Exploiting front-court angles that force diagonal movement.",
            "Adapting serve returns to prevent early net control."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Standing_Para_Targets",
        "title": "Exploiting Target Areas in Standing Para-Badminton Matches",
        "outline": [
            "Directing shots to prosthetic or impaired limb reach limits.",
            "Forcing deep-to-front court movements to test balance bounds.",
            "Adapting placement based on standing opponent's classification."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Mixed_Doubles_Tactics",
        "title": "Tactical Refinements in Mixed Doubles Match Play",
        "outline": [
            "Targeting the female player at the net to draw errors.",
            "Lifting to the male player to test physical smash limits.",
            "Improving partner coordination to prevent mid-court confusion."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_CounterAttack_Disruption",
        "title": "Analyzing and Disrupting Opponent Counter-Attacking Patterns",
        "outline": [
            "Identifying common setup shots that trigger opponent counter-attacks.",
            "Using defensive net blocks to neutralize counter-attacking pace.",
            "Varying shot speeds to prevent opponent from settling into counter patterns."
        ]
    },
    {
        "filename": "Topic_L3_CC_MidMatch_Crosswind_Defense",
        "title": "Adapting Defense Formations to High-Drift Crosswinds",
        "outline": [
            "Shifting defensive stance slightly to the windward side of the court.",
            "Directing defense lifts to drift-assisted safe zones.",
            "Predicting opponent smash paths based on crosswind angles."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Psychological_Warmups",
        "title": "Designing Personalized Pre-Match Psychological Warm-ups",
        "outline": [
            "Creating customized mental routines matching player anxiety profiles.",
            "Combining positive self-talk with short visualization sequences.",
            "Structuring warm-ups to ease anxiety and focus the athlete's mind."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Breathing_Stabilization",
        "title": "Implementing Controlled Breathing for Heart Rate Stabilization",
        "outline": [
            "Using slow box-breathing (4s inhale, 4s hold, 4s exhale, 4s hold).",
            "Using breathing techniques to lower pre-match heart rates.",
            "Fostering parasympathetic nervous system activation before entering court."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Cognitive_SelfTalk",
        "title": "Cognitive Reframing and Positive Self-Talk Protocols",
        "outline": [
            "Identifying negative self-talk patterns under high stress.",
            "Replacing anxiety-driven statements with constructive, process-focused cues.",
            "Developing short personal cue phrases to boost confidence."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_PPR_HighStakes",
        "title": "Pre-Performance Routines for High-Stakes Finals",
        "outline": [
            "Standardizing warm-up timelines: Physical, cognitive, tactical.",
            "Restricting distractions from media and visitors near match time.",
            "Developing exit routines to help players recover from finals pressure."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Sensory_Deprivation",
        "title": "Sensory Deprivation and Focus Restructuring Pre-Match",
        "outline": [
            "Using noise-canceling headphones to block out stadium noise.",
            "Creating a quiet private space to help players focus.",
            "Restricting social media use on competition days to maintain focus."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Auditory_Pacing",
        "title": "Music and Auditory Pacing in Pre-Match Routines",
        "outline": [
            "Selecting music tracks to adjust athlete arousal levels.",
            "Matching beat pacing (BPM) with desired movement speed.",
            "Using auditory cues to trigger positive performance states."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_CallRoom_Distractions",
        "title": "Managing Distractions in the Call Room and Warm-Up Areas",
        "outline": [
            "Preparing players for call room procedures and waiting times.",
            "Using cognitive exercises to maintain focus during delays.",
            "Ignoring opponent behaviors and mental games in the call room."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Visualization_Scenarios",
        "title": "Visualizing Technical Execution and Rally Scenarios",
        "outline": [
            "Guiding athletes through vivid visualization of perfect strokes.",
            "Simulating recovery and adaptation during challenging points.",
            "Fostering kinesthetic imagery to prime neuromuscular pathways."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Cue_Words",
        "title": "Establishing Pre-Match Behavioral Anchors and Cue Words",
        "outline": [
            "Selecting simple cue words that trigger desired movement styles.",
            "Correlating cues with physical triggers (e.g. racket tap).",
            "Integrating cue phrases during physical warm-up sets."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Coach_Induced_Pressure",
        "title": "Managing Coach-Induced Pressure and Expectations",
        "outline": [
            "Ensuring coach communication remains focused on athlete welfare.",
            "Avoiding output expectations; emphasizing performance targets.",
            "Providing a calm environment for the player before matches."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Doubles_Alignment",
        "title": "Pre-Match Routines for Doubles Partners: Alignment Strategies",
        "outline": [
            "Conducting shared tactical and coordinate planning meetings.",
            "Structuring verbal and non-verbal routines to align partner focus.",
            "Managing differences in partner anxiety levels through cooperation."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Sleep_Rest_24h",
        "title": "Sleep and Rest Management in the 24 Hours Pre-Match",
        "outline": [
            "Optimizing pre-match sleep duration and room conditions.",
            "Managing light rest periods on double-competition days.",
            "Managing pre-competition anxiety to prevent sleep issues."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Hydrotherapy_Activation",
        "title": "Hydrotherapy and Physical Activation Protocols in Pre-Match",
        "outline": [
            "Using warm showers or light pool work to ease muscle stiffness.",
            "Structuring physical activation routines post-hydrotherapy.",
            "Balancing hydrotherapy duration to prevent muscle relaxation."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Media_Access",
        "title": "Managing Media Access and Interviews Pre-Competition",
        "outline": [
            "Setting guidelines for media access before tournament matches.",
            "Preparing players with simple responses for common press questions.",
            "Protecting athletes from negative media reporting."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Para_Wheelchair",
        "title": "Pre-Match Routines for Para-Badminton Wheelchair Athletes",
        "outline": [
            "Conducting wheelchair mechanical and tire pressure checks.",
            "Adjusting strapping and positioning for optimal comfort.",
            "Designing specific physical warm-ups for wheelchair players."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Nutrition_Glycogen",
        "title": "Nutritional Timing and Glycogen Priming Pre-Match",
        "outline": [
            "Structuring high-carbohydrate meals 3-4 hours before the match.",
            "Timing energy gel intake during the warm-up window.",
            "Monitoring hydration status to prevent pre-match cramping."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Schedule_Delays",
        "title": "Handling Sudden Schedule Delays or Court Changes",
        "outline": [
            "Maintaining flexible physical and mental warm-up plans.",
            "Using relaxation techniques during extended delay periods.",
            "Adapting to venue changes without losing focus."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Somatosensory_Exercises",
        "title": "Somatosensory Releasing Exercises for Muscle Tension Relief",
        "outline": [
            "Using progressive muscle relaxation to lower physical tension.",
            "Implementing light massage or shaking drills in the warm-up.",
            "Releasing muscle stiffness to support smooth coordination."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Team_Culture_Pressure",
        "title": "Building Collective Team Culture and Pressure Shielding",
        "outline": [
            "Fostering team support networks to shield individual players.",
            "Creating shared goals to promote team alignment.",
            "Using team meetings to resolve performance-related conflicts."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Dynamic_ROM_Activation",
        "title": "Pre-Match Dynamic Range of Motion Activation",
        "outline": [
            "Structuring dynamic stretches for major joints (shoulder, hip, ankle).",
            "Gradually increasing movement speeds during the warm-up.",
            "Integrating badminton-specific footwork to prime muscles."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Choking_Focus_Shifts",
        "title": "Countering Choking Under Pressure: Focus Shifts",
        "outline": [
            "Identifying psychological triggers of choking under pressure.",
            "Shifting focus from outcome anxiety to technical actions.",
            "Using breathing patterns to lower high physical arousal."
        ]
    },
    {
        "filename": "Topic_L3_CC_PreMatch_Coaches_Checklist",
        "title": "Pre-Match Checklist for Coaches: Equipment and Logistics",
        "outline": [
            "Verifying rackets, shoes, clothing, and energy drinks are ready.",
            "Checking tournament schedules, court numbers, and opponent details.",
            "Preparing backup equipment and emergency medical supplies."
        ]
    },

    # --- Category 6: Advanced Physiology (AP) ---
    {
        "filename": "Topic_L3_AP_VO2_Max_Testing_Protocols",
        "title": "Badminton-Specific Incremental VO2 Max Testing Protocols",
        "outline": [
            "Designing on-court shuttle run tests to measure aerobic capacity.",
            "Tracking oxygen consumption (VO2) using portable gas analyzers.",
            "Benchmarking maximum heart rates during exhausting court drills."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_Singles_Elite",
        "title": "Analyzing VO2 Max and Aerobic Capacity for Elite Singles",
        "outline": [
            "Correlating VO2 max scores with player recovery speeds.",
            "Measuring differences in aerobic demands for singles vs. doubles.",
            "Integrating VO2 max benchmarks in high-performance profiles."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_OnCourt_Gas",
        "title": "Utilizing On-Court Gas Analysis Systems in Testing",
        "outline": [
            "Calibrating portable metabolic carts for active court movements.",
            "Measuring breathing frequency and oxygen intake in drills.",
            "Using gas analysis results to design custom fitness plans."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_Recovery_Correlation",
        "title": "Correlating VO2 Max Performance with Core Recovery Rates",
        "outline": [
            "Evaluating oxygen debt recovery times post-shuttle drills.",
            "Correlating VO2 max levels with heart rate drop speeds.",
            "Using aerobic fitness indicators to guide training density choices."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_HRV_Correlation",
        "title": "Heart Rate Variability Correlation with VO2 Max Benchmarks",
        "outline": [
            "Tracking rest HRV changes alongside VO2 max progression.",
            "Evaluating autonomic nervous recovery post-aerobic efforts.",
            "Using HRV-VO2 metrics to adjust weekly training loads."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_Oxygen_Limits",
        "title": "Physiological Limits of Oxygen Delivery in Long Rallies",
        "outline": [
            "Analyzing capillary density and muscle oxygenation in players.",
            "Identifying cardiorespiratory limits under high fatigue states.",
            "Designing training routines to improve oxygen delivery speeds."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_PreSeason_Conditioning",
        "title": "Integrating VO2 Max Benchmarks in Pre-Season Training",
        "outline": [
            "Establishing baseline VO2 max scores before starting pre-season.",
            "Designing periodized programs to build a solid aerobic base.",
            "Re-testing fitness levels to measure training program success."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_Aerobic_Improvement",
        "title": "Aerobic Conditioning Protocols to Improve Badminton VO2 Max",
        "outline": [
            "Structuring high-intensity interval training (HIIT) for court play.",
            "Using off-court running/cycling to build cardiorespiratory base.",
            "Monitoring training zone times using telemetry systems."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_Singles_vs_Doubles",
        "title": "Comparing Aerobic Capacities of Singles vs. Doubles Players",
        "outline": [
            "Analyzing VO2 max score differences between disciplines.",
            "Measuring cardiorespiratory load differences in matches.",
            "Designing fitness routines matching specific discipline needs."
        ]
    },
    {
        "filename": "Topic_L3_AP_VO2_Max_Youth_Standards",
        "title": "Age-Group VO2 Max Standards for National Team Pathways",
        "outline": [
            "Establishing VO2 max benchmarks for U15, U17, and U19 players.",
            "Adjusting physical targets to match somatic maturation speeds.",
            "Using fitness database metrics to find high-potential talents."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Profiling_Drills",
        "title": "Blood Lactate Profiling During Badminton-Specific Drills",
        "outline": [
            "Measuring blood lactate levels post-intensive court drills.",
            "Profiling individual player lactate accumulation curves.",
            "Using lactate test results to determine training intensity zones."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Threshold_Mapping",
        "title": "Lactate Threshold 1 and Lactate Threshold 2 Mapping",
        "outline": [
            "Identifying aerobic and anaerobic thresholds via blood testing.",
            "Correlating threshold heart rates with on-court movements.",
            "Designing training sessions to extend the anaerobic threshold."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Clearance_Recovery",
        "title": "Lactate Clearance Rates Recovery Strategies Between Games",
        "outline": [
            "Measuring lactate clearance times during low-intensity active recovery.",
            "Evaluating massage and hydration effects on lactate clearance.",
            "Optimizing recovery choices in the 120-second break between sets."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Testing_Multifeeder",
        "title": "On-Court Lactate Testing Protocols for Multifeeder Work",
        "outline": [
            "Standardizing blood sampling times during multifeeder drills.",
            "Correlating lactate spikes with shuttle feeding frequencies.",
            "Using multifeeder load tests to evaluate anaerobic endurance."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Buffer_Nutrition",
        "title": "Nutritional Interventions to Buffer Blood Lactate Accumulation",
        "outline": [
            "Using sodium bicarbonate to buffer metabolic acid accumulation.",
            "Timing beta-alanine supplementation to boost muscle carnosine.",
            "Managing nutrition plans to support high-intensity efforts."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Training_Intensity",
        "title": "Adjusting Training Intensities Based on Blood Lactate Curves",
        "outline": [
            "Evaluating lactate variations across different training blocks.",
            "Modifying court drill speeds to target specific metabolic paths.",
            "Preventing overtraining using regular lactate monitoring."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Anaerobic_Glycolytic",
        "title": "Anaerobic Capacity Profiling via Lactate",
        "outline": [
            "Measuring peak lactate levels after short, high-intensity efforts.",
            "Evaluating glycolytic system power in elite players.",
            "Designing targeted speed-endurance sessions based on profiling."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_HIIT_Response",
        "title": "Blood Lactate Response to High-Intensity Interval Training",
        "outline": [
            "Tracking lactate levels across different HIIT configurations.",
            "Adjusting work-to-rest ratios to manage metabolic stress.",
            "Evaluating adaptation progress using longitudinal lactate testing."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Buffering_Periodization",
        "title": "Lactate Buffering Capacity Improvements through Periodization",
        "outline": [
            "Structuring training blocks to improve cellular buffering systems.",
            "Combining physical training with nutrition buffering programs.",
            "Re-testing buffering capacity using standardized trial sets."
        ]
    },
    {
        "filename": "Topic_L3_AP_Lactate_Smash_vs_Net",
        "title": "Blood Lactate Comparison in Hard Smashes vs. Net Rallies",
        "outline": [
            "Measuring metabolic demand differences across stroke types.",
            "Correlating energy system use with specific match tactics.",
            "Designing discipline-specific conditioning plans based on results."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Demand_Profiles",
        "title": "High-Performance Metabolic Demand Profiles of Badminton Matches",
        "outline": [
            "Tracking energy demands during elite badminton matches.",
            "Measuring aerobic vs. anaerobic contributions across long sets.",
            "Designing fitness plans matching specific metabolic profiles."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_ATP_CP_Demands",
        "title": "Anaerobic Alactic Demands in Short Explosive Rallies",
        "outline": [
            "Measuring ATP-CP system use during short, powerful rallies.",
            "Evaluating muscle power recovery speeds between rallies.",
            "Designing speed and agility drills to train alactic power."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Lactic_Extended_Rallies",
        "title": "Anaerobic Lactic Demands in Extended High-Intensity Rallies",
        "outline": [
            "Analyzing anaerobic glycolysis use during long rallies.",
            "Evaluating muscle fatigue and acidosis under metabolic load.",
            "Designing drills to build tolerance to metabolic acid build-up."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Energy_System_Ratios",
        "title": "Energy System Contribution Ratios in Elite Matchplay",
        "outline": [
            "Quantifying aerobic, anaerobic lactic, and alactic energy ratios.",
            "Evaluating system ratio changes across three-set matches.",
            "Designing training sessions targeting all three energy systems."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Glycogen_Depletion",
        "title": "Calculating Glycogen Depletion Rates in Tournament Matches",
        "outline": [
            "Estimating muscle glycogen depletion during consecutive match days.",
            "Designing carbohydrate intake schedules to restore glycogen levels.",
            "Preventing fatigue-related performance drops using nutrition support."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Substrate_Utilization",
        "title": "Substrate Utilization During Long Matches",
        "outline": [
            "Measuring shifts between carbohydrate and fat use during play.",
            "Correlating substrate shifts with player fitness and endurance.",
            "Using nutrition interventions to preserve carbohydrate stores."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Caloric_Expenditure",
        "title": "Caloric Demand and Energy Expenditure Profiles of Elite Players",
        "outline": [
            "Estimating hourly caloric burn rates in intensive tournament play.",
            "Designing meal plans to match high daily energy outputs.",
            "Preventing energy deficits that slow recovery and cause injury."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Core_Temperature_Heat",
        "title": "Hydration Status and Core Body Temperature in High Heat Matches",
        "outline": [
            "Monitoring core body temperature rises in hot tournament halls.",
            "Evaluating dehydration impact on physical speed and decision making.",
            "Implementing court-side cooling protocols to manage core heat."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Electrolyte_Replacement",
        "title": "Electrolyte Loss Profiles and Targeted Replacement Strategies",
        "outline": [
            "Measuring sodium, potassium, and magnesium losses in sweat.",
            "Designing custom electrolyte drinks to prevent dehydration cramping.",
            "Monitoring hydration status using body weight pre-post match checks."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_CK_Cortisol_Damage",
        "title": "Biomarkers of Muscle Damage in Multi-Day Events",
        "outline": [
            "Tracking creatine kinase (CK) and cortisol changes during events.",
            "Correlating biomarker spikes with physical fatigue and muscle soreness.",
            "Adjusting recovery protocols based on physiological damage markers."
        ]
    },
    {
        "filename": "Topic_L3_AP_Metabolic_Para_Wheelchair",
        "title": "Metabolic Demands of Wheelchair Para-Badminton Play",
        "outline": [
            "Measuring oxygen intake and heart rate demands in wheelchair play.",
            "Evaluating upper-body muscle fatigue rates during matches.",
            "Designing fitness programs matching specific wheelchair demand profiles."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_CWI_Protocols",
        "title": "Cold Water Immersion Protocols for Post-Match Recovery",
        "outline": [
            "Setting optimal water temperatures (10-15C) and immersion times (10-15m).",
            "Evaluating cold water immersion effects on post-match muscle soreness.",
            "Integrating cold water recovery in multi-day tournament schedules."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_CWT_Sequencing",
        "title": "Contrast Water Therapy Sequencing and Temperature Ratios",
        "outline": [
            "Setting hot (38-40C) and cold (10-12C) water cycle ratios.",
            "Evaluating contrast therapy effects on blood flow and recovery speed.",
            "Designing contrast water routines for post-travel muscle recovery."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_Active_Hydrotherapy",
        "title": "Active Hydrotherapy: Low-Intensity Pool Work for Regeneration",
        "outline": [
            "Structuring low-impact swimming and stretching sessions in pool.",
            "Using water pressure to reduce joint swelling and muscle tightness.",
            "Scheduling active pool sessions on rest days between matches."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_DOMS_Reduction",
        "title": "Physiological Mechanism of Hydrotherapy in Reducing DOMS",
        "outline": [
            "Analyzing how water pressure and temperature reduce inflammation.",
            "Correlating hydrotherapy with faster muscle strength recovery.",
            "Comparing hydrotherapy options with standard passive rest recovery."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_Tournament_Timelines",
        "title": "Designing Tournament Hydrotherapy Timelines for Tight Schedules",
        "outline": [
            "Scheduling hydrotherapy sessions within 60 minutes of match finish.",
            "Coordinating hydrotherapy with nutrition and physical massage timelines.",
            "Managing travel times to recovery facilities during busy tournaments."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_Hyperbaric_vs_Hydro",
        "title": "Hyperbaric Oxygen Therapy vs. Hydrotherapy for Recovery",
        "outline": [
            "Evaluating hyperbaric oxygen therapy effects on muscle repair.",
            "Comparing cost, availability, and recovery speeds of both modalities.",
            "Integrating hyperbaric therapy for acute muscle injury recovery."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_Hydrotherapy_PostTravel",
        "title": "Hydrotherapy Adaptations for Elite Athletes Post-Travel",
        "outline": [
            "Using warm contrast baths to reduce flight-induced stiffness.",
            "Adjusting water temperatures to help reset circadian rhythm sleep.",
            "Restoring joint range of motion through light pool stretching."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_Hydrotherapy_Safety",
        "title": "Contraindications and Safety Standards for Hydrotherapy Protocols",
        "outline": [
            "Screening players for open cuts, skin issues, or heart concerns.",
            "Monitoring water cleanliness and chlorine levels to prevent infection.",
            "Training players on safe temperature transitions during contrast therapy."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_Hydrotherapy_Mobility",
        "title": "Combining Hydrotherapy with Active Mobility Protocols",
        "outline": [
            "Integrating light joint mobilization stretches in warm water.",
            "Using water buoyancy to support pain-free mobility routines.",
            "Structuring warm-up dynamic stretches post-hydrotherapy."
        ]
    },
    {
        "filename": "Topic_L3_AP_Recovery_Hydrotherapy_Biomarkers",
        "title": "Hydrotherapy Effectiveness on Cardiovascular Recovery Biomarkers",
        "outline": [
            "Tracking heart rate variability (HRV) changes post-hydrotherapy.",
            "Measuring blood pressure and heart rate drops during recovery.",
            "Correlating physiological markers with subjective recovery scores."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_CMJ_Fatigue",
        "title": "Neuromuscular Fatigue Monitoring: Countermovement Jump",
        "outline": [
            "Measuring jump height and takeoff force on force plates daily.",
            "Identifying nervous system fatigue using flight-time-to-contraction ratios.",
            "Adjusting weekly training volumes based on jump performance changes."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_IMTP_Force",
        "title": "Isometric Mid-Thigh Pull for Rate of Force Development",
        "outline": [
            "Standardizing testing setups for the isometric mid-thigh pull.",
            "Measuring peak force and rate of force development (RFD).",
            "Correlating lower body strength metrics with jump smash power."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Protein_Repair",
        "title": "Periodized Protein Intake for Muscle Repair in Elite Training",
        "outline": [
            "Structuring protein dose timing (e.g. 20-30g every 3-4 hours) for repair.",
            "Selecting protein sources (whey, casein) to optimize recovery phases.",
            "Timing protein intake before sleep to support overnight muscle recovery."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Supplements_Anaerobic",
        "title": "Beta-Alanine and Creatine Supplementation for Anaerobic Buffering",
        "outline": [
            "Structuring loading and maintenance doses for creatine monohydrate.",
            "Timing beta-alanine intake to prevent skin tingling issues.",
            "Monitoring supplement effects on power and lean muscle mass."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Heat_Shock_Adaptation",
        "title": "Heat Shock Proteins and Thermoregulation Training Adaptations",
        "outline": [
            "Using sauna or hot bath sessions post-training to trigger heat shock proteins.",
            "Fostering cardiorespiratory adaptation to high temperature matchplay.",
            "Monitoring sweat rate adaptations across thermal training programs."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Salivary_Stress_Load",
        "title": "Salivary Cortisol and Alpha-Amylase Profiling for Stress Load",
        "outline": [
            "Standardizing saliva collection timing during intensive camps.",
            "Correlating cortisol levels with athlete physical overtraining.",
            "Using stress marker data to adjust individual recovery plans."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Sleep_Stage_Recovery",
        "title": "Sleep Stage Optimization for Physiological Recovery",
        "outline": [
            "Tracking deep sleep and REM sleep times using smart wearables.",
            "Designing pre-bed routines to increase deep sleep recovery times.",
            "Managing tournament travel to protect players' sleep cycles."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Compression_Garments",
        "title": "Compression Garment Technology for Venous Return and Recovery",
        "outline": [
            "Selecting appropriate pressure levels for post-match wear.",
            "Evaluating compression garment effects on muscle swelling and pain.",
            "Designing compression wear schedules for long travel transit."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Dry_Needling",
        "title": "Dry Needling and Myofascial Release for Acute Muscle Tension",
        "outline": [
            "Using dry needling to release stubborn muscle trigger points.",
            "Coordinating myofascial release sessions with training timelines.",
            "Preventing muscle strain using targeted soft tissue therapies."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Pneumatic_Compression",
        "title": "Pneumatic Compression Therapy Protocols During Tournament Weeks",
        "outline": [
            "Setting appropriate cycle settings and pressures for recovery boots.",
            "Scheduling compression sessions post-match and travel transit.",
            "Comparing compression boots with active recovery walking."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_BFR_Hypertrophy",
        "title": "Blood Flow Restriction Training for Hypertrophy in Rehab",
        "outline": [
            "Setting safe pressure levels for occlusion cuffs during rehab.",
            "Designing low-load resistance exercises using BFR support.",
            "Preventing muscle loss during tendon/joint recovery phases."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Immune_Support_Nutrition",
        "title": "Nutritional Strategies for Immune Support During Tournaments",
        "outline": [
            "Supplementing with Vitamin D, Zinc, and Probiotics on tour.",
            "Managing carbohydrate intake to prevent post-match immune drops.",
            "Ensuring food safety and hygiene protocols during travel."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Iron_Status_Women",
        "title": "Iron Status and Ferritin Monitoring in Elite Women Athletes",
        "outline": [
            "Scheduling regular blood draws to monitor ferritin and iron levels.",
            "Designing nutrition plans to address iron deficiency without anemia.",
            "Correlating iron levels with fatigue and performance metrics."
        ]
    },
    {
        "filename": "Topic_L3_AP_Physiology_Oxidative_Stress_Antioxidants",
        "title": "Oxidative Stress Biomarkers and Antioxidant Timing Protocols",
        "outline": [
            "Measuring markers of free-radical cellular damage post-match.",
            "Timing dietary antioxidant intake to avoid blunting training adaptations.",
            "Selecting polyphenol-rich recovery foods for tournament weeks."
        ]
    }
]

# Write files
count = 0
for t in topics:
    filename = f"{t['filename']}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Check if file has duplicate name in the list (safety check)
    if os.path.exists(filepath):
        print(f"Warning: Duplicate detected for {filename}. Overwriting.")
        
    content = f"[[Level_3]]\n\n"
    content += f"# {t['title']}\n\n"
    content += f"## Structural Outline\n\n"
    for i, point in enumerate(t['outline'], 1):
        content += f"{i}. {point}\n"
    content += f"\n#llm-deep-backlog\n"
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Process complete. Generated exactly {count} micro-topic files inside '{output_dir}'.")
