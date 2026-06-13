import os
import re

def generate_periodization():
    subtopics = ["Macrocycles", "Mesocycles", "Microcycles", "Weekly Loads", "Recovery Cycles", "Competitive Tapering"]
    variations = [
        ("Elite Singles Players", "Focusing on individual court volume and aerobic base transitions.", "Optimizing tournament preparation and post-match recovery.", "Adjusting load based on heart rate variability (HRV) trends."),
        ("Junior Development Programs", "Structuring age-appropriate training intensity ratios.", "Balancing basic motor skill acquisition with tactical court practice.", "Preventing overload during school exams and growth spurts."),
        ("Masters Competitors", "Adapting volume to account for slower physiological recovery rates.", "Prioritizing joint preservation and tendon health in strength training.", "Implementing active recovery protocols to prevent injury."),
        ("Double Peak Seasons", "Structuring a split annual plan with shortened preparation phases.", "Managing high-intensity transition phases between competitive peaks.", "Optimizing supercompensation timing for two major tournaments."),
        ("High-Altitude Adaptation", "Designing the acclimatization phase to handle low oxygen partial pressure.", "Modifying training intensity targets during altitude blocks.", "Timing post-altitude descent for peak tournament readiness."),
        ("Pre-Season Base Building", "Accumulating general physical volume using off-court running.", "Establishing baseline strength and joint stability in weights.", "Reviewing basic stroke mechanics under low physiological fatigue."),
        ("In-Season Maintenance", "Preserving power and speed with low-volume, high-intensity workouts.", "Structuring brief tactical court sharpers between travel weeks.", "Monitoring player subjective readiness and wellness scores."),
        ("Transition Phase", "Integrating low-impact cross-training like swimming or cycling.", "Addressing minor joint imbalances and rehabilitation needs.", "Allowing complete physical and psychological decompression."),
        ("Tapering Phase Strategies", "Reducing weekly training volume by 40-60% while maintaining speed.", "Preserving racket feel and stroke timing with short drills.", "Enhancing neurological readiness and mental confidence."),
        ("School-Age High Performance Players", "Coordinating club, school, and regional training loads.", "Structuring intensive training camps during school breaks.", "Ensuring long-term athlete development (LTAD) principles are met.")
    ]
    
    results = []
    for sub in subtopics:
        for idx, (pop, p1, p2, p3) in enumerate(variations):
            title = f"{sub} for {pop}"
            safe_name = title.replace(" ", "_").replace("/", "_").replace("-", "_")
            results.append((title, safe_name, [p1, p2, p3]))
    return results

def generate_singles_tactics():
    results = []
    
    # Four Corners (12 topics)
    corners_focus = [
        ("Base Position and Center Court Control", "Optimizing footwork recovery paths to the exact court center.", "Using the split-step to prime explosive movement to any corner.", "Minimizing adjustment steps during recovery to conserve energy."),
        ("Deceptive Holding Shots to Corners", "Freezing the opponent at the center using a delayed racket sweep.", "Executing late wrist flicks to redirect the shuttle to rear corners.", "Disguising drop shots and clears with identical racket speed."),
        ("Crosscourt Transition Patterns", "Mastering footwork paths from deep backhand to forehand net.", "Applying chasse steps for rapid lateral and diagonal coverage.", "Maintaining body balance during extreme crosscourt lunging."),
        ("Exploiting the Deep Backhand Corner", "Applying pressure to the opponent's deep backhand corner.", "Exploiting weak backhand clears with decisive overhead smashes.", "Varying drop shots and slice angles to target the backhand line."),
        ("Attacking the Deep Forehand Corner", "Using fast punch clears to push the opponent deep and wide.", "Exploiting late racket preparation in the opponent's forehand rear.", "Following up with tight net drops to exploit the long recovery path."),
        ("Forehand Net to Backhand Rear Transitions", "Mastering the recovery step after a low forehand net shot.", "Pivoting and tracking backward to cover the deep backhand corner.", "Executing defensive clears when caught out of position."),
        ("Footwork Economy and Court Coverage", "Reducing unnecessary adjustment steps during court coverage.", "Utilizing sliding and lunging techniques to extend reach efficiently.", "Maintaining low center of gravity for faster change of direction."),
        ("Recovery to Home Base Dynamics", "Establishing the optimal recovery path after executing a rear court stroke.", "Varying the 'home' base position depending on the shot played.", "Anticipating the opponent's response before completing recovery."),
        ("Exploiting Movement Gaps", "Identifying slow recovery directions in the opponent's movement.", "Chaining shots to force consecutive movements to opposite corners.", "Utilizing sudden changes of direction to exploit poor footwork."),
        ("Underarm Recovery from Deep Corners", "Executing deep lunging steps with correct knee-toe alignment.", "Returning high, deep clears to buy recovery time.", "Handling late contact in deep corners without injuring the ankle."),
        ("Net Shot Tumbling and Net Coverage", "Slicing the shuttle at the net to generate unpredictable tumbling.", "Varying the height and spin of net shots to limit lift quality.", "Transitioning from tight spin shots to fast flat pushes."),
        ("Drills for Court Coverage and Agility", "Implementing random multi-shuttle feeding across all four corners.", "Using shadow footwork to reinforce efficient movement paths.", "Structuring endurance court coverage drills under fatigue.")
    ]
    for title_part, p1, p2, p3 in corners_focus:
        title = f"Singles Tactics: Four Corners - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Change of Pace (12 topics)
    pace_focus = [
        ("Dropshot Deceleration Mechanics", "Using identical preparation for clears and decelerating at contact.", "Executing slow drops to draw the opponent forward and disrupt rhythm.", "Varying slice angles to alter the shuttle's flight speed."),
        ("Half-Smash Variations and Placement", "Varying smash power between full, half, and stick smashes.", "Targeting the opponent's body or open spaces with medium pace.", "Recovering quickly for follow-up net play after a half-smash."),
        ("Attack Loft vs Drive Exchanges", "Alternating deep lifts with fast drives to test opponent reaction.", "Using flat drives to speed up the rally and pressure defense.", "Varying high defensive lifts to slow down the pace and recover."),
        ("Punch Clear Tactical Placements", "Executing flat, fast clears to catch the opponent off guard.", "Forcing late overhead contact by driving the shuttle behind them.", "Combining punch clears with tight drops to stretch the court."),
        ("Rhythm Disruption Strategies", "Alternating very fast rallies with high, slow defensive clears.", "Breaking the opponent's expected timing using deceptive holds.", "Varying serving speed and height to prevent comfortable returns."),
        ("Exploding from Slow Rallies to Attack", "Lulling the opponent into slow rallies before launching a sudden attack.", "Using explosive footwork to intercept slow drop shots early.", "Converting defensive baseline rallies into rapid net-kill attacks."),
        ("Deceptive Hold and Flick Execution", "Holding the racket shape at the net to force the defender to freeze.", "Executing a last-second wrist flick to push the shuttle deep.", "Maintaining racket face control to ensure high-angle clears."),
        ("Slices to Vary Shuttle Flight Speed", "Using crosscourt reverse slices to alter shuttle deceleration.", "Manipulating racket-face angles to create spin and slow down flight.", "Practicing slice consistency under high-speed training feeds."),
        ("Interrupting Opponent Footwork Timing", "Observing the opponent's split-step timing to play early/late shots.", "Varying the contact height to disrupt their movement rhythm.", "Using sudden crosscourt drives to bypass their lateral recovery."),
        ("Varying Net Shot Tumble Rates", "Slicing the shuttle at the net to generate unpredictable tumbling.", "Varying the height and spin of net shots to limit lift quality.", "Transitioning from tight spin shots to fast flat pushes."),
        ("Wind and Drift Adaptation in Singles", "Adjusting shot power when playing with or against the drift.", "Varying clear height to minimize wind interference on flight.", "Selecting tactical playstyles based on hall air currents."),
        ("Exploiting Opponent Stamina Profiles", "Identifying and targeting signs of physical fatigue in the opponent.", "Lengthening rallies using high, deep clears and safe drops.", "Varying game pace to increase the opponent's metabolic demand.")
    ]
    for title_part, p1, p2, p3 in pace_focus:
        title = f"Singles Tactics: Change of Pace - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Baseline Defense (11 topics)
    defense_focus = [
        ("Body Smash Returns and Reflexes", "Adopting a low, wide defensive stance to cover the torso.", "Using quick backhand reflex blocks to return body smashes.", "Directing body returns away from the attacker's path."),
        ("Crosscourt Lifts from Rear Corners", "Executing high, deep crosscourt lifts under maximum pressure.", "Varying lift trajectory to prevent easy intercept smashes.", "Recovering balance and court position post-stroke."),
        ("Block Returns to Net Placement", "Softening the racket grip on contact to drop the smash short.", "Steering defensive blocks into the empty front corners.", "Moving forward to challenge the opponent's net follow-up."),
        ("Drive Returns to Midcourt Zones", "Countering steep smashes with aggressive, flat midcourt drives.", "Forcing the attacker to defend by hitting back into their body.", "Transitioning the defensive rally into an equalized drive exchange."),
        ("High Clear Under Pressure Execution", "Gaining recovery time with high, defensive underarm clears.", "Targeting the baseline to prevent consecutive smash attacks.", "Minimizing errors when hitting from deep, off-balance positions."),
        ("Reaching Deep Corners Footwork Mechanics", "Executing the deep lunging step with correct knee-toe alignment.", "Using recovery pushes from the rear leg to return to the center.", "Handling late contact in deep corners without injuring the ankle."),
        ("Handling Steep Attack Angles", "Anticipating steep drop shots and jump smashes.", "Extending the racket early to catch the shuttle before it dips.", "Varying defense depth to counter extreme attacking angles."),
        ("Low Receive Stances and Weight Distribution", "Lowering the center of gravity to optimize lateral reaction time.", "Positioning the racket head in front of the body, ready for contact.", "Distributing weight evenly on the balls of the feet."),
        ("Deceptive Defensive Clear Execution", "Disguising a high clear as a net block until the last frame.", "Flicking the wrist to redirect the shuttle to the rear court.", "Exploiting the attacker's forward movement anticipation."),
        ("Reading Smasher Shoulder and Hip Orientation", "Analyzing the attacker's shoulder orientation and hip rotation.", "Tracking racket face angles at the point of contact.", "Positioning the defensive stance relative to the smash angle."),
        ("Return of Serve Pressure Strategies", "Positioning to attack weak low serves with steep drops or drives.", "Using deep, high clears on high serves to establish control.", "Varying return angles to test the server's recovery movement.")
    ]
    for title_part, p1, p2, p3 in defense_focus:
        title = f"Singles Tactics: Baseline Defense - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_")
        results.append((title, safe_name, [p1, p2, p3]))
        
    return results

