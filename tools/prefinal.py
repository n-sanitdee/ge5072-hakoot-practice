"""Pre-Final Sets (v2, 27 Nov 2026) — context-rich questions in the final exam's layout.

Mew (26 Nov, late): "make the questions longer and more complex. add more context you find in the book.
remove all vocab+translation questions." + keep Company Profile & Describing Trends "but make sure you draw
it from what is in the department's shared folder".

Layout of one set = the coordinator's student notice (GE5072_รายละเอียดการสอบปลายภาค_1_2026, 70 items):
  1. Grammar, Vocabulary & Expressions — Units 1, 2, 4 (43): Unit 1 14 · Unit 2 14 · Unit 4 15
  2. Company Profile & Describing Trends (17): Company Profile 7 · Describing Trends 10
  3. External Reading (10)

Sources
- Units 1, 2, 4: Business Partner B1 contexts (video/audio scripts 1.1.1, 1.01, 2.1.1, 2.04, 2.05, Ext 2.01, 4.1.1;
  the 1.5 / 2.5 / 4.5 model texts; the 2.2 and 4.2 readings) — new texts written around them, never the book's
  exercise texts.
- Company Profile: ONLY the frames of the coordinator's "GE5072 Company Profile - Introduction to Describing
  Trends 1_2569" (official name + is + a/an + nationality adj + sector; was founded / established / set up by …
  in …; headquarters is situated / located in …; head office is based / located in …; produces / manufactures;
  target markets are in … / target customers are …; revenue / turnover was … in …; main competitors are …).
- Describing Trends: ONLY the coordinator's "GE5072 Describing Trends 1_2569" + project graph pack word set:
  begin/start · stay/stand (at) · go up/rise/increase/improve/grow · go down/fall/drop/decrease/decline ·
  recover · remain stable/steady (+ at) · slight/sharp/dramatic/steady (+ -ly) · at / from…to / to / by / of
  + "in + topic". Never tested: "a growth" vs "growth" (the sheet and the Week 14 deck disagree).

Each passage item = one gap; P() writes one question per gap. Right answer FIRST (the app shuffles).
"""

SETS = [[] for _ in range(4)]
_n = [0]


def P(k, part, les, title, text, gaps):
    _n[0] += 1
    pid = f'p{_n[0]}'
    for i, (opts, ex) in enumerate(gaps, 1):
        assert '{%d}' % i in text, (title, i)
        SETS[k - 1].append({'p': part, 'les': les, 'pid': pid, 'g': i, 'ct': title, 'ctx': text.strip(),
                            'q': f'Choose the best answer for ({i}).', 'a': opts, 'ex': ex})
    assert '{%d}' % (len(gaps) + 1) not in text, title


def Q(k, part, les, q, opts, ex):
    SETS[k - 1].append({'p': part, 'les': les, 'q': q, 'a': opts, 'ex': ex})


# ════════════════════════════════════ SET 1 ════════════════════════════════════
# ── Unit 1 (14) ──
P(1, 'u1', '1.2', "Jenny's careers programme: a new caller", """
Caller: I'm in my final year and I want a job in marketing, but I don't have any work experience.
Jenny: OK. First of all, you {1} apply for an internship this summer. It's the best way to get practical experience.
Caller: But most internships are unpaid.
Jenny: I know. Why don't you {2} for a part-time one, then? You could work in the evenings.
Caller: Good idea. And my online profile?
Jenny: How about {3} a short video about yourself? Recruiters love that. And you ought {4} your profile picture. A photo from a party isn't professional.
Caller: Anything else?
Jenny: Yes. You {5} write "I'm hard-working". Everybody says that. Show it with a real example instead.
""", [
    (['should', 'should to', 'ought', 'could to'],
     '**should + V1** (ไม่มี to) = ให้คำแนะนำ → you **should** apply … • ought ต้องมี to (ought to) • could ไม่มี to'),
    (['look', 'looking', 'to look', 'looked'],
     "**Why don't you + V1 …?** = ทำไมไม่ลอง…ล่ะ → Why don't you **look** for …?"),
    (['making', 'make', 'to make', 'made'],
     '**How about / What about + V-ing** → How about **making** a short video …?'),
    (['to change', 'change', 'changing', 'to changing'],
     '**ought to + V1** → you ought **to change** … (ought ต้องตามด้วย to + กริยาช่อง 1)'),
    (["shouldn't", 'ought', "don't should", 'not should'],
     "บริบทบอกว่า \"ทุกคนก็เขียนแบบนี้\" → ต้องเป็นคำแนะนำเชิง**ห้าม** → **shouldn't + V1** (✗ don't should / not should)"),
])
Q(1, 'u1', '1.1', 'In the 1.1 video, a recruiter says she looks for people who "fit into the team well". '
  'A student writes on her CV: "I played in the university volleyball team for three years." Which skill does this show?',
  ['teamworking skills', 'individual performance', 'a customer-facing job', 'mass production'],
  'จากวิดีโอ 1.1: "if you played in a team – you\'re a **team player**" → แสดง **teamworking skills** (ทักษะการทำงานเป็นทีม)')
Q(1, 'u1', '1.1', '"Employers are not just hiring a package of skills; they\'re hiring a person: ___, flexibility, '
  'enthusiasm – these things matter a lot." (Video 1.1)',
  ['honesty', 'honest', 'honestly', 'dishonest'],
  'อยู่ในรายการ**คำนาม** (flexibility, enthusiasm) จึงต้องเป็นคำนามเหมือนกัน → **honesty** (ความซื่อสัตย์)')
Q(1, 'u1', '1.1', 'Sara has worked at the same company for six years. She is ___ to learn new skills because she wants '
  'to become a team leader, and her manager can always rely ___ her.',
  ['motivated … on', 'motivating … on', 'motivated … in', 'motivation … for'],
  '**be motivated to + V1** = มีแรงจูงใจที่จะ… • **rely on someone** = ไว้ใจ/พึ่งพาใคร → motivated … **on**')
P(1, 'u1', '1.5', 'An email to the whole Sales Department', """
To: All staff, Sales Department
Subject: New Sales Manager

{1}
I would like to introduce myself. I {2} as the new Sales Manager, and I started work in the Bangkok office on Monday. My previous job {3} as Area Manager for a food company in Chiang Mai.
Please feel {4} to contact me by email or phone if you have any questions. I am {5} looking forward to working with you all.
Kind regards,
Somchai Rattanakul
""", [
    (['Dear colleagues,', 'Hey guys,', 'Hi everyone!!', 'Yo team,'],
     'อีเมลถึง**ทั้งแผนก** และส่วนอื่นของอีเมลเป็นภาษาทางการ (I would like to …, Kind regards) → ขึ้นต้นแบบทางการ **Dear colleagues,**'),
    (['have been appointed', 'have appointed', 'am appointing', 'appointed been'],
     '**I have been appointed as …** = ฉันได้รับแต่งตั้งเป็น… (passive: have been + V3)'),
    (['was', 'is', 'were', 'has been'],
     'previous job = งานในอดีตที่จบไปแล้ว + job เอกพจน์ → My previous job **was** as …'),
    (['free', 'freely', 'freedom', 'to free'],
     '**Please feel free to contact me** = ติดต่อได้ตามสะดวก (feel + คำคุณศัพท์ free)'),
    (['really', 'a lot', 'much', 'a bit'],
     '**really** วางหน้ากริยาเพื่อเน้น → I am **really** looking forward … • a lot วางหลังกริยาและกรรม • a bit ทำให้ความหมายอ่อนลง ไม่เหมาะกับการตั้งตารอ'),
])
Q(1, 'u1', '1.5', 'Which sentence belongs in a LESS formal email to colleagues you already know well?',
  ['Perhaps we can meet up over lunch on Friday.', 'I would like to introduce myself as the new manager.',
   'Please do not hesitate to contact us.', 'Yours faithfully,'],
  '**Perhaps we can meet up over lunch** = ชวนแบบไม่ทางการ • ข้ออื่นเป็นภาษาทางการ (would like to, do not hesitate, Yours faithfully)')

# ── Unit 2 (14) ──
P(1, 'u2', '2.2', "Mark's power cut (from the 2.2 reading)", """
Last winter, Mark Nowicki and his family {1} TV one evening when suddenly all the lights went out. It {2} heavily outside, and the storm had cut the power lines. While they {3} in the dark, Mark decided to buy solar panels. Two months later, an engineer {4} the panels on the roof. Now the family's electricity bill is much lower, and they have backup power when there is a power {5}.
""", [
    (['were watching', 'watched', 'are watching', 'was watching'],
     'การกระทำที่**กำลังทำอยู่แล้วถูกขัด** (lights went out) → Past Continuous • Mark and his family = พหูพจน์ → **were watching**'),
    (['was snowing', 'snows', 'is snowing', 'were snowing'],
     '**ฉากหลัง/สภาพอากาศ**ในอดีต → Past Continuous • it → **was snowing**'),
    (['were sitting', 'are sitting', 'was sitting', 'sitting'],
     '**while + Past Continuous** (การกระทำที่ยาวกว่า) • they → **were sitting**'),
    (['installed', 'has installed', 'installs', 'install'],
     'Two months later = เหตุการณ์สั้นที่จบแล้วในอดีต → Past Simple **installed** (✗ has installed ใช้กับเวลาที่จบแล้วไม่ได้)'),
    (['cut', 'bill', 'panel', 'fuel'],
     '**power cut** = ไฟดับ (คำนามประสม)'),
])
Q(1, 'u2', '2.1', "\"Japan's service sector, which includes finance, retail and transportation, ___ about three-quarters "
  "of the country's total economic output.\" (Video 2.1)",
  ['accounts for', 'accounts to', 'is accounted', 'account for'],
  '**account for + สัดส่วน** = คิดเป็น… • ประธาน sector เป็นเอกพจน์ → **accounts for** (กลุ่มคำ which … คั่นกลางไม่เปลี่ยนประธาน)')
