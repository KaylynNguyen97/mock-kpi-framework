# app.py - COMPLETE VERSION FOR QUICK TESTING (Simulated Data) - FIXED
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Dolby Marketing Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1E3A8A;
        font-weight: 700;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #374151;
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-bottom: 2px solid #E5E7EB;
        padding-bottom: 0.5rem;
    }
    .metric-card {
        background-color: #F9FAFB;
        border-radius: 10px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1E3A8A;
    }
    .kpi-label {
        font-size: 0.9rem;
        color: #6B7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .positive-change {
        color: #10B981;
    }
    .negative-change {
        color: #EF4444;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">📊 DOLBY MARKETING PERFORMANCE DASHBOARD</h1>', unsafe_allow_html=True)

# Sidebar for navigation and filters
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Dolby_Laboratories_logo.svg/1280px-Dolby_Laboratories_logo.svg.png", 
             width=200)
    st.markdown("### 📈 Dashboard Navigation")
    
    dashboard_choice = st.selectbox(
        "Select Dashboard View",
        ["📊 Executive Summary", 
         "🎯 Market Position & Lead Gen", 
         "⭐ Product Experience",
         "🤝 Partner Value & Enablement",
         "💡 Innovation Leadership",
         "🎨 Creator Advocacy"]
    )
    
    st.markdown("---")
    st.markdown("### ⚙️ Filters")
    
    # Date range filter
    date_range = st.selectbox(
        "Time Period",
        ["Last 12 Months", "Last 6 Months", "Last Quarter", "Year to Date", "All Time"]
    )
    
    # Market filter (if applicable)
    market_options = ["All Markets", "North America", "Europe", "Asia Pacific", "Latin America"]
    selected_market = st.selectbox("Market", market_options)
    
    st.markdown("---")
    st.markdown("### 📊 Data Status")
    st.info("Using simulated data for demonstration")
    
    if st.button("🔄 Refresh Data"):
        st.rerun()