def generate_doubles_tactics():
    results = []
    
    # Rotations (10 topics)
    rotations = [
        ("Attacking to Defensive Transition", "Shifting from a front-and-back setup to side-by-side defense.", "Communicating responsibilities during midcourt lift transitions.", "Maintaining court coverage without leaving the center line open."),
        ("Defensive to Attacking Transition", "Transitioning from side-by-side to front-and-back after a net block.", "Intercepting weak midcourt drives to claim the net position.", "Pushing forward to pressure the opponent's defensive lift."),
        ("Midcourt Interception Patterns", "Cutting off flat drives in the midcourt to maintain attack.", "Using quick racket-up postures to block transitions.", "Coordinating partner coverage behind the intercepting player."),
        ("Covering the T Area at the Net", "Establishing dominance at the net intersection during rallies.", "Guarding against low flick serves and short returns.", "Using quick side-steps to intercept net-cord drops."),
        ("Counter Attack Movement Pathways", "Turning a defensive block into a fast rotational attack.", "Moving around a partner who is recovering from a deep lunge.", "Exchanging court positions seamlessly during flat drive rallies."),
        ("Lifting Rotation Responsibilities", "Moving to defensive side-by-side positions immediately after lifting.", "Ensuring the player who lifts covers their half of the court.", "Avoiding rotational collision during high, defensive clears."),
        ("No-Look Communication Signals", "Using hand signals behind the back during service preparation.", "Developing intuitive movement based on partner positioning.", "Establishing default rotation paths for common court scenarios."),
        ("Clearing Space for the Smasher", "Moving the net player out of the rear smasher's sightline.", "Securing the net area to handle short, defensive block returns.", "Preventing collisions by defining rear court hitting zones."),
        ("Handling Flat Fast Drive Rallies", "Developing high-speed rotational cycles during drive exchanges.", "Maintaining low, active body stances to counter fast paced shots.", "Avoiding high lifts that surrender the offensive momentum."),
        ("Net Kill Follow Through Rotations", "Moving forward to back up a partner who is attacking the net.", "Rotating to the rear court if the net attacker runs forward.", "Maintaining aggressive pressure on weak, high-net returns.")
    ]
    for title_part, p1, p2, p3 in rotations:
        title = f"Doubles Tactics: Rotations - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Side-by-Side Defense (10 topics)
    side_by_side = [
        ("Court Coverage Split Metrics", "Dividing the court halves evenly during defensive phases.", "Defining responsibilities for shots down the center seam.", "Adjusting defense depth depending on the opponent's smash power."),
        ("Countering Down-the-Line Smashes", "Adopting a ready stance to block steep down-the-line smashes.", "Using a short, punchy backhand block to direct the return.", "Pushing the return into the empty midcourt spaces."),
        ("Crosscourt Drive Returns", "Countering smashes with fast crosscourt drive returns.", "Forcing the net player to reach and miss with steep angles.", "Changing the rally tempo by driving rather than lifting."),
        ("Soft Block Net Drops", "Absorbing smash energy with a relaxed grip to drop short.", "Targeting the front corners to force the opponent to lift.", "Following up the soft block to seize the net position."),
        ("Handling Body Smash Attacks", "Using the elbow-out backhand grip to defend body smashes.", "Shifting the torso quickly to clear space for the racket.", "Directing body blocks away from the opponent's net player."),
        ("Defensive Lifting Angles", "Varying lifts between straight and crosscourt baseline targets.", "Using high, deep lifts to push the attackers far back.", "Using low, fast lifts to catch lagging rear court players."),
        ("Low Defense Racket Preparation", "Positioning the racket low and centered before the smash contact.", "Maintaining loose wrist action to allow quick redirection.", "Avoiding high racket prep that delays low reflex blocks."),
        ("Pushing the Flanks in Defense", "Directing defensive drives into the sidelines to widen defenders.", "Exploiting gaps created when opponents commit to the center.", "Varying push speed to keep the attacking pair off balance."),
        ("Drills for Wall Defense Reflexes", "Using wall-rally drills to develop fast hand-eye coordination.", "Practicing continuous defense against close-range feeding.", "Improving wrist reaction speed and grip transitions."),
        ("Reading Smasher Hip Cues", "Observing the attacker's hip and shoulder rotation cues.", "Anticipating straight versus crosscourt smashes early.", "Adjusting the defensive stance before the shuttle is struck.")
    ]
    for title_part, p1, p2, p3 in side_by_side:
        title = f"Doubles Tactics: Side-by-Side Defense - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Attacking Seams (8 topics)
    seams = [
        ("Targeting the Center Line Seam", "Directing smashes down the middle seam to cause confusion.", "Forcing communication breakdowns between the defensive pair.", "Exploiting racket clashes when both defenders reach for the shuttle."),
        ("Targeting the Diagonal Split Seam", "Hitting crosscourt drops between the front and back defenders.", "Forcing the rear player to run forward and disrupt formation.", "Exploiting the space behind the net player's recovery path."),
        ("Smash Placement Between Defenders", "Varying smash angles to land between side-by-side defenders.", "Targeting the inner shoulder of the non-dominant defender.", "Using half-smashes to place the shuttle short in the center seam."),
        ("Dropshot Placements in the Center Seam", "Executing tight, slow drops directly down the central court line.", "Drawing both defenders forward and causing coverage overlaps.", "Following up with a push clear if both defenders commit forward."),
        ("Drive Through the Midcourt Gap", "Hitting flat drives through the midcourt seam to split defense.", "Forcing quick, awkward backhand responses from defenders.", "Maintaining a fast tempo to prevent defensive rotation."),
        ("Creating Confusion with Attacking Steepness", "Using steep jump smashes to drop the shuttle quickly in the seam.", "Varying contact height to alter the angle of entry.", "Capitalizing on late reaction due to the steepness of attack."),
        ("Exploiting Team Communication Gaps", "Identifying and targeting the weaker communicator in the pair.", "Playing deceptive, split-second placement shots in transition.", "Using variation in pace to test their team chemistry."),
        ("Varying Target Zones in the Midcourt Seam", "Shifting the target zone based on the defender's positioning.", "Using flat pushes that land exactly between front and back zones.", "Monitoring defender balance to exploit sudden weight shifts.")
    ]
    for title_part, p1, p2, p3 in seams:
        title = f"Doubles Tactics: Attacking Seams - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Front-and-Back Setup (7 topics)
    front_back = [
        ("Offensive Dominance Formations", "Maintaining a consistent front-and-back formation to attack.", "Forcing the opponents to lift continuously with steep angles.", "Sustaining offensive pressure until a kill opportunity arises."),
        ("Net Player Interception Tactics", "Intercepting defensive returns early to kill or push the rally.", "Using active lateral movements to block crosscourt net shots.", "Keeping the racket head high at net level to threaten returns."),
        ("Rear Player Smash Volume Management", "Sustaining consecutive smash attacks from the baseline.", "Using footwork recovery to return to position after jump smashes.", "Varying smash intensity to manage energy over long rallies."),
        ("Creating Dip Strokes to Setup Net Kills", "Hitting steep drop shots that force the defender to hit upward.", "Slicing overheads to make the shuttle dip below net height.", "Creating easy interception opportunities for the net partner."),
        ("Controlling the Drive Rallies", "Using flat drives to keep the shuttle low and press attack.", "Intercepting flat returns before they reach the rear court.", "Varying drive speed to force defensive lift errors."),
        ("Serve and Third Shot Dominance", "Executing tight low serves to force a defensive lift.", "Interception of the return by the server (third-shot dominance).", "Moving into an immediate attacking front-and-back formation."),
        ("Maintaining Net Pressure under Pressure", "Smothering the net by moving forward on loose opponent returns.", "Using quick push shots to baseline corners to keep pressure.", "Preventing the opponents from playing soft, net-tumbling returns.")
    ]
    for title_part, p1, p2, p3 in front_back:
        title = f"Doubles Tactics: Front-and-Back Setup - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_")
        results.append((title, safe_name, [p1, p2, p3]))
        
    return results