Q(1, 'u2', '2.1', 'Sony, Nintendo and Panasonic belong to the consumer electronics ___, which is part of the ___ '
  'sector because these companies make products in factories.',
  ['industry … secondary', 'industry … primary', 'industry … tertiary', 'crop … secondary'],
  '**industry** = กลุ่มบริษัทที่ทำธุรกิจแบบเดียวกัน • ผลิตสินค้าในโรงงาน = **secondary sector** (ภาคทุติยภูมิ)')
Q(1, 'u2', '2.1', 'In the 1970s, Japanese cars were cheap, reliable and popular, so domestic car makers in the USA '
  'and Europe lost market share ___ their Japanese rivals.',
  ['to', 'from', 'with', 'at'],
  '**lose market share to a rival** = เสียส่วนแบ่งตลาดให้คู่แข่ง (จากวิดีโอ 2.1)')
P(1, 'u2', '2.5', "Alice's email after the Indonesia meeting", """
Hi Matthew,
Thanks for coming to the meeting with Stanley yesterday. As you know, we {1} open a factory in Indonesia next year, so here are the action points:
• {2} the licence from the Investment Board — Stanley, by next Friday
• book flights and accommodation — Matthew, {3} tomorrow
• open a bank account in Jakarta — Alice, next month
I think the project {4} take a lot of time, but it will be worth it. If you need help with the bookings, just ask — {5} help you.
Best wishes,
Alice
""", [
    (['are going to', 'will to', 'going', 'are will'],
     'As you know … next year = **แผนที่ตัดสินใจไว้แล้ว** → **are going to** + V1'),
    (['get', 'getting', 'to get', 'the getting of'],
     'action point ทุกข้อ**ขึ้นต้นด้วยกริยารูปเดียวกัน** (book, open) → **get**'),
    (['by', 'until', 'on', 'at'],
     'บอกกำหนดเวลา (deadline) → **by** tomorrow = ภายในพรุ่งนี้'),
    (['will', 'is going', 'going to', 'wills'],
     'I think … = **ความคิดเห็น**เกี่ยวกับอนาคต → **will** + V1'),
    (["I'll", 'I going to', "I'm will", 'I will to'],
     '**ข้อเสนอ (offer)** ที่ตัดสินใจตอนพูด → **I\'ll** help you'),
])

# ── Unit 4 (15) ──
P(1, 'u4', '4.1', 'Volvo and Starbucks in China (Video 4.1)', """
Global brands often have to {1} their products to meet local preferences. In China, Volvo launched a high-end sedan without a front passenger seat, because many wealthy buyers have a chauffeur. Starbucks made a smaller change: it decided to {2} in selling premium teas, because China is the home of tea. Both companies first analysed their {3} territories and then adjusted their marketing {4}. Starbucks believes that coffee {5} in China will continue to grow.
""", [
    (['adapt', 'adaptable', 'adaptation', 'adaptability'],
     'have to + **กริยา** → **adapt** (ปรับ) products to meet local preferences'),
    (['specialise', 'special', 'specialist', 'specialisation'],
     'decided to + **กริยา** → **specialise in + V-ing** = เชี่ยวชาญด้าน…'),
    (['target', 'aim', 'goal', 'object'],
     'collocation จากวิดีโอ: **analyse your target territories** = วิเคราะห์ตลาด/ประเทศเป้าหมาย'),
    (['strategy', 'strategic', 'strategically', 'strategise'],
     'their marketing + **คำนาม** → **marketing strategy** = กลยุทธ์การตลาด'),
    (['consumption', 'consume', 'consumable', 'consumer'],
     'coffee ___ will continue to grow → ต้องเป็น**คำนาม**ที่หมายถึงปริมาณการดื่ม → **consumption** (การบริโภค) • consumer = ผู้บริโภค ไม่ใช่สิ่งที่ "grow" ในความหมายนี้'),
])
P(1, 'u4', '4.2', "Einar's jewellery shop (from the 4.2 reading)", """
Einar Parker works on a production line during the day, but in his spare time he makes jewellery. His online shop {1} on Etsy three years ago. Etsy is a website that {2} twelve years ago to sell homemade goods. Each ring {3} by hand, and orders {4} within two days. Sites like this {5} by millions of people, and they help many "sofapreneurs" earn extra money.
""", [
    (['was set up', 'set up', 'was setting up', 'were set up'],
     'ร้านถูกเปิด (ไม่ได้เปิดตัวเอง) + three years ago + เอกพจน์ → passive **was set up**'),
    (['was started', 'is started', 'were started', 'was starting'],
     'เว็บไซต์ถูกก่อตั้ง + twelve years ago + เอกพจน์ → **was started**'),
    (['is made', 'are made', 'makes', 'is making'],
     'each ring (เอกพจน์) ถูกทำ → **is made** by hand'),
    (['are dispatched', 'dispatch', 'is dispatched', 'are dispatching'],
     'orders (พหูพจน์) ถูกส่งออก → **are dispatched**'),
    (['are used', 'use', 'is used', 'are using'],
     'sites (พหูพจน์) ถูกใช้ + by millions of people → **are used**'),
])
P(1, 'u4', '4.5', 'A letter to Ms Liang', """
Dear Ms Liang,
ORDER CONFIRMATION
Thank you for your order (number 5521) for 200 office chairs, which we received this morning. We are writing {1} confirm the details.
As agreed when we talked {2} your order last week, we will deliver the goods to your head office in Shanghai on 12 May. Payment terms are 30 days after the date of the invoice, and we enclose full terms and conditions for your records.
We thank you {3} your business and look forward to {4} you again. If you have any queries, please do not hesitate to contact us.
Yours {5},
Anna Lee
""", [
    (['to', 'for', 'so', 'by'],
     'We are writing **to + V1** (บอกจุดประสงค์) → writing **to** confirm'),
    (['about', 'to', 'for', 'at'],
     '**talk about + เรื่อง** = คุยเรื่อง… (talk to + คน)'),
    (['for', 'to', 'with', 'on'],
     '**thank someone for something** → We thank you **for** your business (✗ thank to)'),
    (['supplying', 'supply', 'supplied', 'be supply'],
     '**look forward to + V-ing** (to เป็นบุพบท) → look forward to **supplying** you'),
    (['sincerely', 'faithfully', 'regards', 'kindly'],
     'รู้ชื่อผู้รับ (**Dear Ms Liang**) → **Yours sincerely,** • Dear Sir/Madam → Yours faithfully,'),
])

# ── Company Profile (7) — coordinator's frames ──
P(1, 'cp', 'CP', 'Company profile: Sunrise Foods', """
Sunrise Foods {1} a Thai snack manufacturer. The company {2} by two sisters, Nida and Ploy Wong, in 2015. Its head office {3} in Chiang Mai, Thailand. It {4} rice crackers, dried fruit and coconut chips. Its target customers {5} teenagers and office workers aged 15 to 35. The company's turnover {6} 120 million baht in 2025. Its main {7} are Crispy King and Snack Town.
""", [
    (['is', 'are', 'was founded', 'has'],
     'โครงสร้างในชีท: **ชื่อบริษัท + is + a/an + สัญชาติ + ประเภทธุรกิจ** → Sunrise Foods **is** a Thai snack manufacturer.'),
    (['was founded', 'founded', 'was found', 'is founding'],
     '**The company / It + was founded / established / set up + by + ผู้ก่อตั้ง + in + ปี** (passive) • found = ก่อตั้ง (founded) ≠ find (found)'),
    (['is located', 'locates', 'located', 'is locating'],
     '**Its head office + is based / located + in + เมือง, ประเทศ**'),
    (['produces', 'produce', 'is produced', 'producing'],
     '**It + produces / manufactures + สินค้า** • it → กริยาเติม -s'),
    (['are', 'is', 'be', 'being'],
     '**Its target customers + are + กลุ่มลูกค้า** (customers พหูพจน์)'),
    (['was', 'were', 'is been', 'has'],
     "**The company's revenue / turnover + was + จำนวน + in + ปี** (turnover เอกพจน์ + ปีที่ผ่านมา)"),
    (['competitors', 'competitor', 'competition', 'compete'],
     "**Its main competitors + are + บริษัท 2 แห่งขึ้นไป** → พหูพจน์ competitors"),
])

