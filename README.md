# 🚌 RedBus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## 📋 Project Overview
The **RedBus Data Scraping and Filtering Application** is designed to extract, analyze, and visualize real-time bus travel information from [RedBus](https://www.redbus.in/).  
This project automates data extraction using **Selenium**, stores it in a **SQL database**, and builds an **interactive Streamlit app** for dynamic filtering and analysis.  

It aims to support **travel aggregators**, **transport agencies**, and **analysts** in understanding travel patterns, pricing trends, and seat availability.

---

## 🎯 Objectives
- Automate extraction of **bus route data** from RedBus using **Selenium**.
- Store the scraped data in a **structured SQL database**.
- Build a **Streamlit web application** for real-time data filtering and visualization.
- Enable filtering by **bus type, route, price range, rating, and seat availability**.

---

## 🧠 Skills & Technologies
| Category | Tools/Technologies |
|-----------|--------------------|
| **Programming** | Python |
| **Web Scraping** | Selenium |
| **Frontend / Visualization** | Streamlit |
| **Database** | SQLite / SQL |
| **Data Handling** | Pandas |
| **Domain** | Transportation |

---

## 🏢 Domain
**Transportation and Travel Analytics**

---

## 🚧 Problem Statement
The project aims to simplify and automate the process of collecting and analyzing bus travel data from RedBus.  
By integrating **web scraping**, **database management**, and **interactive dashboards**, it helps stakeholders:
- Compare pricing across operators.
- Track seat availability trends.
- Perform competitor and market analysis.
- Improve data-driven decision-making in the transport sector.

---

## 💼 Business Use Cases
| Use Case | Description |
|-----------|-------------|
| **Travel Aggregators** | Show real-time bus schedules and seat availability. |
| **Market Analysis** | Understand route popularity, price trends, and service quality. |
| **Customer Service** | Suggest personalized bus options for customers. |
| **Competitor Analysis** | Compare operators’ pricing, ratings, and timing. |

---

## ⚙️ Approach

### 1️⃣ Data Scraping using Selenium
- Automate browser interaction to navigate the RedBus website.
- Extract data fields such as bus name, type, timing, price, rating, and seat availability.
- Scrape multiple routes (including state transport and private buses).

### 2️⃣ Data Storage using SQL
- Store structured data in a relational database (`redbus.db`).
- Database schema designed for efficient querying and filtering.

### 3️⃣ Streamlit Application
- Load the SQL data into Streamlit using Pandas.
- Implement interactive filters:
  - Bus Type
  - Route
  - Price Range
  - Star Rating
  - Seat Availability
- Display filtered data and basic visualizations.

### 4️⃣ Data Filtering & Visualization
- Users can dynamically query data using Streamlit filters.
- Interactive charts showing:
  - Average price by route
  - Top bus operators by frequency

---

## 🧩 Database Schema

**Table Name:** `bus_routes`

| Column Name | Data Type | Description |
|--------------|------------|-------------|
| id | INTEGER (PK) | Auto-increment primary key |
| route_name | TEXT | Route name (From–To) |
| route_link | TEXT | URL for the route on RedBus |
| busname | TEXT | Bus/Operator name |
| bustype | TEXT | Bus type (Sleeper/Seater/AC/Non-AC) |
| departing_time | TEXT | Departure time |
| duration | TEXT | Total travel duration |
| reaching_time | TEXT | Arrival time |
| star_rating | REAL | Average passenger rating |
| price | REAL | Ticket price |
| seats_available | INTEGER | Available seat count |

---

## 🧾 Dataset Description
**Source:** [RedBus Official Website](https://www.redbus.in/)  
**Format:** Data scraped and stored in a **SQL database**.  

**Fields collected:**
- Bus Route Name & Link  
- Bus Name / Operator  
- Bus Type (Sleeper / Seater / AC / Non-AC)  
- Departing & Reaching Time  
- Duration  
- Star Rating  
- Price  
- Seat Availability  

---

## 🛠️ Project Deliverables
1. ✅ **Python Script** for data scraping (`scraper.py`)
2. ✅ **SQL Schema** for database creation (`db_setup.py`)
3. ✅ **Streamlit Application** (`streamlit_app.py`)
4. ✅ **Database File** (`redbus.db`)
5. ✅ **Documentation** (`README.md`)
6. ✅ **Screenshots / Video** of the working app

---

## 🧪 Project Evaluation Metrics
| Metric | Description |
|---------|-------------|
| **Scraping Accuracy** | Correctness and completeness of data scraped |
| **Database Design** | Proper relational schema and indexing |
| **Application Usability** | User-friendliness of Streamlit interface |
| **Filter Functionality** | Responsiveness and accuracy of filters |
| **Code Quality** | Modularity, readability, and adherence to PEP8 |

---

## 🚀 How to Run the Project

### 🔧 Step 1: Install Dependencies
```bash
pip install -r requirements.txt

### To Launch The Streamlitt App
streamlit run streamlit_app.py

### 📊 Sample Output (Streamlit)
Interactive filters for:

Bus Type

Route
> Price Range
> Star Rating
> Seat Availability

Charts:
> Average Price by Route

> Top Bus Operators by Count

> Download Filtered Data as CSV
