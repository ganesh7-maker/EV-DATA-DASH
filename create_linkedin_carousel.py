import os
import sys
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    font_dir = "C:/Windows/Fonts"
    if bold:
        paths = [
            os.path.join(font_dir, "segoeuib.ttf"),
            os.path.join(font_dir, "arialbd.ttf"),
            os.path.join(font_dir, "calibrib.ttf")
        ]
    else:
        paths = [
            os.path.join(font_dir, "segoeui.ttf"),
            os.path.join(font_dir, "arial.ttf"),
            os.path.join(font_dir, "calibri.ttf")
        ]
    for p in paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

# Dimensions (1080 x 1350 px - LinkedIn 4:5 ratio)
WIDTH, HEIGHT = 1080, 1350

# Colors
BG_DARK = (11, 19, 43)          # #0B132B Dark Obsidian
CARD_BG = (28, 37, 65)          # #1C2541 Slate Navy
CARD_BG_LIGHT = (38, 49, 80)    # #263150 Lighter Slate
CYAN = (72, 202, 228)           # #48CAE4 Bright Cyan
BLUE_ACCENT = (0, 119, 182)     # #0077B6 Deep Blue
GREEN_ACCENT = (74, 222, 128)   # #4ADE80 Emerald Green
GOLD_ACCENT = (251, 191, 36)    # #FBBF24 Amber Gold
WHITE = (255, 255, 255)
MUTED = (148, 163, 184)         # #94A3B8 Soft Slate Gray

def create_base_slide(slide_num, total_slides=10, category="ENTERPRISE DATA & AI PLATFORM"):
    img = Image.new("RGB", (WIDTH, HEIGHT), BG_DARK)
    draw = ImageDraw.Draw(img)

    # Top Accent Bar
    draw.rectangle([0, 0, WIDTH, 12], fill=CYAN)

    # Category Pill / Tag
    f_cat = get_font(22, bold=True)
    draw.text((70, 50), category.upper(), font=f_cat, fill=CYAN)

    # Footer Slide Number & Indicator
    f_foot = get_font(20, bold=False)
    footer_text = f"Slide {slide_num} of {total_slides}  *  Swipe ->" if slide_num < total_slides else f"Slide {slide_num} of {total_slides}  *  Connect & Share"
    draw.text((70, HEIGHT - 70), footer_text, font=f_foot, fill=MUTED)
    draw.line([70, HEIGHT - 90, WIDTH - 70, HEIGHT - 90], fill=(40, 55, 85), width=2)

    return img, draw

def draw_card(draw, box, bg_color=CARD_BG, border_color=CYAN, border_width=2, radius=20):
    x1, y1, x2, y2 = box
    draw.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=bg_color, outline=border_color, width=border_width)

def render_slide_1():
    img, draw = create_base_slide(1, 10, "DATA ENGINEERING & AI PORTFOLIO")

    # Big Title
    f_title = get_font(60, bold=True)
    draw.text((70, 130), "EV Fleet Analytics", font=f_title, fill=WHITE)
    draw.text((70, 205), "& AI Platform", font=f_title, fill=CYAN)

    # Subtitle
    f_sub = get_font(28, bold=False)
    draw.text((70, 300), "End-to-End Battery Health Monitoring, AI Peak-Shifting\n& Zero-Touch RPA Data Pipeline", font=f_sub, fill=MUTED)

    # Architecture Overview Box
    draw_card(draw, [70, 420, WIDTH - 70, 800], bg_color=CARD_BG, border_color=BLUE_ACCENT, border_width=3)
    f_h = get_font(32, bold=True)
    draw.text((100, 450), "ENTERPRISE TECH STACK", font=f_h, fill=CYAN)

    f_item = get_font(26, bold=False)
    items = [
        ("• Kaggle Telemetry Data", "Raw CSV Dataset"),
        ("• Alteryx YXMD", "ETL & Imputation Pipeline"),
        ("• Snowflake DW", "Star Schema & CDC Streams"),
        ("• UiPath RPA", "Orchestration & Auto-Refresh"),
        ("• Power BI & Fabric", "6-Page Dark Blue Dashboard"),
        ("• Streamlit AI Engine", "Predictive SOH & Cost Model")
    ]
    y_pos = 510
    for left_t, right_t in items:
        draw.text((110, y_pos), left_t, font=get_font(26, bold=True), fill=WHITE)
        draw.text((480, y_pos), f"-> {right_t}", font=f_item, fill=MUTED)
        y_pos += 45

    # 3 Stat Cards at Bottom
    card_w = (WIDTH - 140 - 40) // 3
    stats = [
        ("14%", "Cost Savings", GREEN_ACCENT),
        ("SOH", "Battery Health", CYAN),
        ("0-Touch", "RPA Pipeline", GOLD_ACCENT)
    ]
    for i, (val, label, color) in enumerate(stats):
        x1 = 70 + i * (card_w + 20)
        draw_card(draw, [x1, 840, x1 + card_w, 1020], bg_color=CARD_BG_LIGHT, border_color=color, border_width=2)
        draw.text((x1 + 30, 870), val, font=get_font(46, bold=True), fill=color)
        draw.text((x1 + 25, 950), label, font=get_font(22, bold=False), fill=WHITE)

    return img