def generate_mixed_tactics():
    results = []
    
    # Female Net Dominance (10 topics)
    net_dom = [
        ("T-Line Positioning during Service", "Positioning the female partner close to the T-line during service.", "Maintaining an active ready stance to cut off net returns.", "Shifting laterally to cover the front court corners efficiently."),
        ("Net Interception and Reflex Kills", "Anticipating and intercepting loose drives and drops early.", "Executing quick tap and brush shots to secure direct points.", "Coordinating with the male partner to allow clean baseline clears."),
        ("Tight Tumbling Drops at the Net", "Playing tight, spinning net drops to force high defensive lifts.", "Varying drop placement to exploit the opponent net player.", "Following up net shots to maintain forward pressure."),
        ("Defending against opponent Flick Serves", "Anticipating the opponent's flick serve to minimize reaction time.", "Using high, deceptive drops or clears to counter flick serves.", "Coordinating backward movement paths with the male partner."),
        ("Lateral Net Movement Footwork Patterns", "Mastering the chasse step for rapid side-to-side net coverage.", "Staying light on the balls of the feet to transition quickly.", "Avoiding deep court retreats, keeping focus on the net."),
        ("Brush Kills at the Net Tape", "Executing quick wrist brush strokes to kill high net returns.", "Avoiding hitting the net by using a lateral racket swing.", "Positioning the body weight forward to maximize speed."),
        ("Guarding the Net intersection (T Area)", "Anchoring near the T-line to block straight net returns.", "Using backhand reflex blocks to return flat midcourt drives.", "Maintaining a high racket posture to threaten the server."),
        ("Racket-High Ready Stances at the Net", "Keeping the racket frame above net height at all times.", "Minimizing racket preparation time for net interceptions.", "Using a relaxed grip to adjust angles on short notice."),
        ("Deflecting Smashes to Empty Spaces", "Redirecting opponent smashes into empty court spaces.", "Absorbing smash power with a soft contact point.", "Recovering net posture immediately after defensive blocks."),
        ("Crosscourt Net Drop Interception Pathways", "Reading the opponent's crosscourt drops to intercept early.", "Using quick footwork to step across and kill the shuttle.", "Minimizing the gap between the net and racket contact.")
    ]
    for title_part, p1, p2, p3 in net_dom:
        title = f"Mixed Doubles Tactics: Female Net Dominance - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Male Backcourt Coverage (10 topics)
    backcourt = [
        ("Endurance and Stamina Profiles", "Developing high-level aerobic and anaerobic capacity for coverage.", "Managing energy during consecutive baseline smash rallies.", "Using efficient deep footwork to cover both rear corners."),
        ("Rear Court Smash Variation and Speed", "Varying smash power, angle, and placement from the backcourt.", "Using steep down-the-line smashes to target the female defender.", "Integrating half-smashes to disrupt defensive timing."),
        ("Steep Half-Smash Angles and Placement", "Executing steep half-smashes to target opponent hip zones.", "Using wrist snap to create dip without full arm rotation.", "Following up half-smashes with rapid court adjustments."),
        ("Deceptive Deep Clears from Baseline", "Using identical preparation for smashes to hit deep clears.", "Forcing the opponent's defense to reset by pushing them back.", "Relieving baseline pressure with well-placed attacking clears."),
        ("China Step and Scissor Kick Footwork", "Developing explosive side-to-side footwork in the rear court.", "Using scissor kicks and China steps to cover wide angles.", "Minimizing transition time between rear corners."),
        ("Jump Smash Kinetics and Body Rotation", "Optimizing jump height and body rotation for maximum smash speed.", "Ensuring safe landing mechanics to prevent knee and ankle strain.", "Maintaining kinetic chain continuity from legs to racket face."),
        ("Midcourt Coverage during Partner Shifts", "Covering the midcourt space when the female partner is forced wide.", "Restoring the front-and-back formation as soon as possible.", "Communicating positions during sudden defensive rotations."),
        ("Serving and Immediate Backcourt Movement", "Executing consistent serves and moving to backcourt coverage.", "Protecting the partner from returns targetting the server.", "Using deep court positioning to handle clear returns."),
        ("Fatigue Management during Long Rallies", "Monitoring fatigue levels during high-volume baseline rallies.", "Using tactical lifts to buy recovery time when exhausted.", "Structuring off-court endurance training to match match play demands."),
        ("Interception of Midcourt Crosscourt Lifts", "Designing drills to practice intercepting crosscourt lifts.", "Improving reaction speed to cut off opponent flat drives.", "Coordinating court coverage zones with the net partner.")
    ]
    for title_part, p1, p2, p3 in backcourt:
        title = f"Mixed Doubles Tactics: Male Backcourt Coverage - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Target Matchups (10 topics)
    matchups = [
        ("Exploiting the Opponent Female Defender", "Directing attacks at the opponent female's body or hip area.", "Clearing over the opponent female to force her to the backcourt.", "Using tight drops to pull her away from her net domain."),
        ("Isolating and Fatiguing the Opponent Male", "Playing flat drives past the female to keep the male running.", "Using crosscourt drops to test his lateral movement recovery.", "Wearing down the opponent male with repetitive baseline work."),
        ("Smashing to the Defender Hip Zone", "Targeting the defender's right hip (for right-handers) to restrict movement.", "Varying smash speed to prevent comfortable defensive blocks.", "Utilizing steep angles to make hip defense difficult."),
        ("Clearing High and Deep Over Net Players", "Executing deep, high clears over the net player's head.", "Forcing the opponent female to play defensive backcourt shots.", "Exploiting the resulting formation breakdown in their defense."),
        ("Targeting Serves to Female Backhand Corners", "Targeting the opponent female's backhand during low serves.", "Using flick serves to keep the opponent male from rushing the net.", "Varying serve angles to create weak third-shot returns."),
        ("Interrupting Male Movement with Deceptive Holds", "Using deceptive holds to freeze the male player at the backcourt.", "Hitting crosscourt shots to force long, diagonal sprints.", "Varying paces to disrupt his footwork timing and rhythm."),
        ("Varying Smash and Drop Entry Angles", "Alternating straight smashes with crosscourt drops to confuse defense.", "Targeting the seams between the front and back players.", "Executing steep slices to force off-balance returns."),
        ("Exploiting Midcourt Seams in Mixed Play", "Playing dropshots directly between the net and baseline players.", "Forcing communication doubts over who covers the midcourt.", "Capitalizing on court space left open during rotation errors."),
        ("Pace Control to Neutralize Baseline Attakers", "Using high, slow clears to neutralize the male player's power.", "Taking speed off the ball with soft net drops.", "Disrupting his attacking rhythm through frequent pace changes."),
        ("Forcing Side-by-Side Defensive Formations", "Forcing the opponent mixed pair into a side-by-side setup.", "Targeting the female player in the rear court to exploit weak clears.", "Exploiting their lack of standard doubles rotational habits.")
    ]
    for title_part, p1, p2, p3 in matchups:
        title = f"Mixed Doubles Tactics: Target Matchups - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    return results

