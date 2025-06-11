# jskaza.github.io

🌟 **A modern, elegant academic website** showcasing research, publications, and professional work with a focus on clean design and exceptional user experience.

**Visit: [jskaza.github.io](https://jskaza.github.io)**

## 🚀 Key Features

### ⚡ Lightning-Fast Performance
Built with [**Zola**](https://www.getzola.org/) (written in Rust), delivering incredibly fast builds.

### 📄 Data-Driven Content
- **Simple TOML files** contain all data - that's all that needs to be managed!

### 🎓 Automated Google Scholar Integration
- `fetch_pubs.py` script automatically pulls latest publications from Google Scholar
- Keeps publication list always up-to-date without manual intervention

### 📋 Dynamic CV Generation
- CV PDF is automatically built using [**Typst**](https://typst.app/) from the same TOML data
- Single source of truth for all professional information
- Consistent information between website and CV

### 🎨 Modern Design
- Clean, responsive design optimized for academic portfolios
- Fast loading times thanks to Zola's efficient static site generation
- Professional appearance suitable for academic and research contexts

## 📋 Requirements

### Core Dependencies

#### Zola
Static site generator (written in Rust)
```bash
# Install via package manager (recommended)
# macOS
brew install zola

# Linux
# Debian/Ubuntu
sudo apt install zola
# Or download from: https://github.com/getzola/zola/releases
```

#### Python 3.7+
Required for automated publication fetching
```bash
# Install Python packages
pip install scholarly tomli-w tqdm
```

#### Typst
Modern typesetting system for CV generation
```bash
# Install via package manager
# macOS
brew install typst

# Linux
# Download from: https://github.com/typst/typst/releases
# Or use cargo: cargo install --git https://github.com/typst/typst --locked typst-cli
```

### Python Package Details

The `fetch_pubs.py` script requires:
- **`scholarly`** - For Google Scholar API access and publication data retrieval
- **`tomli-w`** - For writing TOML configuration files
- **`tqdm`** - For progress bars during publication fetching

### Typst Package Dependencies

The CV template uses:
- **`@preview/fontawesome:0.5.0`** - FontAwesome icons (automatically downloaded by Typst)

### Quick Setup
```bash
# 1. Install Zola
brew install zola  # macOS
# or download from GitHub releases for other platforms

# 2. Install Python dependencies
pip install scholarly tomli-w tqdm

# 3. Install Typst
brew install typst  # macOS
# or download from GitHub releases

# 4. Build the site
zola build

# 5. Serve locally for development
zola serve
```