def render_slide_2():
    img, draw = create_base_slide(2, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "The EV Fleet Challenge", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "Fleet managers face 3 critical operational bottlenecks:", font=f_sub, fill=MUTED)

    problems = [
        ("1. Battery Degradation Risks", "Sudden roadside failures caused by unmonitored cell degradation below 80% State of Health (SOH).", GOLD_ACCENT),
        ("2. Spiking Energy Utility Bills", "Unoptimized peak-hour charging resulting in massive demand surcharges and high electricity costs.", (239, 68, 68)),
        ("3. Fragmented Telemetry Data", "Telemetry scattered across charging stations, vehicle logs, and spreadsheets without unified analytics.", CYAN)
    ]

    y_pos = 280
    for title, desc, color in problems:
        draw_card(draw, [70, y_pos, WIDTH - 70, y_pos + 200], bg_color=CARD_BG, border_color=color, border_width=2)
        draw.text((100, y_pos + 25), title, font=get_font(32, bold=True), fill=color)
        
        words = desc.split()
        lines, curr = [], ""
        for w in words:
            if len(curr + " " + w) > 50:
                lines.append(curr)
                curr = w
            else:
                curr = (curr + " " + w).strip()
        if curr:
            lines.append(curr)
            
        ly = y_pos + 80
        for l in lines:
            draw.text((100, ly), l, font=get_font(24, bold=False), fill=WHITE)
            ly += 35
        y_pos += 240

    return img

def render_slide_3():
    img, draw = create_base_slide(3, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "System Architecture", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "Modern automated data pipeline from ingestion to AI insights:", font=f_sub, fill=MUTED)

    steps = [
        ("1", "Telemetry Data Source", "Kaggle EV Dataset (CSV Ingestion)", GREEN_ACCENT),
        ("2", "Alteryx YXMD Workflow", "Null Imputation, Metric Calculation & Deduplication", CYAN),
        ("3", "Snowflake Data Warehouse", "Raw/Staging/Core Star Schema, Streams & Tasks", BLUE_ACCENT),
        ("4", "UiPath RPA Orchestrator", "Automated Snowflake SP Triggers & PBI Refresh", GOLD_ACCENT),
        ("5", "Power BI & Fabric Suite", "6-Page Dark Obsidian Executive Dashboards", CYAN),
        ("6", "Streamlit AI Engine", "SOH Degradation Model & Peak-Shift Cost Optimizer", GREEN_ACCENT)
    ]

    y_pos = 270
    for num, title, desc, color in steps:
        draw_card(draw, [70, y_pos, WIDTH - 70, y_pos + 110], bg_color=CARD_BG, border_color=color, border_width=2)
        draw.ellipse([95, y_pos + 25, 155, y_pos + 85], fill=color)
        draw.text((117, y_pos + 33), num, font=get_font(32, bold=True), fill=BG_DARK)

        draw.text((180, y_pos + 20), title, font=get_font(28, bold=True), fill=WHITE)
        draw.text((180, y_pos + 60), desc, font=get_font(22, bold=False), fill=MUTED)

        y_pos += 130

    return img

