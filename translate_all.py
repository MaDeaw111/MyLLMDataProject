import os
import re
import argparse
import sys

sys.stdout.reconfigure(encoding='utf-8')

# BWF Categories
CATEGORIES = [
    '1_Technical_Skills',
    '2_Tactical_And_Match_Play',
    '3_Movement_And_Biomechanics',
    '4_Physical_And_Sport_Science',
    '5_Coaching_Methodology'
]

# Translation mapping for key terms in badminton curriculum
TH_DICT = {
    'an in-depth guide on the': 'แนวทางเชิงลึกเกี่ยวกับ',
    'an in-depth guide on': 'แนวทางเชิงลึกเกี่ยวกับ',
    'integration with special populations and inclusivity': 'ยุทธศาสตร์ความเท่าเทียมและการเข้าถึงสำหรับผู้บกพร่องทางร่างกายและสติปัญญา',
    'associative learning stage': 'ขั้นตอนการเรียนรู้แบบเชื่อมโยง (Associative Stage)',
    'cognitive learning stage': 'ขั้นตอนการเรียนรู้แบบพุทธิปัญญา (Cognitive Stage)',
    'autonomous learning stage': 'ขั้นตอนการเรียนรู้แบบอัตโนมัติ (Autonomous Stage)',
    'characteristics and coaching adjustments for players': 'ลักษณะเฉพาะและการปรับตัวของผู้ฝึกสอนสำหรับนักกีฬา',
    'refining movement patterns with fewer errors': 'การขัดเกลารูปแบบการเคลื่อนไหวโดยลดข้อผิดพลาดให้น้อยลง',
    'adapting': 'การดัดแปลง',
    'wheelchair (wh1/wh2)': 'วีลแชร์ (WH1/WH2)',
    'standing (sl3/sl4/su5)': 'ยืนเล่น (SL3/SL4/SU5)',
    'para-badminton': 'พาราแบดมินตัน',
    'players': 'นักกีฬา',
    'modifying communication and teaching techniques': 'การดัดแปลงเทคนิคการสื่อสารและการสอน',
    'intellectual disabilities (id)': 'ผู้ที่มีความบกพร่องทางสติปัญญา (ID)',
    'deaf players': 'นักกีฬาหูหนวก',
    'creating an inclusive environment': 'การสร้างสภาพแวดล้อมที่ครอบคลุมและเท่าเทียม',
    'respects diverse learning speeds and physical abilities': 'ที่เคารพความเร็วในการเรียนรู้และความสามารถทางร่างกายที่แตกต่างกัน',
    'cooperative feeding drill sequencing': 'การจัดลำดับแบบฝึกป้อนลูกแบบร่วมมือกัน',
    'representative match play simulation': 'การจำลองสถานการณ์แข่งขันเสมือนจริง',
    'workload monitoring and load adjustments': 'การควบคุมปริมาณงานและการปรับภาระงานซ้อม',
    'foundational technical coordination and movement': 'การประสานทักษะและการเคลื่อนไหวทางเทคนิคพื้นฐาน',
    'progressive training practices and feedback': 'แนวทางปฏิบัติการซ้อมที่ก้าวหน้าและข้อมูลสะท้อนกลับ',
    'tactical pattern adaptation and player safety': 'การดัดแปลงรูปแบบทางยุทธวิธีและความปลอดภัยของนักกีฬา',
    'under': 'ภายใต้',
    'simulation': 'การจำลอง',
    'distractions': 'สิ่งรบกวน',
    'auditory': 'ทางเสียง',
    'visual': 'ทางการมองเห็น',
    'learning': 'การเรียนรู้',
    'style': 'รูปแบบ',
    'method': 'วิธีการ',
    'shaping': 'ค่อยเป็นค่อยไป (Shaping)',
    'chaining': 'เชื่อมโยง (Chaining)',
    'whole-part-whole': 'ทั้งหมด-ส่วนย่อย-ทั้งหมด',
    'v-grip': 'จับไม้ V-Grip',
    'thumb grip': 'จับไม้ Thumb Grip',
    'panhandle grip': 'จับไม้ Panhandle Grip',
    'grip': 'การจับไม้',
    'forehand clear': 'ลูกเซฟโฟร์แฮนด์ (Forehand Clear)',
    'backhand clear': 'ลูกเซฟแบ็คแฮนด์ (Backhand Clear)',
    'forehand dropshot': 'ลูกหยอดโฟร์แฮนด์ (Forehand Dropshot)',
    'backhand dropshot': 'ลูกหยอดแบ็คแฮนด์ (Backhand Dropshot)',
    'forehand high serve': 'ลูกเสิร์ฟสูงโฟร์แฮนด์ (Forehand High Serve)',
    'forehand flick serve': 'ลูกเสิร์ฟสะบัดโฟร์แฮนด์ (Forehand Flick Serve)',
    'backhand low serve': 'ลูกเสิร์ฟหยอดแบ็คแฮนด์ (Backhand Low Serve)',
    'backhand flick serve': 'ลูกเสิร์ฟสะบัดแบ็คแฮนด์ (Backhand Flick Serve)',
    'forehand and backhand net kills': 'ลูกแย็บหน้าเน็ตแบบโฟร์แฮนด์และแบ็คแฮนด์',
    'forehand and backhand net lifts': 'ลูกโยนหลังหน้าเน็ตแบบโฟร์แฮนด์และแบ็คแฮนด์',
    'forehand and backhand net shots': 'ลูกหยอดหน้าเน็ตแบบโฟร์แฮนด์และแบ็คแฮนด์',
    'midcourt drives': 'ลูกดาดกลางคอร์ท (Midcourt Drives)',
    'forehand pulled dropshot': 'ลูกหยอดตัดหน้าเน็ตแบบดึงโฟร์แฮนด์',
    'jump smash': 'ลูกกระโดดตบ (Jump Smash)',
    'forehand smash': 'ลูกตบโฟร์แฮนด์ (Forehand Smash)',
    'split step': 'จังหวะสปลิทสเต็ป (Split Step)',
    'split-step': 'จังหวะสปลิทสเต็ป (Split Step)',
    'lunging': 'การก้าวลันจ์',
    'forearm pronation': 'ทักษะการคว่ำข้อมือท่อนแขน (Forearm Pronation)',
    'forearm supination': 'ทักษะการหงายข้อมือท่อนแขน (Forearm Supination)',
    'biomechanics': 'หลักการชีวกลศาสตร์',
    'footwork': 'ทักษะฟุตเวิร์ค',
    'anaerobic': 'ระบบพลังงานแอนาโรบิก',
    'aerobic': 'ระบบพลังงานแอโรบิก',
    'vo2 max': 'ความสามารถในการใช้ออกซิเจนสูงสุด (VO2 Max)',
    'lactate threshold': 'เกณฑ์การสะสมกรดแลคติก (Lactate Threshold)',
    'ischemic preconditioning': 'การเตรียมกล้ามเนื้อก่อนออกกำลังกาย (Ischemic Preconditioning)',
    'hydrotherapy': 'การฟื้นฟูร่างกายด้วยน้ำ (Hydrotherapy)',
    'sleep': 'การนอนหลับ',
    'active recovery': 'การฟื้นฟูร่างกายเชิงรุก (Active Recovery)',
    'injury prevention': 'แนวทางการป้องกันอาการบาดเจ็บ',
    'coaching philosophy': 'ปรัชญาและแนวคิดการเป็นผู้ฝึกสอน',
    'coaching process': 'กระบวนการโค้ชและวิธีวิทยาการสอน',
    'feedback': 'การส่งมอบข้อมูลป้อนกลับ (Feedback)',
    'pedagogy': 'ทฤษฎีการสอนแบดมินตัน',
    'inclusivity': 'แนวทางความเท่าเทียมและโอกาสการมีส่วนร่วม',
    'biomechanical analysis': 'การวิเคราะห์ชีวกลศาสตร์',
    'video setup': 'ระบบบันทึกวิดีโอ',
    'minutes': 'นาที',
    'minute': 'นาที',
    'video': 'วิดีโอ',
    'shadow': 'การซ้อมเงา (Shadow)',
    'run biomechanical sequences': 'ดำเนินการเคลื่อนไหวเชิงชีวกลศาสตร์',
    'checking joint angles': 'ตรวจสอบมุมของข้อต่อ',
    'movement symmetry': 'ความสมมาตรของการเคลื่อนไหว',
    'practice 60-second recovery routines': 'ฝึกกิจวัตรการฟื้นฟูร่างกาย 60 วินาที',
    'during 11-point match intervals': 'ระหว่างการพักเกม 11 แต้ม',
    'implement diaphragmatic breathing': 'ฝึกการหายใจด้วยกะบังลม',
    'to lower heart rate quickly': 'เพื่อลดอัตราการเต้นของหัวใจอย่างรวดเร็ว',
    'high-load target drill': 'แบบฝึกซ้อมเป้าหมายปริมาณงานสูง',
    'machine / racket feed': 'ป้อนลูกด้วยเครื่อง / แร็กเก็ต',
    'high-velocity cooperative feeds': 'การป้อนลูกร่วมกันความเร็วสูง',
    'player executes target strokes under fatigue': 'นักกีฬาตีลูกเป้าหมายภายใต้สภาวะความล้า',
    'open rally pressure test': 'การทดสอบความกดดันในการเล่นโต้กลับแบบเปิด',
    'live play (2v1 feeders)': 'การเล่นจริง (ผู้ป้อนลูก 2 ต่อ 1)',
    'play under restricted boundaries': 'เล่นภายใต้ขอบเขตที่จำกัด',
    'force rapid tactical adjustments and quick recovery': 'บีบให้ปรับเปลี่ยนแทกติกอย่างรวดเร็วและฟื้นตัวได้ฉับพลัน',
    'interval heart rate drop': 'การลดลงของอัตราการเต้นของหัวใจในช่วงพัก',
    'reduce heart rate by >20 bpm within the 60-second mid-game interval': 'ลดอัตราการเต้นของหัวใจมากกว่า 20 ครั้งต่อนาทีภายในช่วงพักเกม 60 วินาที',
    'lactate accumulation buffer': 'การกันชนการสะสมของกรดแลคติก (Lactate Buffer)',
    'limit blood lactate levels to <8.0 mmol/L during high-intensity competitive sets': 'จำกัดระดับกรดแลคติกในเลือดต่ำกว่า 8.0 mmol/L ในระหว่างเซตการแข่งความเข้มข้นสูง',
    'gaze focus retention': 'การรักษาจุดโฟกัสสายตา',
    'maintain gaze fixation on the anchor target in 9 out of 10 interval points': 'รักษาการจ้องมองที่เป้าหมายหลักใน 9 จาก 10 แต้มในช่วงพัก'
}

