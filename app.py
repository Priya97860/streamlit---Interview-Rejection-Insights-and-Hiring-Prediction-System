import streamlit as st
import pandas as pd
import random
import re
st.set_page_config(layout="wide")

# ---------------- SESSION ----------------

if "page" not in st.session_state:
    st.session_state.page = "login"

if "users" not in st.session_state:
    st.session_state.users = {}

if "score" not in st.session_state:
    st.session_state.score = 0


# ---------------- DOMAIN DATA ----------------

domain_roles = {

"IT":["Python Developer","Data Analyst","Web Developer"],

"Finance":["Accountant","Financial Analyst"],

"Banking":["Bank Clerk","Loan Officer"],

"Healthcare":["Nurse","Medical Assistant"],

"Retail":["Sales Executive","Store Manager"]

}


# ---------------- ROLE SKILLS ----------------

role_skills = {

"Python Developer":["Python","OOP","APIs","Git"],

"Data Analyst":["Python","SQL","Excel","Power BI"],

"Web Developer":["HTML","CSS","JavaScript"],

"Accountant":["Accounting","Tally","Excel"],

"Financial Analyst":["Finance","Excel","Statistics"],

"Bank Clerk":["Banking Basics","Customer Service"],

"Loan Officer":["Finance","Risk Analysis"],

"Nurse":["Patient Care","Medical Knowledge"],

"Medical Assistant":["Medical Support","Communication"],

"Sales Executive":["Sales","Communication","Negotiation"],

"Store Manager":["Management","Sales","Customer Handling"]

}