def render_slide_4():
    img, draw = create_base_slide(4, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "Snowflake DW & Star Schema", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "High-performance enterprise data modeling in Snowflake:", font=f_sub, fill=MUTED)

    cards = [
        ("Medallion Architecture", ["RAW: Staging raw CSV streams", "STAGING: Cleaning & type casting", "CORE: Dimensional Star Schema (DIM_VEHICLE, FACT_CHARGING_SESSIONS)"], CYAN),
        ("CDC Streams & Tasks", ["Automated Change Data Capture streams", "Scheduled tasks running daily transformations", "Zero manual pipeline intervention required"], GREEN_ACCENT),
        ("Stored Procedures", ["SP_POPULATE_STAR_SCHEMA: Upsert core tables", "SP_CALCULATE_BATTERY_DEGRADATION: Identify high-risk battery cells below 80% SOH threshold"], GOLD_ACCENT)
    ]

    y_pos = 270
    for title, bullets, color in cards:
        draw_card(draw, [70, y_pos, WIDTH - 70, y_pos + 220], bg_color=CARD_BG, border_color=color, border_width=2)
        draw.text((100, y_pos + 25), title, font=get_font(30, bold=True), fill=color)
        by = y_pos + 75
        for b in bullets:
            draw.text((100, by), f"• {b}", font=get_font(24, bold=False), fill=WHITE)
            by += 40
        y_pos += 250

    return img

def render_slide_5():
    img, draw = create_base_slide(5, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "Zero-Touch RPA with UiPath", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "Automating repetitive data engineering tasks end-to-end:", font=f_sub, fill=MUTED)

    rpa_steps = [
        ("1. Directory File Watcher", "Monitors incoming telemetry CSV files from charging stations and uploads to Snowflake stage."),
        ("2. Stored Procedure Execution", "Triggers Snowflake SPs to process raw data into Star Schema facts and dimensions."),
        ("3. Power BI Dataset Refresh", "Sends REST API trigger to refresh Power BI & Fabric datasets automatically."),
        ("4. Executive Email Dispatch", "Generates daily summary report PDF and dispatches anomaly alerts to fleet managers.")
    ]

    y_pos = 280
    for title, desc in rpa_steps:
        draw_card(draw, [70, y_pos, WIDTH - 70, y_pos + 180], bg_color=CARD_BG, border_color=GOLD_ACCENT, border_width=2)
        draw.text((100, y_pos + 25), title, font=get_font(28, bold=True), fill=GOLD_ACCENT)
        
        words = desc.split()
        lines, curr = [], ""
        for w in words:
            if len(curr + " " + w) > 52:
                lines.append(curr)
                curr = w
            else:
                curr = (curr + " " + w).strip()
        if curr:
            lines.append(curr)
            
        ly = y_pos + 75
        for l in lines:
            draw.text((100, ly), l, font=get_font(24, bold=False), fill=WHITE)
            ly += 35
        y_pos += 205

    return img

def render_slide_6():
    img, draw = create_base_slide(6, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "6-Page BI Dashboard Suite", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "Built with Microsoft Fabric Dark Obsidian design system:", font=f_sub, fill=MUTED)

    pages = [
        ("1. Executive Summary", "Fleet KPI cards, total energy used, cost growth & active vehicles."),
        ("2. Battery Health & SOH", "Degradation trendlines, high-risk cell alerts (< 80% SOH)."),
        ("3. Charging Efficiency", "Peak vs Off-peak kWh usage, charger utilization rates."),
        ("4. Fleet Operations", "Distance traveled, efficiency (kWh/mi), vehicle telemetry."),
        ("5. Energy Cost Analysis", "Peak rate surcharges, monthly expenditure & savings breakdown."),
        ("6. AI Anomaly & Q&A", "Natural language Q&A interface & ML degradation forecasts.")
    ]

    grid_w = (WIDTH - 140 - 20) // 2
    for i, (title, desc) in enumerate(pages):
        row = i // 2
        col = i % 2
        x1 = 70 + col * (grid_w + 20)
        y1 = 280 + row * 240
        
        draw_card(draw, [x1, y1, x1 + grid_w, y1 + 220], bg_color=CARD_BG, border_color=CYAN, border_width=2)
        draw.text((x1 + 20, y1 + 20), title, font=get_font(25, bold=True), fill=CYAN)
        
        words = desc.split()
        lines, curr = [], ""
        for w in words:
            if len(curr + " " + w) > 24:
                lines.append(curr)
                curr = w
            else:
                curr = (curr + " " + w).strip()
        if curr:
            lines.append(curr)
            
        ly = y1 + 75
        for l in lines:
            draw.text((x1 + 20, ly), l, font=get_font(21, bold=False), fill=WHITE)
            ly += 30

    return img

