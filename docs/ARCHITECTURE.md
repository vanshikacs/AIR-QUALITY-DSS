AirFlow DSS follows a clean, layered architecture that separates concerns and maintains testability.

## Layers

### 1. Data Layer (`src/data/`)

**Responsibility:** External data integration and validation

**Components:**
- `api_client.py`: WAQI API integration
- `quality.py`: Data quality assessment
- `models.py`: Type-safe data models

**Key Classes:**
- `AQIAPIClient`: Handles API requests
- `DataQualityAssessor`: Evaluates data reliability
- `AQIData`: Type-safe data model

**Why This Design:**
- Isolates external dependencies
- Makes testing easier (can mock API)
- Centralizes data validation

### 2. Analysis Layer (`src/analysis/`)

**Responsibility:** Business logic and calculations

**Components:**
- `exposure.py`: Risk scoring algorithms
- `trends.py`: Statistical analysis
- `optimization.py`: Time window identification
- `profiles.py`: Profile management

**Key Classes:**
- `ExposureAnalyzer`: Transparent risk calculation
- `TrendAnalyzer`: Pattern detection
- `TimeWindowOptimizer`: Timing recommendations
- `ProfileManager`: User profile storage

**Why This Design:**
- Pure functions testable in isolation
- No UI dependencies
- Reusable across different interfaces

### 3. UI Layer (`src/ui/`)

**Responsibility:** User interface and visualization

**Components:**
- `pages/`: Individual page implementations
- `components.py`: Reusable UI elements
- `visualizations.py`: Chart generation

**Why This Design:**
- Separates presentation from logic
- Reusable components
- Easy to modify UI without touching logic

### 4. State Management (`src/state.py`)

**Responsibility:** Centralized state handling

**Why Separate:**
- Single source of truth
- Avoids state pollution
- Easy to track all state variables

### 5. Utilities (`src/utils/`)

**Responsibility:** Configuration and helpers

**Components:**
- `constants.py`: All configuration
- `helpers.py`: Utility functions

**Why Separate:**
- Easy to find configuration
- Avoids magic numbers
- Single place to update constants

## Data Flow

```
User Input → UI Layer → Analysis Layer → Data Layer → API
                ↓            ↓              ↓
            State Update ← Results ← Processed Data
                ↓
          UI Re-render
```

## Design Decisions

### Why Models?

Type-safe data models (`dataclasses`) provide:
- Compile-time checking
- Auto-completion in IDEs
- Clear contracts between layers
- Easy serialization

### Why Separate Pages?

Each page in its own file:
- Easier to navigate codebase
- Parallel development possible
- Smaller files = easier review
- Clear responsibilities

### Why Constants File?

Centralizing configuration:
- Single source of truth
- Easy to tune parameters
- No magic numbers in code
- Clear documentation

## Testing Strategy

Each layer can be tested independently:

```python
# Test Analysis Layer
def test_exposure_calculator():
    profile = UserProfile(...)
    analyzer = ExposureAnalyzer(aqi=150, profile=profile)
    result = analyzer.calculate()
    assert result.score > 0
```

## Future Enhancements

### Adding Database

Would add to Data Layer:
```
src/data/
  ├── api_client.py
  ├── db_client.py      # New
  └── repositories.py   # New
```

### Adding Authentication

Would add new layer:
```
src/auth/
  ├── __init__.py
  ├── authenticator.py
  └── user_manager.py
```

## Refactoring Guide

### Moving from Monolithic to Layered

1. **Identify responsibilities** in current code
2. **Extract data fetching** → `src/data/`
3. **Extract calculations** → `src/analysis/`
4. **Extract UI rendering** → `src/ui/`
5. **Update imports** in `app.py`
6. **Test each layer** independently

### Example Refactoring

**Before (Monolithic):**
```python
def calculate_score(aqi, hours, activity):
    # API call, calculation, and UI all mixed
    response = requests.get(...)
    score = aqi * hours * activity_mult
    st.write(f"Score: {score}")
```

**After (Layered):**
```python
# Data Layer
class AQIAPIClient:
    def fetch_aqi(location): ...

# Analysis Layer
class ExposureAnalyzer:
    def calculate(self): ...

# UI Layer
def render_exposure_page():
    client = AQIAPIClient()
    data = client.fetch_aqi(...)
    analyzer = ExposureAnalyzer(...)
    result = analyzer.calculate()
    st.write(f"Score: {result.score}")
```

---

**Key Takeaway:** Each layer has ONE job. This makes code easier to understand, test, and modify.