# ---------------- QUESTIONS ----------------
role_questions = {

"Python Developer":[
("What is Python?",["Programming Language","Database","OS","Browser"],"Programming Language"),
("Which keyword creates a function?",["def","function","create","lambda"],"def"),
("Which data type is immutable?",["Tuple","List","Dictionary","Set"],"Tuple"),
("Which library is used for data analysis?",["Pandas","Tkinter","Flask","Django"],"Pandas"),
("What does OOP stand for?",["Object Oriented Programming","Open Output Program","Object Output Process","None"],"Object Oriented Programming"),
("Which operator checks equality?",["==","=","!=","<"],"=="),
("Which symbol is used for comments?",["#","//","--","**"],"#"),
("Which keyword stops loop?",["break","stop","exit","halt"],"break"),
("Which keyword skips iteration?",["continue","skip","pass","next"],"continue"),
("Which function prints output?",["print()","show()","write()","display()"],"print()"),
("Which library creates graphs?",["Matplotlib","Tkinter","Flask","Django"],"Matplotlib"),
("Which keyword handles exception?",["try","handle","fix","catch"],"try"),
("Which block handles error?",["except","error","handle","fail"],"except"),
("Which module handles JSON?",["json","data","file","dict"],"json"),
("Which method adds element to list?",["append()","add()","insert()","push()"],"append()"),
("Which keyword defines class?",["class","object","define","create"],"class"),
("Which library is used for ML?",["Scikit-learn","Flask","Tkinter","Django"],"Scikit-learn"),
("Which keyword returns value?",["return","send","output","give"],"return"),
("Which library performs numerical computing?",["NumPy","Pandas","Flask","Tkinter"],"NumPy"),
("Which method removes list element?",["remove()","delete()","cut()","erase()"],"remove()"),
("Which loop iterates over sequence?",["for","while","loop","repeat"],"for"),
("Which keyword creates anonymous function?",["lambda","def","anon","func"],"lambda"),
("Which data type stores key-value?",["Dictionary","Tuple","Set","List"],"Dictionary"),
("Which module handles dates?",["datetime","date","calendar","time"],"datetime"),
("Which operator checks membership?",["in","==","!=","="],"in")
],

"Data Analyst":[
("Which tool is used for visualization?",["Power BI","Paint","Notepad","Word"],"Power BI"),
("Which language used for data analysis?",["Python","HTML","CSS","PHP"],"Python"),
("SQL is used for?",["Database Query","Design","Networking","Security"],"Database Query"),
("Excel formula for average?",["AVERAGE","SUM","COUNT","MAX"],"AVERAGE"),
("Which Python library analyzes data?",["Pandas","TensorFlow","Flask","Django"],"Pandas"),
("Which chart shows trend?",["Line Chart","Pie Chart","Bar Chart","Table"],"Line Chart"),
("Which SQL command retrieves data?",["SELECT","GET","SHOW","PULL"],"SELECT"),
("Which Excel formula counts cells?",["COUNT","SUM","AVERAGE","MAX"],"COUNT"),
("Which chart shows proportion?",["Pie Chart","Line Chart","Bar Chart","Scatter"],"Pie Chart"),
("Which language used for statistics?",["R","HTML","CSS","PHP"],"R"),
("Which library handles arrays?",["NumPy","Flask","Tkinter","Django"],"NumPy"),
("Which chart compares categories?",["Bar Chart","Pie Chart","Line Chart","Table"],"Bar Chart"),
("Which SQL clause filters rows?",["WHERE","FILTER","LIMIT","GROUP"],"WHERE"),
("Which Excel function finds maximum?",["MAX","SUM","COUNT","AVERAGE"],"MAX"),
("Which chart shows relationships?",["Scatter Plot","Pie Chart","Bar","Table"],"Scatter Plot"),
("Which process removes incorrect data?",["Data Cleaning","Coding","Testing","Debugging"],"Data Cleaning"),
("Which SQL clause groups rows?",["GROUP BY","ORDER BY","SORT","FILTER"],"GROUP BY"),
("Which Excel feature summarizes data?",["Pivot Table","Chart","Sort","Filter"],"Pivot Table"),
("Which Python library visualizes data?",["Matplotlib","Flask","Tkinter","Django"],"Matplotlib"),
("Which SQL clause sorts results?",["ORDER BY","GROUP BY","SORT","FILTER"],"ORDER BY"),
("Which tool handles big data?",["Python","Paint","Word","Notepad"],"Python"),
("Which chart compares multiple values?",["Bar Chart","Pie Chart","Table","Line"],"Bar Chart"),
("Which step interprets patterns?",["Data Analysis","Coding","Testing","Design"],"Data Analysis"),
("Which library creates interactive plots?",["Plotly","Flask","Tkinter","Django"],"Plotly"),
("Which SQL function counts rows?",["COUNT()","SUM()","AVG()","MAX()"],"COUNT()")
],

"Web Developer":[
("Which language structures web pages?",["HTML","Python","Java","C++"],"HTML"),
("Which language styles web pages?",["CSS","HTML","Python","Java"],"CSS"),
("Which language adds interactivity?",["JavaScript","HTML","CSS","SQL"],"JavaScript"),
("Which tag creates hyperlink?",["<a>","<p>","<img>","<div>"],"<a>"),
("Which CSS property changes text color?",["color","font","background","style"],"color"),
("Which tag inserts image?",["<img>","<picture>","<image>","<photo>"],"<img>"),
("Which method sends form data securely?",["POST","GET","PUT","DELETE"],"POST"),
("Which framework is JS based?",["React","Django","Flask","Laravel"],"React"),
("Which attribute links CSS file?",["href","src","link","style"],"href"),
("Which tag creates list?",["<ul>","<div>","<table>","<form>"],"<ul>"),
("Which protocol loads web pages?",["HTTP","FTP","SMTP","TCP"],"HTTP"),
("Which tag defines division?",["<div>","<span>","<section>","<box>"],"<div>"),
("Which CSS layout system?",["Flexbox","Grid","Float","All"],"All"),
("Which JS keyword declares variable?",["let","var","const","All"],"All"),
("Which HTML version latest?",["HTML5","HTML4","HTML3","HTML2"],"HTML5"),
("Which attribute used for image path?",["src","href","link","path"],"src"),
("Which tag creates table row?",["<tr>","<td>","<th>","<table>"],"<tr>"),
("Which tag creates form?",["<form>","<input>","<submit>","<button>"],"<form>"),
("Which database used with web apps?",["MySQL","Excel","Paint","Word"],"MySQL"),
("Which framework is Python based?",["Django","React","Angular","Vue"],"Django"),
("Which method updates data?",["PUT","GET","POST","FETCH"],"PUT"),
("Which tag defines header?",["<header>","<head>","<top>","<nav>"],"<header>"),
("Which tag defines footer?",["<footer>","<bottom>","<end>","<last>"],"<footer>"),
("Which CSS property controls layout?",["display","color","font","align"],"display"),
("Which tag creates input field?",["<input>","<text>","<enter>","<field>"],"<input>")
],

"Accountant":[
("Which statement shows financial position?",["Balance Sheet","Income Statement","Cash Flow","Ledger"],"Balance Sheet"),
("Which record tracks transactions?",["Ledger","Journal","Balance Sheet","Invoice"],"Ledger"),
("Which principle records revenue when earned?",["Accrual","Matching","Cost","Conservatism"],"Accrual"),
("Which account type is cash?",["Asset","Liability","Equity","Expense"],"Asset"),
("Which account shows company profit?",["Income Statement","Balance Sheet","Ledger","Journal"],"Income Statement"),
("Which record first captures transaction?",["Journal","Ledger","Trial Balance","Invoice"],"Journal"),
("Which statement shows cash movement?",["Cash Flow","Income Statement","Balance Sheet","Ledger"],"Cash Flow"),
("Which account type is loan?",["Liability","Asset","Equity","Revenue"],"Liability"),
("Which principle matches expenses with revenue?",["Matching","Accrual","Cost","Consistency"],"Matching"),
("Which book summarizes ledger balances?",["Trial Balance","Journal","Invoice","Receipt"],"Trial Balance"),
("Which account shows owner's interest?",["Equity","Asset","Expense","Revenue"],"Equity"),
("Which document records sales?",["Invoice","Receipt","Voucher","Ledger"],"Invoice"),
("Which statement reports profit?",["Income Statement","Balance Sheet","Cash Flow","Ledger"],"Income Statement"),
("Which tax applied to goods/services in India?",["GST","VAT","Service Tax","Income Tax"],"GST"),
("Which depreciation method spreads cost evenly?",["Straight Line","Reducing","Double","Sum"],"Straight Line"),
("Which account type is salary?",["Expense","Revenue","Asset","Equity"],"Expense"),
("Which document proves payment received?",["Receipt","Invoice","Voucher","Ledger"],"Receipt"),
("Which report lists assets/liabilities?",["Balance Sheet","Ledger","Journal","Trial Balance"],"Balance Sheet"),
("Which software used for accounting?",["Tally","Paint","Notepad","Word"],"Tally"),
("Which entry affects two accounts?",["Double Entry","Single Entry","Trial","Balance"],"Double Entry"),
("Which report checks ledger accuracy?",["Trial Balance","Invoice","Journal","Receipt"],"Trial Balance"),
("Which tax applies to income?",["Income Tax","GST","VAT","Service Tax"],"Income Tax"),
("Which account increases with debit?",["Asset","Revenue","Equity","Income"],"Asset"),
("Which account decreases with credit?",["Asset","Expense","Revenue","Income"],"Asset"),
("Which report used for auditing?",["Financial Statement","Invoice","Receipt","Voucher"],"Financial Statement")
],

"Financial Analyst":[
("Which statement shows company profitability?",["Income Statement","Balance Sheet","Ledger","Trial Balance"],"Income Statement"),
("Which ratio measures profitability?",["Net Profit Margin","Current Ratio","Debt Ratio","Quick Ratio"],"Net Profit Margin"),
("Which tool analysts use for financial modeling?",["Excel","Paint","Notepad","Word"],"Excel"),
("Which statement shows financial position?",["Balance Sheet","Income Statement","Cash Flow","Ledger"],"Balance Sheet"),
("Which ratio measures liquidity?",["Current Ratio","Profit Ratio","Equity Ratio","Debt Ratio"],"Current Ratio"),
("Which report tracks cash movement?",["Cash Flow Statement","Income Statement","Ledger","Journal"],"Cash Flow Statement"),
("Which valuation method uses future cash flows?",["DCF","NPV","IRR","ROI"],"DCF"),
("Which ratio measures debt level?",["Debt-to-Equity","Profit Margin","Return Ratio","Liquidity Ratio"],"Debt-to-Equity"),
("Which metric measures investment return?",["ROI","DCF","NPV","Payback"],"ROI"),
("Which analysis compares financial statements?",["Financial Analysis","Data Analysis","Market Research","Forecasting"],"Financial Analysis"),
("Which software used for financial analysis?",["Excel","Paint","Word","Notepad"],"Excel"),
("Which metric measures shareholder return?",["EPS","GDP","CPI","ROI"],"EPS"),
("Which market includes stocks trading?",["Stock Market","Bond Market","Forex","Commodity"],"Stock Market"),
("Which financial ratio measures efficiency?",["Asset Turnover","Debt Ratio","Profit Margin","Liquidity"],"Asset Turnover"),
("Which concept values money over time?",["Time Value of Money","Cash Flow","Liquidity","Budget"],"Time Value of Money"),
("Which tool forecasts financial trends?",["Financial Modeling","Accounting","Auditing","Taxing"],"Financial Modeling"),
("Which analysis evaluates company performance?",["Ratio Analysis","Market Analysis","Trend Study","Audit"],"Ratio Analysis"),
("Which metric measures company growth?",["Revenue Growth","Liquidity Ratio","Debt Ratio","Asset Ratio"],"Revenue Growth"),
("Which document shows company earnings?",["Income Statement","Ledger","Invoice","Trial Balance"],"Income Statement"),
("Which concept reduces future value?",["Discounting","Compounding","Forecasting","Budgeting"],"Discounting"),
("Which metric shows market value per share?",["EPS","ROI","DCF","NPV"],"EPS"),
("Which analysis studies market trends?",["Trend Analysis","Ratio Analysis","Risk Analysis","Audit"],"Trend Analysis"),
("Which indicator measures profitability?",["Gross Margin","Debt Ratio","Current Ratio","Liquidity"],"Gross Margin"),
("Which model predicts company performance?",["Financial Model","Accounting Model","Audit Model","Tax Model"],"Financial Model"),
("Which analysis compares competitors?",["Comparative Analysis","Ratio Analysis","Trend Analysis","Financial Audit"],"Comparative Analysis")
],

"Bank Clerk":[
("Which document opens bank account?",["KYC","Invoice","Receipt","Voucher"],"KYC"),
("Which account type earns interest?",["Savings Account","Current Account","Loan Account","Credit Account"],"Savings Account"),
("Which card withdraws cash?",["Debit Card","Credit Card","PAN Card","Aadhar"],"Debit Card"),
("Which system transfers money instantly?",["IMPS","Cheque","Draft","NEFT"],"IMPS"),
("Which document verifies identity?",["Aadhar","Invoice","Bill","Voucher"],"Aadhar"),
("Which system transfers money online?",["NEFT","Cash","Cheque","Draft"],"NEFT"),
("Which cheque crossing ensures safety?",["Account Payee","Bearer","Open","Blank"],"Account Payee"),
("Which account type businesses use?",["Current Account","Savings Account","Loan Account","Deposit"],"Current Account"),
("Which deposit locks money for period?",["Fixed Deposit","Savings","Recurring","Current"],"Fixed Deposit"),
("Which system transfers high value funds?",["RTGS","NEFT","Cheque","IMPS"],"RTGS"),
("Which bank document records transactions?",["Passbook","Invoice","Voucher","Ledger"],"Passbook"),
("Which number identifies bank branch?",["IFSC","PIN","OTP","MICR"],"IFSC"),
("Which service allows ATM withdrawal?",["Debit Card","Credit Card","Loan","Cheque"],"Debit Card"),
("Which bank exam recruits clerks?",["IBPS","UPSC","SSC","RRB"],"IBPS"),
("Which system used for cheque clearing?",["CTS","ATM","POS","NEFT"],"CTS"),
("Which code identifies bank globally?",["SWIFT","IFSC","PIN","MICR"],"SWIFT"),
("Which account has minimum balance rule?",["Savings","Loan","Credit","Fixed"],"Savings"),
("Which bank product gives interest income?",["Deposit","Loan","Card","Cheque"],"Deposit"),
("Which department handles cash?",["Teller","Manager","Audit","IT"],"Teller"),
("Which process verifies identity?",["KYC","GST","PAN","TDS"],"KYC"),
("Which device prints passbook?",["Passbook Printer","ATM","POS","Scanner"],"Passbook Printer"),
("Which system used for card payments?",["POS","ATM","NEFT","RTGS"],"POS"),
("Which number used for ATM security?",["PIN","OTP","IFSC","MICR"],"PIN"),
("Which account allows unlimited withdrawals?",["Current Account","Savings","Deposit","Loan"],"Current Account"),
("Which department approves loans?",["Loan Department","Audit","HR","IT"],"Loan Department")
],

"Loan Officer":[
("Which score checks creditworthiness?",["Credit Score","Salary","Balance","Tax"],"Credit Score"),
("Which document verifies income?",["Salary Slip","Invoice","Receipt","Voucher"],"Salary Slip"),
("Which loan used for house purchase?",["Home Loan","Car Loan","Personal Loan","Gold Loan"],"Home Loan"),
("Which loan used for vehicle purchase?",["Car Loan","Home Loan","Education Loan","Personal Loan"],"Car Loan"),
("Which document verifies identity?",["Aadhar","Invoice","Receipt","Voucher"],"Aadhar"),
("Which process evaluates borrower risk?",["Credit Assessment","Accounting","Audit","Forecasting"],"Credit Assessment"),
("Which loan requires collateral?",["Secured Loan","Unsecured Loan","Personal Loan","Education Loan"],"Secured Loan"),
("Which loan has no collateral?",["Unsecured Loan","Home Loan","Car Loan","Gold Loan"],"Unsecured Loan"),
("Which ratio measures repayment ability?",["Debt-to-Income","Profit Ratio","Liquidity Ratio","Asset Ratio"],"Debt-to-Income"),
("Which document verifies address?",["Utility Bill","Invoice","Receipt","Voucher"],"Utility Bill"),
("Which loan used for studies?",["Education Loan","Car Loan","Home Loan","Gold Loan"],"Education Loan"),
("Which interest type remains constant?",["Fixed Interest","Variable Interest","Floating","Market"],"Fixed Interest"),
("Which interest changes with market?",["Floating Interest","Fixed Interest","Stable","Constant"],"Floating Interest"),
("Which department approves loan?",["Credit Department","Audit","HR","IT"],"Credit Department"),
("Which bank evaluates collateral value?",["Loan Officer","Auditor","Cashier","Manager"],"Loan Officer"),
("Which term refers repayment period?",["Tenure","Interest","Principal","Balance"],"Tenure"),
("Which fee charged for loan processing?",["Processing Fee","Interest","Tax","Penalty"],"Processing Fee"),
("Which report checks borrower history?",["Credit Report","Bank Report","Ledger","Trial Balance"],"Credit Report"),
("Which document proves property ownership?",["Property Deed","Invoice","Receipt","Voucher"],"Property Deed"),
("Which loan secured by gold?",["Gold Loan","Car Loan","Personal Loan","Education Loan"],"Gold Loan"),
("Which system calculates EMI?",["Loan Calculator","Excel","POS","ATM"],"Loan Calculator"),
("Which factor affects interest rate?",["Credit Score","Name","Age","Gender"],"Credit Score"),
("Which document confirms loan agreement?",["Loan Agreement","Invoice","Receipt","Voucher"],"Loan Agreement"),
("Which bank checks legal documents?",["Legal Department","Audit","HR","IT"],"Legal Department"),
("Which step finalizes loan approval?",["Sanction","Review","Check","Apply"],"Sanction")
],

"Nurse":[
("Which device measures blood pressure?",["Sphygmomanometer","Thermometer","Stethoscope","ECG"],"Sphygmomanometer"),
("Which organ pumps blood?",["Heart","Liver","Lung","Kidney"],"Heart"),
("Which vitamin strengthens bones?",["Vitamin D","Vitamin C","Vitamin B","Vitamin A"],"Vitamin D"),
("Which device measures body temperature?",["Thermometer","ECG","X-ray","BP Machine"],"Thermometer"),
("Which organ filters blood?",["Kidney","Heart","Liver","Lung"],"Kidney"),
("Which test measures blood sugar?",["Glucose Test","ECG","X-ray","MRI"],"Glucose Test"),
("Which infection control method?",["Hand Washing","Injection","Bandage","Medicine"],"Hand Washing"),
("Which injection given in muscle?",["Intramuscular","Intravenous","Subcutaneous","Oral"],"Intramuscular"),
("Which injection given in vein?",["Intravenous","Intramuscular","Oral","Topical"],"Intravenous"),
("Which device listens heart sound?",["Stethoscope","Thermometer","BP Machine","X-ray"],"Stethoscope"),
("Which blood cells fight infection?",["WBC","RBC","Platelets","Plasma"],"WBC"),
("Which blood cells carry oxygen?",["RBC","WBC","Platelets","Plasma"],"RBC"),
("Which blood component helps clotting?",["Platelets","RBC","WBC","Plasma"],"Platelets"),
("Which test records heart activity?",["ECG","X-ray","MRI","CT"],"ECG"),
("Which organ helps breathing?",["Lungs","Heart","Kidney","Liver"],"Lungs"),
("Which disease caused by high sugar?",["Diabetes","Asthma","Cancer","Flu"],"Diabetes"),
("Which device measures oxygen?",["Pulse Oximeter","Thermometer","ECG","BP"],"Pulse Oximeter"),
("Which fluid prevents dehydration?",["IV Fluid","Blood","Saline","Medicine"],"IV Fluid"),
("Which patient care includes hygiene?",["Nursing Care","Medical Care","Surgery","Diagnosis"],"Nursing Care"),
("Which vaccine prevents TB?",["BCG","Polio","MMR","Hepatitis"],"BCG"),
("Which vitamin improves immunity?",["Vitamin C","Vitamin D","Vitamin A","Vitamin B"],"Vitamin C"),
("Which body organ detoxifies blood?",["Liver","Kidney","Heart","Lungs"],"Liver"),
("Which infection spreads through air?",["Tuberculosis","Diabetes","Cancer","Fracture"],"Tuberculosis"),
("Which department treats emergency?",["ER","OPD","ICU","Ward"],"ER"),
("Which nurse monitors critical patients?",["ICU Nurse","Ward Nurse","Clinic Nurse","Lab Nurse"],"ICU Nurse")
],

"Sales Executive":[
("Which process identifies potential customers?",["Lead Generation","Marketing","Promotion","Advertising"],"Lead Generation"),
("Which skill convinces customers?",["Communication","Coding","Design","Testing"],"Communication"),
("Which tool manages customers?",["CRM","ERP","POS","ATM"],"CRM"),
("Which process closes sales deal?",["Closing","Opening","Pitch","Promotion"],"Closing"),
("Which stage explains product?",["Presentation","Prospecting","Closing","Follow-up"],"Presentation"),
("Which strategy increases sales?",["Promotion","Coding","Design","Testing"],"Promotion"),
("Which method builds customer relationship?",["Follow-up","Ignore","Delay","Reject"],"Follow-up"),
("Which metric measures sales success?",["Revenue","Design","Coding","Testing"],"Revenue"),
("Which stage identifies prospects?",["Prospecting","Closing","Follow-up","Presentation"],"Prospecting"),
("Which strategy offers discounts?",["Sales Promotion","Advertising","Branding","Marketing"],"Sales Promotion"),
("Which skill handles objections?",["Negotiation","Coding","Testing","Design"],"Negotiation"),
("Which process studies market?",["Market Research","Accounting","Auditing","Forecasting"],"Market Research"),
("Which method builds trust?",["Customer Service","Promotion","Design","Coding"],"Customer Service"),
("Which system tracks leads?",["CRM","ERP","POS","ATM"],"CRM"),
("Which metric measures profit?",["Profit Margin","Coding","Design","Testing"],"Profit Margin"),
("Which technique persuades buyers?",["Sales Pitch","Coding","Design","Testing"],"Sales Pitch"),
("Which strategy increases brand awareness?",["Advertising","Coding","Design","Testing"],"Advertising"),
("Which method improves retention?",["Customer Support","Coding","Testing","Design"],"Customer Support"),
("Which process analyzes sales data?",["Sales Analysis","Coding","Design","Testing"],"Sales Analysis"),
("Which technique attracts new customers?",["Lead Generation","Coding","Design","Testing"],"Lead Generation"),
("Which strategy offers bundle deals?",["Bundling","Coding","Testing","Design"],"Bundling"),
("Which metric tracks growth?",["Sales Growth","Coding","Testing","Design"],"Sales Growth"),
("Which approach focuses on customer needs?",["Consultative Selling","Hard Selling","Cold Selling","Direct Selling"],"Consultative Selling"),
("Which process improves conversion rate?",["Sales Funnel Optimization","Coding","Testing","Design"],"Sales Funnel Optimization"),
("Which step maintains long-term clients?",["Relationship Management","Promotion","Design","Coding"],"Relationship Management")
],
"Medical Assistant":[
("What is HIPAA compliance?",["Health Privacy Act","Hardware Protocol","None","Coding"],"Health Privacy Act"),
("Which instrument measures blood pressure?",["Sphygmomanometer","Thermometer","Oximeter","Scale"],"Sphygmomanometer"),
("First aid includes?",["CPR, Bandaging, Shock care","Cooking","Coding","Networking"],"CPR, Bandaging, Shock care"),
("Patient record management is?",["Recording & maintaining patient data","Deleting files","Gaming","Design"],"Recording & maintaining patient data"),
("Which vitamin helps in clotting?",["Vitamin K","Vitamin A","Vitamin C","Vitamin D"],"Vitamin K"),
("Which device measures oxygen level?",["Pulse Oximeter","Stethoscope","Thermometer","Glucose meter"],"Pulse Oximeter"),
("Injection safety requires?",["Sterile techniques","Coding","Gaming","Design"],"Sterile techniques"),
("What is infection control?",["Preventing infections","Designing apps","Networking","Gaming"],"Preventing infections"),
("Medical assistant role in lab?",["Collect sample & record results","Coding","Gaming","Design"],"Collect sample & record results"),
("Which route is used for insulin?",["Subcutaneous","Oral","Intravenous","Topical"],"Subcutaneous"),
("Patient confidentiality means?",["Keep info private","Share freely","Post online","Ignore"],"Keep info private"),
("Which part of the body is gluteus?",["Buttocks","Arm","Leg","Head"],"Buttocks"),
("Which blood type is universal donor?",["O negative","A positive","B positive","AB negative"],"O negative"),
("Normal body temperature?",["36.5-37.5°C","35°C","40°C","38°C"],"36.5-37.5°C"),
("Normal adult pulse?",["60-100 bpm","30-50 bpm","120-150 bpm","110-130 bpm"],"60-100 bpm"),
("Sterilization methods include?",["Autoclaving, Boiling, Chemical","Cooking","Coding","Design"],"Autoclaving, Boiling, Chemical"),
("What is aseptic technique?",["Prevent contamination","Delete files","Gaming","Design"],"Prevent contamination"),
("What is CPR?",["Cardiopulmonary Resuscitation","Coding","Gaming","Networking"],"Cardiopulmonary Resuscitation"),
("Medical chart contains?",["Patient history & vitals","Coding","Gaming","Design"],"Patient history & vitals"),
("Which PPE is used for airborne disease?",["N95 Mask","Gloves","Apron","Hat"],"N95 Mask"),
("What is triage?",["Prioritizing patients by severity","Coding","Gaming","Networking"],"Prioritizing patients by severity"),
("Which device checks blood sugar?",["Glucometer","Thermometer","Pulse Oximeter","Scale"],"Glucometer"),
("What is patient advocacy?",["Support & protect patient's rights","Ignore patient","Delete data","Coding"],"Support & protect patient's rights"),
("Which vitamin prevents rickets?",["Vitamin D","Vitamin K","Vitamin A","Vitamin C"],"Vitamin D"),
("Which organ produces insulin?",["Pancreas","Liver","Heart","Kidney"],"Pancreas"),
("Which solution is used for disinfecting?",["Alcohol, Bleach","Water","Oil","Cooking"],"Alcohol, Bleach")
],


"Store Manager":[
("What is inventory management?",["Tracking stock & orders","Coding","Gaming","Design"],"Tracking stock & orders"),
("What is SWOT analysis?",["Strengths, Weaknesses, Opportunities, Threats","Coding","Gaming","Networking"],"Strengths, Weaknesses, Opportunities, Threats"),
("How to improve customer satisfaction?",["Feedback & service quality","Ignore customers","Coding","Design"],"Feedback & service quality"),
("Which KPI measures sales?",["Revenue & Profit","Temperature","Pulse","Design"],"Revenue & Profit"),
("How to handle staff conflict?",["Mediate & resolve","Ignore","Shout","Fire them"],"Mediate & resolve"),
("Budget planning includes?",["Forecasting & allocation","Coding","Gaming","Design"],"Forecasting & allocation"),
("What is FIFO?",["First In First Out","Coding","Gaming","Networking"],"First In First Out"),
("What is shrinkage in retail?",["Loss of inventory","Gaming","Coding","Networking"],"Loss of inventory"),
("Customer complaints handled by?",["Service desk & manager","Coding","Gaming","Networking"],"Service desk & manager"),
("Daily sales report includes?",["Sales & returns","Coding","Gaming","Networking"],"Sales & returns"),
("What is merchandising?",["Display & promote products","Ignore","Coding","Gaming"],"Display & promote products"),
("What is cross-selling?",["Sell related products","Ignore","Coding","Gaming"],"Sell related products"),
("Store layout helps?",["Smooth customer flow","Confuse customers","Coding","Gaming"],"Smooth customer flow"),
("What is POS system?",["Point of Sale system","Password system","Design system","Networking"],"Point of Sale system"),
("How to manage inventory shortage?",["Reorder & track","Ignore","Coding","Gaming"],"Reorder & track"),
("Staff scheduling ensures?",["Adequate coverage & fairness","Ignore","Coding","Gaming"],"Adequate coverage & fairness"),
("How to increase footfall?",["Promotions & marketing","Ignore","Coding","Gaming"],"Promotions & marketing"),
("What is KPI?",["Key Performance Indicator","Knowledge Performance Indicator","None","Coding"],"Key Performance Indicator"),
("Sales forecasting helps?",["Plan stock & orders","Ignore","Gaming","Coding"],"Plan stock & orders"),
("Loss prevention includes?",["Security & audit","Coding","Ignore","Gaming"],"Security & audit"),
("Customer retention means?",["Loyal customers","New customers","Ignore","Coding"],"Loyal customers"),
("Which leadership style is best?",["Transformational","Autocratic","Laissez-faire","None"],"Transformational"),
("How to resolve vendor issues?",["Negotiation & contract management","Ignore","Coding","Gaming"],"Negotiation & contract management"),
("Which financial report is essential?",["P&L Statement","Temperature report","Gaming report","None"],"P&L Statement"),
("Staff training includes?",["Product knowledge & service skills","Ignore","Coding","Gaming"],"Product knowledge & service skills")
],

}