# ── Describing Trends (10) — coordinator's sheet ──
P(1, 'dt', 'DT', 'Sunrise coconut chips — monthly sales (thousand packs), Jan–Jun 2025', """
DATA: Jan 20 · Feb 20 · Mar 26 · Apr 18 · May 19 · Jun 19

In January, sales stood {1} 20,000 packs, and they remained {2} in February. In March, they rose {3} from 20,000 {4} 26,000 packs after a TV advert. However, there was a {5} fall {6} sales in April, when they dropped {7} 18,000 packs. In May, sales recovered {8}, rising {9} 1,000 packs, and they {10} stable at 19,000 packs in June.
""", [
    (['at', 'by', 'of', 'in'],
     '**stood / stayed / began / started + at + ตัวเลข** = อยู่ที่ระดับ… (at = จุดที่แน่นอน)'),
    (['steady', 'steadily', 'steadiness', 'steadied'],
     'ชีทเน้น: **remain + คำคุณศัพท์ steady / stable** ไม่ใช่ adverb → remained **steady**'),
    (['sharply', 'sharp', 'sharpness', 'sharpen'],
     'ขยายกริยา rose → **adverb** → rose **sharply** (sharp = adj ใช้กับคำนาม)'),
    (['to', 'by', 'of', 'at'],
     '**from + จุดเริ่ม … to + จุดที่ไปถึง** → from 20,000 **to** 26,000'),
    (['dramatic', 'dramatically', 'drama', 'dramatise'],
     'a + **adjective** + noun → a **dramatic** fall (26,000 → 18,000 ลดลงมากและเร็ว)'),
    (['in', 'of', 'by', 'at'],
     '**a fall + in + หัวข้อ (sales)** → a dramatic fall **in** sales'),
    (['to', 'by', 'from', 'at'],
     '**to + จุดที่ไปถึง** → dropped **to** 18,000 packs'),
    (['slightly', 'slight', 'slighter', 'slightness'],
     'เพิ่มขึ้นแค่ 1,000 = เล็กน้อย • ขยายกริยา recovered → adverb **slightly**'),
    (['by', 'to', 'of', 'at'],
     '**กริยา + by + ส่วนต่าง** → rising **by** 1,000 packs (18,000 → 19,000)'),
    (['remained', 'remains', 'was remained', 'remaining'],
     'in June (อดีต) → **remained** stable at … • remain ไม่ใช้ passive'),
])

# ════════════════════════════════════ SET 2 ════════════════════════════════════
# ── Unit 1 (14) ──
P(2, 'u1', '1.1', 'A recruiter at a careers fair', """
"Many students think their grades are everything, but a large part of university life is based on individual {1}. In business, things are quite different. Most recruiters look for people who work {2} in a team and who can adapt {3} new tasks and roles. If you played in a sports team, you know how to set {4}. And remember: employers hire a person, not just a skillset, so show your {5} and enthusiasm."
""", [
    (['performance', 'perform', 'performer', 'performing'],
     'individual + **คำนาม** → **individual performance** = ผลงานส่วนบุคคล (จากวิดีโอ 1.1)'),
    (['well', 'good', 'best', 'goodly'],
     'ขยายกริยา work → ใช้ **adverb well** → **work well in a team** (✗ work good)'),
    (['to', 'for', 'with', 'at'],
     '**adapt to new tasks and roles** = ปรับตัวเข้ากับงานและบทบาทใหม่'),
    (['goals', 'the box', 'a reputation', 'market share'],
     '**set goals** = ตั้งเป้าหมาย (วิดีโอ 1.1: "you set goals, you can achieve")'),
    (['honesty', 'honest', 'honestly', 'dishonestly'],
     'your + **คำนาม** และคู่กับ enthusiasm (คำนาม) → **honesty**'),
])
Q(2, 'u1', '1.2', 'Caller: "I\'m good at problem solving, but my profile doesn\'t show it."\n'
  'Jenny: "___ telling me about a time when you dealt with a problem?"',
  ['How about', "Why don't you", 'You should', 'You ought to'],
  'ช่องว่างตามด้วย **V-ing (telling)** → ใช้ **How about / What about** • Why don\'t you, should, ought to ตามด้วย V1')
Q(2, 'u1', '1.2', 'Friend: "I really don\'t earn enough in my present job."\nWhich reply gives advice correctly?',
  ['You ought to look for a better-paid job.', 'You ought look for a better-paid job.',
   'You ought to looking for a better-paid job.', 'You ought to looked for a better-paid job.'],
  '**ought to + V1** → You ought **to look** for …')
Q(2, 'u1', '1.1', 'Lord Sugar says in the 1.1 video: "It\'s their own ___ that\'s gonna get them a job."',
  ['determination', 'determine', 'determined', 'determinedly'],
  'their own + **คำนาม** → **determination** (ความมุ่งมั่น)')
P(2, 'u1', '1.5', "Gabriela's email, written again (1.5)", """
Dear colleagues,
I would like to introduce myself. I have been {1} as the new HR Manager, and I started work today. Before I joined, I was working in a {2} similar position at a hotel group. Please {3} free to contact me if you have any questions. I {4} look forward to meeting you all in person.
{5}
Gabriela de Souza
""", [
    (['appointed', 'appoint', 'appointing', 'appointment'],
     'have been + **V3** (passive) → I have been **appointed** as …'),
    (['very', 'much', 'a lot', 'a bit of'],
     'หน้า**คำคุณศัพท์ธรรมดา** (similar) ใช้ **very / really** → a **very** similar position • much / a lot ใช้หน้าคำเปรียบเทียบ'),
    (['feel', 'feeling', 'to feel', 'felt'],
     '**Please feel free to + V1** (Please + กริยาช่อง 1)'),
    (['very much', 'very', 'a lot of', 'much more'],
     '**I very much look forward to …** (very much วางหน้าหรือหลังกริยาได้) • ✗ I very look forward'),
    (['Kind regards,', 'Bye for now,', 'See ya,', 'Cheers mate,'],
     'อีเมลทั้งฉบับเป็น**ภาษาทางการ** (Dear colleagues, I would like to …) → ปิดแบบทางการ **Kind regards,**'),
])
Q(2, 'u1', '1.5', '"Dear colleagues, I would like to introduce myself. I have been appointed as the new IT Manager. '
  'Please feel free to contact me. I look forward to meeting you. Kind regards, Tom"\n'
  'Which of the seven parts is missing?',
  ['Previous job', 'Greeting', 'Invitation', 'Sign off'],
  '7 ส่วน: Greeting → Opening → New job → **Previous job** → Invitation → Closing → Sign off • อีเมลนี้ไม่บอกงานเดิม')

# ── Unit 2 (14) ──
P(2, 'u2', '2.1', "Japan's economy (Video 2.1)", """
Japan's industrialised, free-market economy is the third {1} in the world. Its service sector, which includes finance, retail and tourism, accounts {2} three-quarters of total output, and many Japanese banks are global {3}. However, Japan's manufacturing industries have made the biggest global {4}. Japanese car makers enjoy a reputation for producing reliable vehicles, and in 2010 Nissan {5} the Leaf, the world's first all-electric car for the mass market.
""", [
    (['largest', 'large', 'largely', 'most large'],
     'the third + **ขั้นสูงสุด** → **the third largest** in the world = ใหญ่เป็นอันดับสามของโลก'),
    (['for', 'to', 'of', 'with'],
     '**account for** = คิดเป็น (สัดส่วน)'),
    (['players', 'plants', 'crops', 'sectors'],
     '**be a global player** = บริษัทที่มีบทบาทในตลาดโลก'),
    (['impact', 'important', 'impactful', 'impacting'],
     '**make a global impact** = สร้างผลกระทบระดับโลก (the biggest + คำนาม)'),
    (['released', 'relieved', 'realised', 'reduced'],
     '**release a product** = ออกวางจำหน่ายสินค้า → Nissan **released** the Leaf'),
])
Q(2, 'u2', '2.1', 'A company in Rayong buys crude oil and turns it into plastic parts for cars. Which sector is it in?',
  ['the secondary sector', 'the primary sector', 'the tertiary sector', 'the service sector'],
  'นำวัตถุดิบ (น้ำมันดิบ) มา**ผลิตเป็นสินค้า**ในโรงงาน → **secondary sector** • การขุดน้ำมันเองจึงจะเป็น primary')
P(2, 'u2', '2.2', 'Big oil goes green (from the 2.2 reading)', """
Some years ago, Total, one of the world's largest oil and gas companies, {1} two-thirds of the solar company SunPower. At the time, it was the biggest investment in renewable energy by any large oil company. Today, stricter regulations on greenhouse gas {2} and competition from cheaper wind and solar power mean that oil companies {3} a critical choice. They can diversify {4} renewable energies, or they can stick {5} oil and gas.
""", [
    (['bought', 'was buying', 'buys', 'has buying'],
     'เหตุการณ์ที่**จบแล้ว**ครั้งเดียวในอดีต (Some years ago) → Past Simple **bought**'),
    (['emissions', 'emits', 'emitted', 'emitting'],
     'greenhouse gas + **คำนาม** → **greenhouse gas emissions** = การปล่อยก๊าซเรือนกระจก'),
    (['face', 'faces', 'facing', 'is facing'],
     'oil companies (พหูพจน์) + ปัจจุบัน → **face** a critical choice = เผชิญการตัดสินใจครั้งสำคัญ'),
    (['into', 'to', 'on', 'with'],
     '**diversify into** = ขยายกิจการไปสู่…'),
    (['to', 'on', 'in', 'for'],
     '**stick to** = ยึดอยู่กับ… ไม่เปลี่ยน'),
])
Q(2, 'u2', '2.2', 'While the engineers ___ the solar panels, it started to rain, so they stopped work for an hour.',
  ['were installing', 'installed', 'are installing', 'was installing'],
  '**while + Past Continuous** (การกระทำยาวที่ถูกขัด) • engineers พหูพจน์ → **were installing**')
