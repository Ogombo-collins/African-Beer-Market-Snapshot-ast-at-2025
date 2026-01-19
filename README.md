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

This interactive dashboard provides strategic market intelligence for the African beer industry, covering 15 countries across four sub-regions: Southern Africa, East Africa, West Africa, and Central Africa. The application enables users to explore relationships between production capacity, consumption patterns, pricing strategies, and emerging digital retail channels.

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
- **Production Volume Filter**: Slider control to filter markets by production capacity (0–35 million hectoliters)
- **Price Range Filter**: Dynamic pricing filter ($0.85–$4.50 per 500ml bottle)

### Real-Time Analytics
- **Dynamic KPI Cards**: Auto-updating metrics based on filter selections
  - Number of markets analyzed
  - Average beer price across selected markets
  - Total production volume
  - Top consuming market with per-capita data

### Visualizations
- **Interactive Scatter Plot**: Consumption vs. production analysis with regional color coding
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

- **Business Insider Africa** – Market reports and consumption statistics
- **Kirin Holdings Global Beer Report (2022)** – International beer production and consumption data
- **Global Data Consolidations** – Industry analysis and market trends
- **WHO Global Health Observatory** – Public health and alcohol consumption data
- **Primary Research** – Digital retail channel verification (2024–2025)

**Data Timeline**: Primary dataset spans 2022–2025, with production and consumption figures reflecting the most recent available statistics as of January 2025.

---

## Technical Stack

### Core Technologies
- **Python 3.8+** – Primary programming language
- **Streamlit 1.28+** – Web application framework
- **Pandas 2.0+** – Data manipulation and analysis
- **Altair 5.0+** – Declarative statistical visualization library

### Key Libraries
```python
streamlit>=1.28.0
pandas>=2.0.0
altair>=5.0.0

## Installation