# ---------------- LOGIN PAGE ----------------

if st.session_state.page == "login":

    st.title("Interview Hiring Prediction System")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    if col1.button("Login"):

        if username in st.session_state.users and st.session_state.users[username] == password:

            st.success("Login Successful")

            st.session_state.page = "domain"
            st.rerun()

        else:

            st.error("Invalid Username or Password")

    if col2.button("Register"):

        st.session_state.page = "register"
        st.rerun()

import re

# Password validation function
def strong_password(password):

    pattern = r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

    if re.match(pattern, password):
        return True
    else:
        return False


# ---------------- REGISTER PAGE ----------------

if st.session_state.page == "register":

    st.title("User Registration")

    new_user = st.text_input("Enter Username")

    new_pass = st.text_input("Enter Password", type="password")

    st.info("Password must contain:\n• Minimum 8 characters\n• 1 Alphabet\n• 1 Number\n• 1 Special Character")


    if st.button("Register User"):

        if new_user == "" or new_pass == "":
            st.warning("Please enter username and password")

        elif new_user in st.session_state.users:
            st.warning("Username already exists")

        elif not strong_password(new_pass):
            st.warning("⚠ Password must contain minimum 8 characters, 1 alphabet, 1 number and 1 special character")

        else:
            st.session_state.users[new_user] = new_pass
            st.success("Account Created Successfully")


    if st.button("Back to Login"):

        st.session_state.page = "login"
        st.rerun()