Q(2, 'u2', '2.5', 'Kenzo: "Can someone email all the staff about Friday\'s meeting?"\nSusan: "Sure. ___ it straight after this meeting."',
  ["I'll do", "I'm doing to", 'I will to do', 'I going to do'],
  'ตัดสินใจ/เสนอตัว**ตอนพูด** → **will** → I\'ll do it (ฟังเสียง 2.05: "I\'ll email them straight after this meeting")')
Q(2, 'u2', '2.5', 'According to the rules in 2.5, every action point should include …',
  ['a verb, the person responsible and a deadline', 'a greeting, a question and a signature',
   'the history of the company', 'a list of everyone at the meeting'],
  'กฎ action point: **ขึ้นต้นด้วยกริยา + ชื่อผู้รับผิดชอบ + กำหนดเวลา** เช่น "book flights — Matthew, by tomorrow"')

# ── Unit 4 (15) ──
P(2, 'u4', '4.1', 'One size does not fit all', """
When a global fast-food chain enters a new market, one size does not always fit all. In Thailand, for example, its menus are {1} to local tastes: you can order rice dishes and spicy chicken. This kind of product {2} helps the brand appeal to local customers. Some drinks are even {3}: customers choose their own toppings. The company also studies the {4} habits of young people, because they are its most important {5}.
""", [
    (['adapted', 'adapt', 'adaptable', 'adaptation'],
     'are + **V3** (passive) → menus are **adapted** to local tastes'),
    (['customisation', 'customise', 'customisable', 'customer'],
     'product + **คำนาม** → **product customisation** = การปรับแต่งสินค้าให้เหมาะกับตลาด'),
    (['customisable', 'customise', 'customisation', 'customising'],
     'are + **คำคุณศัพท์** → **customisable** = ปรับแต่งได้ (ลูกค้าเลือก topping เอง)'),
    (['consumption', 'consume', 'consumable', 'consumed'],
     'the + ___ + habits → ใช้**คำนาม**ขยาย → **consumption habits** = พฤติกรรมการบริโภค'),
    (['consumers', 'consumes', 'consumption', 'consumable'],
     'its most important + **คำนามที่เป็นคน** → **consumers** (ผู้บริโภค)'),
])
P(2, 'u4', '4.2', 'Online marketplaces (4.2)', """
Alibaba {1} in Hangzhou, China, in 1999. Today it {2} by hundreds of millions of people, and thousands of small businesses sell their products through it. eBay, another early online marketplace, {3} PayPal in 2002. On these sites, many products {4} worldwide, and a commission {5} on every sale.
""", [
    (['was founded', 'founded', 'is founded', 'was founding'],
     'Alibaba ถูกก่อตั้ง + 1999 → passive อดีต **was founded**'),
    (['is used', 'uses', 'is using', 'are used'],
     'Alibaba (เอกพจน์) ถูกใช้ + Today → **is used** by …'),
    (['bought', 'was bought', 'is bought', 'buys'],
     '**eBay เป็นผู้ซื้อ** (ทำเอง) → active **bought** • ดูประธานก่อน: ทำเอง = active'),
    (['are shipped', 'ship', 'is shipped', 'are shipping'],
     'products (พหูพจน์) ถูกส่ง → **are shipped**'),
    (['is charged', 'charges', 'are charged', 'is charging'],
     'a commission (เอกพจน์) ถูกเรียกเก็บ → **is charged**'),
])
P(2, 'u4', '4.5', "Mr Chahal's late delivery (4.5)", """
Mr Chahal is the buyer for a factory in Mumbai. Last week he complained {1} the supplier about a late delivery. The supplier apologised and agreed {2} him that the delay was not acceptable. Now Mr Chahal is waiting {3} the next shipment, which should arrive {4} the factory on Monday. He says he will think {5} changing suppliers if the goods are late again.
""", [
    (['to', 'at', 'with', 'for'],
     '**complain to + คน** (ร้องเรียนต่อใคร) • complain about + เรื่อง'),
    (['with', 'to', 'at', 'for'],
     '**agree with + คน** = เห็นด้วยกับ…'),
    (['for', 'to', 'at', 'about'],
     '**wait for** = รอ'),
    (['at', 'to', 'in', 'for'],
     '**arrive at + สถานที่** (the factory, the warehouse) • ✗ arrive to'),
    (['about', 'at', 'for', 'to'],
     '**think about + V-ing** = พิจารณา…'),
])

# ── Company Profile (7) ──
P(2, 'cp', 'CP', 'Company profile: Green Bowl Co., Ltd.', """
Green Bowl Co., Ltd. is {1} Thai healthy-food restaurant chain. It {2} in 2019 by Krit Somboon. Its headquarters {3} situated in Bangkok, Thailand. The company {4} salads, rice bowls and fresh juice. Its target {5} are in Thailand and Vietnam. Its revenue {6} 85 million baht in 2025. The company's main competitors {7} Salad Corner and Fresh Leaf.
""", [
    (['a', 'an', 'the', '— (no word)'],
     '**ชื่อบริษัท + is + a/an + สัญชาติ + ประเภทธุรกิจ** • Thai ออกเสียงพยัญชนะ → **a** Thai …'),
    (['was set up', 'set up', 'was setting up', 'is set up'],
     '**It + was founded / established / set up + in + ปี + by + ผู้ก่อตั้ง** (passive อดีต)'),
    (['is', 'be', 'being', 'to be'],
     '**Its headquarters + is / are + situated / located + in + เมือง, ประเทศ** (ชีทใช้ได้ทั้ง is และ are)'),
    (['sells', 'sell', 'is sold', 'selling'],
     'The company = it → กริยาเติม -s → **sells**'),
    (['markets', "market's", 'marketing', 'marketed'],
     "**Its target markets + are + in + ประเทศ/ภูมิภาค** (พหูพจน์ markets)"),
    (['was', 'were', 'has', 'is being'],
     '**Its revenue / turnover + was + จำนวน + in + ปี**'),
    (['are', 'is', 'be', 'being'],
     "**The company's main competitors + are + บริษัท 2 แห่งขึ้นไป**"),
])

# ── Describing Trends (10) ──
P(2, 'dt', 'DT', 'Siam Fruit Co. — exports (million baht), 2021–2025', """
DATA: 2021 40 · 2022 40 · 2023 55 · 2024 30 · 2025 32

Exports began {1} 40 million baht in 2021 and stayed at the same level in 2022. In 2023, they went up {2} from 40 to 55 million baht. However, there was a {3} decrease {4} 25 million baht in 2024, when exports fell {5} 30 million baht. In 2025, exports recovered {6}.
""", [
    (['at', 'by', 'of', 'to'],
     '**began / started / stood / stayed + at + ตัวเลข** = จุดเริ่มต้น/ระดับที่แน่นอน'),
    (['dramatically', 'dramatic', 'drama', 'dramatical'],
     'ขยายกริยา went up → **adverb** • 40 → 55 = เพิ่มมากและเร็ว → **dramatically**'),
    (['sharp', 'sharply', 'sharpen', 'sharpness'],
     'a + **adjective** + noun → a **sharp** decrease (55 → 30)'),
    (['of', 'in', 'by', 'at'],
     '**คำนาม + of + ส่วนต่าง** → a decrease **of** 25 million baht (กริยาใช้ by, คำนามใช้ of)'),
    (['to', 'by', 'of', 'at'],
     '**to + จุดที่ไปถึง** → fell **to** 30 million baht'),
    (['slightly', 'slight', 'slightness', 'slighted'],
     'ขยายกริยา recovered • 30 → 32 = เพิ่มเล็กน้อย → **slightly**'),
])
Q(2, 'dt', 'DT', '"Production increased dramatically to 5 million units in September."\nWhich sentence has the same meaning?',
  ['There was a dramatic increase in production to 5 million units in September.',
   'There was a dramatically increase in production to 5 million units in September.',
   'There was a dramatic increased in production to 5 million units in September.',
   'There was dramatic increase of production to 5 million units in September.'],
  'แพทเทิร์นในชีท: **There was + a + adjective + noun + in + หัวข้อ + to/of/from…to + ตัวเลข** → a **dramatic increase in** production')
Q(2, 'dt', 'DT', '"We had a sharp drop in profit from 35 million to 20 million dollars in 2024."\n= "Profit ___ from 35 million to 20 million dollars in 2024."',
  ['dropped sharply', 'dropped sharp', 'sharp dropped', 'was dropped sharply'],
  'noun → verb: a drop → **dropped** • adjective → adverb: sharp → **sharply** • ไม่ใช้ passive')
