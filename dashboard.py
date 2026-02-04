import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Page config
st.set_page_config(
    page_title="Square Seller Insights",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("Square Seller Insights Dashboard")
st.markdown("*Analysis of 1,000+ seller reviews from Square and Shopify*")
st.markdown("---")

# Load data
@st.cache_data
def load_data():
    square = pd.read_csv("square_reviews_analyzed.csv")
    shopify = pd.read_csv("shopify_reviews_analyzed.csv")
    return square, shopify

square_df, shopify_df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
rating_filter = st.sidebar.slider("Rating Range", 1, 5, (1, 5))

square_filtered = square_df[
    (square_df['rating'] >= rating_filter[0]) & 
    (square_df['rating'] <= rating_filter[1])
]
shopify_filtered = shopify_df[
    (shopify_df['rating'] >= rating_filter[0]) & 
    (shopify_df['rating'] <= rating_filter[1])
]

# Top metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Reviews", f"{len(square_filtered) + len(shopify_filtered):,}")
with col2:
    square_rating = square_filtered['rating'].mean()
    st.metric("Square Avg Rating", f"{square_rating:.2f}/5")
with col3:
    shopify_rating = shopify_filtered['rating'].mean()
    delta = square_rating - shopify_rating
    st.metric("Shopify Avg Rating", f"{shopify_rating:.2f}/5", delta=f"{delta:.2f} lower", delta_color="inverse")
with col4:
    square_churn = (square_filtered['is_churn_risk'].sum() / len(square_filtered) * 100)
    st.metric("Square Churn Risk", f"{square_churn:.1f}%")

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Key Findings", 
    "Analysis", 
    "Competitive Comparison", 
    "Recommendations",
    "Methodology"
])

with tab1:
    st.header("Key Findings")
    
    st.success("**Finding #1:** Square maintains a 3.08/5 rating compared to Shopify's 2.17/5 — a full point advantage indicating significantly higher seller satisfaction.")
    
    st.warning("**Finding #2:** 77% of Shopify sellers show churn risk compared to 51% for Square, representing 50% higher likelihood of sellers leaving the Shopify platform.")
    
    st.info("**Finding #3:** Support is the #1 concern for both platforms (183 Square mentions, 154 Shopify mentions), presenting a clear optimization opportunity.")

with tab2:
    st.header("Square Seller Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sentiment Distribution")
        sentiment_data = square_filtered['sentiment'].value_counts().reset_index()
        sentiment_data.columns = ['sentiment', 'count']
        fig = px.bar(sentiment_data, x='sentiment', y='count', 
                     title="Square shows polarization: strong positive and negative sentiment")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Top Themes")
        theme_data = square_filtered['theme'].value_counts().head(5).reset_index()
        theme_data.columns = ['theme', 'count']
        fig = px.bar(theme_data, x='theme', y='count',
                     title="Support and ease-of-use are primary concerns")
        st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.header("Square vs Shopify")
    
    st.subheader("Key Metrics Comparison")
    comparison = pd.DataFrame({
        'Metric': ['Average Rating', 'Churn Risk'],
        'Square': [
            f"{square_filtered['rating'].mean():.2f}/5",
            f"{(square_filtered['is_churn_risk'].sum()/len(square_filtered)*100):.1f}%"
        ],
        'Shopify': [
            f"{shopify_filtered['rating'].mean():.2f}/5",
            f"{(shopify_filtered['is_churn_risk'].sum()/len(shopify_filtered)*100):.1f}%"
        ],
        'Square Advantage': [
            f"+{square_rating - shopify_rating:.2f} points",
            f"-{((square_filtered['is_churn_risk'].sum()/len(square_filtered)) - (shopify_filtered['is_churn_risk'].sum()/len(shopify_filtered)))*100:.1f}%"
        ]
    })
    st.table(comparison)
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Sentiment Comparison")
        square_sentiment = square_filtered['sentiment'].value_counts().reset_index()
        square_sentiment.columns = ['sentiment', 'count']
        square_sentiment['platform'] = 'Square'
        
        shopify_sentiment = shopify_filtered['sentiment'].value_counts().reset_index()
        shopify_sentiment.columns = ['sentiment', 'count']
        shopify_sentiment['platform'] = 'Shopify'
        
        combined = pd.concat([square_sentiment, shopify_sentiment])
        fig = px.bar(combined, x='sentiment', y='count', color='platform', 
                     barmode='group', title="Shopify skews significantly more negative")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("Theme Comparison")
        square_themes = square_filtered['theme'].value_counts().head(5).reset_index()
        square_themes.columns = ['theme', 'count']
        square_themes['platform'] = 'Square'
        
        shopify_themes = shopify_filtered['theme'].value_counts().head(5).reset_index()
        shopify_themes.columns = ['theme', 'count']
        shopify_themes['platform'] = 'Shopify'
        
        combined_themes = pd.concat([square_themes, shopify_themes])
        fig = px.bar(combined_themes, x='theme', y='count', color='platform', 
                     barmode='group', title="Similar pain points across platforms")
        st.plotly_chart(fig, use_container_width=True)