# ---------------- DOMAIN PAGE ----------------
elif st.session_state.page == "domain":

    st.title("Select Domain")

    domain = st.selectbox("Choose Domain", list(domain_roles.keys()))

    role = st.selectbox("Job Role", domain_roles[domain])

    skills = st.multiselect("Role Skills", role_skills[role])

    if st.button("Start Mock Test"):

        st.session_state.role = role
        st.session_state.page = "mock"
        st.rerun()


# ---------------- MOCK TEST ----------------

elif st.session_state.page == "mock":

    st.title("Mock Interview Test")
    st.info("""
📌 **Mock Interview Instructions**

• Total Questions : 25  
• Each Question : 10 Marks  
• Total Marks : 250  
• Pass Mark : 150  
• Minimum 15 Correct Answers Required to Pass
""")

    role = st.session_state.role

    # Generate questions only once
    if "mock_questions" not in st.session_state:
        st.session_state.mock_questions = random.sample(role_questions[role], 25)

    questions = st.session_state.mock_questions


    for i, (q, opts, correct) in enumerate(questions):

        st.radio(
            f"Q{i+1}. {q}",
            opts,
            index=None,
            key=f"q{i}"
        )


    if st.button("Submit Test"):

        score = 0
        unanswered = 0
        results = []

        for i, (q, opts, correct) in enumerate(questions):

            user_ans = st.session_state.get(f"q{i}")

            if user_ans is None:
                unanswered += 1

            elif user_ans == correct:
                score += 10
                results.append((i+1, True, correct))

            else:
                results.append((i+1, False, correct))


        if unanswered > 0:
            st.warning(f"⚠ Please answer all questions before submitting. {unanswered} question(s) left.")

        else:
            st.session_state.score = score
            st.session_state.results = results

            del st.session_state.mock_questions

            st.session_state.page = "dashboard"
            st.rerun()


