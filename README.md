# DevinSom-CloudAutomationCostSavings 💰

## 🌩️ Overview
This project automates AWS cost savings by detecting **idle EC2 instances** and **unattached EBS volumes**.  
It uses **AWS Lambda**, **EventBridge (Scheduler)**, and **CloudWatch** to run daily scans and identify unused resources that can be shut down to reduce costs.

---

## 🧠 Problem Solved
Many organizations waste cloud budget on idle compute and storage.  
This automation identifies those unused resources automatically and creates a daily report — helping to **reduce unnecessary AWS billing**.

---

## 🏗️ Architecture
**Services Used:**
- **AWS Lambda** – Runs a Python script that scans EC2 instances for idle status.  
- **Amazon EventBridge (Scheduler)** – Triggers the Lambda function daily at a set time.  
- **Amazon CloudWatch** – Logs each run’s results for cost monitoring and auditing.  
- *(Optional)* **Amazon SNS** – Sends email alerts when idle resources are found.

**Workflow:**
1. EventBridge triggers the Lambda function daily.  
2. Lambda checks for idle EC2 instances and unattached EBS volumes.  
3. Results are logged in CloudWatch (and optionally sent via SNS email).  

---

## 🧰 Technologies
- AWS Lambda (Python 3.12)
- Amazon EventBridge
- Amazon CloudWatch
- AWS IAM Roles & Permissions
- *(Optional)* Amazon SNS for alerts
- View the full automation code here: [idle_resource_cleaner.py](./idle_resource_cleaner.py)

---

## 🧪 How It Works
1. Lambda scans AWS EC2 for stopped or idle instances.  
2. If idle resources exist, it logs them in CloudWatch.  
3. Scheduler (EventBridge) runs this check automatically every 24 hours.  
4. Results can be extended to email alerts or dashboards.

---

## 📸 Screenshots
Include screenshots of:
- Lambda test result  
- EventBridge schedule page  
- CloudWatch log output  

---

## 📈 Impact
✅ Automated detection of unused AWS resources  
✅ Reduced potential monthly costs  
✅ Demonstrated knowledge of **FinOps and Cloud Automation** principles  

---

## 🚀 Future Enhancements
- Add SNS email alerts for daily summaries  
- Expand to monitor S3, RDS, and Lambda costs  
- Integrate data into an S3 dashboard for visualization  

---

## 👤 Author
**Devin Som**  
Information Technology Student | Cloud Computing Enthusiast  
[Portfolio Website](https://devinsom.github.io/DevinSom-portfolio) • [LinkedIn](https://www.linkedin.com/in/devinsom)
