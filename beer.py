import streamlit as st
import pandas as pd
import altair as alt

# 1. Page Configuration & Setup
st.set_page_config(
    page_title="African Beer Market Intelligence Snapshot as at 2025",
    page_icon="🍺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Polished Design
st.markdown("""
    <style>
    /* Main Background - Gradient */
    .stApp {
        background: linear-gradient(135deg, #fdfbf7 0%, #fff7ed 100%);
    }
    
    /* Card Container Styling */
    .css-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }
    
    /* Stats Card Base */
    .stat-card {
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: left;
        border: 1px solid rgba(0,0,0,0.05);
    }
    
    /* Typography */
    h1, h2, h3 { color: #78350f !important; font-family: 'Segoe UI', sans-serif; }
    p { color: #4b5563; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #fffbeb;
        border-right: 1px solid #fed7aa;
    }
    
    /* Summary Section Highlight */
    .leader-text {
        color: #b45309; 
        font-weight: bold;
        background-color: #fff7ed;
        padding: 2px 6px;
        border-radius: 4px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Data Loading (Comprehensive Dataset)
@st.cache_data
def load_data():
    data = [
        {
            "country": "Botswana", "region": "Southern Africa", 
            "liters_per_capita": 150.0, "production_m_hl": 0.55, "avg_price_usd": 1.80,
            "top_brands": "St Louis Lager, Heineken, Carling Black Label, Windhoek Lager", "review_snapshot": "Crisp lagers for hot climate",
            "digital_channels": "Liquorama App, Sefalana Online Store, Yourmart"
        },
        {
            "country": "Namibia", "region": "Southern Africa", 
            "liters_per_capita": 90.8, "production_m_hl": 3.0, "avg_price_usd": 1.60,
            "top_brands": "Windhoek, Tafel, Hansa Pilsner", "review_snapshot": "Purity Law (Reinheitsgebot) preference",
            "digital_channels": "Namibia Breweries (NBL) Online Store, Dial-A-Drink (DAM Namibia), "
        },
        {
            "country": "Gabon", "region": "Central Africa", 
            "liters_per_capita": 78.3, "production_m_hl": 3.00, "avg_price_usd": 1.30,
            "top_brands": "Regab, Castel", "review_snapshot": "Regab is the 'national bread'",
            "digital_channels": "Glovo Libreville"
        },
        {
            "country": "Seychelles", "region": "East Africa", 
            "liters_per_capita": 77.0, "production_m_hl": 0.12, "avg_price_usd": 4.50,
            "top_brands": "SeyBrew, Eku, Heineken", "review_snapshot": "Fresh, tourism-driven taste",
            "digital_channels": "Seybrew.com"
        },
        {
            "country": "South Africa", "region": "Southern Africa", 
            "liters_per_capita": 69.0, "production_m_hl": 35.10, "avg_price_usd": 1.50,
            "top_brands": "Carling, Castle, Heineken", "review_snapshot": "Sophisticated, and diverse palate divided on traditional and premium beer",
            "digital_channels": "Checkers Sixty60, Uber Eats,Takealot.com"
        },
        {
            "country": "Angola", "region": "Southern Africa", 
            "liters_per_capita": 33.4, "production_m_hl": 12.00, "avg_price_usd": 0.85,
            "top_brands": "Cuca, Nocal, Tigra", "review_snapshot": "Must be served freezing cold",
            "digital_channels": "Tupuca, Socios, Candando online"
        },
        {
            "country": "Cameroon", "region": "Central Africa", 
            "liters_per_capita": 25.0, "production_m_hl": 9.10, "avg_price_usd": 1.25,
            "top_brands": "Castel, Guinness, Beaufort", "review_snapshot": "Loyal to local heritage brands, with a strong preference for large-format glass bottles (65cl).",
            "digital_channels": "Glovo cameroon, DOVV Online"
        },
        {
            "country": "Zimbabwe", "region": "Southern Africa", 
            "liters_per_capita": 22.0, "production_m_hl": 6.50, "avg_price_usd": 1.80,
            "top_brands": "Zambezi,Carling black label, Castle lager, Chibuku", "review_snapshot": "Split: Clear Lager vs Sorghum beer",
            "digital_channels": "SPAR Zimbabwe, TM Pick n Pay Online"
        },
        {
            "country": "Mozambique", "region": "Southern Africa", 
            "liters_per_capita": 11.9, "production_m_hl": 4.10, "avg_price_usd": 1.12,
            "top_brands": "2M, Laurentina Preta, Heineken", "review_snapshot": "Dark lagers are highly rated",
            "digital_channels": "Ubuy Mozambique"
        },
        {
            "country": "Tanzania", "region": "East Africa", 
            "liters_per_capita": 8.0, "production_m_hl": 4.69, "avg_price_usd": 1.30,
            "top_brands": "Kilimanjaro, Serengeti, Safari", "review_snapshot": "Strong national identity brands",
            "digital_channels": "Distro"
        },
        {
            "country": "Uganda", "region": "East Africa", 
            "liters_per_capita": 7.3, "production_m_hl": 4.20, "avg_price_usd": 1.20,
            "top_brands": "Nile Special, Club Pilsner, Tusker", "review_snapshot": "Nile Special is cult-status",
            "digital_channels": "Jumia Food, Kikuubo Online, Glovo"
        },
        {
            "country": "Kenya", "region": "East Africa", 
            "liters_per_capita": 8.0, "production_m_hl": 4.50, "avg_price_usd": 2.30,
            "top_brands": "Tusker, White Cap, Guinnes", "review_snapshot": "Tusker is a national symbol; while craft beer is an upcoming favorite for young consumers",
            "digital_channels": "EABL'S The Bar, Drinks Vine, Dial A Drink Kenya"
        },
        {
            "country": "Ghana", "region": "West Africa", 
            "liters_per_capita": 10.0, "production_m_hl": 3.00, "avg_price_usd": 1.40,
            "top_brands": "Club Premium, Star, Tale beer", "review_snapshot": "Crisp finish taste preferred",
            "digital_channels": "Liquour Junction, Tales from Ghana"
        },
        {
            "country": "Nigeria", "region": "West Africa", 
            "liters_per_capita": 8.3, "production_m_hl": 17.73, "avg_price_usd": 1.15,
            "top_brands": "Star, Goldberg, Guinness, Hero Lager", "review_snapshot": "The market is stil largely loyal to Guinness",
            "digital_channels": "Drinks.ng, Glovo"
        },
        {
            "country": "Ethiopia", "region": "East Africa", 
            "liters_per_capita": 12.2, "production_m_hl": 12.67, "avg_price_usd": 0.95,
            "top_brands": "St. George, Habesha", "review_snapshot": "Sentiment is rooted in heritage and gradual premiumization",
            "digital_channels": "Habesha App"
        }
    ]
    return pd.DataFrame(data)

df = load_data()

# 4. Sidebar Filters
with st.sidebar:
    st.header("🔍 Market Filters")
    
    # Region Filter
    all_regions = sorted(df['region'].unique())
    selected_regions = st.multiselect(
        "Select Regions:",
        options=all_regions,
        default=all_regions,
        help="Filter the dashboard by African sub-regions."
    )
    
    st.divider()

    # Production Filter Slider
    min_production = float(df['production_m_hl'].min())
    max_production = float(df['production_m_hl'].max())
    production_range = st.slider(
        "Max Production Volume (Million hl):",
        min_value=min_production,
        max_value=max_production,
        value=max_production,
        step=0.1,
        format="%.2f M hl",
        help="Filter markets by their total beer production volume in million hectoliters."
    )
    st.divider()
    
    # Price Filter
    min_price = float(df['avg_price_usd'].min())
    max_price = float(df['avg_price_usd'].max())
    
    price_range = st.slider(
        "Max Price per Beer ($):",
        min_value=min_price,
        max_value=max_price,
        value=max_price,
        step=0.10,
        format="$%.2f",
        help="Price is based on average retail price in 2025 for a standard 500ml bottle."
    )
    
    st.info("💡 **Tip:** Use the price slider to find affordable markets (e.g., Angola) vs. premium markets (e.g., Seychelles).")

# 5. Filtering Logic
filtered_df = df[
    (df['region'].isin(selected_regions)) & 
    (df['avg_price_usd'] <= price_range)
]

# 6. Main Dashboard Layout

# --- Header ---
st.markdown("""
    <div class="css-card">
        <h1>🍺 African Beer Market Snapshot</h1>
        <p>  Analysis of beer consumption, production, and digital retail trends across top African markets as at 2025.</p>
    </div>
""", unsafe_allow_html=True)

# --- KPI Cards (Dynamic) ---
col1, col2, col3, col4 = st.columns(4)

avg_price = filtered_df['avg_price_usd'].mean()
total_prod = filtered_df['production_m_hl'].sum()
top_consumer = filtered_df.loc[filtered_df['liters_per_capita'].idxmax()] if not filtered_df.empty else None

with col1:
    st.markdown(f"""
        <div class="stat-card" style="background-color: #fffbeb;">
            <div style="color: #b45309; font-size: 0.8rem; font-weight: 600;">MARKETS ANALYZED</div>
            <div style="color: #78350f; font-size: 1.5rem; font-weight: 700;">{len(filtered_df)}</div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="stat-card" style="background-color: #f0fdf4;">
            <div style="color: #15803d; font-size: 0.8rem; font-weight: 600;">AVERAGE PRICE (2025)</div>
            <div style="color: #14532d; font-size: 1.5rem; font-weight: 700;">${avg_price:.2f}</div>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="stat-card" style="background-color: #eff6ff;">
            <div style="color: #1d4ed8; font-size: 0.8rem; font-weight: 600;">TOTAL PRODUCTION</div>
            <div style="color: #1e3a8a; font-size: 1.5rem; font-weight: 700;">{total_prod:.1f} M hl</div>
        </div>
    """, unsafe_allow_html=True)

with col4:
    if top_consumer is not None:
        st.markdown(f"""
            <div class="stat-card" style="background-color: #faf5ff;">
                <div style="color: #7e22ce; font-size: 0.8rem; font-weight: 600;">TOP CONSUMER</div>
                <div style="color: #581c87; font-size: 1.2rem; font-weight: 700;">{top_consumer['country']}</div>
                <div style="color: #6b21a8; font-size: 0.8rem;">{top_consumer['liters_per_capita']} L/capita</div>
            </div>
        """, unsafe_allow_html=True)

st.write("") # Spacer

# --- Visualization Section ---

# Scatter Plot Visualization 
st.subheader("🎯 Market Dynamics: Consumption vs. Production")

# 1. Create the base scatter plot
scatter = alt.Chart(filtered_df).mark_circle(size=200).encode(
    x=alt.X('production_m_hl:Q', 
            title='Production (Million hl)',
            scale=alt.Scale(zero=False)),
    y=alt.Y('liters_per_capita:Q', 
            title='Consumption (Liters/Capita)'),
    color=alt.Color('region:N', legend=alt.Legend(title="Region")),
    tooltip=[
        alt.Tooltip('country:N', title='Country'),
        alt.Tooltip('region:N', title='Region'),
        alt.Tooltip('liters_per_capita:Q', title='Liters/Capita', format='.1f'),
        alt.Tooltip('production_m_hl:Q', title='Production (M hl)', format='.2f'),
        alt.Tooltip('avg_price_usd:Q', title='Avg Price', format='$.2f')
    ]
).interactive()

# 2. Add labels
labels = scatter.mark_text(
    align='left',
    baseline='middle',
    dx=10 
).encode(
    text='country:N'
)

# 3. Combine
final_scatter = (scatter + labels).properties(
    height=500,
    title="African Beer Market: High-Volume Producers vs. Heavy Consumers"
)

st.altair_chart(final_scatter, use_container_width=True)

# --- Detailed Data Table ---
st.subheader("📋 Market Details & Retail Intelligence")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True,
    column_order=("country", "region", "liters_per_capita", "production_m_hl", "avg_price_usd", "top_brands", "digital_channels"),
    column_config={
        "country": st.column_config.TextColumn("Country", width="small"),
        "region": st.column_config.TextColumn("Region", width="small"),
        "liters_per_capita": st.column_config.ProgressColumn(
            "Consumption(L)/Capita",
            format="%.1f L",
            min_value=0,
            max_value=150,
            width="medium"
        ),
        "production_m_hl": st.column_config.NumberColumn(
            "Production (M hl)",
            format="%.2f M",
            width="small"
        ),
        "avg_price_usd": st.column_config.NumberColumn(
            "Avg Price ($)",
            format="$%.2f",
            width="small"
        ),
        "top_brands": st.column_config.TextColumn("Top Brands", width="medium"),
        "digital_channels": st.column_config.TextColumn("Digital Retail", width="medium"),
    }
)

# --- Expandable Insights ---
with st.expander("📝 View Consumer Sentiment Snapshots"):
    for _, row in filtered_df.iterrows():
        st.markdown(f"**{row['country']}:** {row['review_snapshot']}")

# --- Summary Visuals ---
if not filtered_df.empty:
    st.markdown("---")
    st.subheader("📈 Regional Performance View (Production vs. Consumption Trends)")
    # 1. Calculations
    # Group by region to find leaders
    regional_summary = filtered_df.groupby('region').agg({
        'production_m_hl': 'sum',
        'liters_per_capita': 'sum' 
    }).reset_index()
    
    # Identify Leaders
    leader_prod = regional_summary.loc[regional_summary['production_m_hl'].idxmax(), 'region']
    leader_cons = regional_summary.loc[regional_summary['liters_per_capita'].idxmax(), 'region']
    
    # 2. Layout
    sum_col1, sum_col2, sum_col3 = st.columns(3)

    # 3. Column A: Total Production Volume by Region
    with sum_col1:
        st.markdown("##### 🏭 Production by Region")
        sorted_prod = regional_summary.sort_values('production_m_hl', ascending=False)
        for _, row in sorted_prod.iterrows():
            r_name = row['region']
            val = row['production_m_hl']
            # Bold the leader
            if r_name == leader_prod:
                st.markdown(f":trophy: **{r_name}: {val:.2f} M hl**")
            else:
                st.markdown(f"{r_name}: {val:.2f} M hl")

    # 4. Column B: Total & Average Consumption Stats (Global/Filtered)
    with sum_col2:
        st.markdown("##### 🍺 Consumption Snapshot")
        avg_lpc = filtered_df['liters_per_capita'].mean()
        total_lpc = filtered_df['liters_per_capita'].sum() 
        # we display the Average Consumption Rate across the filtered selection.
        st.metric(label="Average Consumption Rate", value=f"{avg_lpc:.1f} L/capita")
        st.metric(label="Total Consumption Volume", value=f"{total_lpc:.1f} L/capita")
        #st.caption("Average liters consumed per person across selected markets.")

    # 5. Column C: Total Beer Consumption by Region (Avg Intensity)
    with sum_col3:
        st.markdown("##### 🌍 Consumption by Region")
        sorted_cons = regional_summary.sort_values('liters_per_capita', ascending=False)
        for _, row in sorted_cons.iterrows():
            r_name = row['region']
            val = row['liters_per_capita']
            # Bold the leader
            if r_name == leader_cons:
                st.markdown(f":trophy: **{r_name}: {val:.1f} L/capita**")
            else:
                st.markdown(f"{r_name}: {val:.1f} L/capita")

# --- Footer ---
st.markdown("---")
col_f1, col_f2 = st.columns([3, 1])
with col_f1:
    st.caption("Data Sources: Business Insider Africa, Kirin Holdings Global Beer Report(2022),Global Data Consolidations, and WHO Global Health Observatory.")
    st.caption("Note: Timelies of dataset used are primarily between 2022-2025.")
    st.caption("Developed by Collins Ogombo | © 2026 All rights reserved.")
with col_f2:
    csv = filtered_df.to_csv(index=False)
    st.download_button(
        label="Download Filtered Data",
        data=csv,
        file_name='african_beer_market_2025.csv',
        mime='text/csv',
        use_container_width=True
    )