def render_slide_7():
    img, draw = create_base_slide(7, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "AI Engine & Cost Optimizer", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "Machine Learning & Smart Energy Scheduling:", font=f_sub, fill=MUTED)

    draw_card(draw, [70, 270, WIDTH - 70, 430], bg_color=CARD_BG_LIGHT, border_color=GREEN_ACCENT, border_width=3)
    draw.text((100, 300), "14% Monthly Energy Cost Savings", font=get_font(42, bold=True), fill=GREEN_ACCENT)
    draw.text((100, 365), "Achieved via AI-driven peak-shifting charging algorithms.", font=get_font(24, bold=False), fill=WHITE)

    cards = [
        ("Predictive Battery Degradation", "Linear regression & ML model predicts SOH degradation trajectory and flags battery replacements before roadside failures occur.", CYAN),
        ("Peak-Shifting Recommendations", "Automatically shifts vehicle charging schedules from peak utility rate hours to off-peak night windows.", GREEN_ACCENT),
        ("Natural Language Assistant", "Streamlit-powered conversational AI engine enabling fleet managers to ask questions in plain English.", GOLD_ACCENT)
    ]

    y_pos = 460
    for title, desc, color in cards:
        draw_card(draw, [70, y_pos, WIDTH - 70, y_pos + 175], bg_color=CARD_BG, border_color=color, border_width=2)
        draw.text((100, y_pos + 20), title, font=get_font(28, bold=True), fill=color)
        
        words = desc.split()
        lines, curr = [], ""
        for w in words:
            if len(curr + " " + w) > 52:
                lines.append(curr)
                curr = w
            else:
                curr = (curr + " " + w).strip()
        if curr:
            lines.append(curr)
            
        ly = y_pos + 70
        for l in lines:
            draw.text((100, ly), l, font=get_font(23, bold=False), fill=WHITE)
            ly += 32
        y_pos += 195

    return img

def render_slide_8():
    img, draw = create_base_slide(8, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "Enterprise Data Governance", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "Security, Compliance & Quality Assurance:", font=f_sub, fill=MUTED)

    gov_cards = [
        ("Role-Based Access Control (RBAC)", ["Analyst Role: Read-only access to anonymized marts", "Manager Role: Full access to operational fleet data", "Executive Role: Aggregated KPI & cost view"], CYAN),
        ("Dynamic Data Masking & Encryption", ["AES-256 encryption at rest and in transit", "Column-level masking on driver PII & vehicle IDs", "Full compliance with enterprise security standards"], BLUE_ACCENT),
        ("Data Quality & Audit Logging", ["Automated quality exception matrix on nulls & bounds", "Complete line-item audit logs for all ETL runs", "Lineage tracking from source Kaggle CSV to Power BI"], GREEN_ACCENT)
    ]

    y_pos = 270
    for title, bullets, color in gov_cards:
        draw_card(draw, [70, y_pos, WIDTH - 70, y_pos + 230], bg_color=CARD_BG, border_color=color, border_width=2)
        draw.text((100, y_pos + 25), title, font=get_font(28, bold=True), fill=color)
        by = y_pos + 75
        for b in bullets:
            draw.text((100, by), f"• {b}", font=get_font(23, bold=False), fill=WHITE)
            by += 42
        y_pos += 255

    return img

