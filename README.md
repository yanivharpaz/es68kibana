# Elasticsearch 6.8 + Kibana 6.8 with Python Data Streamer

This project sets up a local Elasticsearch 6.8 and Kibana 6.8 development environment using Docker Compose, and streams synthetic data over the past 60 days using Python. It’s ideal for building and testing dashboards in Kibana.

---

## 📦 Project Structure

```
.
├── docker-compose.yml     # Elasticsearch + Kibana setup
├── stream_data.py         # Python script to generate and insert data
├── README.md              # You're here!
```

---

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-org/es68-kibana-stream.git
cd es68-kibana-stream
```

---

### 2. Start Elasticsearch and Kibana

```bash
docker-compose up
```

- Elasticsearch: [http://localhost:9200](http://localhost:9200)
- Kibana: [http://localhost:5601](http://localhost:5601)

> ⏳ **Note:** It may take up to a minute for Elasticsearch and Kibana to fully initialize.

---

### 3. Install Python Dependencies

Create a virtual environment and install the Elasticsearch client:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install elasticsearch==7.13.4
```

---

### 4. Stream Synthetic Data

Run the Python script to generate and index 60 days of synthetic data (~500 documents per day):

```bash
python stream_data.py
```

This script will:
- Create an index called `product-events`
- Generate ~30,000 synthetic documents
- Randomly assign 3 values for `ProductSource` and 8 for `ProductType`
- Evenly distribute timestamps across the past 60 days

---

## 📊 Building Dashboards in Kibana

After the data is ingested:

1. Open Kibana at [http://localhost:5601](http://localhost:5601)
2. Navigate to **Stack Management > Index Patterns**
3. Create a new index pattern:
   - **Index name:** `product-events`
   - **Timestamp field:** `timestamp`
4. Explore visualizations under **Dashboard > Create new dashboard**:
   - Bar chart of `ProductType` counts
   - Pie chart by `ProductSource`
   - Time series of `Amount` or `UnitsSold`

---

## 🔧 Tech Stack

- **Elasticsearch** 6.8.23
- **Kibana** 6.8.23
- **Python** 3.7+ (tested with 3.10)
- **Elasticsearch Python Client** 7.13.4 (compatible with ES 6.8)

---

## 🧹 Cleanup

To stop and remove containers and associated volumes:

```bash
docker-compose down -v
```

---

## 📄 License

MIT License. Feel free to use and modify as needed.

---

## 💬 Questions?

Feel free to open an issue or contact the maintainer for enhancements, questions, or continuous data streaming options.
