# Create README.md
cat > README.md << 'EOF'
# Square Seller Insights Dashboard

**Live Demo:** [square-seller-insights.streamlit.app](https://square-seller-insights.streamlit.app)

An AI-powered product intelligence system analyzing 1,000+ seller reviews from Square and Shopify to identify competitive opportunities and inform product strategy.

![Dashboard Preview](https://img.shields.io/badge/Status-Live-success)
![Python](https://img.shields.io/badge/Python-3.10-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.54.0-red)

---

## Key Findings

**Finding #1:** Square maintains a 3.08/5 rating vs Shopify's 2.17/5 — a full point advantage

**Finding #2:** 77% of Shopify sellers show churn risk vs 51% for Square (50% higher)

**Finding #3:** Support is the #1 concern for both platforms, presenting optimization opportunity

---

## Project Overview

This project demonstrates my approach to product research and strategy:
- Identify high-value data sources
- Extract insights at scale using AI
- Translate findings into actionable recommendations
- Build professional deliverables

### What I Built

- **Data Pipeline:** Collected 1,000+ reviews from iTunes App Store API
- **AI Analysis:** Used GPT-4o-mini to categorize themes, sentiment, and churn signals
- **Interactive Dashboard:** Built with Streamlit and Plotly for data exploration
- **Strategic Recommendations:** Developed 3 data-driven product opportunities

---

## Technical Stack

| Component | Technology | Why |
|-----------|------------|-----|
| Data Collection | iTunes API + Python | Free, reliable, 500+ reviews per app |
| AI Analysis | OpenAI GPT-4o-mini | Optimal price/performance for classification |
| Dashboard | Streamlit + Plotly | Rapid development, professional results |
| Deployment | Streamlit Cloud + GitHub | Free hosting, version control |

---

## Repository Structure
```
square-seller-insights/
├── dashboard.py                      # Main Streamlit application
├── requirements.txt                  # Python dependencies
├── square_reviews_analyzed.csv       # Analyzed Square reviews
├── shopify_reviews_analyzed.csv      # Analyzed Shopify reviews
└── README.md                         # This file
```

---

## Features

### 1. Interactive Dashboard
- Filter by rating range
- Explore across multiple dimensions
- Real-time data updates

### 2. Competitive Analysis
- Side-by-side comparison of Square vs Shopify
- Sentiment distribution analysis
- Theme frequency comparison

### 3. Data-Driven Recommendations
- Target frustrated Shopify sellers
- Optimize support operations
- Address sentiment polarization

### 4. Transparent Methodology
- Clear documentation of approach
- Explanation of AI usage
- Technical implementation details

---

## Methodology

### Data Collection
- Scraped 500+ reviews per platform from iTunes App Store
- Time period: July 2025 - February 2026
- Focus on Square Point of Sale and Shopify apps

### AI Analysis
- Designed classification schema for themes and sentiment
- Used GPT-4o-mini for structured data extraction
- Validated outputs for consistency and accuracy
- Processed 1,000 reviews in ~30 minutes

### Analysis Framework
- **Sentiment:** very_positive, positive, neutral, negative, very_negative
- **Themes:** support, ease-of-use, pricing, features, reliability, integration
- **Churn Risk:** Boolean indicator based on negative sentiment + specific language patterns
- **Feature Mentions:** Extracted specific product features mentioned

---

## Key Insights

### Competitive Opportunity
Shopify sellers demonstrate 50% higher churn risk and rate the platform 0.91 points lower than Square sellers, representing a significant acquisition opportunity.

### Support as Differentiator
Support is the #1 complaint for both platforms, but Square outperforms. Doubling down on support excellence could create a lasting competitive moat.

### Polarization Problem
Square shows clear polarization (43% very negative, 43% very positive). Understanding why certain sellers succeed while others struggle presents an opportunity to improve product-market fit.

---

## Product Recommendations

### 1. Target Frustrated Shopify Sellers
**Expected Impact:** 10-20% capture rate of dissatisfied Shopify merchants

**Actions:**
- Build Shopify-to-Square migration tools
- Launch "Switch in 3 Steps" campaign
- Offer first-quarter fee reduction

### 2. Optimize Support Operations
**Expected Impact:** 15-25% reduction in churn risk

**Actions:**
- Implement AI-powered support triage
- Reduce response time from 24h to 4h
- Expand weekend coverage

### 3. Address Sentiment Polarization
**Expected Impact:** 10-15% improvement in overall satisfaction

**Actions:**
- Segment-specific onboarding flows
- Early warning system for at-risk sellers
- Proactive white-glove support for complex accounts

---

## Running Locally
```bash
# Clone repository
git clone https://github.com/ShreeyaRishi/square-seller-insights.git
cd square-seller-insights

# Install dependencies
pip install -r requirements.txt

# Run dashboard
streamlit run dashboard.py
```

The dashboard will open at `http://localhost:8501`

---

## About This Project

This project was built as part of my application for the Square Associate Product Manager program. It demonstrates:

- **AI-Native Approach:** Using AI to accelerate analysis while maintaining strategic control
- **Product Thinking:** Connecting data insights to business strategy and outcomes
- **Technical Execution:** Building and deploying production-ready applications
- **Communication:** Presenting complex analysis in accessible, actionable formats

### What AI Did
- Processed 1,000 reviews in 30 minutes
- Consistent categorization at scale
- Code assistance and debugging

### What I Did
- Defined the research framework and questions
- Designed the analysis methodology
- Chose competitive benchmarks
- Interpreted findings through a product lens
- Made strategic recommendations
- Built and deployed the dashboard

---

## Contact

**Shreeya Rishi Kairamkonda**
- Email: shreeyarishikairamkonda@gmail.com
- LinkedIn: [linkedin.com/in/shreeyarishik](https://linkedin.com/in/shreeyarishik)
- GitHub: [@ShreeyaRishi](https://github.com/ShreeyaRishi)

---

## License

This project is open source and available for educational purposes.

---

*Built with ❤️ for Square | February 2026*
EOF

echo "✅ README.md created!"