Q(2, 'dt', 'DT', 'Production remained ___ at 100,000 units between 2023 and 2024.',
  ['stable', 'stably', 'stability', 'stabilise'],
  'ชีท (Note): **remain + คำคุณศัพท์ stable / steady** ไม่ใช่ adverb → remained **stable** at …')
Q(2, 'dt', 'DT', 'Our share price went up ___ 0.5% in 2025.',
  ['by', 'of', 'at', 'in'],
  '**กริยา + by + ส่วนต่าง** → went up **by** 0.5%')

# (Set 1, Unit 2 — 14th item)
Q(1, 'u2', '2.2', 'Which sentence is correct?',
  ['I knew the answer when the manager asked me.', 'I was knowing the answer when the manager asked me.',
   'I was know the answer when the manager asked me.', 'I knowing the answer when the manager asked me.'],
  '**know** เป็น state verb (กริยาแสดงสภาวะ) ไม่ใช้รูป continuous → Past Simple **knew**')

# ════════════════════════════════════ SET 3 ════════════════════════════════════
# ── Unit 1 (14) ──
P(3, 'u1', '1.2', 'Advice for a nervous friend (1.2)', """
Mali: I get so nervous before interviews. I can't sleep the night before.
Ben: Why not {1} some practice interviews with a friend? It really helps.
Mali: Good idea. And my new job starts in three months. What should I do until then?
Ben: You {2} go on a short course. How about {3} an online course in Excel? And you ought {4} in touch with your new manager, so you can ask questions.
Mali: Should I post about the new job on social media?
Ben: No, you {5} put anything about your new company online before you start.
""", [
    (['do', 'doing', 'to do', 'did'],
     "**Why not + V1 …?** = ลอง…ดูสิ → Why not **do** … (แต่ Why not **try + V-ing**)"),
    (['could', 'ought', 'could to', 'can to'],
     '**could + V1** = เสนอแนะแบบสุภาพ → You **could** go on a course (✗ ought go — ought ต้องมี to)'),
    (['taking', 'take', 'to take', 'took'],
     '**How about + V-ing** → How about **taking** an online course?'),
    (['to keep', 'keep', 'keeping', 'to keeping'],
     '**ought to + V1** → ought **to keep** in touch with …'),
    (["shouldn't", 'should not to', "don't should", 'not should'],
     "คำตอบ No → คำแนะนำเชิงห้าม **shouldn't + V1** (✗ should not to / don't should)"),
])
Q(3, 'u1', '1.1', 'Interviewer: "The system crashed an hour before the deadline. What did you do? '
  'Give me an example of how you were resourceful ___ pressure."',
  ['under', 'in', 'on', 'with'],
  '**be resourceful under pressure** = มีไหวพริบหาทางออกได้แม้อยู่ภายใต้ความกดดัน')
Q(3, 'u1', '1.1', "A pilot's schedule changes every week, so the job needs a lot of ___. Pilots must also be ___ "
  "because passengers' lives depend on them.",
  ['flexibility … dependable', 'flexible … dependability', 'flexibility … dependability', 'flexible … dependable'],
  'a lot of + **คำนาม** → **flexibility** • must be + **คำคุณศัพท์** → **dependable** (ไว้ใจได้)')
Q(3, 'u1', '1.1', 'Nok always shares ideas, listens to others and helps her colleagues. Her manager says she is a real team ___.',
  ['player', 'playing', 'play', 'played'],
  '**team player** = คนที่ทำงานเป็นทีมได้ดี (คำนามประสม)')
P(3, 'u1', '1.5', "Alexis's email to his new team (1.5, less formal)", """
Hi everyone,
I'm Alexis and I want to say hello. I've just {1} the job of IT Supervisor, so I'll be looking after all your computers! I was a technician at a bank {2}. I'm {3} excited to be working here, and I'm sure we'll get on really well.
{4} we can meet up over lunch this week?
{5},
Alexis
""", [
    (['got', 'get', 'getting', 'gets'],
     "**I've just got the job of …** (have + V3) = เพิ่งได้งาน… (ภาษาไม่ทางการ)"),
    (['before', 'ago', 'after', 'since'],
     '**I was a … before.** = ก่อนหน้านี้ฉันเป็น… • ago ต้องมีช่วงเวลาข้างหน้า เช่น two years ago'),
    (['really', 'a lot', 'much', 'a bit of'],
     'หน้า**คำคุณศัพท์** excited → **really / very** • a lot วางหลังกริยา'),
    (['Perhaps', 'Please feel free', 'Kindly', 'Dear'],
     '**Perhaps we can meet up over lunch …?** = ชวนแบบไม่ทางการ'),
    (['Bye for now', 'Yours faithfully', 'Yours sincerely', 'Dear colleagues'],
     'อีเมลไม่ทางการ (Hi everyone, I\'m …) → ปิดด้วย **Bye for now / Best wishes** ให้ register ตรงกันทั้งฉบับ'),
])
Q(3, 'u1', '1.5', 'The new office is ___ further from my home than my old one, but I don\'t mind.',
  ['a bit', 'very', 'quite', 'really'],
  'หน้า**คำเปรียบเทียบ** (further) ใช้ **a bit / a little / much / a lot** → a bit further')

# ── Unit 2 (14) ──
P(3, 'u2', '2.5', "Nikolay's email after the team meeting (Audio Ext 2.01)", """
Subject: Action points from today's team meeting
Hi all,
We met this morning to discuss last week's problems with deliveries and staff. {1} the action points:
• look for alternative suppliers — Aiko, by next week's meeting
• {2} for two new factory staff — Genna, this week
• send Aiko a list of the equipment we need — Philip, {3} tomorrow
• write a report on the delivery problems — Sam, by Thursday
We {4} have a follow-up meeting next Monday at 10:00. I think the new suppliers {5} solve most of our delivery problems.
Nikolay
""", [
    (['Here are', 'There is', 'Here is', 'This are'],
     'action points เป็นพหูพจน์ → **Here are** the action points'),
    (['advertise', 'advertising', 'to advertise', 'advertised'],
     'action point ขึ้นต้นด้วย**กริยารูปเดียวกัน** (look, send, write) → **advertise**'),
    (['by', 'until', 'at', 'on'],
     'กำหนดเวลา → **by** tomorrow = ภายในพรุ่งนี้'),
    (['are going to', 'will to', 'going', 'are will'],
     'การประชุมที่**นัดไว้แล้ว** (next Monday at 10:00) = แผน → **are going to**'),
    (['will', 'are going', 'wills', 'going to'],
     'I think … = ความคิดเห็น → **will** + V1'),
])
Q(3, 'u2', '2.2', 'I ___ to the supplier on the phone when the battery ran out.',
  ['was talking', 'talked', 'am talking', 'were talking'],
  'การกระทำยาวที่**ถูกขัด** (when + Past Simple) → I **was talking** … (ตัวอย่างใน p.119)')
Q(3, 'u2', '2.2', '___ we were waiting at the airport, our flight to Jakarta was cancelled.',
  ['While', 'During', 'For', 'Meanwhile'],
  '**while + Past Continuous** (we were waiting) • during ตามด้วยคำนาม เช่น during the wait')
P(3, 'u2', '2.2', 'Solar power for factories (2.2 compound nouns)', """
Many factories in Thailand have put solar {1} on their roofs. They are a long-term {2}: they are expensive at first, but they cut the electricity {3} and reduce greenhouse gases, which contribute to global {4}. Companies can also get a tax {5} for using renewable energy.
""", [
    (['panels', 'fuels', 'cuts', 'bills'],
     '**solar panels** = แผงโซลาร์เซลล์'),
    (['investment', 'invest', 'invested', 'investor'],
     'a long-term + **คำนาม** → **a long-term investment** = การลงทุนระยะยาว'),
    (['bill', 'panel', 'fuel', 'warming'],
     '**electricity bill** = ค่าไฟฟ้า'),
    (['warming', 'warm', 'warmth', 'warmed'],
     '**global warming** = ภาวะโลกร้อน'),
    (['deduction', 'deduct', 'deducted', 'deductive'],
     '**tax deduction** = การลดหย่อนภาษี'),
])
Q(3, 'u2', '2.1', 'Toyota was successful ___ selling the Prius, the first mass-produced hybrid car. (Video 2.1)',
  ['in', 'at', 'on', 'of'],
  '**be successful in + V-ing** = ประสบความสำเร็จในการ…')