def translate_phrase(text):
    text_lower = text.lower()
    phrases = [
        ('vo2 max testing under auditory distractions simulation', 'การทดสอบ VO2 Max ภายใต้การจำลองสิ่งรบกวนทางเสียง'),
        ('blood lactate thresholds under 11-point interval coaching', 'เกณฑ์กรดแลคติกในเลือดภายใต้การโค้ชช่วงพัก 11 แต้ม'),
        ('blood lactate thresholds under tactical changes & strategy', 'เกณฑ์กรดแลคติกในเลือดภายใต้การเปลี่ยนแปลงเชิงยุทธวิธีและแผนการเล่น'),
        ('blood lactate thresholds under physiological stress & anticipation', 'เกณฑ์กรดแลคติกในเลือดภายใต้ความเครียดทางสรีรวิทยาและการคาดการณ์'),
        ('blood lactate thresholds under visual occlusion training', 'เกณฑ์กรดแลคติกในเลือดภายใต้การฝึกแบบจำกัดการมองเห็น'),
        ('blood lactate thresholds under auditory distractions simulation', 'เกณฑ์กรดแลคติกในเลือดภายใต้การจำลองสิ่งรบกวนทางเสียง'),
        ('ischemic preconditioning under 11-point interval coaching', 'การเตรียมความพร้อมกล้ามเนื้อ (Ischemic Preconditioning) ภายใต้การโค้ชช่วงพัก 11 แต้ม'),
        ('ischemic preconditioning under tactical changes & strategy', 'การเตรียมความพร้อมกล้ามเนื้อ (Ischemic Preconditioning) ภายใต้การเปลี่ยนแปลงเชิงยุทธวิธีและแผนการเล่น'),
        ('ischemic preconditioning under physiological stress & anticipation', 'การเตรียมความพร้อมกล้ามเนื้อ (Ischemic Preconditioning) ภายใต้ความเครียดทางสรีรวิทยาและการคาดการณ์'),
        ('ischemic preconditioning under visual occlusion training', 'การเตรียมความพร้อมกล้ามเนื้อ (Ischemic Preconditioning) ภายใต้การฝึกแบบจำกัดการมองเห็น'),
        ('ischemic preconditioning under auditory distractions simulation', 'การเตรียมความพร้อมกล้ามเนื้อ (Ischemic Preconditioning) ภายใต้การจำลองสิ่งรบกวนทางเสียง'),
        ('hydrotherapy & recovery under 11-point interval coaching', 'วารีบำบัดและการฟื้นฟูร่างกายภายใต้การโค้ชช่วงพัก 11 แต้ม'),
        ('sleep, rest & active recovery under notational analysis', 'การนอนหลับ การพักผ่อน และการฟื้นฟูร่างกายอย่างกระฉับกระเฉงภายใต้การวิเคราะห์จดบันทึกการเล่น')
    ]
    for eng, th in phrases:
        if eng in text_lower:
            return th
            
    # Fallback word-by-word/regex replacement
    translated = text
    # Sort keys by length in reverse to match longest phrases first
    sorted_keys = sorted(TH_DICT.keys(), key=len, reverse=True)
    for k in sorted_keys:
        translated = re.sub(r'\b' + re.escape(k) + r'\b', TH_DICT[k], translated, flags=re.IGNORECASE)
        
    # Translate prefixes
    translated = re.sub(r'\bPlan L1\b', 'แผนการซ้อม L1', translated, flags=re.IGNORECASE)
    translated = re.sub(r'\bPlan L2\b', 'แผนการซ้อม L2', translated, flags=re.IGNORECASE)
    translated = re.sub(r'\bPlan L3\b', 'แผนการซ้อม L3', translated, flags=re.IGNORECASE)
    translated = re.sub(r'\bTopic L1\b', 'หัวข้อ L1', translated, flags=re.IGNORECASE)
    translated = re.sub(r'\bTopic L2\b', 'หัวข้อ L2', translated, flags=re.IGNORECASE)
    translated = re.sub(r'\bTopic L3\b', 'หัวข้อ L3', translated, flags=re.IGNORECASE)
    
    return translated