def load_simulated_data():
    """Generate simulated data for demonstration"""
    st.sidebar.info("📊 Using simulated data for demonstration")
    
    # Generate dates
    dates = pd.date_range(start='2023-01-01', end='2024-01-01', freq='M')
    quarters = [f'Q{(i%4)+1} 202{3 if i<4 else 4}' for i in range(len(dates))]
    
    # Brand Health Index
    brand_health = pd.DataFrame({
        'Date': quarters[:8],
        'Composite_Brand_Health_Score': [78.2, 79.5, 81.3, 82.1, 83.4, 84.2, 85.0, 85.5]
    })
    
    # Digital Brand Presence
    markets = ['North America', 'Europe', 'Asia Pacific']
    digital_presence = pd.DataFrame({
        'Market': np.repeat(markets, 4),
        'Composite_Digital_Presence_Score': [85.3, 87.2, 82.4, 86.1, 83.2, 84.5, 81.3, 85.6, 79.4, 81.2, 78.5, 80.3]
    })
    
    # Marketing Qualified Leads
    mql_data = []
    sources = ['Organic Search', 'Paid Social', 'Email', 'Events']
    for i, date in enumerate(dates[:6]):
        for source in sources:
            base = 200 + i * 50
            total = base + np.random.randint(-20, 50)
            mql_count = int(total * (0.25 + i * 0.03))
            mql_data.append({
                'Date': date,
                'Lead_Source': source,
                'Total_Leads': total,
                'MQL_Count': mql_count,
                'Lead_Score_Average': 68 + i * 3 + np.random.randint(-5, 5),
                'Conversion_Rate': mql_count / total
            })
    mql_df = pd.DataFrame(mql_data)
    
    # Product NPS
    touchpoints = ['Website Demo', 'Product Tour', 'Trial Signup', 'First Login']
    product_nps_data = []
    for i, quarter in enumerate(quarters[:8]):
        for j, touchpoint in enumerate(touchpoints):
            product_nps_data.append({
                'Date': quarter,
                'Year_Quarter': quarter,
                'Touchpoint': touchpoint,
                'NPS_Score': 45 + i * 3 + j * 2,
                'Value_Communication_Score': 4.0 + i * 0.1 + j * 0.05,
                'Ease_Of_Understanding_Score': 4.2 + i * 0.08 + j * 0.03,
                'Brand_Clarity_Score': 4.1 + i * 0.09 + j * 0.04,
                'Entertainment_Value_Score': 4.3 + i * 0.07 + j * 0.06,
                'Promoters_Pct': 50 + i * 2 + j * 1,
                'Passives_Pct': 30 - i * 1,
                'Detractors_Pct': 20 - i * 1 - j * 0.5
            })
    product_nps_df = pd.DataFrame(product_nps_data)
    
    # Partner NPS
    regions = ['NA', 'EMEA', 'APAC']
    partner_types = ['Technology', 'Channel', 'Strategic']
    partner_nps_data = []
    for year in [2022, 2023]:
        for region in regions:
            for p_type in partner_types:
                partner_nps_data.append({
                    'Year': year,
                    'Region': region,
                    'Partner_Type': p_type,
                    'NPS_Score': 55 + (year-2022) * 5 + np.random.randint(-10, 10),
                    'Brand_Awareness_Score': 4.1 + (year-2022) * 0.2 + np.random.uniform(-0.1, 0.1),
                    'Innovation_Leadership_Score': 4.2 + (year-2022) * 0.3 + np.random.uniform(-0.1, 0.1)
                })
    partner_nps_df = pd.DataFrame(partner_nps_data)
    
    # Partner Mentions
    partners = ['Partner A', 'Partner B', 'Partner C', 'Partner D']
    partner_mentions_data = []
    for i, date in enumerate(dates[:6]):
        for partner in partners:
            partner_mentions_data.append({
                'Date': date,
                'Partner_Name': partner,
                'Mention_Count': 100 + i * 40 + np.random.randint(-20, 50),
                'Estimated_Reach': 500000 + i * 200000 + np.random.randint(-100000, 300000),
                'Co_Branded': np.random.choice(['Yes', 'No'], p=[0.6, 0.4])
            })
    partner_mentions_df = pd.DataFrame(partner_mentions_data)
    
    # Innovation Leadership
    categories = ['Audio Tech', 'Immersive Experience', 'Cinema Innovation', 'Gaming Tech']
    audiences = ['Consumers', 'Professionals', 'Developers', 'Partners']
    innovation_data = []
    for i, date in enumerate(dates[:6]):
        for j, category in enumerate(categories):
            for audience in audiences:
                innovation_data.append({
                    'Date': date,
                    'Innovation_Category': category,
                    'Audience': audience,
                    'Innovation_Leadership_Index': 70 + i * 3 + j * 2,
                    'Association_Share_Pct': 30 + i * 5 + j * 3,
                    'Positive_Sentiment_Pct': 70 + i * 2,
                    'Negative_Sentiment_Pct': 10 - i * 0.5,
                    'Neutral_Sentiment_Pct': 20 - i * 1.5,
                    'Category_Sentiment_Score': 4.0 + i * 0.1 + j * 0.05,
                    'Total_Mentions': 200 + i * 100 + j * 50
                })
    innovation_df = pd.DataFrame(innovation_data)
    
    # Creator NPS
    content_types = ['Video Tutorial', 'Case Study', 'Social Campaign', 'Event Content']
    cohorts = ['Cohort 1', 'Cohort 2', 'Cohort 3', 'Cohort 4']
    creator_nps_data = []
    for i, quarter in enumerate(quarters[:8]):
        for j, content_type in enumerate(content_types):
            creator_nps_data.append({
                'Date': quarter,
                'Quarter': quarter,
                'Content_Type': content_type,
                'Cohort': cohorts[j % 4],
                'NPS_Score': 52 + i * 2 + j * 1,
                'Program_Value_Score': 4.2 + i * 0.1 + j * 0.05,
                'Workflow_Efficiency_Score': 4.1 + i * 0.08 + j * 0.03,
                'Promoters_Pct': 55 + i * 2 + j * 1,
                'Passives_Pct': 30 - i * 1,
                'Detractors_Pct': 15 - i * 1 - j * 0.5,
                'Response_Count': 80 + i * 20 + j * 10
            })
    creator_nps_df = pd.DataFrame(creator_nps_data)
    
    return {
        'Brand_Health_Index': brand_health,
        'Digital_Brand_Presence': digital_presence,
        'Marketing_Qualified_Leads': mql_df,
        'Product_NPS': product_nps_df,
        'Partner_NPS': partner_nps_df,
        'Partner_Brand_Mentions': partner_mentions_df,
        'Creator_Lab_NPS': creator_nps_df,
        'Innovation_Leadership_Index': innovation_df
    }