# ── Unit 4 (15) ──
P(3, 'u4', '4.1', 'Volvo and Jaguar in China (Video 4.1)', """
Volvo launched a new high-end sedan in Shanghai. The car was {1} for the Chinese market: there is no front passenger seat, because many wealthy buyers have a {2}. Jaguar adopted a similar approach and packed the back of its car with luxury features. Both companies wanted their cars to appeal {3} premium customers. Mass-market consumer {4}, on the other hand, made only {5} changes for the middle class.
""", [
    (['customised', 'customise', 'customisable', 'customisation'],
     'was + **V3** (passive) → the car was **customised** for the Chinese market'),
    (['chauffeur', 'multinational', 'retailer', 'parent company'],
     'ไม่มีเบาะหน้าเพราะคนรวย**มีคนขับรถ** → **chauffeur** (คนขับรถส่วนตัว)'),
    (['to', 'for', 'at', 'with'],
     '**appeal to** = ดึงดูดใจ (✗ appeal for)'),
    (['brands', "brand's", 'branding', 'branded'],
     '**mass-market consumer brands** = แบรนด์สินค้าที่คนทั่วไปซื้อใช้ (พหูพจน์ + made)'),
    (['slight', 'slightly', 'slightness', 'slights'],
     'only + **adjective** + noun (changes) → **slight** changes (วิดีโอ: "even if only slightly")'),
])
P(3, 'u4', '4.2', 'An online shop listing (4.2, active or passive?)', """
Handmade by Nok — online shop
All our bags {1} by hand in Chiang Mai, and the leather {2} from a local farm. We {3} worldwide, and every order {4} within 48 hours. Personalised bags {5} too: just send us the name you want on the bag.
""", [
    (['are made', 'make', 'is made', 'are making'],
     'bags (พหูพจน์) ถูกทำ → **are made** by hand'),
    (['is bought', 'buys', 'are bought', 'is buying'],
     'leather (นับไม่ได้ = เอกพจน์) ถูกซื้อ → **is bought**'),
    (['ship', 'are shipped', 'is shipped', 'shipping'],
     '**We เป็นผู้ส่ง** (ทำเอง) → active **ship** • ไม่ใช่ทุกช่องจะเป็น passive — ดูประธานก่อน'),
    (['is dispatched', 'dispatches', 'are dispatched', 'is dispatching'],
     'every order (เอกพจน์) ถูกส่ง → **is dispatched**'),
    (['are offered', 'offer', 'is offered', 'are offering'],
     'bags (พหูพจน์) ถูกเสนอขาย → **are offered**'),
])
P(3, 'u4', '4.5', 'A letter confirming an order (4.5)', """
Dear Sir/Madam,
We are pleased to {1} your order for 50 desks, which we received yesterday. The {2} price is $120 per desk, and you will receive a 5% discount providing you pay within ten days. We will {3} the goods to your warehouse on 3 June. Please find our terms and conditions {4}.
If you have any queries, please do not hesitate to contact us.
Yours {5},
David Chan, Sales Manager
""", [
    (['confirm', 'complain', 'hesitate', 'belong'],
     '**We are pleased to confirm your order** = ยินดีที่จะยืนยันคำสั่งซื้อ'),
    (['unit', 'head', 'early', 'cash'],
     '**unit price** = ราคาต่อหน่วย ($120 per desk)'),
    (['deliver', 'apply', 'wait', 'listen'],
     '**deliver the goods** = ส่งสินค้า'),
    (['enclosed', 'enclose', 'enclosing', 'encloses'],
     '**Please find … enclosed** = ส่วนที่แนบมาด้วย (Enclosures)'),
    (['faithfully', 'sincerely', 'regards', 'kindly'],
     'ไม่รู้ชื่อผู้รับ (**Dear Sir/Madam**) → **Yours faithfully,**'),
])

# ── Company Profile (7) ──
P(3, 'cp', 'CP', 'Company profile: Siam Silk Ltd.', """
Siam Silk Ltd. is a Thai textile {1}. It was {2} by Somsak and Malee Chen in 1987. The company's head office is based {3} Nakhon Ratchasima, Thailand. It {4} silk scarves, ties and cushion covers. Its target customers are tourists and people {5} 25 to 60 with high incomes. The company's turnover was 300 million baht {6} 2025. Its main competitors {7} Thai Silk House and Royal Weave.
""", [
    (['manufacturer', 'manufacture', 'manufactured', 'manufacturing'],
     'a Thai textile + **คำนามที่เป็นบริษัท** → **manufacturer** (ผู้ผลิต) • ชีท: "a Japanese car manufacturer"'),
    (['established', 'establish', 'establishing', 'establishment'],
     '**was founded / established / set up + by + ผู้ก่อตั้ง + in + ปี** (was + V3)'),
    (['in', 'at', 'on', 'to'],
     '**is based / located + in + เมือง, ประเทศ**'),
    (['produces', 'produce', 'producing', 'is produced'],
     '**It + produces / manufactures + สินค้า** (it → เติม -s)'),
    (['aged', 'age', 'ages', 'aging'],
     'ชีท: "people **aged** 30 to 50 with middle incomes" → people aged … to …'),
    (['in', 'on', 'at', 'by'],
     '**turnover was + จำนวน + in + ปี**'),
    (['are', 'is', 'was', 'be'],
     "**Its main competitors + are + บริษัท 2 แห่งขึ้นไป**"),
])

# ── Describing Trends (10) ──
P(3, 'dt', 'DT', "Café website visitors (thousand), Jan–Jun", """
DATA: Jan 8 · Feb 8 · Mar 12 · Apr 11 · May 11 · Jun 6

Website visitors started {1} 8,000 in January and {2} at the same level in February. In March, there was a {3} rise {4} visitors {5} 4,000, to 12,000. Visitor numbers then went down {6} to 11,000 in April and remained {7} in May. In June, they fell {8} to 6,000.
""", [
    (['at', 'by', 'of', 'in'],
     '**started / began / stood / stayed + at + ตัวเลข**'),
    (['stayed', 'stays', 'was stayed', 'staying'],
     'อดีต (in February) → **stayed** at the same level • ไม่ใช้ passive'),
    (['sharp', 'sharply', 'sharpness', 'sharpen'],
     'a + **adjective** + noun → a **sharp** rise (8,000 → 12,000)'),
    (['in', 'of', 'by', 'at'],
     '**a rise + in + หัวข้อ** → a sharp rise **in** visitors'),
    (['of', 'by', 'to', 'at'],
     '**คำนาม + of + ส่วนต่าง** → a rise … **of** 4,000'),
    (['slightly', 'slight', 'slighter', 'slightness'],
     'ขยายกริยา went down • 12,000 → 11,000 = ลดเล็กน้อย → **slightly**'),
    (['steady', 'steadily', 'steadiness', 'steadied'],
     '**remain + adjective** → remained **steady** (ชีท: ไม่ใช้ adverb หลัง remain)'),
    (['dramatically', 'dramatic', 'drama', 'dramatical'],
     'ขยายกริยา fell • 11,000 → 6,000 = ลดมากและเร็ว → **dramatically**'),
])
Q(3, 'dt', 'DT', 'Which sentence is correct?',
  ['Sales stood at 10 million dollars in May.', 'Sales stood by 10 million dollars in May.',
   'Sales stood of 10 million dollars in May.', 'Sales stood to 10 million dollars in May.'],
  'ชีท: **Subject + stood / stayed / began / started + at + ตัวเลข + เวลา**')
Q(3, 'dt', 'DT', '"There was a steady rise in fruit exports last year." = "Fruit exports ___ last year."',
  ['rose steadily', 'rose steady', 'steady rose', 'were risen steadily'],
  'a rise → **rose** • steady → **steadily** • rise ไม่ใช้ passive')

# ════════════════════════════════════ SET 4 ════════════════════════════════════
# ── Unit 1 (14) ──
P(4, 'u1', '1.1', 'What employers want (Video 1.1)', """
"In the twenty-first century, the idea of a career for life is long gone," says the presenter. Employers want skills that can be {1} to a range of tasks and roles. Recruiters look for people who are good {2} problem solving and who have good communication {3}. They also value personal qualities such as {4} and enthusiasm. One expert says: "If you are {5} and have a can-do attitude, you will get wherever you want."
""", [
    (['applied', 'apply', 'applying', 'application'],
     'can be + **V3** (passive) → skills that can be **applied** to a range of tasks'),
    (['at', 'in', 'with', 'for'],
     '**be good at + V-ing / คำนาม** → good **at** problem solving (✗ good in)'),
    (['skills', 'skilled', 'skilful', 'skilfully'],
     'good communication + **คำนาม** → **communication skills**'),
    (['flexibility', 'flexible', 'flexibly', 'inflexible'],
     'such as + **คำนาม** คู่กับ enthusiasm → **flexibility**'),
    (['motivated', 'motivation', 'motivate', 'motivates'],
     'If you are + **คำคุณศัพท์** → **motivated** (มีแรงจูงใจ)'),
])
Q(4, 'u1', '1.2', 'Caller: "When I did my degree, I created a website for one of my projects."\n'
  'Jenny: "That\'s great! So you really ___ put that on your social media profile."',
  ['should', 'ought', 'should to', 'could to'],
  '**should + V1** → you really **should** put … (ought ต้องมี to)')
Q(4, 'u1', '1.2', 'Caller: "I\'ve never thought of putting my hiking on my profile."\nJenny: "Well, you ought ___ outside the box."',
  ['to think', 'think', 'thinking', 'thought'],
  '**ought to + V1** → you ought **to think** outside the box (ฟังเสียง 1.01)')
Q(4, 'u1', '1.2', 'In lesson 1.2, which sentence is a SUGGESTION (not advice)?',
  ["Why don't you join a professional networking site?", 'You should join a professional networking site.',
   'You ought to join a professional networking site.', "You shouldn't join a professional networking site."],
  'สไลด์ 1.2: **ให้คำแนะนำ (advice)** = should / shouldn\'t / ought to / could • **เสนอแนะ (suggestion)** = Why not / **Why don\'t you** / What about / How about')