# Rich section generator in Thai
def generate_sections_th(filename, title_th, description_th, outline_points_th, category_th):
    # Core Purpose
    if category_th == '1_Technical_Skills_TH':
        purpose = f"วัตถุประสงค์หลักของการฝึกทักษะ **{title_th}** (ทำไปเพื่ออะไร) คือการสร้างความคุ้นชินและพฤติกรรมการเล่นที่ถูกต้องตามหลักชีวกลศาสตร์ ในกีฬาแบดมินตัน การปรับแรงบีบมือที่หน้าไม้ให้เหมาะสม การคว่ำหรือหงายข้อมือ (Forearm Pronation/Supination) และการตีลูกในจุดปะทะที่เหมาะสมที่สุดเป็นรากฐานที่สำคัญ การฝึกสิ่งนี้ช่วยให้นักกีฬาสามารถสร้างความเร็วหัวไม้ได้สูงสุดโดยใช้แรงน้อยที่สุด ควบคุมวิถีลูกได้อย่างมีประสิทธิภาพ และรักษาความสม่ำเสมอภายใต้แรงกดดันของการแข่งขันในขณะที่ลดความล้าของข้อต่อ"
    elif category_th == '2_Tactical_And_Match_Play_TH':
        purpose = f"วัตถุประสงค์หลักของการฝึกฝน **{title_th}** (ทำไปเพื่ออะไร) คือการพัฒนาสติปัญญาทางยุทธวิธีและยุทธศาสตร์การเล่นในแมตช์จริง ผู้ฝึกสอนต้องฝึกฝนให้นักกีฬาเข้าใจการครอบคลุมพื้นที่คอร์ท การหมุนวนตำแหน่งในประเภทคู่ และรูปแบบการเล่นในประเภทเดี่ยวเพื่อฉกฉวยโอกาสจากจุดอ่อนของคู่ต่อสู้ สิ่งนี้ทำให้นักกีฬาสามารถตัดสินใจได้อย่างรวดเร็ว กำหนดจังหวะการเล่น และดำเนินแผนการเล่นตามแผนภายใต้ความกดดันของการแข่งขัน"
    elif category_th == '3_Movement_And_Biomechanics_TH':
        purpose = f"วัตถุประสงค์หลักของการฝึกฝน **{title_th}** (ทำไปเพื่ออะไร) คือการเพิ่มประสิทธิภาพการเคลื่อนไหวร่างกายและชีวกลศาสตร์ของการตีลูก การวางฟุตเวิร์คที่ถูกต้อง (Chasse, Crossover) จังหวะการสปลิทสเต็ป และการประสานงานของสายโซ่จลนศาสตร์ช่วยให้นักกีฬาเคลื่อนที่ครอบคลุมคอร์ทได้อย่างรวดเร็วและสามารถตีลูกจากฐานที่มั่นคง สิ่งนี้ช่วยลดพลังงานที่ใช้ไป เพิ่มความเร็วการตอบสนอง และป้องกันอาการบาดเจ็บสะสมเชิงกลที่รยางค์ล่าง"
    elif category_th == '4_Physical_And_Sport_Science_TH':
        purpose = f"วัตถุประสงค์หลักของการพัฒนา **{title_th}** (ทำไปเพื่ออะไร) คือการสร้างความสามารถทางกายภาพและความยืดหยุ่นทางสรีรวิทยาที่จำเป็นสำหรับแบดมินตันระดับสูง การพัฒนาระบบพลังงาน (ความทนทานแบบใช้ออกซิเจนและไม่ใช้อออกซิเจน) พลังระเบิด ความเร็ว-ความคล่องตัว และความอ่อนตัวมีความสำคัญอย่างยิ่ง การบูรณาการเวชศาสตร์การกีฬา โภชนาการ การจัดการปริมาณงานในช่วงการเจริญเติบโต (PHV) และการฟื้นฟูร่างกายอย่างกระฉับกระเฉงจะช่วยป้องกันภาวะฝึกเกินและการบาดเจ็บจากการเล่นกีฬา"
    else: # 5_Coaching_Methodology_TH
        purpose = f"วัตถุประสงค์หลักของการฝึกทักษะ **{title_th}** (ทำไปเพื่ออะไร) คือการวางระเบียบวิธีวิทยาการสอนและกรอบการทำงานสำหรับผู้ฝึกสอน การประยุกต์ใช้รูปแบบการเรียนรู้ (VAK) ระยะของการเรียนรู้ทักษะกลไก และขั้นตอนการสอนที่คืบหน้า (Shaping, Chaining) ช่วยให้ผู้ฝึกสอนออกแบบแบบฝึกที่มีประสิทธิภาพ สิ่งนี้ช่วยรับประกันการจัดการกลุ่มที่ปลอดภัย โครงสร้างการฝึกอบรมที่ครอบคลุม และการส่งมอบข้อมูลป้อนกลับที่ชัดเจน"

    # Deep-Dive Synthesis
    p1_desc = outline_points_th[0] if len(outline_points_th) > 0 else "ทักษะพื้นฐาน"
    p2_desc = outline_points_th[1] if len(outline_points_th) > 1 else "การดำเนินเทคนิค"
    p3_desc = outline_points_th[2] if len(outline_points_th) > 2 else "ขั้นตอนการบูรณาการซ้อม"
    
    if category_th == '1_Technical_Skills_TH':
        p1 = f"การวิเคราะห์เชิงลึกเกี่ยวกับ **{p1_desc}** แสดงให้เห็นว่าการวางนิ้วและแรงบีบของมือมีความสำคัญอย่างยิ่ง นักกีฬาต้องรักษาการจับไม้ที่ผ่อนคลายเพื่อช่วยให้ข้อมือมีความยืดหยุ่นสูงสุดและรองรับการหมุนท่อนแขนอย่างรวดเร็ว (Pronation หรือ Supination) การจับไม้ที่เกร็งเกินไปจะจำกัดช่วงของการเคลื่อนไหว ส่งผลให้ความเร็วหัวไม้ลดลงขณะสัมผัสลูก"
        p2 = f"นอกจากนี้ การปรับจุดปะทะลูกให้สัมพันธ์กับร่างกายตามที่ระบุใน **{p2_desc}** จะช่วยให้มั่นใจได้ถึงการส่งผ่านแรงที่ดีที่สุด การสัมผัสลูกที่เร็วหรือช้าเกินไปจะขัดขวางสายโซ่จลนศาสตร์ (Kinetic Chain) นักกีฬาต้องจัดระเบียบร่างกายเพื่อปะทะลูกด้านหน้าไหล่ข้างที่ตีไม้เล็กน้อยเพื่อเพิ่มระยะและแรงง้างสูงสุด"
        p3 = f"ประการสุดท้าย การบูรณาการ **{p3_desc}** เข้ากับแบบฝึกป้อนลูกช่วยสร้างทักษะนี้แบบอัตโนมัติ การเปลี่ยนจากการป้อนลูกหลายลูกด้วยมือมาเป็นการตีโต้ด้วยแร็กเก็ตช่วยให้นักพัฒนาความคุมทักษะได้ในจังหวะความเร็วที่เพิ่มขึ้น ผู้ฝึกสอนควรเน้นที่จุดตรวจสอบทางเทคนิคมากกว่าตัวชี้วัดผลลัพธ์ในระยะแรกของการเรียนรู้"
    elif category_th == '2_Tactical_And_Match_Play_TH':
        p1 = f"การวิเคราะห์ **{p1_desc}** เน้นย้ำถึงความสำคัญของความเข้าใจพื้นที่และการครอบคลุมพื้นที่คอร์ท ในการแข่งขันประเภทเดี่ยวหรือประเภทคู่ นักกีฬาต้องดำเนินรูปแบบการตีที่สร้างพื้นที่ว่างในสนามของคู่ต่อสู้ สิ่งนี้ต้องการความสม่ดเสมอในการเปลี่ยนแปลงความเร็วและมุมของลูกเพื่อบีบให้คู่ต่อสู้ออกจากตำแหน่งตั้งรับเดิม"
        p2 = f"ภายใต้ความเครียดในเกมแข่งขัน การจัดการจังหวะการเปลี่ยนผ่านตามที่อธิบายใน **{p2_desc}** จะกำหนดว่าใครเป็นผู้ควบคุมการตีโต้ การเปลี่ยนผ่านจากการบล็อกรับเป็นการโต้กลับ หรือการตามไปแย็บหน้าเน็ตต้องเกิดขึ้นอย่างเป็นอัตโนมัติ ผู้ฝึกสอนควรใช้ข้อจำกัดของเกมแข่งขันจริงในการจำลองเพื่อสร้างความตระหนักรู้สถานการณ์จริงในการฝึกซ้อม"
        p3 = f"นอกจากนี้ การประสานยุทธวิธีร่วมกับ **{p3_desc}** เป็นสิ่งสำคัญในการรักษาประสิทธิภาพการเล่น การวิเคราะห์แนวโน้มของคู่ต่อสู้และการปรับตำแหน่งของผู้เสิร์ฟ/ผู้รับในระหว่างช่วงพักเกมสามารถเปลี่ยนโมเมนตัมของแมตช์ได้ ผู้ฝึกสอนควรใช้เครื่องมือวิเคราะห์วิดีโอเพื่อบันทึกความสม่ำเสมอในการเล่นยุทธวิธีในช่วงการเตรียมแข่งขัน"
    elif category_th == '3_Movement_And_Biomechanics_TH':
        p1 = f"การทำความเข้าใจพารามิเตอร์ทางชีวกลศาสตร์ของ **{p1_desc}** เป็นสิ่งจำเป็นสำหรับประสิทธิภาพการเคลื่อนที่ กลไกสปลิทสเต็ป (Split-step) ต้องสอดคล้องกับจังหวะการตีของคู่ต่อสู้พอดี เพื่อกระตุ้นแรงตึงตัวของกล้ามเนื้อน่องล่วงหน้าสำหรับการระเบิดพลังเคลื่อนที่ไปด้านข้างหรือด้านหน้า การจับจังหวะสปลิทสเต็ปที่ผิดพลาดจะเพิ่มเวลาตอบสนองอย่างมีนัยสำคัญ"
        p2 = f"ในระหว่างการเคลื่อนที่ในสนาม การจัดการแรงเบรกและชะลอตัวตามที่เห็นใน **{p2_desc}** ช่วยป้องกันข้อต่อจากแรงปะทะที่รุนแรง การก้าวลันจ์ลงด้วยส้นเท้าไปจนถึงปลายเท้า โดยที่เข่าอยู่ในแนวตั้งตรงเหนือข้อเท้าจะป้องกันอาการเอ็นสะบ้าอักเสบ (Patellar Tendinopathy) ผู้ฝึกสอนต้องมุ่งเน้นการจัดตำแหน่งเท้าที่ถูกต้องระหว่างการเปลี่ยนทิศทางอย่างรวดเร็ว"
        p3 = f"ท้ายที่สุด ลำดับสายโซ่จลนศาสตร์ของ **{p3_desc}** เป็นตัวกำหนดแรงขับเคลื่อน แรงที่สร้างจากการเหยียดขาและการหมุนสะโพกต้องส่งผ่านอย่างราบรื่นผ่านกระดูกสันหลังส่วนอกและไหล่ การส่งแรงที่ลื่นไหลช่วยสร้างความเร็วหัวไม้ที่สูงโดยไม่สร้างภาระหนักเกินไปกับกลุ่มกล้ามเนื้อรอบข้อต่อไหล่ (Rotator Cuff)"
    elif category_th == '4_Physical_And_Sport_Science_TH':
        p1 = f"การปรับตัวทางสรีรวิทยาในกีฬาแบดมินตันต้องการเป้าหมายที่เฉพาะเจาะจงกับ **{p1_desc}** การฝึกซ้อมช่วงสลับความเข้มข้นสูง (HIIT) จะกระตุ้นระบบพลังงานแบบแอนาโรบิกแลคติก (Anaerobic Lactic System) เพื่อสร้างความทนทานต่อการสะสมของกรดแลคติก ขณะเดียวกันการฝึกความทนทานแบบแอโรบิก (Aerobic Endurance) จะสนับสนุนการฟื้นตัวอย่างรวดเร็วระหว่างการตีโต้และการแข่งขัน"
        p2 = f"เพื่อป้องกันภาวะฝึกเกิน (Overtraining) การจัดการภาระการฝึกซ้อมตามที่อภิปรายใน **{p2_desc}** เป็นสิ่งสำคัญ การติดตามข้อมูลอัตราการเต้นของหัวใจและการใช้สเกลวัดระดับความเหนื่อยช่วยให้ผู้ฝึกสอนปรับปริมาณการฝึกซ้อมได้ ภายใต้ช่วงเวลาการเจริญเติบโตอย่างรวดเร็ว (PHV) ปริมาณการฝึกต้องได้รับการปรับขนาดอย่างระมัดระวังเพื่อปกป้องกระดูกและข้อต่อที่กำลังพัฒนา"
        p3 = f"นอกจากนี้ การผสมผสานโปรโตคอลการฟื้นฟูสมรรถภาพร่วมกับ **{p3_desc}** ช่วยให้มั่นใจได้ถึงการกลับมาลงสนามได้อย่างปลอดภัย การฝึกเสริมความแข็งแรงแบบเอ็กเซนตริก (Eccentric Strengthening) สำหรับข้อเท้าและข้อไหล่ช่วยกระตุ้นการจัดเรียงตัวใหม่ของเนื้อเยื่อ การดื่มน้ำและการรับประทานคาร์โบไฮเดรต-คาเฟอีนยังช่วยป้องกันความล้าที่เกิดจากการขาดน้ำได้อย่างมีประสิทธิภาพ"
    else: # 5_Coaching_Methodology_TH
        p1 = f"การประยุกต์ใช้หลักการเรียนการสอนกับ **{p1_desc}** ช่วยเร่งการเรียนรู้ทักษะกลไก ผู้ฝึกสอนควรปรับการสอนให้สอดคล้องกับรูปแบบการเรียนรู้ของนักกีฬา (VAK) ผู้เรียนผ่านการมองเห็น (Visual) จะได้รับประโยชน์จากการสาธิตที่ชัดเจนและแผนภาพกระดานดำ ขณะที่ผู้เรียนผ่านการเคลื่อนไหว (Kinesthetic) ต้องการข้อมูลสะท้อนกลับทางกายภาพทันที"
        p2 = f"การออกแบบการฝึกซ้อมที่ก้าวหน้าตามที่ระบุใน **{p2_desc}** เป็นพื้นฐานสำคัญของกระบวนการโค้ช แผนการซ้อมต้องระบุรายละเอียดของระยะเวลา ประเภทการป้อนลูก และมาตรการด้านความปลอดภัย ผู้ฝึกสอนควรใช้วิธี 'Shaping' หรือปรับแต่งกฎเกณฑ์/อุปกรณ์เพื่อค่อยๆ เข้าใกล้ทักษะเป้าหมายที่ต้องการ"
        p3 = f"สุดท้าย การกำหนดปรัชญาการโค้ชที่เน้นไปที่ **{p3_desc}** ช่วยส่งเสริมความเท่าเทียม การปรับขนาดของคอร์ท ความสูงของเน็ตเสิร์ฟ และขนาดแร็กเก็ตช่วยให้นักกีฬาที่มีความพิการทางกายหรือสติปัญญาสามารถมีส่วนร่วมได้อย่างเต็มที่ การจัดการกลุ่มที่ปลอดภัยและการตระหนักรู้ขอบเขตจริยธรรมสร้างความไว้วางใจและการเล่นกีฬาระยะยาว"

    synthesis = f"{p1}\n\n{p2}\n\n{p3}"

    # Practical Coaching Application
    if category_th == '1_Technical_Skills_TH':
        app = f"ในระหว่างการฝึกซ้อมทางเทคนิค 90 นาที ผู้ฝึกสอนออกแบบแบบฝึกซ้อมบนสนามเพื่อเน้นการตีลูกนี้ หลังจากการสาธิตการเปลี่ยนการจับไม้ ผู้ฝึกสอนจัดกลุ่มนักกีฬา ผู้ป้อนลูก A ป้อนลูกอันเดอร์แฮนด์ 20 ลูกไปยังโซนตีของนักกีฬา B ผู้ฝึกสอนสังเกตนักกีฬา B โดยเน้นไปที่ **{p1_desc}** (เช่น แรงบีบมือ) ผู้ฝึกสอนให้คำแนะนำด้วยเสียงทันที (เช่น 'ผ่อนคลายนิ้วมือ') และใช้วางกรวยเป้าหมายบนสนามเพื่อวัดความแม่นยำ หากนักกีฬาทำสำเร็จ 15 ใน 20 ลูก จะได้ขยับไปฝึกตีโต้ด้วยแร็กเก็ต"
    elif category_th == '2_Tactical_And_Match_Play_TH':
        app = f"ผู้ฝึกสอนจำลองเกมเดี่ยวแบบครึ่งคอร์ท โดยกำหนดให้นักกีฬา A เล่นเฉพาะลูกหยอดและลูกเซฟ ขณะที่นักกีฬา B สามารถตีลูกใดก็ได้แต่ต้องเป้าหมายไปที่มุมแบ็คแฮนด์ สถานการณ์เชิงยุทธวิธีนี้เน้นย้ำไปที่ **{p1_desc}** ผู้ฝึกสอนยืนอยู่ข้างคอร์ท จดบันทึกวิธีที่นักกีฬาปรับการครอบคลุมพื้นที่และการตั้งรับตำแหน่งกลางคอร์ท ในระหว่างการพักเกม ผู้ฝึกสอนประเมินแผนผังเชิงยุทธวิธีเพื่อชี้ให้นักกีฬาเห็นว่าตำแหน่งการรับส่งผลต่อผลลัพธ์การเล่นอย่างไร"
    elif category_th == '3_Movement_And_Biomechanics_TH':
        app = f"ในระหว่างการฝึกซ้อมการเคลื่อนไหว ผู้ฝึกสอนออกแบบวงจรเงาฟุตเวิร์ค (Shadow Footwork) กรวยเป้าหมายถูกจัดวางไว้ที่มุมทั้งสี่ นักกีฬาทำสปลิทสเต็ปที่ตำแหน่งฐานกลางคอร์ทและสไลด์ตัวไปยังมุมต่างๆ โดยเน้นไปที่ **{p1_desc}** (เช่น การก้าวลันจ์ลงด้วยส้นเท้าก่อน) ผู้ฝึกสอนใช้กล้องความเร็วสูงเพื่อบันทึกการเคลื่อนไหว และให้นักกีฬาดูลักษณะหัวเข่าและข้อเท้าในช่วงพัก เพื่อแก้ไขพฤติกรรมการลงเท้าที่บกพร่องทันที"
    elif category_th == '4_Physical_And_Sport_Science_TH':
        app = f"ผู้ฝึกสอนออกแบบวงจรการเตรียมความพร้อมทางกายภาพเฉพาะสำหรับแบดมินตัน ประกอบด้วยการเคลื่อนไหวหลายลูกความเข้มข้นสูงเป็นเวลา 40 วินาทีตามด้วยการพัก 20 วินาที แบบฝึกนี้มีเป้าหมายที่ **{p1_desc}** (เช่น ความทนทานต่อกรดแลคติก) ผู้ฝึกสอนตรวจสอบอัตราการเต้นของหัวใจของนักกีฬาระหว่างเซสชัน หากอัตราการเต้นของหัวใจฟื้นตัวไม่ต่ำกว่า 130 ครั้งต่อนาทีในช่วงพัก ผู้ฝึกสอนจะปรับลดความเร็วในการป้อนลูกลงเพื่อความปลอดภัยและป้องกันการฝึกเกิน"
    else: # 5_Coaching_Methodology_TH
        app = f"เพื่อสอนแบบฝึกซ้อมยุทธวิธีใหม่ ผู้ฝึกสอนใช้วิธีวิทยาการสอนแบบ 'ทั้งหมด-ส่วนย่อย-ทั้งหมด' (Whole-Part-Whole) ขั้นแรก ปล่อยให้นักกีฬาเล่นเกมอย่างอิสระเพื่อสังเกตการตอบสนองตามธรรมชาติ (ทั้งหมด) ต่อจากนั้น แยกแยะจังหวะการเปลี่ยนผ่านที่สำคัญ โดยเน้นไปที่ **{p1_desc}** โดยใช้กระดานแสดงภาพและ shadow play (ส่วนย่อย) สุดท้าย บูรณาการการเคลื่อนไหวกลับเข้าไปในเกมแข่งขันที่ควบคุม (ทั้งหมด) ผู้ฝึกสอนส่งมอบคำแนะนำที่เป็นบวกโดยใช้สไตล์ VAK ให้เหมาะสมกับนักกีฬาแต่ละคน"

    # Sample QA Pair
    question = f"ผู้ฝึกสอนควรออกแบบขั้นตอนการฝึกซ้อมและตรวจสอบจุดทางเทคนิค/หลักการสอนสำหรับ **{title_th}** อย่างไร?"
    if category_th == '1_Technical_Skills_TH':
        answer = f"เพื่อพัฒนาทักษะ **{title_th}** ผู้ฝึกสอนควรจัดโครงสร้างการสอนเป็น 3 ระยะหลัก:\n1. **กลศาสตร์การจับไม้และข้อมือ**: เน้นที่ **{p1_desc}** เพื่อให้นักกีฬารักษาแรงจับที่ผ่อนคลายเพื่อสร้างแรงสะบัดในการตีลูก\n2. **การจัดตำแหน่งจุดปะทะ**: จัดท่าทางร่างกายเพื่อให้สอดคล้องกับ **{p2_desc}** โดยมั่นใจว่าจุดปะทะลูกอยู่ด้านหน้าร่างกายเพื่อประสิทธิภาพการส่งแรงสูงสุด\n3. **ความต่อเนื่องของแบบฝึก**: ออกแบบการป้อนลูกเพื่อสร้างความสม่ำเสมอ โดยเริ่มจากการป้อนลูกด้วยมือไปจนถึงการตีโต้จริงเพื่อผสาน **{p3_desc}** เข้าด้วยกัน"
    elif category_th == '2_Tactical_And_Match_Play_TH':
        answer = f"เพื่อประยุกต์ใช้ **{title_th}** ในเชิงยุทธวิธี ผู้ฝึกสอนควรออกแบบสถานการณ์แมตช์จำลอง:\n1. **การตั้งตำแหน่งในสนาม**: แนะนำนักกีฬาเกี่ยวกับ **{p1_desc}** เพื่อรักษาการครอบคลุมคอร์ทสูงและจำกัดมุมการตีของคู่ต่อสู้\n2. **การเปลี่ยนผ่านเกม**: เน้นที่ **{p2_desc}** เพื่อสร้างการตอบสนองอัตโนมัติเมื่อต้องเปลี่ยนจากการรับเป็นรุกภายใต้ความกดดัน\n3. **การปรับเปลี่ยนตามข้อมูล**: บูรณาการข้อมูลจาก **{p3_desc}** ระหว่างแมตช์และช่วงพัก โดยใช้บันทึกการสังเกตเพื่อปรับเปลี่ยนยุทธศาสตร์การเสิร์ฟและการรับ"
    elif category_th == '3_Movement_And_Biomechanics_TH':
        answer = f"เพื่อเพิ่มประสิทธิภาพชีวกลศาสตร์การเคลื่อนไหวสำหรับ **{title_th}** ผู้ฝึกสอนควรจัดการจุดตรวจเชิงจลนศาสตร์:\n1. **การเร่งความเร็วและจังหวะ**: ตั้งเป้าไปที่ **{p1_desc}** โดยการปรับจังหวะสปลิทสเต็ปและการออกแรงผลักฟุตเวิร์คในก้าวแรก\n2. **การชะลอตัวและการลงเท้า**: จัดตำแหน่งข้อต่อเพื่อรองรับ **{p2_desc}** โดยมั่นใจว่าแนวเข่าอยู่เหนือเท้าเพื่อซับแรงกระแทกจากการลงเท้า\n3. **ประสิทธิภาพสายโซ่จลนศาสตร์**: ประสานส่วนต่างๆ ของร่างกายเพื่อจัดการ **{p3_desc}** โดยส่งผ่านแรงจากรยางค์ล่างขึ้นไปยังหัวไม้"
    elif category_th == '4_Physical_And_Sport_Science_TH':
        answer = f"เพื่อสร้างสมรรถภาพทางกายสำหรับ **{title_th}** ผู้ฝึกสอนควรประยุกต์ใช้วิทยาศาสตร์การกีฬา:\n1. **การฝึกระบบพลังงาน**: มุ่งเน้นที่ **{p1_desc}** เพื่อพัฒนาความทนทานแบบไม่ใช้ออกซิเจนซึ่งจำเป็นสำหรับการตีโต้ที่รวดเร็ว\n2. **การจัดการภาระการฝึกซ้อม**: ติดตามตัวชี้วัดความเหนื่อยล้าของนักกีฬาและปรับปริมาณการฝึกตาม **{p2_desc}** โดยเฉพาะในช่วงความเจริญเติบโตอย่างรวดเร็ว (PHV)\n3. **การฟื้นตัวและการป้องกันการบาดเจ็บ**: บูรณาการ **{p3_desc}** (เช่น การเสริมความแข็งแรงของข้อต่อ โภชนาการการคืนน้ำ) เพื่อรักษาสุขภาพของเนื้อเยื่อกล้ามเนื้อ"
    else: # 5_Coaching_Methodology_TH
        answer = f"เพื่อส่งมอบการสอนที่มีประสิทธิภาพสำหรับ **{title_th}** ผู้ฝึกสอนควรใช้กรอบการทำงานวิธีวิทยาการสอน:\n1. **การสื่อสารที่ครอบคลุม**: ปรับการสอนตามสไตล์การเรียนรู้ (VAK) โดยเน้นไปที่ **{p1_desc}** เพื่อการส่งมอบสัญญาณคำสั่งที่ชัดเจน\n2. **การออกแบบบทเรียนที่มีโครงสร้าง**: เขียนแผนการซ้อมที่ระบุ **{p2_desc}** พร้อมการประเมินความเสี่ยงและมาตรการความปลอดภัย\n3. **ความครอบคลุมและการดัดแปลง**: บูรณาการ **{p3_desc}** เพื่อดัดแปลงกฎ ขนาดสนาม หรืออุปกรณ์ให้เหมาะสมกับการฝึกพาราแบดมินตัน"
                 
    qa_pair = f"**คำถาม:** {question}\n\n**คำตอบ:** {answer}"
    
    return purpose, synthesis, app, qa_pair