with tab4:
    st.header("Product Recommendations")
    
    st.markdown("""
    Based on analysis of 1,000+ seller reviews, here are three data-driven recommendations 
    to strengthen Square's market position:
    """)
    
    st.markdown("---")
    
    st.subheader("1. Target Frustrated Shopify Sellers")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **The Opportunity**
        
        Shopify demonstrates 77% churn risk versus Square's 51%, with an average rating 
        nearly one full point lower. This dissatisfaction represents a significant 
        acquisition opportunity.
        
        **Recommended Actions**
        - Build seamless Shopify-to-Square migration tools with data import capabilities
        - Launch targeted campaign: "Switch from Shopify in 3 Steps"
        - Offer first-quarter fee reduction for verified Shopify switchers
        - Develop case studies showcasing successful migrations and outcomes
        
        **Success Metrics**
        - Migration tool adoption rate
        - Shopify-to-Square conversion rate
        - 90-day retention of migrated sellers
        - Post-migration satisfaction scores
        """)
    
    with col2:
        st.info("""
        **Expected Impact**
        
        10-20% capture rate of dissatisfied Shopify sellers
        
        **Implementation**
        
        Q2 2026: Launch migration tools
        
        Q3 2026: Full marketing campaign
        """)
    
    st.markdown("---")
    
    st.subheader("2. Optimize Support Operations")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **The Data**
        
        Support is the #1 complaint theme across both platforms. However, this represents 
        an opportunity: improving support could differentiate Square and reduce churn.
        
        **Recommended Actions**
        - Implement AI-powered support triage to reduce initial response times
        - Reduce first-response target from 24 hours to under 4 hours
        - Create tiered support based on seller revenue and complexity
        - Expand weekend coverage and add live chat for urgent issues
        - Build predictive support system that proactively identifies struggling sellers
        
        **Success Metrics**
        - Average first response time
        - Support satisfaction (CSAT) scores
        - First-contact resolution rate
        - Correlation between support quality and retention
        """)
    
    with col2:
        st.warning("""
        **Expected Impact**
        
        15-25% reduction in churn risk
        
        20+ point improvement in CSAT
        
        **Implementation**
        
        Q2 2026: AI triage pilot
        
        Q3 2026: Full rollout
        """)
    
    st.markdown("---")
    
    st.subheader("3. Address Sentiment Polarization")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        **The Pattern**
        
        Square shows clear polarization: 43% very negative, 43% very positive, with only 
        14% in the middle. This suggests the product works extremely well for some segments 
        but poorly for others.
        
        **Recommended Actions**
        - Conduct in-depth interviews with very negative sellers to identify root causes
        - Segment analysis to understand which seller types succeed vs struggle
        - Create multiple onboarding paths tailored to seller segment and use case
        - Build early warning system to identify at-risk sellers within first 30 days
        - Implement proactive white-glove onboarding for complex or high-value accounts
        
        **Success Metrics**
        - Reduction in "very negative" sentiment percentage
        - Increase in "positive" and "neutral" (the middle ground)
        - Segment-specific satisfaction and retention rates
        - 90-day success rate by cohort
        """)
    
    with col2:
        st.success("""
        **Expected Impact**
        
        10-15% improvement in overall satisfaction
        
        Shift toward balanced distribution
        
        **Implementation**
        
        Q2 2026: Research phase
        
        Q3 2026: Segmented onboarding launch
        """)

with tab5:
    st.header("Methodology")
    
    st.markdown("""
    This analysis demonstrates an AI-native approach to product research: using AI tools 
    to accelerate data processing while maintaining complete ownership of strategy, 
    framework design, and recommendations.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Research Approach")
        st.markdown("""
        **Data Collection**
        - Collected 1,000+ reviews from iTunes App Store API
        - Sources: Square Point of Sale and Shopify apps
        - Time period: July 2025 - February 2026
        - Represents real seller feedback across both platforms
        
        **Analysis Framework**
        - Designed classification schema for themes and sentiment
        - Used GPT-4o-mini for structured data extraction at scale
        - Validated outputs for consistency and accuracy
        - Synthesized patterns into strategic insights
        
        **Product Strategy**
        - Identified competitive positioning opportunities
        - Connected data insights to business outcomes
        - Developed actionable recommendations with success metrics
        - Prioritized based on expected impact and feasibility
        """)
    
    with col2:
        st.subheader("AI Usage")
        st.markdown("""
        **Where AI Helped**
        - Processing 1,000 reviews in 30 minutes (vs weeks of manual analysis)
        - Consistent categorization of themes and sentiment
        - Pattern identification across large dataset
        - Code development and debugging assistance
        
        **Where Human Judgment Was Essential**
        - Defining what questions to ask
        - Designing the analysis framework
        - Choosing competitive benchmarks
        - Interpreting what the data means for product strategy
        - Making strategic recommendations
        - Building the narrative and dashboard
        
        This represents modern product work: leveraging AI for speed and scale 
        while maintaining complete creative and strategic control.
        """)
    
    st.markdown("---")
    
    st.subheader("Technical Implementation")
    
    tech_stack = pd.DataFrame({
        'Component': ['Data Collection', 'Analysis', 'Dashboard', 'Deployment'],
        'Technology': ['iTunes API + Python', 'OpenAI GPT-4o-mini', 'Streamlit + Plotly', 'Streamlit Cloud + GitHub'],
        'Why This Choice': [
            'Free public API with 500+ reviews per app available',
            'Optimal price-to-performance ratio for text classification',
            'Rapid prototyping with professional results',
            'Free hosting with shareable public URL'
        ]
    })
    
    st.table(tech_stack)
    
    st.markdown("---")
    
    st.info("""
    **Primary Insight:** Analysis reveals that Shopify sellers demonstrate 50% higher churn risk 
    and rate the platform 0.91 points lower than Square sellers, representing a significant 
    market opportunity for targeted acquisition and positioning strategies.
    """)

st.markdown("---")
st.caption("Created by Shreeya Rishi Kairamkonda | February 2026")