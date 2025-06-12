# peritus: a Zola theme for academic portfolio sites

[![Zola](https://img.shields.io/badge/Zola-Compatible-blue)](https://www.getzola.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![Theme Preview](https://raw.githubusercontent.com/jskaza/peritus/refs/heads/main/peritus-theme-preview.png)

A clean, modular [Zola](https://www.getzola.org/) theme for academic CVs and research portfolios. Inspired by the popular [Hugo Academic CV theme](https://github.com/HugoBlox/theme-academic-cv), it is perfect for researchers, academics, educators, and students who want to showcase their work, publications, and achievements.

🚀 Check out a [live demo](https://jskaza.github.io/) to see the theme in action.

## 🌟 Features

- **Decouple Data from Design**: Content managed through structured TOML files, keeping your data completely separate from style
  - Each content type (publications, experience, conferences, education, interests, social) has its own dedicated data file in the `data/` directory
  
- **Modular & Extensible Content**: Built-in support for academic content like publications, talks, and experience. New sections can be added by creating TOML files and matching templates.
  - Follow the established pattern: create `data/newsection.toml` 
  - Add corresponding template in `templates/newsection.html`
  - Add to the navbar in `config.toml` (see `config.toml` for an example)

## ⚡ Quick Start

### Prerequisites

- [Zola](https://www.getzola.org/documentation/getting-started/installation/)

### Installation

1. **Create a new Zola site:**
   ```bash
   zola init my-peritus-site
   cd my-peritus-site
   ```

2. **Add the theme to your themes directory:**
   ```bash
   mkdir -p themes
   cd themes
   git clone https://github.com/jskaza/peritus
   ```

3. **Configure the theme in `config.toml`:**
   ```toml
   theme = "peritus"
   ```
4. **Start the development server:**
   ```bash
   zola serve
   ```

## ⚙️ Configuration

### Basic Configuration

Edit `config.toml` to customize your site:

```toml
# The URL the site will be built for
base_url = "https://markscout.xyz"

# Whether to automatically compile all Sass files in the sass directory
compile_sass = true

# The site title and description; they are used in feeds by default.
title = "Mark S"
description = "Professional Portfolio"

[extra]
# Put all your custom variables here
# The URL of the CV, which can be downloaded from the landing page
# fictional example; replace with your actual info
cv_url = "https://en.wikipedia.org/wiki/Severance_(TV_series)"
name = "Mark S"
role = "Macrodata Refiner"
organization = "Lumon Industries"
location = "Kier, PE"

# Bio/about section, this is prominently displayed on the landing page
bio = """
Hi, I’m Mark Scout. By day—or at least, what feels like day—I work as a Macrodata Refinement department head at Lumon Industries. I’ve undergone the severance procedure, which means my work self and personal self are completely separate. I can’t tell you much about what I do outside the office, because I don’t know. What I do know is that I take pride in leading my team and hitting quota, even if I don’t fully understand what our data means. People say I’m dependable, maybe a little reserved, but I try to keep things running smoothly. Lately, though, I’ve started asking questions—about the work, the rules, and what it really means to be "me."
"""

# navbar items
[[extra.menu]]
name = "Publications"
url = "/publications/"
weight = 1

[[extra.menu]]
name = "Conferences & Talks"
url = "/conferences/"
weight = 2

[[extra.menu]]
name = "Experience"
url = "/experience/"
weight = 3

# Color theme configuration
[extra.colors]
primary_color = "#39444C"         
secondary_color = "#C8102E"       
accent_color = "#98A6AD"         
text_color = "#2C2F33"           
background_color = "#F8F9FA"      
card_background = "#FFFFFF"      
border_color = "#D0D3D4"        
light_background = "#EDF0F2"      
```
### 📋 Content Type Fields

Each content type supports specific fields for structured data entry and templating:

#### 📚 Publications (`data/publications.toml`)
```toml
[[publication]]
title = "Your Paper Title"
pub_year = 2025
author = ["First Author", "Second Author"]
journal = "Journal Name"
volume = "12(3)"
url = "https://link-to-paper.com"
abstract = """
Your abstract text here...
"""
```

#### 💼 Experience (`data/experience.toml`)
```toml
[[experience]]
title = "Job Title"
company = "Company Name"
location = "Company Location"
start_date = 2020
end_date = 2025 # optional for current roles
description = "Role description..."
```

#### 🎤 Conferences (`data/conferences.toml`)
```toml
[[conference]]
title = "Presentation Title"
year = 2025
author = ["First Author", "Second Author"]
venue = "Conference Name"
location = "Venue Location"
links = [
    { name = "Slides", url = "https://slides-link.com" },
    { name = "Poster", url = "https://poster-link.com" }
] # both optional
```

#### 🎓 Education (`data/education.toml`)
```toml
[[education]]
degree = "Ph.D. in Field of Study"
institution = "University Name"
```

#### 🔬 Interests (`data/interests.toml`)
```toml
interests = [
    "Research Area 1",
    "Research Area 2",
    "Research Area 3"
]
```

#### 🌐 Social (`data/social.toml`)
```toml
[[social]]
name = "Platform Name"
url = "https://profile-url.com"
icon = "fab fa-github"
```

## 📄 License

This theme is licensed under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Inspired by the excellent [Hugo Academic CV theme](https://github.com/HugoBlox/theme-academic-cv)
- Built with [Zola](https://www.getzola.org/)
- Icons by [Font Awesome](https://fontawesome.com/)



*🛠️ Contributions are welcome! Please feel free to submit a pull request.*

*⭐ Star this repo if you find it helpful!*