# Load data function
@st.cache_data(ttl=3600)
def load_data():
    """Load simulated data for quick testing"""
    return load_simulated_data()

# Load data
with st.spinner("Loading data..."):
    data = load_data()

# Extract dataframes
brand_health_df = data.get('Brand_Health_Index', pd.DataFrame())
digital_presence_df = data.get('Digital_Brand_Presence', pd.DataFrame())
mql_df = data.get('Marketing_Qualified_Leads', pd.DataFrame())
product_nps_df = data.get('Product_NPS', pd.DataFrame())
partner_nps_df = data.get('Partner_NPS', pd.DataFrame())
partner_mentions_df = data.get('Partner_Brand_Mentions', pd.DataFrame())
creator_nps_df = data.get('Creator_Lab_NPS', pd.DataFrame())
innovation_df = data.get('Innovation_Leadership_Index', pd.DataFrame())

# Set up plotting style - FIXED: Changed from seaborn-v0_8-darkgrid to default
plt.style.use('default')
sns.set_palette("husl")

# EXECUTIVE SUMMARY DASHBOARD
def show_executive_summary():
    st.markdown('<h2 class="sub-header">📈 Executive Summary</h2>', unsafe_allow_html=True)
    
    # Key Metrics Row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_score = brand_health_df['Composite_Brand_Health_Score'].mean()
        st.markdown(f'<div class="kpi-value">{avg_score:.1f}</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">Brand Health Index</div>', unsafe_allow_html=True)
        st.caption("↗️ +8.1% YoY")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        total_mqls = mql_df['MQL_Count'].sum()
        st.markdown(f'<div class="kpi-value">{total_mqls:,.0f}</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">Total MQLs</div>', unsafe_allow_html=True)
        st.caption("↗️ +15% vs last period")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_nps = product_nps_df['NPS_Score'].mean()
        st.markdown(f'<div class="kpi-value">{avg_nps:.0f}</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">Product NPS</div>', unsafe_allow_html=True)
        st.caption("↗️ +12 points")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_innovation = innovation_df['Innovation_Leadership_Index'].mean()
        st.markdown(f'<div class="kpi-value">{avg_innovation:.1f}</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">Innovation Index</div>', unsafe_allow_html=True)
        st.caption("↗️ +7.2%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Second row of metrics
    col5, col6, col7, col8 = st.columns(4)
    
    with col5:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        overall_rate = (mql_df['MQL_Count'].sum() / mql_df['Total_Leads'].sum() * 100)
        st.markdown(f'<div class="kpi-value">{overall_rate:.1f}%</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">MQL Conversion</div>', unsafe_allow_html=True)
        st.caption("↗️ +2.3%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col6:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        total_mentions = partner_mentions_df['Mention_Count'].sum()
        st.markdown(f'<div class="kpi-value">{total_mentions:,.0f}</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">Brand Mentions</div>', unsafe_allow_html=True)
        st.caption("↗️ +42%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col7:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_partner_nps = partner_nps_df['NPS_Score'].mean()
        st.markdown(f'<div class="kpi-value">{avg_partner_nps:.0f}</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">Partner NPS</div>', unsafe_allow_html=True)
        st.caption("↗️ +9 points")
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col8:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        avg_creator_nps = creator_nps_df['NPS_Score'].mean()
        st.markdown(f'<div class="kpi-value">{avg_creator_nps:.0f}</div>', unsafe_allow_html=True)
        st.markdown('<div class="kpi-label">Creator NPS</div>', unsafe_allow_html=True)
        st.caption("↗️ +11 points")
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Charts Row
    st.markdown('<h3 class="sub-header">Performance Trends</h3>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Brand Health Trend")
        fig, ax = plt.subplots(figsize=(10, 4))
        brand_health_summary = brand_health_df.groupby('Date')['Composite_Brand_Health_Score'].mean().reset_index()
        ax.plot(range(len(brand_health_summary)), brand_health_summary['Composite_Brand_Health_Score'], 
               marker='o', linewidth=2, color='#3498db')
        ax.set_xlabel('Quarter')
        ax.set_ylabel('Composite Score')
        ax.set_xticks(range(len(brand_health_summary)))
        ax.set_xticklabels(brand_health_summary['Date'], rotation=45)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with col2:
        st.subheader("MQL Conversion Trend")
        fig, ax = plt.subplots(figsize=(10, 4))
        conversion_trend = mql_df.groupby('Date')['Conversion_Rate'].mean().reset_index()
        ax.plot(conversion_trend['Date'], conversion_trend['Conversion_Rate']*100, 
               marker='o', linewidth=2, color='#e67e22')
        ax.set_xlabel('Month')
        ax.set_ylabel('Conversion Rate (%)')
        ax.grid(True, alpha=0.3)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks

# MARKET POSITION DASHBOARD
def show_market_position_dashboard():
    st.markdown('<h2 class="sub-header">🎯 Market Position & Lead Generation</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📈 Trends", "📊 Performance", "🎯 Lead Quality"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Brand Health Index Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            brand_health_summary = brand_health_df.groupby('Date')['Composite_Brand_Health_Score'].mean().reset_index()
            ax.plot(range(len(brand_health_summary)), brand_health_summary['Composite_Brand_Health_Score'], 
                   marker='o', linewidth=2, color='#3498db')
            ax.set_xlabel('Quarter')
            ax.set_ylabel('Composite Score')
            ax.set_xticks(range(len(brand_health_summary)))
            ax.set_xticklabels(brand_health_summary['Date'], rotation=45)
            ax.grid(True, alpha=0.3)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("Lead Score Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            lead_score_trend = mql_df.groupby('Date')['Lead_Score_Average'].mean().reset_index()
            ax.plot(lead_score_trend['Date'], lead_score_trend['Lead_Score_Average'], 
                   marker='o', linewidth=2, color='#9b59b6')
            ax.set_xlabel('Month')
            ax.set_ylabel('Average Lead Score')
            ax.grid(True, alpha=0.3)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Digital Brand Presence by Market")
            fig, ax = plt.subplots(figsize=(10, 5))
            digital_presence_summary = digital_presence_df.groupby('Market')['Composite_Digital_Presence_Score'].mean().reset_index()
            colors = ['#2ecc71', '#3498db', '#e74c3c']
            bars = ax.bar(digital_presence_summary['Market'], 
                       digital_presence_summary['Composite_Digital_Presence_Score'],
                       color=colors, alpha=0.8)
            ax.set_ylabel('Composite Score')
            ax.set_ylim(70, 90)
            
            for bar in bars:
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                       f'{height:.1f}', ha='center', va='bottom', fontsize=10)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("MQL Volume by Month")
            fig, ax = plt.subplots(figsize=(10, 5))
            mql_volume = mql_df.groupby('Date').agg({
                'Total_Leads': 'sum',
                'MQL_Count': 'sum'
            }).reset_index()
            
            x = range(len(mql_volume))
            width = 0.35
            ax.bar([i - width/2 for i in x], mql_volume['Total_Leads'], width, 
                  label='Total Leads', alpha=0.7)
            ax.bar([i + width/2 for i in x], mql_volume['MQL_Count'], width, 
                  label='MQLs', alpha=0.7)
            ax.set_xlabel('Month')
            ax.set_ylabel('Count')
            ax.set_xticks(x)
            ax.set_xticklabels([str(d)[:7] for d in mql_volume['Date']], rotation=45)
            ax.legend()
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab3:
        st.subheader("MQL Performance by Lead Source")
        fig, ax = plt.subplots(figsize=(12, 6))
        mql_summary = mql_df.groupby('Lead_Source').agg({
            'Total_Leads': 'sum',
            'MQL_Count': 'sum'
        }).reset_index()
        mql_summary['Conversion_Rate'] = (mql_summary['MQL_Count'] / mql_summary['Total_Leads']) * 100
        
        x = np.arange(len(mql_summary))
        width = 0.35
        ax.bar(x - width/2, mql_summary['Total_Leads'], width, label='Total Leads', alpha=0.7)
        ax.bar(x + width/2, mql_summary['MQL_Count'], width, label='MQLs', alpha=0.7)
        
        # FIXED: Changed ax4 to ax2 for consistency
        ax2 = ax.twinx()
        ax2.plot(x, mql_summary['Conversion_Rate'], color='red', marker='o', linewidth=2, label='Conversion Rate')
        ax2.set_ylabel('Conversion Rate (%)', color='red')
        ax2.tick_params(axis='y', labelcolor='red')
        
        ax.set_xlabel('Lead Source')
        ax.set_ylabel('Count')
        ax.set_xticks(x)
        ax.set_xticklabels(mql_summary['Lead_Source'], rotation=45, ha='right')
        ax.legend(loc='upper left')
        ax2.legend(loc='upper right')
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks

# PRODUCT EXPERIENCE DASHBOARD
def show_product_experience_dashboard():
    st.markdown('<h2 class="sub-header">⭐ Product Experience - "First Meet" NPS</h2>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["📈 NPS Trends", "🎯 Experience Metrics"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("NPS Score Trend by Touchpoint")
            fig, ax = plt.subplots(figsize=(10, 5))
            
            # Extract quarter and year for sorting
            product_nps_df['Year_Quarter'] = product_nps_df['Date']
            
            nps_by_touchpoint = product_nps_df.pivot_table(
                index='Year_Quarter', 
                columns='Touchpoint', 
                values='NPS_Score',
                aggfunc='mean'
            ).reset_index()
            
            # Sort chronologically
            quarter_order = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 
                           'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
            nps_by_touchpoint['Year_Quarter'] = pd.Categorical(nps_by_touchpoint['Year_Quarter'], 
                                                              categories=quarter_order, ordered=True)
            nps_by_touchpoint = nps_by_touchpoint.sort_values('Year_Quarter')
            
            touchpoints = [col for col in nps_by_touchpoint.columns if col != 'Year_Quarter']
            
            for i, touchpoint in enumerate(touchpoints):
                ax.plot(range(len(nps_by_touchpoint)), nps_by_touchpoint[touchpoint], 
                       marker='o', linewidth=2, label=touchpoint)
            
            ax.set_xlabel('Quarter')
            ax.set_ylabel('NPS Score')
            ax.set_xticks(range(len(nps_by_touchpoint)))
            ax.set_xticklabels(nps_by_touchpoint['Year_Quarter'], rotation=45)
            ax.grid(True, alpha=0.3)
            ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("NPS Distribution")
            categories = ['Promoters_Pct', 'Passives_Pct', 'Detractors_Pct']
            
            latest_quarter = product_nps_df['Year_Quarter'].max()
            latest_data = product_nps_df[product_nps_df['Year_Quarter'] == latest_quarter]
            avg_distribution = latest_data[categories].mean().values
            
            fig, ax = plt.subplots(figsize=(8, 5))
            labels = ['Promoters', 'Passives', 'Detractors']
            colors = ['#2ecc71', '#f39c12', '#e74c3c']
            
            wedges, texts, autotexts = ax.pie(avg_distribution, labels=labels, colors=colors,
                                             autopct='%1.1f%%', startangle=90)
            ax.set_title(f'NPS Distribution ({latest_quarter})', fontweight='bold')
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab2:
        st.subheader("Experience Metrics")
        
        latest_quarter = product_nps_df['Year_Quarter'].max()
        latest_data = product_nps_df[product_nps_df['Year_Quarter'] == latest_quarter]
        
        experience_metrics = ['Value_Communication_Score', 'Ease_Of_Understanding_Score', 
                             'Brand_Clarity_Score', 'Entertainment_Value_Score']
        
        experience_scores = latest_data[experience_metrics].mean().reset_index()
        experience_scores.columns = ['Metric', 'Average_Score']
        experience_scores['Metric'] = experience_scores['Metric'].str.replace('_Score', '').str.replace('_', ' ')
        
        # Display as a bar chart
        fig, ax = plt.subplots(figsize=(10, 5))
        colors = plt.cm.Paired(np.linspace(0, 1, len(experience_scores)))
        bars = ax.bar(experience_scores['Metric'], experience_scores['Average_Score'], color=colors)
        ax.set_ylabel('Average Score (1-5)')
        ax.set_ylim(3.5, 5)
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
        
        for bar, score in zip(bars, experience_scores['Average_Score']):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.05,
                   f'{score:.2f}', ha='center', va='bottom', fontsize=10)
        
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks
        
        # Also show as a dataframe
        st.dataframe(experience_scores, use_container_width=True)

# PARTNER DASHBOARD
def show_partner_dashboard():
    st.markdown('<h2 class="sub-header">🤝 Partner Value & Enablement</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 NPS Analysis", "📣 Brand Mentions", "🌐 Regional View"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Partner NPS Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            nps_trend = partner_nps_df.groupby('Year')['NPS_Score'].mean().reset_index()
            
            ax.plot(nps_trend['Year'], nps_trend['NPS_Score'], marker='o', 
                   linewidth=2, markersize=8, color='#3498db')
            ax.set_xlabel('Year')
            ax.set_ylabel('Average NPS Score')
            ax.grid(True, alpha=0.3)
            
            for i, row in nps_trend.iterrows():
                ax.text(row['Year'], row['NPS_Score'] + 1, 
                       f'{row["NPS_Score"]:.1f}', ha='center', fontsize=10)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("Brand Perception by Partner Type")
            fig, ax = plt.subplots(figsize=(10, 5))
            avg_scores = partner_nps_df.groupby('Partner_Type').agg({
                'Brand_Awareness_Score': 'mean',
                'Innovation_Leadership_Score': 'mean'
            }).reset_index()
            
            x = np.arange(len(avg_scores))
            width = 0.35
            
            ax.bar(x - width/2, avg_scores['Brand_Awareness_Score'], width, 
                  label='Brand Awareness', alpha=0.7)
            ax.bar(x + width/2, avg_scores['Innovation_Leadership_Score'], width, 
                  label='Innovation Leadership', alpha=0.7)
            
            ax.set_xlabel('Partner Type')
            ax.set_ylabel('Average Score')
            ax.set_xticks(x)
            ax.set_xticklabels(avg_scores['Partner_Type'], rotation=45, ha='right')
            ax.legend()
            ax.set_ylim(3.5, 5)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab2:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Partner Brand Mentions Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            mentions_trend = partner_mentions_df.groupby('Date').agg({
                'Mention_Count': 'sum',
                'Estimated_Reach': 'sum'
            }).reset_index()
            
            ax.plot(mentions_trend['Date'], mentions_trend['Mention_Count'], 
                   marker='o', linewidth=2, color='#2ecc71', label='Mention Count')
            ax.set_xlabel('Month')
            ax.set_ylabel('Mention Count', color='#2ecc71')
            ax.tick_params(axis='y', labelcolor='#2ecc71')
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
            
            ax4b = ax.twinx()
            ax4b.plot(mentions_trend['Date'], mentions_trend['Estimated_Reach']/1000000, 
                     marker='s', linewidth=2, color='#e74c3c', label='Estimated Reach (M)')
            ax4b.set_ylabel('Estimated Reach (Millions)', color='#e74c3c')
            ax4b.tick_params(axis='y', labelcolor='#e74c3c')
            
            lines1, labels1 = ax.get_legend_handles_labels()
            lines2, labels2 = ax4b.get_legend_handles_labels()
            ax.legend(lines1 + lines2, labels1 + labels2, loc='upper left')
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("Brand Mentions by Partner")
            fig, ax = plt.subplots(figsize=(10, 5))
            mentions_by_partner = partner_mentions_df.groupby('Partner_Name')['Mention_Count'].sum().reset_index()
            mentions_by_partner = mentions_by_partner.sort_values('Mention_Count', ascending=True)
            
            colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(mentions_by_partner)))
            bars = ax.barh(mentions_by_partner['Partner_Name'], mentions_by_partner['Mention_Count'], color=colors)
            ax.set_xlabel('Total Mention Count')
            
            for bar in bars:
                width = bar.get_width()
                ax.text(width + 5, bar.get_y() + bar.get_height()/2,
                       f'{int(width)}', ha='left', va='center', fontsize=9)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab3:
        st.subheader("Partner NPS Score Heatmap")
        partner_nps_pivot = partner_nps_df.pivot_table(
            index='Region',
            columns='Partner_Type',
            values='NPS_Score',
            aggfunc='mean'
        )
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(partner_nps_pivot, annot=True, fmt='.1f', cmap='YlOrRd', 
                   cbar_kws={'label': 'NPS Score'}, ax=ax)
        ax.set_xlabel('Partner Type')
        ax.set_ylabel('Region')
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks

# INNOVATION DASHBOARD
def show_innovation_dashboard():
    st.markdown('<h2 class="sub-header">💡 Innovation Leadership</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📈 Index Trends", "🧭 Category Analysis", "🎯 Sentiment Insights"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Innovation Leadership Index Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            innovation_trend = innovation_df.groupby('Date')['Innovation_Leadership_Index'].mean().reset_index()
            
            ax.plot(innovation_trend['Date'], innovation_trend['Innovation_Leadership_Index'], 
                   marker='o', linewidth=2, color='#9b59b6')
            ax.set_xlabel('Month')
            ax.set_ylabel('Innovation Leadership Index')
            ax.grid(True, alpha=0.3)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("Total Innovation Mentions Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            mentions_trend = innovation_df.groupby('Date')['Total_Mentions'].sum().reset_index()
            
            ax.plot(mentions_trend['Date'], mentions_trend['Total_Mentions'], 
                   marker='o', linewidth=2, color='#e67e22')
            ax.set_xlabel('Month')
            ax.set_ylabel('Total Mentions')
            ax.grid(True, alpha=0.3)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab2:
        st.subheader("Innovation Category Performance")
        
        latest_date = innovation_df['Date'].max()
        latest_innovation = innovation_df[innovation_df['Date'] == latest_date]
        
        category_performance = latest_innovation.groupby('Innovation_Category').agg({
            'Innovation_Leadership_Index': 'mean',
            'Association_Share_Pct': 'mean'
        }).reset_index()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        x = np.arange(len(category_performance))
        width = 0.35
        
        bars1 = ax.bar(x - width/2, category_performance['Innovation_Leadership_Index'], 
                      width, label='Leadership Index', alpha=0.7)
        bars2 = ax.bar(x + width/2, category_performance['Association_Share_Pct'], 
                      width, label='Association Share %', alpha=0.7)
        
        ax.set_xlabel('Innovation Category')
        ax.set_ylabel('Score / Percentage')
        ax.set_xticks(x)
        ax.set_xticklabels(category_performance['Innovation_Category'], rotation=45, ha='right')
        ax.legend()
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab3:
        st.subheader("Sentiment Analysis")
        
        sentiment_cols = ['Positive_Sentiment_Pct', 'Negative_Sentiment_Pct', 'Neutral_Sentiment_Pct']
        latest_date = innovation_df['Date'].max()
        latest_innovation = innovation_df[innovation_df['Date'] == latest_date]
        
        sentiment_by_category = latest_innovation.groupby('Innovation_Category')[sentiment_cols].mean().reset_index()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        x = np.arange(len(sentiment_by_category))
        bottom = np.zeros(len(sentiment_by_category))
        
        colors = ['#2ecc71', '#e74c3c', '#f39c12']
        for i, col in enumerate(sentiment_cols):
            ax.bar(x, sentiment_by_category[col], bottom=bottom, 
                  label=col.replace('_Sentiment_Pct', ''), color=colors[i])
            bottom += sentiment_by_category[col].values
        
        ax.set_xlabel('Innovation Category')
        ax.set_ylabel('Sentiment Percentage')
        ax.set_xticks(x)
        ax.set_xticklabels(sentiment_by_category['Innovation_Category'], rotation=45, ha='right')
        ax.legend(title='Sentiment')
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks

# CREATOR DASHBOARD
def show_creator_dashboard():
    st.markdown('<h2 class="sub-header">🎨 Creator Advocacy</h2>', unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["📊 NPS Analysis", "📈 Program Performance", "👥 Cohort Insights"])
    
    with tab1:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Average NPS by Content Type")
            fig, ax = plt.subplots(figsize=(10, 5))
            nps_by_content = creator_nps_df.groupby('Content_Type')['NPS_Score'].mean().reset_index()
            nps_by_content = nps_by_content.sort_values('NPS_Score', ascending=False)
            
            colors = plt.cm.Set2(np.linspace(0, 1, len(nps_by_content)))
            bars = ax.bar(nps_by_content['Content_Type'], nps_by_content['NPS_Score'], color=colors)
            ax.set_xlabel('Content Type')
            ax.set_ylabel('Average NPS Score')
            ax.set_ylim(0, 60)
            plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
            
            for bar, score in zip(bars, nps_by_content['NPS_Score']):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                       f'{score:.1f}', ha='center', va='bottom', fontsize=10)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("Creator NPS Trend")
            fig, ax = plt.subplots(figsize=(10, 5))
            creator_nps_df['Quarter'] = creator_nps_df['Date']
            nps_trend = creator_nps_df.groupby('Quarter')['NPS_Score'].mean().reset_index()
            
            quarter_order = ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023', 
                           'Q1 2024', 'Q2 2024', 'Q3 2024', 'Q4 2024']
            nps_trend['Quarter'] = pd.Categorical(nps_trend['Quarter'], categories=quarter_order, ordered=True)
            nps_trend = nps_trend.sort_values('Quarter')
            
            ax.plot(range(len(nps_trend)), nps_trend['NPS_Score'], marker='o', 
                   linewidth=2, color='#3498db')
            ax.set_xlabel('Quarter')
            ax.set_ylabel('Average NPS Score')
            ax.set_xticks(range(len(nps_trend)))
            ax.set_xticklabels(nps_trend['Quarter'], rotation=45)
            ax.grid(True, alpha=0.3)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab2:
        st.subheader("Program Evaluation by Content Type")
        
        avg_scores = creator_nps_df.groupby('Content_Type').agg({
            'Program_Value_Score': 'mean',
            'Workflow_Efficiency_Score': 'mean'
        }).reset_index()
        
        fig, ax = plt.subplots(figsize=(12, 6))
        x = np.arange(len(avg_scores))
        width = 0.35
        
        ax.bar(x - width/2, avg_scores['Program_Value_Score'], width, 
              label='Program Value', alpha=0.7)
        ax.bar(x + width/2, avg_scores['Workflow_Efficiency_Score'], width, 
              label='Workflow Efficiency', alpha=0.7)
        
        ax.set_xlabel('Content Type')
        ax.set_ylabel('Average Score')
        ax.set_xticks(x)
        ax.set_xticklabels(avg_scores['Content_Type'], rotation=45, ha='right')
        ax.legend()
        ax.set_ylim(3.5, 5)
        plt.tight_layout()  # FIXED: Added tight_layout
        st.pyplot(fig)
        plt.close()  # FIXED: Close figure to prevent memory leaks
    
    with tab3:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("NPS Score by Cohort")
            fig, ax = plt.subplots(figsize=(10, 5))
            cohort_performance = creator_nps_df.groupby('Cohort')['NPS_Score'].mean().reset_index()
            cohort_order = ['Cohort 1', 'Cohort 2', 'Cohort 3', 'Cohort 4']
            cohort_performance['Cohort'] = pd.Categorical(cohort_performance['Cohort'], 
                                                        categories=cohort_order, ordered=True)
            cohort_performance = cohort_performance.sort_values('Cohort')
            
            colors = plt.cm.viridis(np.linspace(0.2, 0.8, len(cohort_performance)))
            bars = ax.bar(cohort_performance['Cohort'], cohort_performance['NPS_Score'], color=colors)
            ax.set_xlabel('Cohort')
            ax.set_ylabel('Average NPS Score')
            ax.set_ylim(0, 60)
            
            for bar, score in zip(bars, cohort_performance['NPS_Score']):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 1,
                       f'{score:.1f}', ha='center', va='bottom', fontsize=10)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks
        
        with col2:
            st.subheader("Total Survey Responses by Content Type")
            fig, ax = plt.subplots(figsize=(10, 5))
            response_by_type = creator_nps_df.groupby('Content_Type')['Response_Count'].sum().reset_index()
            response_by_type = response_by_type.sort_values('Response_Count', ascending=True)
            
            colors = plt.cm.coolwarm(np.linspace(0.2, 0.8, len(response_by_type)))
            bars = ax.barh(response_by_type['Content_Type'], response_by_type['Response_Count'], color=colors)
            ax.set_xlabel('Total Response Count')
            
            for bar in bars:
                width = bar.get_width()
                ax.text(width + 2, bar.get_y() + bar.get_height()/2,
                       f'{int(width)}', ha='left', va='center', fontsize=9)
            plt.tight_layout()  # FIXED: Added tight_layout
            st.pyplot(fig)
            plt.close()  # FIXED: Close figure to prevent memory leaks

# Main app routing
if dashboard_choice == "📊 Executive Summary":
    show_executive_summary()
elif dashboard_choice == "🎯 Market Position & Lead Gen":
    show_market_position_dashboard()
elif dashboard_choice == "⭐ Product Experience":
    show_product_experience_dashboard()
elif dashboard_choice == "🤝 Partner Value & Enablement":
    show_partner_dashboard()
elif dashboard_choice == "💡 Innovation Leadership":
    show_innovation_dashboard()
elif dashboard_choice == "🎨 Creator Advocacy":
    show_creator_dashboard()

# Footer
st.markdown("---")
col1, col2, col3 = st.columns(3)
with col2:
    st.caption("© 2024 Dolby Marketing Analytics Dashboard | Data refreshes hourly")
