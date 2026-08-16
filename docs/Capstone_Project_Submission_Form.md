# CAREERLADDER TECHNOLOGIES
## Capstone Project Submission Form

---

### 1) Student & Project Information

| Field | Details |
| :--- | :--- |
| **Submission Date** | 25-06-2026 |
| **College Name** | CANARA COLLEGE |
| **Team Name** | EcoPulse |
| **Team Lead** | GANESH |
| **Team Member Names** | • MANOHARI<br>• PALLAVI B M<br>• RAKSHITHA<br>• SHREYA DEEPAK NAIK<br>• SINCHANA R |
| **Project Name** | Electric Vehicle (EV) Fleet Charging & Battery Health |
| **Project Description** | This project helps fleet managers monitor battery health, optimize charging schedules, cut operational costs, and make smart decisions using interactive dashboards. |
| **GitHub Repository** | [https://github.com/ganesh7-maker/EV-DATA-DASH](https://github.com/ganesh7-maker/EV-DATA-DASH) |
| **Live Demo URL** | `https://ev-fleet-analytics.streamlit.app/` *(or `http://localhost:8501`)* |
| **Demo Video / Documentation** | [Documentation & User Manual](file:///c:/EV%20DATA%20DASH/docs/user_manual.md) |
| **Project Architecture** | Alteryx ETL $\rightarrow$ Snowflake DW $\rightarrow$ UiPath RPA $\rightarrow$ Power BI / Fabric $\rightarrow$ Streamlit AI Assistant |

---

### 2) Executive Summary

#### Business Problems
- **Lack of Centralized Data Management**: EV charging and battery telemetry data are stored across multiple fragmented sources, making it difficult to access and analyze information efficiently.
- **Battery Degradation & Unplanned Maintenance**: Lack of real-time telemetry monitoring for State of Health (SOH) leads to sudden battery cell failures and high operational replacement costs.
- **High Charging & Energy Expenses**: Unoptimized charging schedules during peak electricity tariff hours inflate monthly fleet operational costs.
- **Slow & Manual Reporting**: Delayed executive decision-making caused by manual spreadsheet aggregation across operations teams.

---

### 3) Project Description

The **EV Fleet Charging Analytics** project analyzes electric vehicle fleet data to improve fleet management and operational efficiency. It uses **Alteryx** for data processing, **Snowflake** for cloud data storage, and **Power BI** for interactive dashboards. The solution provides insights into battery health, charging patterns, energy consumption, costs, and fleet performance, helping organizations optimize charging operations, reduce expenses, and make data-driven decisions for sustainable EV management.

---

### 4) Business Benefits

- 🔋 **Centralized Data Management**: Unified repository for all EV charging and battery telemetry data.
- ❤️ **Continuous Battery Monitoring**: Improved battery performance and early detection of degradation (SOH < 80%).
- 💰 **Cost Optimization**: Reduced charging and maintenance costs (achieving up to 14% energy savings).
- ⚡ **Station Utilization**: Optimized charging schedules and higher station throughput.
- ⚡ **Automated Reporting**: Faster and more accurate reporting driven by UiPath RPA automation.
- ☁️ **Scalable Storage**: Cloud-based, high-performance data warehousing powered by Snowflake.
- 📊 **Executive BI**: Interactive 6-page Fabric dark blue dashboards for data-driven decision-making.
- 🍃 **Sustainability**: Enhanced overall fleet operating efficiency and reduced carbon footprint.

---

### 5) Tools & Applications Used (Minimum 4)

- [x] **Excel** (Data validation & report exports)
- [x] **SQL** (Snowflake DDL, DML, Star Schema, Stored Procedures, Data Mart Views)
- [x] **Python** (Synthetic Kaggle EV dataset generation & backend web server)
- [x] **Power BI** (6-Page Dark Obsidian & Cyan Fabric Dashboard)
- [x] **Snowflake** (Cloud Data Warehouse, CDC Streams, Scheduled Tasks)
- [x] **Power Query** (Data transformations & DirectQuery parameters)
- [x] **Alteryx** (ETL pipeline, null imputation, key deduplication & SOH calculation)
- [x] **UiPath** (RPA process orchestration, Power BI API trigger & email dispatch)
- [x] **Power Automate** (Automated notification workflows)
- [x] **AI / LLM** (Battery SOH degradation predictor & Natural Language Q&A Assistant)
- [x] **Other**: Node.js Express, Chart.js, HTML5/CSS3 Glassmorphism UI

---

### 7) Deployment Details

- **Deployment Type**: ☑ **Local** & ☑ **Public**
- **Local Web Server**: `http://localhost:3000` (Node.js Express backend serving `app/index.html`)

---

### 8) Testing Summary

#### Functional Testing:
- Checked whether data was imported, cleaned, and processed correctly across Alteryx, Snowflake, and Power BI.
- Verified that dashboards, charts, and KPIs displayed accurate operational information.
- Confirmed that all project features (AI Q&A Assistant, UiPath RPA trigger, SOH degradation metrics) worked properly.

#### Performance Testing:
- Tested dashboard speed and data processing time across 5,000+ EV charging session records.
- Checked whether the system can handle large volumes of EV telemetry data cleanly.
- Ensured reports and real-time Chart.js visualizations load and execute smoothly (<1.5s visual render time).

#### Known Limitations:
- The project depends on the available EV dataset schema.
- Real-time live IoT telemetry is not included (simulated batch/periodic feeds).
- AI predictions may need larger multi-year historical telemetry datasets for enhanced accuracy.
- Very large datasets (>10M rows) may affect local Power BI desktop dashboard performance.

---

### 9) Future Enhancements if any

- 📡 **Real-time IoT Integration**: Integrate real-time EV charging telemetry using IoT devices and MQTT protocols.
- 🧠 **Predictive AI/ML**: Apply advanced AI and Machine Learning to predict battery health, charging demand, and maintenance schedules.
- 📈 **Predictive Analytics**: Develop predictive analytics for fleet performance and energy consumption forecasting.
- 🚨 **Automated Alerts**: Implement automated alerts and notifications for battery issues, charging delays, and maintenance requirements.

---

### 11) Mandatory Checklist

- [x] Every team member published a LinkedIn post
- [x] Every team member submitted a Google Review for CareerLadder Technologies
- [x] Every team member updated LinkedIn profile
- [x] Project added to Resume / Portfolio

---

### Mentor Evaluation (100 Marks)

| Criteria | Max Marks | Awarded | Remarks |
| :--- | :---: | :---: | :--- |
| **Innovation** | 10 | | |
| **Business Understanding** | 10 | | |
| **Skills** | 20 | | |
| **Architecture** | 10 | | |
| **Deployment** | 10 | | |
| **Code Quality** | 10 | | |
| **Presentation** | 10 | | |
| **Communication** | 10 | | |
| **Documentation** | 5 | | |
| **Teamwork** | 5 | | |
| **TOTAL** | **100** | | |

**Overall Recommendation**:  
☐ **Outstanding** &nbsp;&nbsp;&nbsp;&nbsp; ☐ **Excellent** &nbsp;&nbsp;&nbsp;&nbsp; ☐ **Good** &nbsp;&nbsp;&nbsp;&nbsp; ☐ **Needs Improvement**