def generate_sports_science():
    results = []
    
    # Aerobic Endurance (12 topics)
    aerobic = [
        ("On-Court Long Interval Drills", "Designing continuous 10-15 minute technical feeding drills.", "Maintaining player heart rate within 70-80% of HR max.", "Focusing on movement efficiency and stroke accuracy under fatigue."),
        ("Off-Court Continuous Running", "Structuring steady-state running sessions for cardiovascular health.", "Calculating baseline training paces based on lactate thresholds.", "Integrating low-impact cross-training like swimming to avoid joint strain."),
        ("Heart Rate Zone Calculations", "Determining individual training zones using Karvonen formula.", "Monitoring heart rate recovery rates after intensive rallies.", "Using heart rate data to adjust daily cardiovascular workloads."),
        ("VO2 Max Field Testing Protocols", "Implementing badminton-specific incremental field tests.", "Measuring maximal oxygen uptake and gas exchange variables.", "Using test results to design individual aerobic power programs."),
        ("Fartlek Training on Court", "Varying movement speed on court to simulate match play dynamics.", "Alternating fast footwork sprints with active recovery jogging.", "Structuring work-to-rest intervals to challenge aerobic capacity."),
        ("Active Recovery Aerobic Flush", "Using low-intensity cycling or light jogging to clear metabolic waste.", "Maintaining heart rate below aerobic threshold (under 60% HR max).", "Enhancing muscular restoration and tissue healing post-match."),
        ("Cardiovascular Adaptations to Play", "Analyzing changes in stroke volume and cardiac output over time.", "Understanding rest heart rate decreases due to training adaptations.", "Evaluating the correlation between aerobic fitness and match longevity."),
        ("Mitochondrial Density Development Pathways", "Stimulating muscle cellular adaptations through consistent aerobic volume.", "Optimizing oxygen utilization at the mitochondrial level.", "Structuring training blocks to maximize oxidative enzyme activity."),
        ("Capillary Network Angiogenesis Principles", "Enhancing muscle capillary density to improve oxygen delivery.", "Structuring long, slow distance training to trigger angiogenesis.", "Measuring recovery rate improvements during short match intervals."),
        ("Base Phase Aerobic Volume Guidelines", "Establishing baseline aerobic training volumes in early pre-season.", "Gradually increasing weekly mileage or court minutes safely.", "Preventing early fatigue accumulation prior to high-intensity phases."),
        ("Aerobic Power vs Aerobic Capacity Training", "Differentiating training methods for VO2 max vs metabolic efficiency.", "Structuring intervals to target aerobic power output.", "Designing longer sessions to build systemic aerobic capacity."),
        ("Interval Training Work-to-Rest Configuration", "Configuring work-rest ratios to target specific energy systems.", "Using 1:1 or 2:1 ratios for aerobic capacity development.", "Monitoring heart rate drops to determine the start of the next set.")
    ]
    for title_part, p1, p2, p3 in aerobic:
        title = f"Sports Science: Aerobic Endurance - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Anaerobic Lactic (12 topics)
    lactic = [
        ("Glycolysis Metabolic Pathways", "Analyzing the breakdown of glycogen to produce energy during long rallies.", "Understanding the accumulation of hydrogen ions and lactic acid.", "Evaluating metabolic fatigue signs in high-intensity match play."),
        ("Lactate Threshold Identification", "Designing sessions at or slightly above the lactate threshold.", "Improving the body's ability to clear lactate during active play.", "Tracking blood lactate levels using portable testing devices."),
        ("HIIT and Glycolytic Power", "Structuring on-court HIIT sets (e.g., 30s work, 30s rest).", "Maximizing anaerobic energy production during interval repetitions.", "Monitoring performance drop-offs to prevent excessive muscle damage."),
        ("Intracellular Buffering Adaptations", "Improving intracellular buffering to delay the onset of acidosis.", "Using high-intensity, repeated sprint sets to trigger adaptations.", "Integrating nutritional strategies to support pH regulation."),
        ("Acidosis Tolerance Court Drills", "Designing drills that force players to move under severe leg fatigue.", "Maintaining technical stroke control despite high metabolic burn.", "Structuring safety protocols and mental resilience techniques."),
        ("Lactate Clearance Kinetics", "Measuring the rate of lactate clearance during active recovery periods.", "Comparing active recovery (walking) to passive recovery (sitting).", "Optimizing recovery protocols between matches in multi-round events."),
        ("Blood Lactate Testing Protocols", "Conducting incremental exercise tests on-court with earlobe blood draws.", "Identifying lactate threshold points (LT1 and LT2).", "Using test data to calibrate training intensity zones."),
        ("Recovery from Acidosis in Match Breaks", "Maximizing breathing techniques and hydration during the 11-point break.", "Using active movement to prevent leg blood pooling.", "Re-establishing mental focus under physiological discomfort."),
        ("Neuromuscular Fatigue under Lactic Stress", "Analyzing changes in motor unit recruitment when muscle pH drops.", "Addressing the loss of footwork coordination and reaction speed.", "Implementing drills to preserve stroke accuracy under lactic load."),
        ("Nutritional Buffering Interventions", "Evaluating beta-alanine and sodium bicarbonate supplementation.", "Timing carbohydrate intake to optimize muscle glycogen stores.", "Maintaining hydration to support metabolic waste transport."),
        ("Active vs Passive Lactic Clearance", "Comparing post-session metabolic clearance rates of active vs passive rest.", "Selecting the recovery modality based on subsequent event timing.", "Implementing low-intensity movements to maintain circulation."),
        ("Periodization of Lactic Tolerance Phase", "Scheduling lactic tolerance phases in the mid-to-late pre-season.", "Progressing from volume-based intervals to tournament-specific setups.", "Monitoring cumulative systemic stress to prevent overtraining.")
    ]
    for title_part, p1, p2, p3 in lactic:
        title = f"Sports Science: Anaerobic Lactic - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Anaerobic Alactic (12 topics)
    alactic = [
        ("ATP-CP System Energy Kinetics", "Understanding adenosine triphosphate and creatine phosphate breakdown.", "Analyzing energy release during short, explosive badminton movements.", "Evaluating the role of phosphagen stores in immediate power output."),
        ("Phosphagen System Restoration Curves", "Analyzing recovery time curves for creatine phosphate resynthesis.", "Understanding why 90-120 seconds of rest is needed for alactic recovery.", "Structuring training sessions to prevent premature lactic shift."),
        ("Explosive Power and RFD Metrics", "Designing on-court jumps, lunges, and sprints targeting the ATP-CP system.", "Maximizing rate of force development (RFD) during short movements.", "Tracking power output using wearable technology and accelerometers."),
        ("Short High-Speed Sprint Protocols", "Implementing linear and multi-directional sprints under 6 seconds.", "Ensuring maximal effort and explosive acceleration on each rep.", "Providing complete recovery windows between sprint repetitions."),
        ("High-Velocity Multi-Feeding Drills", "Designing 5-8 shuttle rapid feeding drills with full effort.", "Focusing on high-speed footwork and smash execution.", "Structuring rest periods to maintain maximum movement velocity."),
        ("Work-to-Rest Ratios for Alactic Speed", "Establishing work-to-rest ratios of 1:10 to 1:20 for alactic training.", "Preventing accumulation of lactic acid to preserve neuromuscular power.", "Using rest intervals for visualization and cognitive coaching."),
        ("Neuromuscular Motor Unit Recruitment", "Optimizing high-threshold motor unit recruitment for explosive speed.", "Improving inter-muscular coordination in complex court movements.", "Evaluating neurological fatigue and its impact on first-step reaction."),
        ("Power Output Acceleration Monitoring", "Measuring contact times and flight times during repetitive jump tests.", "Using velocity-based training (VBT) devices for power measurement.", "Adjusting training volume when explosive performance drops by 10%."),
        ("Creatine and CP Resynthesis Rates", "Enhancing CP resynthesis through targeted interval training.", "Evaluating the impact of creatine supplementation on alactic capacity.", "Monitoring recovery improvements in elite performance testing."),
        ("Integrating Alactic Sprints in Warmups", "Structuring short, explosive speed drills post-general warm-up.", "Priming the neuromuscular system before matches or heavy court work.", "Ensuring drills do not induce fatigue prior to the main session."),
        ("Alactic Speed vs Lactic Endurance Demands", "Comparing the physiological demands of short sprints vs long rallies.", "Balancing alactic speed training with lactic capacity work.", "Adapting training distribution to match the player's competitive discipline."),
        ("Seasonal Periodization of Alactic Training", "Integrating alactic speed development across all macrocycle phases.", "Transitioning from general power to badminton-specific speed.", "Maintaining explosive qualities during the competitive season.")
    ]
    for title_part, p1, p2, p3 in alactic:
        title = f"Sports Science: Anaerobic Alactic - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Strength Periodization (12 topics)
    strength = [
        ("Anatomical Adaptation Phase Guidelines", "Building tendon and ligament strength using high repetitions and low load.", "Correcting bilateral imbalances and establishing baseline posture.", "Targeting core stability and joint mobility in early preparation."),
        ("Hypertrophy Block Structure", "Increasing muscle cross-sectional area to support force potential.", "Structuring rep ranges of 8-12 with moderate-to-high volume.", "Monitoring body composition changes and nutritional alignment."),
        ("Maximum Strength Compound Lifts", "Developing peak force production using high loads and low repetitions.", "Focusing on compound lifts like back squats and deadlifts.", "Ensuring complete neurological recovery between strength sets."),
        ("Conversion to Explosive Power", "Translating maximum strength into badminton-specific explosive power.", "Integrating Olympic lift variations and loaded jump squats.", "Emphasizing the speed of movement and rate of force development."),
        ("Strength Maintenance in Season", "Preserving strength gains during the competitive season with low volume.", "Scheduling short, high-intensity strength sessions once or twice weekly.", "Avoiding muscular soreness that interferes with tournament play."),
        ("Active Decompression and Recovery", "Using mobility work and bodyweight training to unload the joints.", "Targeting core alignment and soft tissue health post-strength blocks.", "Restoring muscle length-tension relationships after heavy loading."),
        ("Progressive Overload Weekly Schemes", "Incrementally increasing resistance, volume, or density over weeks.", "Tracking performance metrics to ensure adaptation takes place.", "Implementing scheduled de-loads to allow physiological recovery."),
        ("Eccentric Braking vs Concentric Drive", "Understanding eccentric strength's role in lunging and braking forces.", "Using concentric power development to drive explosive court jumps.", "Designing eccentric overloading protocols for injury prevention."),
        ("Isometric Core Strength Transfers", "Developing core strength to transfer force between upper and lower body.", "Using planks, carries, and pallof presses to resist rotation.", "Integrating static holds into functional movement sequences."),
        ("Reps, Sets, and Percentage 1RM", "Calculating optimal volume-load configurations for each training block.", "Using percentage of 1-Repetition Maximum (1RM) to set intensity.", "Adapting training variables based on player readiness and feedback."),
        ("1RM and Relative Strength Testing", "Implementing safe testing methods (e.g., 3RM or estimated 1RM).", "Evaluating relative strength (force-to-bodyweight ratios).", "Using testing milestones to adjust subsequent strength blocks."),
        ("Unilateral Stability Injury Prevention", "Targeting vulnerable areas like the rotator cuff, hamstrings, and ankles.", "Using single-leg exercises to develop unilateral stability.", "Balancing agonist and antagonist muscle groups across joints.")
    ]
    for title_part, p1, p2, p3 in strength:
        title = f"Sports Science: Strength Periodization - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Plyometric Training (12 topics)
    plyo = [
        ("Squat Jump Triple Extension Biomechanics", "Analyzing triple extension mechanics (hip, knee, and ankle joints).", "Developing concentric power from a static starting position.", "Optimizing arm drive to increase vertical jump height."),
        ("Force Plate Squat Rebound Testing", "Measuring ground reaction forces and contact times using force plates.", "Calculating the reactive strength index (RSI) during rebound jumps.", "Using force-time curves to identify movement deficiencies."),
        ("Depth Jump Drop Heights and Landing", "Determining optimal drop heights based on reactive strength testing.", "Maximizing eccentric load absorption and transition speed.", "Ensuring safe landing postures to prevent joint stress."),
        ("Stretch-Shortening Cycle Elastic Energy", "Understanding the amortization phase between stretch and contraction.", "Optimizing elastic energy storage in muscles and tendons.", "Designing drills to shorten contact time and maximize force."),
        ("CMJ Central Nervous Fatigue Metrics", "Measuring jump height, peak power output, and contraction times.", "Using CMJ tests to monitor central nervous system fatigue.", "Tracking performance changes across periodized training blocks."),
        ("On-Court Lateral Bounds and Push-off", "Designing lateral jumps to replicate wide defensive footwork.", "Improving push-off power and change-of-direction speed.", "Integrating single-leg bounds with racket swing actions."),
        ("RSI and Rapid Force Development", "Calculating RSI to evaluate rapid force development.", "Using RSI scores to guide plyometric volume and intensity.", "Comparing player RSI trends to track athletic development."),
        ("Knee Valgus and Landing Mechanics", "Teaching proper knee tracking (avoiding valgus collapse) on landings.", "Absorbing landing force through active hip and knee flexion.", "Selecting appropriate training surfaces to reduce joint stress."),
        ("Volume and Foot Contact Guidelines", "Tracking volume using total foot contacts per training session.", "Managing progressive increases in plyometric intensity safely.", "Structuring recovery periods between plyometric training blocks."),
        ("Neurological Recovery Rest Windows", "Allowing 2-3 minutes of passive rest for neurological recovery.", "Ensuring maximum power output on every single repetition.", "Avoiding fatigue-induced degradation of movement quality."),
        ("Complex Training: Weights and Plyometrics", "Designing complex training sets (heavy squat followed by vertical jump).", "Utilizing post-activation potentiation (PAP) to boost power.", "Monitoring recovery demands of combined training protocols."),
        ("Unilateral Bound Progressions for Elites", "Transitioning from bilateral hops to intense unilateral bounds.", "Adding cognitive cues and reactive targets to plyometric drills.", "Customizing programs to match the player's on-court role.")
    ]
    for title_part, p1, p2, p3 in plyo:
        title = f"Sports Science: Plyometric Training - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Speed/Agility (12 topics)
    speed = [
        ("Change of Direction (COD) Angles", "Analyzing foot planting angles and force application in COD.", "Optimizing center of mass management during direction changes.", "Reducing foot contact times to increase court speed."),
        ("Deceleration and Eccentric Braking Forces", "Developing eccentric leg strength to absorb high braking forces.", "Mastering deceleration footwork before playing rear court overheads.", "Reducing injury risk during sudden, high-speed stops."),
        ("Reactive Agility Cognitive Decision Drills", "Designing drills using visual and auditory cues for direction changes.", "Improving decision-making and cognitive reaction times on court.", "Simulating unpredictable match play movement patterns."),
        ("Footwork Efficiency and Zone Selections", "Refining chasse, running steps, and cross steps for efficiency.", "Selecting footwork patterns based on target court zones.", "Drilling footwork sequences to build automatic execution."),
        ("Split-Step Pre-Tension Timing", "Mastering the timing of the split-step relative to opponent contact.", "Optimizing pre-tension in lower limbs for rapid launch.", "Drilling first-step transitions to all four corners."),
        ("Center of Gravity in Agility Transitions", "Maintaining a low center of gravity to enhance stability and reaction.", "Controlling body lean when transitioning between court ends.", "Integrating core strength with agility to control balance."),
        ("Forwards-Backwards Linear Transition Drills", "Designing drills for fast transitions from net play to rear court.", "Mastering the pivot step and backpedaling mechanics safely.", "Maintaining court awareness during rapid linear movement."),
        ("Lateral Shuffling and Stance Width", "Improving lateral movement speed across the midcourt line.", "Optimizing stance width and stride length during lateral drives.", "Structuring high-repetition lateral agility drills."),
        ("Visual Reaction Lights and Cues", "Using LED reaction lights or coach hand signals to guide movement.", "Enhancing perceptual-cognitive skills in court positioning.", "Measuring changes in reaction times when adding visual tasks."),
        ("Agility Test Design and Asymmetries", "Administering standardized agility tests to measure progress.", "Adapting testing layouts to match badminton court dimensions.", "Using test profiles to identify lateral movement asymmetries."),
        ("Fatigue-Induced Change of Direction Drops", "Analyzing direction change efficiency drops during long matches.", "Identifying footwork breakdown markers as fatigue accumulates.", "Structuring agility conditioning to improve fatigue resistance."),
        ("Closed-to-Open Agility Drill Progressions", "Progressing from closed shadow routines to open reactive drills.", "Increasing movement complexity and speed demands gradually.", "Customizing agility pathways to match player styles.")
    ]
    for title_part, p1, p2, p3 in speed:
        title = f"Sports Science: Speed and Agility - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Flexibility (8 topics)
    flex = [
        ("Dynamic Warm-up Movement Preparation", "Designing dynamic movement preparation protocols before training.", "Increasing core temperature and local muscle blood flow.", "Activating badminton-specific joints and movement ranges."),
        ("Static Stretching Post-Session Relaxation", "Implementing static stretching to restore resting muscle length.", "Holding stretches for 20-30 seconds to stimulate tissue relaxation.", "Targeting primary tight areas like hamstrings, hips, and calves."),
        ("PNF Contract-Relax Stretching Protocols", "Using contract-relax methods to increase joint range of motion.", "Coordinating partner-assisted stretches for major muscle groups.", "Structuring PNF stretching during recovery-focused sessions."),
        ("Hip Mobility and Deep Lunge Range", "Improving hip internal and external rotation capabilities.", "Designing daily mobility routines to prevent hip impingements.", "Evaluating hip range of motion needs for extreme reach lunges."),
        ("Thoracic and Glenohumeral Mobility", "Developing thoracic and glenohumeral mobility for smashes.", "Using resistance bands and wall slides to improve shoulder range.", "Preventing subacromial impingement through regular mobility work."),
        ("Ankle Dorsiflexion Calf Mobility", "Improving ankle dorsiflexion range to support deep squats and lunges.", "Preventing Achilles tendon stress through calf mobility drills.", "Measuring ankle mobility limitations using simple wall tests."),
        ("Myofascial Foam Roller Release", "Using massage balls and rollers to address tissue restrictions.", "Restoring sliding capacity of fascial layers post-training.", "Targeting the plantar fascia, IT band, and thoracic spine."),
        ("Goniometer Range of Motion Testing", "Implementing standard range of motion tests (e.g., sit-and-reach).", "Tracking changes in joint angles using simple goniometer tools.", "Adapting flexibility training based on daily stiffness markers.")
    ]
    for title_part, p1, p2, p3 in flex:
        title = f"Sports Science: Flexibility - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    return results

