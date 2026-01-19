# African Beer Market Intelligence Snapshot

A comprehensive data visualization dashboard analyzing beer consumption patterns, production volumes, pricing dynamics, and digital retail trends across 15 major African markets as of 2025.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Data Sources](#data-sources)
- [Technical Stack](#technical-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Dashboard Components](#dashboard-components)
- [Data Dictionary](#data-dictionary)
- [Key Insights](#key-insights)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

This interactive dashboard provides strategic market intelligence for the African beer industry, covering 15 countries across four sub-regions: Southern Africa, East Africa, West Africa, and Central Africa. The web-app dashboard enables users to explore relationships between production capacity, consumption patterns, pricing strategies, and emerging digital retail channels.

### Project Objectives

- Provide comparative analysis of beer markets across African regions
- Visualize the relationship between production volumes and per-capita consumption
- Track pricing variations across different market segments
- Map digital retail adoption and e-commerce channels
- Enable data-driven decision-making for market entry and expansion strategies

---

## Features

### Interactive Filtering System
- **Regional Selection**: Multi-select filter for African sub-regions (Southern, East, West, Central Africa)
- **Production Volume Filter**: Slider control to filter markets by production capacity (0-35 million hectoliters)
- **Price Range Filter**: Dynamic pricing filter ($0.85 - $4.50 per 500ml bottle)

### Real-Time Analytics
- **Dynamic KPI Cards**: Auto-updating metrics based on filter selections
  - Number of markets analyzed
  - Average beer price across selected markets
  - Total production volume
  - Top consuming market with per-capita data

### Visualizations
- **Interactive Scatter Plot**: Consumption vs. Production analysis with regional color coding
- **Hover Tooltips**: Detailed market information on data point interaction
- **Regional Performance Summary**: Comparative production and consumption metrics by region

### Data Exploration
- **Comprehensive Data Table**: Sortable, filterable table with progress indicators for consumption metrics
- **Consumer Sentiment Analysis**: Expandable section with market-specific taste preferences and cultural insights
- **Digital Retail Intelligence**: E-commerce platforms and delivery services by market

### Export Capability
- **CSV Download**: Export filtered data for further analysis in Excel, Python, or other tools

---

## Data Sources

This analysis synthesizes data from multiple authoritative sources:

- **Business Insider Africa Article** - Market reports on beer production nations in Africa. [Business Insider Africa: Top 10 African countries with the highest beer production](https://africa.businessinsider.com/local/markets/business-insider-africa-presents-the-top-10-african-countries-with-the-highest-beer/g41xx5z)
- **Kirin Holdings Global Beer Report (2022)** - International beer production and consumption data
- **Global Data Consolidations** - Industry analysis and market trends
- **WHO Global Health Observatory** - Public health and alcohol consumption data
- **Primary Research** - Digital retail channel verification (2024-2025)

**Data Timeline**: Primary dataset spans 2022-2025, with production and consumption figures reflecting the most recent available statistics.

---

## Technical Stack

### Core Technologies
- **Python 3.8+**: Primary programming language
- **Streamlit 1.28+**: Web application framework
- **Pandas 2.0+**: Data manipulation and analysis
- **Altair 5.0+**: Declarative statistical visualization library

### Key Libraries
```python
streamlit>=1.28.0
pandas>=2.0.0
altair>=5.0.0
```

### Design Framework
- **Custom CSS**: Responsive design with gradient backgrounds and card-based layout
- **Color Scheme**: Warm amber/brown palette (primary: #78350f, #b45309)
- **Typography**: Segoe UI font family for clean, professional appearance

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/Ogombo-collins/African-Beer-Market-Snapshot-ast-at-2025.git
cd african-beer-market-intelligence
```

2. **Create Virtual Environment** (Optional but recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the Application**
```bash
streamlit run app.py
```

5. **Access the Dashboard**
The application will automatically open in your default browser at `http://localhost:8501`

---

## Usage (Web-App)

### Basic Navigation

1. **Filter Markets**: Use the sidebar controls to narrow down your analysis
   - Select specific regions of interest
   - Adjust production volume threshold
   - Set price range parameters

2. **Explore Visualizations**: 
   - Hover over scatter plot points for detailed market information
   - Identify outliers and patterns in consumption vs. production
   - Compare regional performance metrics

3. **Review Data Tables**: 
   - Sort by any column to identify leaders in specific metrics
   - Use progress bars to quickly assess consumption intensity
   - Cross-reference digital retail channels for market entry planning

4. **Export Data**: 
   - Apply desired filters
   - Click "Download Filtered Data" button
   - Save CSV file for offline analysis

### Sample Use Cases

**Market Entry Analysis**
```
Goal: Identify affordable markets with high consumption
Steps: 
1. Set price range to $0.85 - $1.50
2. Sort by liters_per_capita (descending)
3. Review digital_channels for distribution opportunities
```

**Regional Comparison**
```
Goal: Compare Southern Africa vs. East Africa markets
Steps:
1. Filter to Southern Africa only, note KPIs
2. Filter to East Africa only, compare KPIs
3. Reset to both regions for side-by-side visualization
```

**Premium Market Analysis**
```
Goal: Find high-price, high-consumption markets
Steps:
1. Set price range to $2.00 - $4.50
2. Review top brands and consumer sentiment
3. Identify premium positioning opportunities
```

---

## Dashboard Components

### Header Section
- Project title and description
- Visual branding with gradient background

### KPI Dashboard
Four dynamic metric cards displaying:
- **Markets Analyzed**: Count of countries meeting filter criteria
- **Average Price**: Mean retail price across selected markets
- **Total Production**: Sum of production volumes (million hectoliters)
- **Top Consumer**: Country with highest per-capita consumption

### Interactive Visualization
**Market Dynamics Scatter Plot**
- **X-axis**: Production volume (million hectoliters)
- **Y-axis**: Per-capita consumption (liters)
- **Color**: Regional classification
- **Labels**: Country names
- **Interactivity**: Hover tooltips, zoom, pan

### Data Table
Comprehensive market data with custom column configurations:
- **Country & Region**: Text identifiers
- **Consumption**: Progress bar visualization (0-150L scale)
- **Production**: Numeric display with million hectoliters format
- **Avg Price**: Currency-formatted ($) values
- **Top Brands**: Leading market brands
- **Digital Channels**: E-commerce and delivery platforms
- **Interactivity**: Click full screen icon on top right to see whole table

### Consumer Insights
Expandable section containing market-specific observations:
- Taste preferences and cultural context
- Brand loyalty patterns
- Temperature and serving preferences
- Beer style trends (lager, dark beer, sorghum beer, etc.)

### Regional Performance Summary
Three-column comparative view:
- **Production Leaders**: Total output by region with trophy indicators
- **Consumption Metrics**: Average and total consumption statistics
- **Regional Rankings**: Per-capita consumption intensity by region

---

## Data Dictionary

### Core Metrics

| Field | Type | Description | Unit | Range |
|-------|------|-------------|------|-------|
| `country` | String | African nation name | - | 15 markets |
| `region` | Categorical | Sub-regional classification | - | Southern, East, West, Central Africa |
| `liters_per_capita` | Float | Annual per-person consumption | Liters | 7.3 - 150.0 |
| `production_m_hl` | Float | Total national beer production | Million hectoliters | 0.12 - 35.10 |
| `avg_price_usd` | Float | Average retail price (500ml bottle) | USD | $0.85 - $4.50 |
| `top_brands` | String | Leading beer brands in market | - | Comma-separated list |
| `review_snapshot` | String | Consumer taste preferences summary | - | Text description |
| `digital_channels` | String | E-commerce and delivery platforms | - | Comma-separated list |

### Calculated Metrics

- **Average Price**: Mean of `avg_price_usd` across filtered markets
- **Total Production**: Sum of `production_m_hl` across filtered markets
- **Top Consumer**: Country with maximum `liters_per_capita` value
- **Markets Analyzed**: Count of countries meeting filter criteria

---

## Key Insights

### Market Leaders

**Highest Per-Capita Consumption**
1. Botswana - 150.0 L/capita (Southern Africa)
2. Namibia - 90.8 L/capita (Southern Africa)
3. Gabon - 78.3 L/capita (Central Africa)

**Largest Production Volumes**
1. South Africa - 35.10 million hl (Southern Africa)
2. Nigeria - 17.73 million hl (West Africa)
3. Ethiopia - 12.67 million hl (East Africa)

**Pricing Segments**
- **Premium Markets**: Seychelles ($4.50), Kenya ($2.30), Zimbabwe ($1.80)
- **Mid-Range Markets**: Botswana ($1.80), Namibia ($1.60), South Africa ($1.50)
- **Value Markets**: Angola ($0.85), Ethiopia ($0.95), Mozambique ($1.12)

### Regional Patterns

**Southern Africa**
- Highest per-capita consumption globally
- Mature markets with established beer culture
- Strong digital retail infrastructure
- Premium and traditional brands coexist

**East Africa**
- Moderate consumption, high production capacity
- Strong national brand loyalty (e.g., Tusker in Kenya, Nile Special in Uganda)
- Emerging craft beer movement
- Growing digital delivery services

**West Africa**
- Large population markets with lower per-capita consumption
- Guinness brand dominance in Nigeria
- Expanding production capacity
- Early-stage e-commerce adoption

**Central Africa**
- Limited market data availability
- French brewery influence (Castel)
- Gabon shows high per-capita consumption
- Developing digital retail channels

### Consumer Behavior Insights

- **Temperature Preference**: Most markets emphasize "ice-cold" serving (Angola, Botswana)
- **Format Preference**: Large-format bottles popular in Cameroon (65cl)
- **Heritage Loyalty**: Strong attachment to local brands (Regab in Gabon, St. George in Ethiopia)
- **Market Segmentation**: Clear split between traditional lagers and sorghum beer in Zimbabwe

---

## Future Enhancements

### Planned Features (Welcome to collaborators who can help with these:)

**Version 2.0**
- [ ] Time-series analysis showing market growth trends (2020-2025)
- [ ] Market attractiveness scoring model incorporating GDP, urbanization, competition
- [ ] Brewery ownership mapping (SABMiller, Heineken, Castel, local)
- [ ] Import/export flow visualization

**Version 2.1**
- [ ] Consumer demographic overlay (age distribution, income levels)
- [ ] Regulatory environment index by market
- [ ] Distribution infrastructure mapping
- [ ] Seasonal consumption patterns

**Version 3.0**
- [ ] Predictive analytics for market growth forecasting
- [ ] Competitor analysis dashboard
- [ ] Investment opportunity scoring
- [ ] API integration for real-time data updates

### Data Expansion
- Add remaining African markets (Morocco, Algeria, Ivory Coast, Senegal, etc.)
- Incorporate craft beer segment analysis
- Include non-alcoholic beer trends
- Add spirits and wine categories for complete beverage alcohol view

---

## Contributing

Contributions are welcome! To contribute to this project:

### Reporting Issues
- Use GitHub Issues to report bugs or suggest features
- Provide detailed description with steps to reproduce (for bugs)
- Include screenshots if applicable

### Submitting Changes
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### Data Updates
To suggest data corrections or additions:
- Provide authoritative source citations
- Include publication date and access date
- Specify exact metric being updated

### Code Standards
- Follow PEP 8 style guidelines for Python code
- Include docstrings for new functions
- Update README.md for new features
- Test dashboard functionality before submitting PR

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Usage Terms
- Free for academic and non-commercial use
- Commercial use requires attribution
- Data sources must be cited when publishing derivative works

---

## Contact

**Developer**: Collins Ogombo

**Project Repository**: [GitHub - African Beer Market Intelligence](https://github.com/Ogombo-collins/African-Beer-Market-Snapshot-ast-at-2025.git)

**Questions or Feedback**: Open an issue on GitHub or contact via [collinsogomboochiko@gmail.com]

---

## Acknowledgments

- Business Insider Africa for market intelligence reporting
- Kirin Holdings for comprehensive global beer production data
- WHO Global Health Observatory for public health statistics
- African e-commerce platforms for digital retail verification
- Streamlit community for visualization framework support

---

## Changelog

### Version 1.0.0 (January 2026)
- Initial release with 15 African markets
- Interactive filtering system (region, production, price)
- Scatter plot visualization with regional color coding
- Comprehensive data table with custom formatting
- Consumer sentiment snapshots
- Regional performance summaries
- CSV export functionality
- Responsive design with custom CSS

---

**Last Updated**: January 19, 2026  
**Data Version**: 2025 Market Snapshot  
**Dashboard Version**: 1.0.0