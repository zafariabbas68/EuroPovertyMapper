
# EuroPovertyMapper 🌍📊

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Eurostat Data](https://img.shields.io/badge/data-Eurostat-orange)](https://ec.europa.eu/eurostat)

A comprehensive Python tool for analyzing and visualizing poverty risk across European regions using Eurostat data. Create stunning, publication-ready choropleth maps with advanced statistical analysis.

## 📋 Overview

EuroPovertyMapper processes real-time Eurostat data to generate high-quality visualizations of poverty risk across European NUTS2 regions. The project combines geospatial analysis, statistical processing, and professional visualization to provide insights into European social inequality patterns.

![Example Map](https://via.placeholder.com/800x500.png?text=EuroPovertyMapper+Visualization)

## ✨ Features

- **📊 Real-time Data**: Automated fetching from Eurostat API
- **🗺️ Professional Maps**: Multiple color schemes and styles
- **📈 Statistical Analysis**: Comprehensive regional and country-level insights
- **🎨 Customizable Visuals**: Ultra-high resolution (400 DPI) outputs
- **🔧 Robust Processing**: Handles data inconsistencies and missing values
- **📁 Multiple Formats**: PNG, PDF, SVG export options

## 🚀 Quick Start

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/yourusername/euro-poverty-mapper.git
cd euro-poverty-mapper
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from euro_poverty_mapper import EuroPovertyMapper

# Initialize the mapper
mapper = EuroPovertyMapper()

# Generate a poverty risk map
fig, analysis = mapper.generate_map(year=2024, style='ultra_visual')

# Save the visualization
mapper.save_map(fig, 'europe_poverty_2024.png')

# View statistical analysis
print(analysis.summary)
```

### Jupyter Notebook Example

```python
# Import the module
import euro_poverty_mapper as epm

# Load and process data
data = epm.load_eurostat_data()
processed_data = epm.process_data(data)

# Create visualization
fig = epm.create_visualization(processed_data, style='ocean_theme')
plt.show()

# Generate analysis report
report = epm.generate_analysis_report(processed_data)
print(report)
```

## 📊 Sample Output

### Statistical Summary (2024 Data)
```
EUROPEAN POVERTY RISK ANALYSIS
================================
📊 BASIC STATISTICS:
• Regions analyzed: 327 NUTS2 regions
• Average poverty rate: 21.1%
• Range: 6.6% (lowest) to 59.5% (highest)
• Standard deviation: 7.9%

🌍 REGIONAL PATTERNS:
• Highest risk: Bulgaria (31.7%), Greece (28.5%), Romania (27.7%)
• Lowest risk: Czechia (11.4%), Slovenia (14.4%), Netherlands (15.4%)
```

### Risk Category Distribution
- 🔵 Very Low Risk (<12.5%): 9.2% of regions
- 🟢 Low Risk (12.5-15.5%): 14.7% of regions  
- 🟡 Medium-Low Risk (15.5-19.5%): 24.8% of regions
- 🟠 Medium-High Risk (19.5-25.0%): 27.2% of regions
- 🔴 High Risk (25.0-33.0%): 13.8% of regions
- ⚫ Very High Risk (≥33.0%): 10.4% of regions

## 🛠️ Technical Details

### Data Sources
- **Primary**: Eurostat API (ILC_PEPS11N, ILC_PEPS01N)
- **Geographical**: Eurostat GISCO NUTS 2021 Level 2
- **Coverage**: 334 NUTS2 regions across Europe

### Dependencies
```txt
pandas>=1.5.0
geopandas>=0.12.0
matplotlib>=3.6.0
requests>=2.28.0
numpy>=1.21.0
contextily>=1.3.0
```

### Project Structure
```
euro-poverty-mapper/
├── src/
│   ├── data_processor.py    # Data fetching and cleaning
│   ├── spatial_analyzer.py  # Geospatial operations
│   ├── visualizer.py        # Map generation
│   └── analyzer.py          # Statistical analysis
├── examples/
│   ├── basic_usage.ipynb    # Getting started guide
│   └── advanced_analysis.ipynb
├── outputs/                 # Generated visualizations
├── tests/                   # Unit tests
└── docs/                    # Documentation
```

## 🎨 Visualization Styles

### Available Color Schemes
1. **`vibrant_rainbow`** - High contrast for maximum visibility
2. **`ocean_blues`** - Professional and calm appearance  
3. **`sunset_oranges`** - Warm and engaging
4. **`forest_greens`** - Natural and intuitive
5. **`purple_majesty`** - Modern and distinctive
6. **`luxury_gold`** - Premium and sophisticated

### Output Quality
- **Resolution**: 400 DPI (print-ready)
- **Formats**: PNG, PDF, SVG
- **Transparency**: Optional transparent backgrounds
- **Customization**: Full control over all visual elements

## 📈 Use Cases

### Academic Research
- Regional inequality studies
- Social policy impact assessment
- Comparative European analysis

### Policy Making
- Resource allocation planning
- Regional development strategies
- EU cohesion policy evaluation

### Data Journalism
- Interactive data stories
- Publication-ready graphics
- Social inequality reporting

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/yourusername/euro-poverty-mapper.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
pytest tests/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Eurostat** for providing comprehensive European statistics
- **GISCO** for geographical data services
- **Matplotlib** and **GeoPandas** communities for excellent visualization tools

## 📞 Support

- 📧 **Email**: your-email@example.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/yourusername/euro-poverty-mapper/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/yourusername/euro-poverty-mapper/discussions)

## 🔗 Related Projects

- [EuroStat-Data-Visualizer](https://github.com/example/eurostat-visualizer) - General Eurostat data visualization
- [EU-Regional-Analytics](https://github.com/example/eu-analytics) - Comprehensive EU regional analysis toolkit

---

<div align="center">
  
**Made with ❤️ for the European data community**

*Understanding inequality through data visualization*

</div>
```

## Key Repository Files Structure

```
EuroPovertyMapper/
├── README.md
├── TECHNICAL_REPORT.md
├── requirements.txt
├── setup.py
├── src/
│   ├── __init__.py
│   ├── data_processor.py
│   ├── spatial_analyzer.py
│   ├── visualizer.py
│   └── analyzer.py
├── examples/
│   ├── basic_usage.ipynb
│   ├── advanced_analysis.ipynb
│   └── sample_outputs/
├── tests/
│   ├── __init__.py
│   ├── test_data_processing.py
│   └── test_visualization.py
├── docs/
│   ├── installation.md
│   ├── api_reference.md
│   └── contributing.md
├── outputs/
│   └── sample_maps/
└── CONTRIBUTING.md
```

This repository structure and documentation provide a professional foundation for your Eurostat poverty mapping project that will be valuable for both technical users and general audiences interested in European social data analysis.