def generate_psychology():
    results = []
    
    # The 5 Cs (25 topics: 5 per C)
    cs = {
        "Commitment": [
            ("Long-Term Athlete Development Pathway", "Fostering persistence through multi-year training progressions.", "Helping players maintain motivation when performance gains slow.", "Aligning long-term goals with day-to-day training commitment."),
            ("Daily Training Discipline and Focus", "Encouraging focus and effort during repetitive basic drills.", "Managing fatigue-induced drops in training enthusiasm.", "Coaching players to take personal responsibility for preparation."),
            ("Overcoming Rehabilitation Injury Setbacks", "Supporting athlete motivation during restricted rehabilitation phases.", "Setting developmental milestones for non-injured body segments.", "Managing psychological stress related to return-to-play concerns."),
            ("Balancing Life, Academics and Training", "Helping players manage school, family, and training demands.", "Structuring resting periods to avoid burnout and mental fatigue.", "Establishing supportive networks for dual-career path athletes."),
            ("Coaches Autonomy-Supportive Environments", "Structuring training environments to support athlete autonomy.", "Providing constructive, competence-affirming feedback.", "Building strong coach-player relationships based on trust.")
        ],
        "Communication": [
            ("Doubles Partnership Court Rapport", "Developing positive, supportive communication between partners.", "Establishing clear agreements on midcourt coverage and calls.", "Managing partner conflict during high-stress matches."),
            ("Coach-Player Feedback Loop Metrics", "Encouraging players to voice feelings and physical feedback.", "Using active listening to understand athlete concerns.", "Developing shared technical terms to speed up communications."),
            ("Non-Verbal Body Language Cues", "Using body language to show confidence and support.", "Reading opponent non-verbal indicators to adjust tactics.", "Eliminating negative gestures after errors to stay focused."),
            ("Active Listening and Player Autonomy", "Checking understanding by paraphrasing player statements.", "Creating safe spaces for open communication and sharing.", "Observing player reactions to calibrate coaching messages."),
            ("Squad Conflict Resolution Protocols", "Structuring group protocols to resolve interpersonal issues.", "Addressing team cliques and double-standard perceptions.", "Fostering cooperative atmospheres in squad training sessions.")
        ],
        "Concentration": [
            ("Focus Retention during Long Rallies", "Maintaining attention on shuttle flight despite lung fatigue.", "Reducing mental chatter and distraction during point play.", "Drilling focus retention in high-fatigue multi-feed setups."),
            ("Narrowing Attention to Ignore Crowd Noise", "Using narrow focus techniques to block out hall noise.", "Integrating mock crowd noise into high-pressure drills.", "Refining pre-point routines to ground attention on court."),
            ("Re-Focusing Triggers post Error", "Implementing a quick physical trigger to clear error memory.", "Reframing mistakes as neutral feedback rather than failure.", "Focusing attention on the immediate next point strategy."),
            ("Pre-Serve Physical and Breath Routines", "Designing consistent physical actions before serving.", "Using deep breathing to lower heart rate and calm thoughts.", "Visualizing target serve paths and third-shot responses."),
            ("Attentional Flexibility: Broad vs Narrow", "Shifting focus from narrow (shuttle contact) to broad (opponent position).", "Drilling focus flexibility under changing match dynamics.", "Recognizing focus lock-ups and using release techniques.")
        ],
        "Control": [
            ("Arousal Regulation and Breathing Rates", "Using rapid breathing to boost energy when feeling lethargic.", "Implementing progressive muscle relaxation to reduce tension.", "Monitoring physiological markers of state anxiety."),
            ("Reframing Pre-Match Nervous Arousal", "Reframing pre-match nerves as performance readiness.", "Structuring consistent warm-up and mental prep timetables.", "Using music and self-talk to manage nervous energy."),
            ("Emotional Stability under Poor Decisions", "Developing emotional resilience against external unfairness.", "Using deep-breathing resets to let go of anger quickly.", "Maintaining tactical discipline despite emotional spikes."),
            ("Vagal Nerve Activation between Points", "Using exhalation techniques to trigger vagal nerve activation.", "Walking to collect the shuttle deliberately to buy time.", "Stabilizing breathing before initiating the serve routine."),
            ("Outcome-Independence in Tight Finishes", "Focusing on execution steps rather than match outcomes.", "Embracing pressure moments as challenges rather than threats.", "Maintaining aggressive tactical choices in tight finishes.")
        ],
        "Confidence": [
            ("Self-Efficacy Progression Tracking", "Building self-belief through structured, progressive success.", "Using video logs of successful play to reinforce efficacy.", "Developing confidence in specific strokes through volume repetition."),
            ("Reframing Self-Talk for Action Cueing", "Replacing critical self-talk with action-focused commands.", "Developing personalized confidence mantras for match use.", "Interrupting negative thoughts with verbal trigger resets."),
            ("First-Person Kinesthetic Imagery Routines", "Visualizing perfect stroke execution from a first-person view.", "Mental rehearsal of tactical plans for specific opponents.", "Practicing imagery routines during off-court rest blocks."),
            ("Thorough Physical Preparation Connection", "Connecting thorough physical preparation to match readiness.", "Establishing contingency plans for equipment and weather issues.", "Developing confidence through consistent coaching routines."),
            ("Rebuilding Confidence post Performance Slumps", "Focusing on fundamental skills to rebuild confidence.", "Reducing pressure by setting short-term process targets.", "Analyzing performance trends objectively to find solutions.")
        ]
    }
    for c_name, sub_list in cs.items():
        for title_part, p1, p2, p3 in sub_list:
            title = f"Psychology: The 5 Cs - {c_name} - {title_part}"
            safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
            results.append((title, safe_name, [p1, p2, p3]))
            
    # Motivational Cues (10 topics)
    cues = [
        ("Verbal Action Trigger Words", "Selecting short action words (e.g., 'explode', 'relax', 'reach').", "Using triggers to activate specific movement patterns on court.", "Coordinating verbal cues with physical execution timing."),
        ("Visual Markings and Anchoring", "Using court markings or equipment as visual reminders.", "Anchoring focus and calm by looking at a specific spot.", "Fostering positive mental states through visual cues."),
        ("Kinesthetic Feeling Sensory Cues", "Focusing on the physical feel of correct racket contact.", "Using movement cues (e.g., 'heel-to-toe') to guide footwork.", "Translating mechanical instructions into sensory cues."),
        ("Self-Selected vs Coach-Led Prompts", "Allowing players to create their own emotional triggers.", "Coordinating coach cue usage during active court training.", "Evaluating retention differences between player-led and coach cues."),
        ("Neural Priming for Explosive Power", "Using high-energy cue words to trigger fast movements.", "Activating fast-twitch motor units through mental priming.", "Structuring speed drills that incorporate power cues."),
        ("Calming Cues for Technical Accuracy", "Using quiet, calming cues (e.g., 'smooth', 'guide') for placement.", "Discharging excess tension before executing fine drops.", "Stabilizing racket hand control through relaxation cues."),
        ("Grounding Triggers for Emotional Calm", "Using grounding cue words to lower stress in matches.", "Combining calming cues with steady breathing routines.", "Mitigating panic responses during fast point exchanges."),
        ("Speak-Aloud Integration in Training", "Structuring training sessions around specific cue focuses.", "Encouraging players to speak cues aloud during execution.", "Progressive transfer of cues from drills into open match play."),
        ("Quantifying Cue Performance Efficacy", "Tracking stroke success rates before and after cue use.", "Refining or replacing cues that fail to produce outcomes.", "Monitoring player compliance and comfort with cues."),
        ("Tailoring Cues to Sensory Preferences", "Adapting cue styles to match introverted and extroverted players.", "Using sensory cues that fit the player's learning style.", "Modifying cues to match age and experience levels.")
    ]
    for title_part, p1, p2, p3 in cues:
        title = f"Psychology: Motivational Cues - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Goal Setting (10 topics)
    goals = [
        ("Outcome vs Process Goals Balance", "Differentiating outcome goals (winning) from process goals (execution).", "Structuring process-oriented targets to manage performance anxiety.", "Balancing goal types across seasonal training phases."),
        ("Quantitative Milestones for Serve Accuracy", "Setting quantitative targets for low serve clearance height.", "Tracking serve placement percentages in match conditions.", "Designing progression milestones for flick serve accuracy."),
        ("Split-Step Footwork Recovery Timing", "Establishing split-step timing targets during drills.", "Tracking recovery step counts from deep baseline corners.", "Using video analysis to check footwork alignment consistency."),
        ("SMART Offseason Conditioning Goals", "Defining Specific, Measurable strength and fitness targets.", "Structuring time-bound recovery and conditioning milestones.", "Ensuring off-season goals support upcoming season needs."),
        ("Chaining Short-Term to Long-Term Goals", "Chaining weekly short-term goals to support annual targets.", "Using step-by-step milestones to keep athletes motivated.", "Adjusting long-term goals based on player development rates."),
        ("Athletic Journals for Tracking Goals", "Implementing player training journals to log daily goals.", "Scheduling regular goal-review sessions between coach and athlete.", "Celebrating goal achievements to support self-efficacy."),
        ("Supporting Autonomy with Player Ownership", "Involving the player in the goal-creation process.", "Fostering intrinsic motivation by supporting autonomy.", "Encouraging self-reflection on progress and challenges."),
        ("Rehabilitation Goals post Injury Setbacks", "Reframing training goals to focus on rehabilitation.", "Setting recovery milestones to manage returning anxiety.", "Preventing early return attempts by sticking to objective rehab goals."),
        ("Shared Team Goals in Doubles partnerships", "Establishing shared tactical and behavioral targets.", "Aligning individual player goals to support team success.", "Fostering mutual accountability within the partnership."),
        ("Process-Oriented Mental Resilience Targets", "Setting process goals to maintain emotional control under stress.", "Tracking compliance with pre-point and pre-serve routines.", "Fostering grit and determination through challenging targets.")
    ]
    for title_part, p1, p2, p3 in goals:
        title = f"Psychology: Goal Setting - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    return results

