# Development Guide

## Getting Started

### Prerequisites
- Python 3.8+
- Git
- pip

### Initial Setup

```bash
# Clone
git clone https://github.com/yourusername/airflow-dss.git
cd airflow-dss

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run
streamlit run app.py
```

## Development Workflow

### Adding a New Feature

1. **Identify the layer:**
   - Data fetching? → `src/data/`
   - Calculation? → `src/analysis/`
   - UI? → `src/ui/`

2. **Create module:**
   ```python
   # src/analysis/new_feature.py
   class NewFeatureAnalyzer:
       def analyze(self): ...
   ```

3. **Add tests:**
   ```python
   # tests/test_new_feature.py
   def test_new_feature():
       analyzer = NewFeatureAnalyzer()
       result = analyzer.analyze()
       assert result is not None
   ```

4. **Integrate:**
   - Import in `app.py`
   - Add to routing if new page
   - Update README

### Code Style

Follow PEP 8:
```python
# Good
def calculate_exposure_score(aqi: float, profile: UserProfile) -> float:
    """Calculate exposure score with clear types"""
    pass

# Bad
def calc(a, p):
    pass
```

### Testing

```bash
# Run all tests
pytest

# Run specific test
pytest tests/test_exposure.py

# With coverage
pytest --cov=src
```

### Documentation

Every module needs:
```python
"""
Module description.

This module handles X by doing Y.
"""

def function_name():
    """
    Function description.
    
    Args:
        param: Description
    
    Returns:
        Description
    """
    pass
```

## Common Tasks

### Adding a New Page

1. Create `src/ui/pages/new_page.py`:
   ```python
   def render_new_page():
       st.title("New Page")
       # Implementation
   ```

2. Update `app.py` routing:
   ```python
   elif page == '🆕 New Page':
       from src.ui.pages.new_page import render_new_page
       render_new_page()
   ```

3. Add to sidebar options

### Modifying Calculations

All calculations in `src/analysis/`:
```python
# src/analysis/exposure.py
class ExposureAnalyzer:
    def calculate(self):
        # Modify here
        pass
```

### Changing UI

UI components in `src/ui/`:
```python
# src/ui/components.py
def render_new_component():
    # Add here
    pass
```

## Troubleshooting

### Import Errors

Ensure you're in project root:
```bash
# Should show app.py, src/, etc.
ls
```

Run from root:
```bash
streamlit run app.py
```

### Module Not Found

Check Python path:
```python
import sys
print(sys.path)
```

### State Issues

Reset state:
```python
# In app.py
if st.button("Reset"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.rerun()
```

## Best Practices

### 1. Keep Functions Small
```python
# Good
def calculate_score():
    factor = calculate_factor()
    multiplier = get_multiplier()
    return factor * multiplier

# Bad
def calculate_everything():
    # 200 lines of code
    pass
```

### 2. Use Type Hints
```python
def process_data(data: AQIData) -> ExposureResult:
    pass
```

### 3. Handle Errors
```python
try:
    data = client.fetch_aqi(location)
except Exception as e:
    st.error(f"Error: {e}")
    return None
```

### 4. Document Assumptions
```python
def calculate_score():
    """
    Calculate exposure score.
    
    Assumes:
    - Linear AQI-risk relationship
    - Continuous outdoor exposure
    """
    pass
```

## Deployment

### Streamlit Cloud

1. Push to GitHub
2. Connect to Streamlit Cloud
3. Deploy from repository

### Docker (Optional)

```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

## Questions?

Check:
1. This guide
2. ARCHITECTURE.md
3. README.md
4. Code docstrings

---

**Happy coding!**