# ---------------- DASHBOARD ----------------

elif st.session_state.page == "dashboard":

    st.title("Interview Result")

    score = st.session_state.score

    st.subheader("Your Interview Score")
    st.write(score)

    # ---------------- PASS / FAIL MESSAGE ----------------

    if score >= 150:
        st.success("🎉 Congratulations! You Passed the Mock Interview")
    else:
        st.error("❌ Sorry! You did not reach the pass mark (150). Try Again!")

    # ---------------- ANSWER ANALYSIS ----------------

    results = st.session_state.results

    st.subheader("Answer Analysis")

    for qno, status, correct in results:

        if status:
            st.success(f"Q{qno} ✔ Correct")
        else:
            st.error(f"Q{qno} ❌ Wrong (Correct answer: {correct})")


    # ---------------- Result Chart ----------------

    if score >= 150:
        selected = 1
        rejected = 0
    else:
        selected = 0
        rejected = 1


    result_data = pd.DataFrame({
        "Result": ["Selected", "Rejected"],
        "Count": [selected, rejected]
    })

    st.subheader("Hiring Result Chart")
    st.bar_chart(result_data.set_index("Result"))


    # ---------------- Yearwise Hiring Trend ----------------

    trend_data = pd.DataFrame({
        "Year": [2022, 2023, 2024, 2025],
        "Selected": [80, 120, 150, 170],
        "Rejected": [200, 180, 160, 140]
    })

    st.subheader("Yearwise Hiring Trend")
    st.line_chart(trend_data.set_index("Year"))


    # ---------------- Rejection Reasons ----------------

    rejection_data = pd.DataFrame({
        "Reason": [
            "Low Interview Score",
            "Lack of Technical Skills",
            "Poor Communication",
            "Experience Mismatch"
        ],
        "Count": [45, 30, 20, 15]
    })

    st.subheader("Top Rejection Reasons")
    st.bar_chart(rejection_data.set_index("Reason"))


    st.divider()


    # Go to prediction page
    if st.button("Go To Prediction"):

        st.session_state.page = "prediction"
        st.rerun()

# ---------------- PREDICTION PAGE ----------------

elif st.session_state.page == "prediction":

    st.title("Prediction Result")

    score = st.session_state.get("score", 0)

    st.write("Your Interview Score:", score)

    if score >= 150:
        st.success("Prediction Result: Selected")
        st.write("Probability: 85%")
        st.write("Suggestion: Good performance. Keep improving your technical depth.")
    else:
        st.error("Prediction Result: Rejected")
        st.write("Probability: 35%")
        st.write("Suggestion: Improve core concepts and practice more interviews.")

    st.divider()

    # Back button
    if st.button("🔄 Take Another Test"):
        st.session_state.score = 0
        st.session_state.page = "domain"
        st.rerun()