def generate_sports_med():
    results = []
    
    # Overtraining (7 topics)
    overtraining = [
        ("Resting Heart Rate and Somatic Signs", "Identifying physical indicators like resting heart rate spikes.", "Recognizing persistent muscle soreness and fatigue.", "Monitoring changes in sleep quality and immunity status."),
        ("Somatic and Emotional Burnout Signs", "Tracking loss of interest and motivation toward training.", "Monitoring increased irritability and emotional exhaustion.", "Addressing player feelings of helplessness and plateauing."),
        ("Daily Wellness Questionnaire Metrics", "Using daily wellness questionnaires to check recovery.", "Monitoring acute-to-chronic training workload ratios.", "Implementing scheduled rest weeks within mesocycles."),
        ("Coaching Adaptations to Vary Stimulus", "Varying training drills and environments to maintain interest.", "Encouraging open communication regarding mental fatigue.", "Providing short training breaks to allow complete decompression."),
        ("Hormonal Cortisol Testosterone Ratios", "Analyzing cortisol-to-testosterone ratio changes.", "Monitoring decreases in maximum aerobic capacity and power.", "Evaluating blood markers like iron and creatine kinase."),
        ("Active Rest and Psychological Decompression", "Designing active rest periods away from badminton courts.", "Encouraging alternative sports and recreational activities.", "Integrating mindfulness and stress-reduction routines."),
        ("Medical Clearance and Return-to-Play Schedules", "Collaborating with medical staff to confirm overtraining.", "Designing progressive, low-load return-to-play schedules.", "Adjusting future training plans to avoid re-occurrence.")
    ]
    for title_part, p1, p2, p3 in overtraining:
        title = f"Sports Medicine: Overtraining and Burnout - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # RICE (7 topics)
    rice = [
        ("Acute Injury Phase Application", "Understanding immediate application of RICE post-injury.", "Managing early inflammatory responses to promote recovery.", "Determining when to seek medical imaging and diagnosis."),
        ("Rest and Weight-Bearing Restrictions", "Protecting the injured area from weight-bearing stress.", "Using crutches or braces to support immobilization.", "Balancing absolute rest with pain-free movement."),
        ("Ice Therapy Timing and Safe Application", "Applying ice for 15-20 minutes every 2-3 hours.", "Preventing tissue damage by using barriers between skin and ice.", "Evaluating the role of ice in pain relief."),
        ("Compression Wraps and Bandages", "Applying compression wraps to control swelling.", "Ensuring correct tension to avoid restricting blood flow.", "Using elastic bandages and specialized compression wear."),
        ("Elevation and Gravity Lymphatic Drainage", "Elevating the injured limb above heart level.", "Assisting gravity in clearing excess fluid from tissues.", "Structuring elevation periods during the initial 48 hours."),
        ("Transitioning from RICE to MEAT Protocols", "Transitioning from RICE to Movement, Exercise, Analgesics, Treatment.", "Encouraging early mobilization to maintain joint range.", "Promoting tissue healing through targeted load."),
        ("Avoiding Heat and Common Mistakes", "Avoiding hot showers and heat rubs in the first 48 hours.", "Preventing excessive movement that can worsen tissue tears.", "Recognizing when wrapping is too tight and restricting flow.")
    ]
    for title_part, p1, p2, p3 in rice:
        title = f"Sports Medicine: RICE Protocol - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Ankle (7 topics)
    ankle = [
        ("Acute Ankle Sprain Early Management", "Applying immediate compression and elevation to limit swelling.", "Assessing weight-bearing capability to rule out fractures.", "Using early, pain-free ankle circles to maintain range."),
        ("Achilles Tendon and Joint Mobility Recovery", "Implementing progressive stretching for the Achilles tendon.", "Using resistance bands to recover inversion and eversion range.", "Addressing joint restrictions using manual therapy methods."),
        ("Proprioception Balance Board Progressions", "Using single-leg balance exercises on stable and unstable surfaces.", "Integrating racket actions with balance board drills.", "Improving joint position sense to prevent re-injury."),
        ("Peroneal Tendon Strength Rebuilding", "Strengthening the peroneal muscles to support lateral stability.", "Using eccentric training to build tendon resiliency.", "Progressing from isometric holds to dynamic band work."),
        ("Supportive Ankle Taping and Bracing", "Applying supportive ankle taping for early on-court work.", "Selecting functional braces that allow standard movement.", "Avoiding long-term dependency on tape to preserve joint strength."),
        ("On-Court Forward-Backward Footwork Reintroduction", "Gradually building up simple forward-backward movement.", "Reintroducing lateral chasse steps under controlled paces.", "Monitoring joint pain and swelling post-session."),
        ("Preventing Chronic Ankle Instability Pathways", "Structuring long-term strength maintenance for the calf and ankle.", "Addressing hip and knee weaknesses that affect foot strike.", "Educating players on shoe traction and landing habits.")
    ]
    for title_part, p1, p2, p3 in ankle:
        title = f"Sports Medicine: Ankle Sprain Rehab - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Patellar Tendinopathy (7 topics)
    patellar = [
        ("Landing and Deceleration Stress Mechanisms", "Analyzing knee tendon loading during jump landings and deep lunges.", "Identifying training volume spikes as primary risk factors.", "Evaluating lower extremity biomechanical imbalances."),
        ("Wall Sits and Isometric Knee Loading", "Using static leg holds (e.g., wall sits) to relieve tendon pain.", "Structuring sets of 45-second holds with high load.", "Integrating isometric work as pre-session preparation."),
        ("Slant Board Eccentric Squat Progressions", "Using slant boards to target the patellar tendon.", "Controlling the downward phase of squats to stimulate tendon repair.", "Progressing load volume based on player pain scores."),
        ("Heavy Slow Resistance Squats and Presses", "Implementing slow squats and leg presses (3-4s up, 3-4s down).", "Structuring heavy resistance sets of 6-8 repetitions.", "Promoting collagen remodeling in damaged tendon tissue."),
        ("Tendon Pain 24-Hour Tracking Protocols", "Monitoring and adjusting daily jump and lunge volume.", "Tracking tendon pain responses 24 hours post-exercise.", "Structuring recovery days between heavy impact training."),
        ("Knee-Toe Alignment in Court Lunges", "Ensuring the knee tracks over the toe during deep lunges.", "Using hip-dominant deceleration to reduce knee load.", "Modifying step-out distances when tendon pain flares."),
        ("Single-Leg Hop and Jump Exit Criteria", "Ensuring pain-free performance during double-leg jumps.", "Verifying strength equality between left and right limbs.", "Gradual progression from low-impact hops to high-velocity jumps.")
    ]
    for title_part, p1, p2, p3 in patellar:
        title = f"Sports Medicine: Patellar Tendinopathy - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Rotator Cuff (7 topics)
    cuff = [
        ("Overhead Stroke Glenohumeral Joint Anatomy", "Understanding the four rotator cuff muscles and shoulder stability.", "Analyzing glenohumeral joint movement during overhand smashes.", "Identifying common muscle imbalances in badminton shoulders."),
        ("Resistance Band Rotations for Strength", "Using resistance bands for internal and external rotation.", "Implementing side-lying dumbbell rotations for stability.", "Progressing load and speed to match stroke demands."),
        ("Serratus Anterior Scapular Stabilization", "Strengthening lower traps and serratus anterior for scapular movement.", "Using rows, Y-T-W raises, and push-up plus exercises.", "Improving shoulder biomechanics to prevent subacromial pinch."),
        ("Body Mass Rotation Kinetic Chain Linkage", "Integrating hip rotation and core power with shoulder action.", "Reducing rotator cuff load by utilizing body mass rotation.", "Drilling overhead stroke mechanics to maintain kinetic flow."),
        ("Elbow Height and Shoulder Contact Points", "Analyzing how poor elbow height increases shoulder strain.", "Correcting late contact points that stress rotator cuff tendons.", "Balancing overhead smash volumes with defensive drives."),
        ("Band Pull-Aparts and Dynamic Activation", "Implementing band pull-aparts and arm circles before play.", "Activating stabilizing muscles prior to high-speed swings.", "Improving shoulder range of motion using dynamic movements."),
        ("Progressive Return-to-Smash Court Testing", "Starting with low-intensity underhand clearances and drives.", "Progressing to half-smashes and controlled drops.", "Verifying pain-free high-speed overhead smashes in drills.")
    ]
    for title_part, p1, p2, p3 in cuff:
        title = f"Sports Medicine: Rotator Cuff Instability - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Thoracic Spine (7 topics)
    thoracic = [
        ("Thoracic Extension and Smash Power Link", "Understanding how thoracic extension contributes to smash speed.", "Addressing overhead power drops due to stiff upper backs.", "Integrating thoracic mobility into regular warm-up protocols."),
        ("Foam Roller and Bench Extension Stretches", "Using foam rollers to stretch and open the thoracic spine.", "Performing bench-assisted thoracic extensions with a dowel.", "Maintaining lumbar spine stability during upper back stretch."),
        ("Quadruped Rib Opener Rotation Drills", "Using quadruped rib openers and thread-the-needle stretches.", "Improving rotation capacity to support backhand movement.", "Drilling rotation mechanics to balance unilateral movement stress."),
        ("Upper Back Stiffness Shoulder Impingement", "Analyzing how thoracic stiffness causes shoulder compensation.", "Improving upper back mobility to resolve impingements.", "Assessing thoracic movement limits during shoulder rehab."),
        ("Lumbar Protection in High-Reach Clears", "Using upper back mobility to prevent excessive lower back arching.", "Protecting the lumbar spine during high-reach overhead clears.", "Coordinating core stability with upper chest mobility."),
        ("Daily 5-10 Minute Desk-Bound Routines", "Designing 5-10 minute daily routines for desk-bound players.", "Varying dynamic stretches to cover rotation and extension.", "Fostering consistent mobility habits in junior players."),
        ("Seated Rotation Testing Protocols", "Using seated rotation tests to measure thoracic mobility.", "Identifying bilateral rotation differences using visual markers.", "Tracking range of motion changes across training phases.")
    ]
    for title_part, p1, p2, p3 in thoracic:
        title = f"Sports Medicine: Thoracic Spine Mobility - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Core (5 topics)
    core = [
        ("Transverse Abdominis Activation and Breathing", "Teaching pelvic tilt and stomach vacuum techniques.", "Activating deep core muscles before starting weight sets.", "Integrating TA control with normal breathing patterns."),
        ("Pallof Presses and Anti-Rotation Stiffness", "Using pallof presses and single-arm carries to resist twist.", "Developing core stiffness to control lateral deceleration.", "Structuring anti-rotation work to protect the lower back."),
        ("Rotational Power Dynamic Stance Balance", "Designing core exercises that involve rotational power.", "Maintaining body control during mid-air stroke contact.", "Improving recovery speed from deep off-balance lunges."),
        ("Glute Bridge and Plank Progressions", "Adding limb movements to standard plank positions.", "Using single-leg glute bridges to build hamstring-glute synergy.", "Adjusting hold durations and loads to match player levels."),
        ("Swiss Ball Stability and Balance Drills", "Implementing swiss ball rollouts and passes to challenge stability.", "Improving balance coordination using unstable base training.", "Integrating racket movements with ball-based core drills.")
    ]
    for title_part, p1, p2, p3 in core:
        title = f"Sports Medicine: Core Stability - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    # Hydration (3 topics)
    hydration = [
        ("Pre-Match Fluids and Urine Color Checks", "Calculating fluid intake targets in the 2-3 hours before play.", "Checking hydration levels using urine color charts.", "Including electrolytes in pre-match fluids to prevent cramps."),
        ("Electrolyte Balancing during Long Matches", "Managing regular fluid intake during 11-point court breaks.", "Using sodium and potassium drinks during long matches.", "Recognizing early signs of dehydration like fatigue and headaches."),
        ("Post-Match Bodyweight Loss Calculations", "Weighing players before and after play to determine water loss.", "Drinking 1.5 liters of fluid for every kilogram of weight lost.", "Timing rehydration alongside post-match carbohydrate recovery.")
    ]
    for title_part, p1, p2, p3 in hydration:
        title = f"Sports Medicine: Hydration - {title_part}"
        safe_name = title.replace(" ", "_").replace(":", "").replace("-", "_").replace("(", "").replace(")", "")
        results.append((title, safe_name, [p1, p2, p3]))
        
    return results