Q(4, 'u1', '1.1', 'Accountants need to be good ___ numbers, and IT staff need to be good ___ computers.',
  ['with … with', 'at … at', 'with … at', 'in … with'],
  '**be good with numbers / computers / people / your hands** • good **at** ใช้กับทักษะหรือกิจกรรม เช่น good at problem solving')
P(4, 'u1', '1.5', 'A formal introduction email (1.5, the seven parts)', """
To: All staff
Subject: Introduction — new Finance Director

{1} colleagues,
I am sending this email to {2} myself. I have been appointed as the new Finance Director. My {3} job was as Chief Accountant at a hotel group in Phuket. Please feel free to contact me {4} email or phone. I very much look forward {5} you all in person.
Kind regards,
Pim Saetang
""", [
    (['Dear', 'Hi', 'Hey', 'Yo'],
     'อีเมลทางการถึงทุกคน → **Dear colleagues,** (ส่วนที่ 1 Greeting)'),
    (['introduce', 'introducing', 'introduction', 'introduced'],
     'to + **V1** → I am sending this email to **introduce** myself (ส่วนที่ 2 Opening)'),
    (['previous', 'previously', 'preview', 'prevent'],
     'My + **คำคุณศัพท์** + job → My **previous** job was as … (ส่วนที่ 4 Previous job)'),
    (['by', 'with', 'in', 'at'],
     '**contact me by email or phone** = ติดต่อทางอีเมลหรือโทรศัพท์'),
    (['to meeting', 'to meet', 'meeting', 'for meeting'],
     '**look forward to + V-ing** → look forward **to meeting** you'),
])

# ── Unit 2 (14) ──
P(4, 'u2', '2.2', 'How Grab started (2.2, past simple vs past continuous)', """
In 2011, Anthony Tan and Tan Hooi Ling {1} at Harvard Business School when they {2} an idea for a taxi-booking app. While they {3} their business plan, they entered it in a school competition. In 2012, they {4} the app in Malaysia. Today the company is called Grab, and it is a big part of the sharing {5} in Southeast Asia.
""", [
    (['were studying', 'are studying', 'was studying', 'study'],
     'การกระทำที่**กำลังดำเนินอยู่**ตอนที่มีเหตุการณ์สั้นเกิดขึ้น (when they had an idea) → **were studying** (they = พหูพจน์)'),
    (['had', 'were having', 'have', 'has'],
     '**when + Past Simple** = เหตุการณ์สั้น → **had** an idea • have an idea ไม่ใช้รูป continuous'),
    (['were writing', 'are writing', 'was writing', 'writing'],
     '**while + Past Continuous** → While they **were writing** …'),
    (['launched', 'were launching', 'launch', 'launches'],
     'In 2012 = เหตุการณ์ที่จบแล้ว → Past Simple **launched**'),
    (['economy', 'economic', 'economical', 'economist'],
     '**sharing economy** = เศรษฐกิจแบ่งปัน (Grab, Airbnb)'),
])
P(4, 'u2', '2.1', "Thailand's three sectors (2.1)", """
Thailand's economy has three sectors. The primary sector includes agriculture, fishing and {1}. The secondary sector turns raw materials into products: for example, Thailand has a large {2} industry that makes cars for export. The tertiary sector includes tourism, {3} and financial services. A courier service, which delivers parcels, is part of {4}. In many countries, the service sector accounts {5} more than half of economic output.
""", [
    (['mining', 'retail', 'insurance', 'construction'],
     'primary sector = นำวัตถุดิบจากธรรมชาติ → **mining** (เหมืองแร่) • retail, insurance = tertiary • construction = secondary'),
    (['automotive', 'automatic', 'automation', 'autonomous'],
     '**the automotive industry** = อุตสาหกรรมยานยนต์'),
    (['retail', 'farming', 'mining', 'manufacturing'],
     'tertiary = ภาคบริการ → **retail** (การค้าปลีก)'),
    (['transportation', 'agriculture', 'extraction', 'textiles'],
     'รับส่งพัสดุ = การขนส่ง → **transportation** (ภาคบริการ)'),
    (['for', 'to', 'of', 'with'],
     '**account for** = คิดเป็น (สัดส่วน)'),
])
Q(4, 'u2', '2.5', 'Bines plc ___ take over our company next month. The contract is ready, and the date is fixed.',
  ['is going to', 'will to', 'going to', 'is will'],
  'เหตุการณ์ที่**วางแผน/กำหนดไว้แล้ว** → **is going to** + V1')
Q(4, 'u2', '2.5', 'Which action point is written correctly?',
  ['email all staff about the meeting — Susan, today', 'All staff should be emailed.',
   'Emailing staff, somebody, sometime.', 'Susan will maybe email staff.'],
  'action point = **กริยา + งาน — ชื่อผู้รับผิดชอบ, กำหนดเวลา** (จากตัวอย่างอีเมล takeover ในบทเรียน 2.5)')
Q(4, 'u2', '2.1', 'Japanese electronics companies are known for producing small, ___ products such as the Walkman, '
  'a ___ cassette player. (Video 2.1)',
  ['innovative … portable', 'innovation … portable', 'innovative … portability', 'innovate … portably'],
  'หน้าคำนามต้องใช้**คำคุณศัพท์**ทั้งคู่ → **innovative** (มีนวัตกรรม) … **portable** (พกพาได้)')
Q(4, 'u2', '2.2', 'Which sentence is correct?',
  ["We didn't own a car when we lived in Bangkok.", "We weren't owning a car when we lived in Bangkok.",
   "We didn't owned a car when we lived in Bangkok.", 'We not owned a car when we lived in Bangkok.'],
  '**own** เป็น state verb ไม่ใช้ continuous • ปฏิเสธอดีต = **didn\'t + V1** → didn\'t **own**')

# ── Unit 4 (15) ──
P(4, 'u4', '4.2', 'Who wants to be a sofapreneur? (4.2 reading)', """
Sofapreneurs are people who earn {1} from websites while sitting at home. Many of them have a day {2} and only work online in their spare time. It is {3} that one percent of US adults make money this way. Governments must make sure that sofapreneurs do not compete unfairly with small shops by {4} tax. For many people, these sites are a way to earn money when they have health problems or caring {5}.
""", [
    (['money', 'monetary', 'moneyed', 'monetise'],
     '**earn money** = หาเงิน'),
    (['job', 'jobs', 'working', 'worker'],
     '**a day job** = งานประจำ'),
    (['estimated', 'estimate', 'estimating', 'estimation'],
     '**It is estimated that …** = มีการประมาณว่า… (passive)'),
    (['avoiding', 'avoid', 'avoided', 'to avoid'],
     'หลังบุพบท **by + V-ing** → by **avoiding** tax'),
    (['responsibilities', 'responsible', 'responsibly', "responsibility's"],
     '**caring responsibilities** = ภาระดูแลคนในครอบครัว'),
])
P(4, 'u4', '4.1', 'Starbucks in China (Video 4.1)', """
When Starbucks opened its flagship store in China, the {1} was different: the words were not there, only the logo. Because China is the home of tea, the company decided to {2} its menu to local tastes and sell a range of {3} teas. Starbucks believes that coffee consumption will continue to {4}, and it wants to set a standard for that {5}.
""", [
    (['branding', "brand's", 'branded', 'brands'],
     'the + **คำนามเอกพจน์** + was → the **branding** was different'),
    (['adapt', 'adaptable', 'adaptation', 'adaptability'],
     'decided to + **V1** → **adapt** its menu to local tastes'),
    (['premium', 'premiums', 'premiere', 'premiered'],
     'a range of + **adjective** + teas → **premium** teas (ระดับพรีเมียม)'),
    (['grow', 'growth', 'grown', 'growing'],
     'continue to + **V1** → continue to **grow**'),
    (['growth', 'grow', 'grew', 'grown'],
     'that + **คำนาม** → that **growth** (การเติบโต)'),
])
P(4, 'u4', '4.5', 'A reply to Mr Chahal (4.5, verbs + prepositions)', """
Dear Mr Chahal,
Thank you {1} your email of 2 May. I have spoken {2} our warehouse manager about the late delivery, and the goods will arrive {3} your factory on Friday. We apologise for the delay and look forward to {4} with you again. We will also pay {5} the extra transport costs.
Yours sincerely,
Anna Lee
""", [
    (['for', 'to', 'about', 'at'],
     '**Thank you for + สิ่งที่ได้รับ** → Thank you **for** your email'),
    (['to', 'at', 'for', 'on'],
     '**speak to + คน** → spoken **to** our warehouse manager'),
    (['at', 'to', 'for', 'with'],
     '**arrive at + สถานที่**'),
    (['working', 'work', 'worked', 'be work'],
     '**look forward to + V-ing** → **working** with you'),
    (['for', 'to', 'at', 'about'],
     '**pay for + สิ่งของ/ค่าใช้จ่าย** → pay **for** the extra costs'),
])

