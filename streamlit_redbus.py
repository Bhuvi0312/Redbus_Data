import streamlit as st
import pandas as pd

# ✅ Must be the very first Streamlit command
st.set_page_config(page_title="Redbus Data Explorer", layout="wide")

# Load data
@st.cache_data
def load_data():
    bus = pd.read_csv("C:\\Users\\bhuva\\Downloads\\project_redbus-main\\project_redbus-main\\bus_data10.csv")
    route = pd.read_csv("C:\\Users\\bhuva\\Downloads\\project_redbus-main\\project_redbus-main\\route_data10.csv")
    # Merge bus + route
    merged = pd.merge(bus, route, left_on="bus_no", right_on="route_no", how="left")
    return merged

df = load_data()

# ---------------- UI ----------------
st.title("🚌 Redbus Data Explorer")
st.markdown("Explore bus & route details with filters and insights")

# Sidebar filters
st.sidebar.header("🔎 Filters")

route_filter = st.sidebar.multiselect(
    "Select Route", options=df["route_name"].dropna().unique()
)

state_filter = st.sidebar.multiselect(
    "Select State", options=df["state_name"].dropna().unique()
)

bus_type_filter = st.sidebar.multiselect(
    "Select Bus Type", options=df["bus_type"].dropna().unique()
)

rating_filter = st.sidebar.slider(
    "Minimum Star Rating", min_value=0.0, max_value=5.0, value=0.0, step=0.1
)

price_filter = st.sidebar.slider(
    "Price Range",
    min_value=int(df["price"].min()),
    max_value=int(df["price"].max()),
    value=(int(df["price"].min()), int(df["price"].max())),
)

# ---------------- Apply Filters ----------------
filtered_df = df.copy()

if route_filter:
    filtered_df = filtered_df[filtered_df["route_name"].isin(route_filter)]
if state_filter:
    filtered_df = filtered_df[filtered_df["state_name"].isin(state_filter)]
if bus_type_filter:
    filtered_df = filtered_df[filtered_df["bus_type"].isin(bus_type_filter)]
if rating_filter > 0:
    filtered_df = filtered_df[filtered_df["star_rating"] >= rating_filter]

filtered_df = filtered_df[
    (filtered_df["price"] >= price_filter[0]) & (filtered_df["price"] <= price_filter[1])
]

# ---------------- Results ----------------
st.subheader("📊 Filtered Results")
st.write(f"Total Results: {len(filtered_df)}")
st.dataframe(filtered_df)

# ---------------- Insights ----------------
st.subheader("📈 Insights")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**Bus Type Distribution**")
    st.bar_chart(filtered_df["bus_type"].value_counts())

with col2:
    st.markdown("**Average Price by State**")
    st.bar_chart(filtered_df.groupby("state_name")["price"].mean())

# ---------------- Seat Availability ----------------
st.subheader("💺 Seat Availability Insights")

col3, col4 = st.columns(2)
with col3:
    st.markdown("**Total Seats by Bus Type**")
    seats_by_type = filtered_df.groupby("bus_type")["seat_availability"].sum()
    st.bar_chart(seats_by_type)

with col4:
    st.markdown("**Top 10 Routes by Seat Availability**")
    seats_by_route = (
        filtered_df.groupby("route_name")["seat_availability"].sum().nlargest(10)
    )
    st.bar_chart(seats_by_route)