def main():
    output_dir = "C:/Users/usEr/MyLLMDataProject/GeneratedTopics/Level_2"
    os.makedirs(output_dir, exist_ok=True)
    
    all_topics = []
    all_topics.extend(generate_periodization())     # 60
    all_topics.extend(generate_singles_tactics())   # 35
    all_topics.extend(generate_doubles_tactics())   # 35
    all_topics.extend(generate_mixed_tactics())     # 30
    all_topics.extend(generate_sports_science())    # 80
    all_topics.extend(generate_psychology())        # 45
    all_topics.extend(generate_sports_med())        # 50
    
    print(f"Total structured topics: {len(all_topics)}")
    
    if len(all_topics) != 335:
        print("ERROR: Total topics does not equal 335!")
        return
        
    written_files = 0
    for title, safe_name, outline in all_topics:
        filename = f"Topic_L2_{safe_name}.md"
        filepath = os.path.join(output_dir, filename)
        
        content = f"[[Level_2]]\n"
        content += f"# {title}\n\n"
        content += f"This micro-topic module covers the technical analysis and coaching guidelines for **{title}**.\n\n"
        content += f"## Technical Outline\n"
        for i, pt in enumerate(outline, 1):
            content += f"{i}. {pt}\n"
        content += f"\n#llm-deep-backlog\n"
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        written_files += 1
        
    print(f"Successfully wrote {written_files} files inside {output_dir}.")

if __name__ == "__main__":
    main()