# ── Company Profile (7) ──
P(4, 'cp', 'CP', 'Company profile: Ocean Fresh Co., Ltd.', """
Ocean Fresh Co., Ltd. is {1} Thai seafood exporter. It was set up {2} 2008 by a group of fishermen in Songkhla. {3} headquarters is located in Songkhla, Thailand. The company exports frozen shrimp, squid and fish {4} Japan and Europe. Its target {5} are supermarkets and hotel chains. Its turnover was 1.2 billion baht in 2025. The company's main {6} are Seafresh Asia and Blue Harbour. {7} also plans to open a factory in Vietnam.
""", [
    (['a', 'an', 'the', '— (no word)'],
     '**ชื่อบริษัท + is + a/an + สัญชาติ + ประเภทธุรกิจ** → **a** Thai seafood exporter'),
    (['in', 'on', 'at', 'by'],
     '**set up … in + ปี** (ชีท: + by + founder(s) + in + year of establishment)'),
    (['Its', "It's", 'Their', 'It'],
     'บริษัท = it → คำแสดงความเป็นเจ้าของ **Its** headquarters (It\'s = It is)'),
    (['to', 'at', 'for', 'with'],
     '**export … to + ประเทศ**'),
    (['customers', 'customer', 'custom', "customer's"],
     '**Its target customers + are + กลุ่มลูกค้า** (พหูพจน์)'),
    (['competitors', 'competitor', 'competitive', 'competition'],
     "**The company's main competitors + are + บริษัท 2 แห่งขึ้นไป**"),
    (['It', 'They', 'Its', 'Their'],
     'บริษัท 1 แห่ง = **It** (ประธาน)'),
])

# ── Describing Trends (10) ──
P(4, 'dt', 'DT', 'Ocean Fresh — annual revenue (million baht), 2021–2025', """
DATA: 2021 900 · 2022 700 · 2023 750 · 2024 1,200 · 2025 1,200

In 2022, revenue went down {1} 200 million baht. In 2023, there was a {2} recovery, and revenue rose {3} 700 {4} 750 million baht. We had a {5} increase {6} revenue in 2024, when it reached 1,200 million baht. Revenue then remained {7} at 1,200 million baht in 2025.
""", [
    (['by', 'of', 'at', 'in'],
     '**กริยา + by + ส่วนต่าง** → went down **by** 200 million baht (900 → 700)'),
    (['slight', 'slightly', 'slighter', 'slightness'],
     'a + **adjective** + noun → a **slight** recovery (700 → 750)'),
    (['from', 'of', 'by', 'at'],
     '**from + จุดเริ่ม … to + จุดที่ไปถึง**'),
    (['to', 'by', 'of', 'at'],
     'from 700 **to** 750'),
    (['dramatic', 'dramatically', 'drama', 'dramatical'],
     'a + **adjective** + noun → a **dramatic** increase (750 → 1,200)'),
    (['in', 'of', 'by', 'at'],
     '**We had + a + adj + noun + in + หัวข้อ** → an increase **in** revenue'),
    (['stable', 'stably', 'stability', 'stabilise'],
     '**remain + adjective stable / steady** → remained **stable** at …'),
])
Q(4, 'dt', 'DT', '"Sales decreased sharply from 55 to 30 million baht in 2024."\n= "There was a ___ in sales from 55 to 30 million baht in 2024."',
  ['sharp decrease', 'sharply decrease', 'sharp decreased', 'sharply decreasing'],
  'verb → noun: decreased → **a decrease** • adverb → adjective: sharply → **sharp**')
Q(4, 'dt', 'DT', 'Which sentence is correct?',
  ['There was a slight fall of 1,000 units in June.', 'There was a slightly fall of 1,000 units in June.',
   'There was a slight fell of 1,000 units in June.', 'There was a slight fall by 1,000 units in June.'],
  '**a + adjective + noun + of + ส่วนต่าง** (คำนามใช้ of • กริยาใช้ by)')
Q(4, 'dt', 'DT', 'Which verb does NOT describe a downward trend?',
  ['recover', 'decline', 'drop', 'go down'],
  'ในชีท **recover** = ฟื้นตัว (ขึ้นหลังจากลดลง) • decline / drop / go down = แนวโน้มขาลง')

# (Set 3, Unit 2 — 14th item)
Q(3, 'u2', '2.1', 'A rice farm in Suphan Buri, a rice-cracker factory in Bangkok and a 7-Eleven shop are all part of one '
  'supply chain. Which sector is the 7-Eleven shop in?',
  ['the tertiary sector', 'the primary sector', 'the secondary sector', 'the automotive industry'],
  'ร้านค้าปลีก = งานบริการ → **tertiary** • นาข้าว = primary • โรงงานข้าวเกรียบ = secondary (เหมือนกิจกรรม supply chain ในบทเรียน 2.1)')

# ════════════════════ External Reading: vocabulary in context (English options) ════════════════════
# The other Section III items are the hand-written reading sets in content.py (er-read, er-expr).
# Not copied: the Week 15 Try It items and homework.
ER_VOCAB = [
    ('¶1: "…sharing their bold predictions for the new year." In this sentence, "predictions" are …',
     ['ideas about what will happen in the future', 'decisions about what happened in the past',
      'prices for new products', 'rules for marketing teams'],
     '**predictions** = การคาดการณ์ → สิ่งที่คิดว่าจะเกิดขึ้นในอนาคต (for the new year)'),
    ('¶2: "…I have pinpointed five trends you need to know." "Pinpointed" is closest in meaning to …',
     ['identified exactly', 'invented quickly', 'forgotten about', 'paid for'],
     '**pinpoint** = ระบุได้อย่างชัดเจน หลังจาก "analyzing the major changes in 2025"'),
    ('¶3: "Even with automation generating videos and ads instantly…" "Automation" means …',
     ['machines and software doing work without people', 'people making everything by hand',
      'a type of TV advert', 'a group of loyal customers'],
     '**automation** = ระบบอัตโนมัติ (AI สร้างวิดีโอและโฆษณาได้ทันที)'),
    ('¶4: "Consumers are looking for authentic stories and genuine connections." "Genuine" is closest in meaning to …',
     ['real and sincere', 'expensive and rare', 'quick and easy', 'old and traditional'],
     '**genuine** = จริงใจ / แท้จริง (คู่กับ authentic)'),
    ('¶4: "…your audience will experience burnout, engagement will decline…" Here "decline" means …',
     ['become lower', 'say no politely', 'stay the same', 'grow quickly'],
     '**decline** (v.) = ลดลง / แย่ลง • ในบริบทนี้ไม่ได้แปลว่า "ปฏิเสธ"'),
    ('¶5: "It is about finding a specific niche and providing value." A "niche" is …',
     ['a small, special group of customers', 'the biggest possible audience',
      'an online advert', 'a famous influencer'],
     '**niche** = กลุ่มเฉพาะ / ตลาดเฉพาะกลุ่ม (ตรงข้ามกับ "the largest volume of people")'),
    ('¶5: "…a space for audiences to interact with one another…" "Interact" means …',
     ['communicate and do things together', 'compete against each other', 'stop talking', 'buy more products'],
     '**interact** = มีปฏิสัมพันธ์ / ติดต่อสื่อสารกัน'),
    ('¶7: "…content that speaks like a human but is strategically structured for machines." "Structured" means …',
     ['organised in a clear way', 'written very quickly', 'hidden from users', 'copied from other sites'],
     '**structured** = ที่ถูกจัดระบบ / มีโครงสร้างชัดเจน'),
    ('¶8: "…much better in 2026 than just stuffing keywords onto a webpage." "Stuffing" means …',
     ['putting in far too many', 'carefully removing', 'translating', 'hiding'],
     '**stuffing** = การยัดเยียด (ยัดคีย์เวิร์ดลงหน้าเว็บมากเกินไป)'),
    ('¶10: "…advertising on traditional TV offers something hard to find today: consistency." "Consistency" means …',
     ['being the same and reliable over time', 'being cheap', 'being new and exciting', 'being very fast'],
     '**consistency** = ความสม่ำเสมอ'),
    ('¶10: "…traditional TV might be the best anchor point for your media strategy…" An "anchor point" is …',
     ['the strong, central part of a plan', 'a place where ships stop',
      'the last and least important part', 'a TV presenter'],
     '**anchor point** = จุดยึดเหนี่ยว / จุดศูนย์กลางของแผน'),
    ('¶11: "…the return on investment has been unpredictable." "Unpredictable" means …',
     ['impossible to know in advance', 'always very high', 'easy to calculate', 'the same every year'],
     '**unpredictable** = ที่คาดเดาไม่ได้'),
    ('¶11: "…micro-creators with very loyal fans…" "Loyal" fans …',
     ['keep supporting the same creator', 'often change to new creators',
      'are paid by brands', 'only watch TV'],
     '**loyal** = ซื่อสัตย์ / ภักดี → สนับสนุนคนเดิมต่อไป'),
    ('¶12: "Mid-sized influencers are struggling to stay relevant." To "stay relevant" is to …',
     ['remain important and interesting to people', 'stay in the same place', 'stay cheap', 'stay young'],
     '**stay relevant** = รักษาสถานะให้อยู่ในกระแสความสนใจ'),
    ('¶12: "When allocating your budget…" "Allocating" means …',
     ['deciding how to share out', 'spending everything at once', 'borrowing', 'hiding'],
     '**allocate** = จัดสรร (เช่น งบประมาณ)'),
]