def render_slide_9():
    img, draw = create_base_slide(9, 10)

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "Key Business Impact & ROI", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "Quantifiable benefits delivered to fleet operations:", font=f_sub, fill=MUTED)

    metrics = [
        ("14%", "Monthly Energy Cost Savings", "Achieved by shifting charging schedules to off-peak rate windows.", GREEN_ACCENT),
        ("< 80%", "SOH Early Warning Threshold", "Predictive alert system preventing unexpected battery cell failures.", GOLD_ACCENT),
        ("100%", "Zero-Touch Automation", "UiPath RPA orchestrates ingestion, Snowflake SPs, and PBI refreshes.", CYAN)
    ]

    y_pos = 280
    for stat, title, desc, color in metrics:
        draw_card(draw, [70, y_pos, WIDTH - 70, y_pos + 210], bg_color=CARD_BG, border_color=color, border_width=3)
        
        draw_card(draw, [100, y_pos + 30, 320, y_pos + 180], bg_color=CARD_BG_LIGHT, border_color=color, border_width=2)
        draw.text((120, y_pos + 65), stat, font=get_font(50, bold=True), fill=color)

        draw.text((350, y_pos + 40), title, font=get_font(30, bold=True), fill=WHITE)
        
        words = desc.split()
        lines, curr = [], ""
        for w in words:
            if len(curr + " " + w) > 35:
                lines.append(curr)
                curr = w
            else:
                curr = (curr + " " + w).strip()
        if curr:
            lines.append(curr)
            
        ly = y_pos + 95
        for l in lines:
            draw.text((350, ly), l, font=get_font(23, bold=False), fill=MUTED)
            ly += 34

        y_pos += 240

    return img

def render_slide_10():
    img, draw = create_base_slide(10, 10, "THANK YOU FOR SWIPING!")

    f_title = get_font(52, bold=True)
    draw.text((70, 130), "Want to Explore the Code?", font=f_title, fill=WHITE)
    f_sub = get_font(26, bold=False)
    draw.text((70, 205), "The full repository, SQL DDLs, DAX & Streamlit app are open-source!", font=f_sub, fill=MUTED)

    draw_card(draw, [70, 280, WIDTH - 70, 750], bg_color=CARD_BG, border_color=CYAN, border_width=3)
    
    draw.text((110, 320), "Full GitHub Repository & Code:", font=get_font(32, bold=True), fill=CYAN)
    draw.text((110, 375), "Link available in the first comment below!", font=get_font(26, bold=False), fill=WHITE)

    draw.line([110, 440, WIDTH - 110, 440], fill=(50, 70, 100), width=2)

    draw.text((110, 470), "Created by Ganesh GK", font=get_font(32, bold=True), fill=GREEN_ACCENT)
    draw.text((110, 525), "• LinkedIn: linkedin.com/in/ganesh-gk-3341a6247", font=get_font(24, bold=False), fill=WHITE)
    draw.text((110, 570), "• What data engineering stack do you use for IoT/EVs?", font=get_font(24, bold=False), fill=WHITE)
    draw.text((110, 615), "• Drop a comment or connect with me on LinkedIn!", font=get_font(24, bold=False), fill=WHITE)

    draw_card(draw, [70, 800, WIDTH - 70, 980], bg_color=CARD_BG_LIGHT, border_color=GOLD_ACCENT, border_width=2)
    draw.text((120, 835), "Follow Ganesh GK for Data & AI Content!", font=get_font(28, bold=True), fill=GOLD_ACCENT)
    draw.text((120, 895), "Sharing insights on Cloud Data Warehousing, Snowflake & RPA.", font=get_font(23, bold=False), fill=MUTED)

    return img

def main():
    slides_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "carousel_slides")
    os.makedirs(slides_dir, exist_ok=True)

    renderers = [
        render_slide_1,
        render_slide_2,
        render_slide_3,
        render_slide_4,
        render_slide_5,
        render_slide_6,
        render_slide_7,
        render_slide_8,
        render_slide_9,
        render_slide_10
    ]

    images = []
    print("Generating 10 LinkedIn Carousel Slides...")
    for idx, renderer in enumerate(renderers, 1):
        img = renderer()
        slide_path = os.path.join(slides_dir, f"slide_{idx:02d}.png")
        img.save(slide_path, "PNG")
        images.append(img)
        print(f" Saved: {slide_path}")

    pdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "EV_Fleet_Analytics_Carousel.pdf")
    if images:
        images[0].save(pdf_path, "PDF", save_all=True, append_images=images[1:], resolution=100.0)
        print("=" * 60)
        print(f"SUCCESS! Created Carousel PDF at: {pdf_path}")
        print("=" * 60)

if __name__ == "__main__":
    main()