# Adapt internal links to point to their Thai counterpart nodes
def adapt_links(text):
    def replace_link(match):
        link_name = match.group(1)
        # Check if the link already ends with _TH
        if link_name.endswith('_TH'):
            return f"[[{link_name}]]"
        return f"[[{link_name}_TH]]"
    return re.sub(r'\[\[(.*?)\]\]', replace_link, text)

# Helper to extract drills from Plan tables
def extract_plan_outline(lines):
    drills = []
    for line in lines:
        if line.strip().startswith('|'):
            parts = [p.strip() for p in line.split('|') if p.strip()]
            if len(parts) >= 3 and parts[0] != 'Drill Phase' and not parts[0].startswith(':---'):
                drill_name = parts[0]
                drill_name = re.sub(r'\*\*|\[\[|\]\]', '', drill_name)
                drill_name = re.sub(r'^\d+[\.\)\s]+', '', drill_name)
                if drill_name:
                    drills.append(drill_name.strip())
    return drills

def process_file_th(filepath, dest_dir, category_th):
    filename = os.path.basename(filepath)
    new_filename = filename.replace('.md', '_TH.md')
    dest_path = os.path.join(dest_dir, new_filename)
    
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
        
    # Translate Title
    title_th = translate_phrase(title)
    
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
    description_th = translate_phrase(description)
    
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
                match = re.match(r'^\s*[\d\*\.\-\+]+\s*(.*)', line)
                if match:
                    text = match.group(1).strip()
                    text = re.sub(r'\*\*|\[\[|\]\]', '', text)
                    if text and not text.startswith('---'):
                        outline_points.append(text)
                        
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
    outline_points_th = [translate_phrase(pt) for pt in outline_points]
    
    # Generate enriched sections in Thai
    purpose, synthesis, app, qa_pair = generate_sections_th(filename, title_th, description_th, outline_points_th, category_th)
    
    # Reconstruct original content sections (like tables and metrics) but translated
    filtered_lines = []
    skip = False
    for line in lines:
        if line.startswith('Category:') or line.startswith('[[Level_') or line.startswith('Source Manual:') or line.startswith('[[Training_Plans]]'):
            continue
        if line.startswith('## Core Purpose & Objectives') or line.startswith('## Deep-Dive Synthesis') or line.startswith('## Practical Coaching Application') or line.startswith('## Sample QA Pair') or line.startswith('## Related Topics') or line.startswith('---'):
            skip = True
            continue
        if skip and line.startswith('#') and not line.startswith('##'):
            skip = False
        if skip:
            continue
        if line.strip() == '#llm-deep-backlog':
            continue
        # Translate the line content dynamically
        translated_line = translate_phrase(line)
        # Make sure markdown tables look correct by preserving formatting
        filtered_lines.append(translated_line)
        
    core_content = "\n".join(filtered_lines).strip()
    if core_content.startswith(f"# {title_th}"):
        core_content = core_content[len(f"# {title_th}"):].strip()
        
    # Rebuild Thai version note
    new_content = f"Category: [[{category_th}]]\n\n"
    new_content += f"# {title_th}\n\n"
    if description_th and description_th not in core_content:
        new_content += f"{description_th}\n\n"
    if core_content:
        new_content += f"{core_content}\n\n"
        
    new_content += f"## วัตถุประสงค์หลัก (ทำไปเพื่ออะไร)\n\n{purpose}\n\n"
    new_content += f"## เนื้อหาเจาะลึก\n\n{synthesis}\n\n"
    new_content += f"## การประยุกต์ใช้ในการฝึกซ้อมจริง\n\n{app}\n\n"
    new_content += f"## ตัวอย่างคำถาม-คำตอบ\n\n{qa_pair}\n\n"
    
    # Extract related topics, translate links
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
        new_content += "## หัวข้อที่เกี่ยวข้อง\n\n"
        for r_topic in sorted(list(set(related))):
            new_content += f"* [[{r_topic}_TH]]\n"
        new_content += "\n"
        
    new_content += "#llm-deep-backlog\n"
    
    # Adapt any existing inline links inside the text
    new_content = adapt_links(new_content)
    
    # Write to destination
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    parser = argparse.ArgumentParser(description="Process and translate GeneratedTopics files to Thai")
    parser.add_argument("--category", type=str, required=True, help="Category name to translate")
    args = parser.parse_args()
    
    target_category = args.category
    if target_category not in CATEGORIES:
        print(f"Error: Invalid category '{target_category}'")
        sys.exit(1)
        
    root_dir = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics"
    dest_root = r"C:\Users\usEr\MyLLMDataProject\GeneratedTopics_TH"
    
    category_th = target_category + "_TH"
    dest_dir = os.path.join(dest_root, category_th)
    os.makedirs(dest_dir, exist_ok=True)
    
    src_dir = os.path.join(root_dir, target_category)
    if not os.path.exists(src_dir):
        print(f"Source category directory does not exist: {src_dir}")
        sys.exit(1)
        
    files = [f for f in os.listdir(src_dir) if f.endswith('.md')]
    print(f"Category {target_category}: Found {len(files)} files to translate.")
    
    processed = 0
    for f in files:
        filepath = os.path.join(src_dir, f)
        process_file_th(filepath, dest_dir, category_th)
        processed += 1
        
    print(f"Category {target_category}: Successfully translated and generated {processed} Thai version files in {category_th}.")

if __name__ == '__main__':
    main()
