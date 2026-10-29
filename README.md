# Supply-Chain-SQL-Analytics
Analyzing freight delays and supply chain bottlenecks using the DataCo dataset (SQL &amp; Python).
# 🚚 Smart Supply Chain Analytics: Identifying Freight Bottlenecks

## 📌 Project Overview
As a Transportation Engineering MSc candidate, I built this project to analyze real-world logistics data and identify the root causes of freight delays. Using the DataCo Smart Supply Chain dataset (180,000+ registered orders), I engineered a local SQLite database and wrote advanced SQL queries to extract actionable business insights regarding delivery performance.

## 🛠️ Tech Stack
* **Database:** SQLite
* **Data Manipulation & Scripting:** Python (Pandas, sqlite3)
* **Analytics:** SQL (Aggregation, CASE statements, Subqueries)

## 📊 Key Business Insights Discovered
By analyzing the historical shipping data, I identified critical inefficiencies in the supply chain:

1. **Massive Late Delivery Volume:** Out of the total dataset, over **98,900 shipments** were flagged as late deliveries, indicating a systemic issue in routing or scheduling.
2. **High-Risk Product Categories:** By comparing scheduled transit times versus actual transit times, I identified the top 5 product categories causing the worst delays. 
   * **Soccer Equipment** averages a delay of **1.87 days** past the scheduled arrival.
   * **As Seen on TV!** and **Women's Golf Clubs** average delays of **1.79** and **1.75 days**, respectively.

## 💻 Sample SQL Methodology
To extract the product category risks, I utilized the following SQL logic to calculate the exact average delay in days:

```sql
SELECT 
    Category_Name,
    AVG(Days_for_shipping_real) as Avg_Actual_Days,
    AVG(Days_for_shipment_scheduled) as Avg_Scheduled_Days,
    ROUND(AVG(Days_for_shipping_real - Days_for_shipment_scheduled), 2) as Avg_Days_Delayed
FROM shipments
WHERE Delivery_Status = 'Late delivery'
GROUP BY Category_Name
ORDER BY Avg_Days_Delayed DESC
LIMIT 5;
