# Fractional-Order Cancer Dynamics with Neural Network Validation

## 🧬 Quantum-Enhanced Fractional Models for Cancer Evolution

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![DOI:Software](https://zenodo.org/badge/DOI/10.5281/zenodo.18523151.svg)](https://doi.org/10.5281/zenodo.18523151)
[![DOI:Paper](https://img.shields.io/badge/DOI-10.1016/j.rineng.2025.106080-blue)](https://doi.org/10.1016/j.rineng.2025.106080)

> **Published Paper**: Jamadar IS, Kumar K, Khan SA, Khan A, Akhtar MN, Bakar EA. "Quantum pressure and memory effects in cancer modeling: a fractional calculus neural network approach." *Results in Engineering*. 2025;27:106080. doi:[10.1016/j.rineng.2025.106080](https://doi.org/10.1016/j.rineng.2025.106080)

> **Software**: Jamadar IS, Kumar K, Khan SA, Khan A, Akhtar MN, Bakar EA. (2025). Fractional-Order Cancer Dynamics with Neural Network Validation (v1.0.0). Zenodo. doi:[10.5281/zenodo.18523151](https://doi.org/10.5281/zenodo.18523151)

---

## 🏆 **Key Achievement**

**PROVEN: Fractional-order models are 47-50% more accurate than integer-order models**

Validated through comprehensive neural network learning across 5 mathematical formulations and published in *Results in Engineering* (Elsevier).

---

## 📊 **Main Results**

| Model Type | RMSE | MAE | R² | Improvement |
|------------|------|-----|----|-----------| 
| **Hilfer Fractional** | 0.107±0.027 | 0.075±0.019 | **0.999956** | **+50.7%** |
| Grünwald-Letnikov | 0.126±0.035 | 0.089±0.019 | 0.999925 | +42.1% |
| Riemann-Liouville | 0.158±0.038 | 0.106±0.025 | 0.999895 | +27.2% |
| Caputo Fractional | 0.153±0.048 | 0.103±0.031 | 0.999891 | +29.4% |
| Integer Order | 0.217±0.083 | 0.141±0.045 | 0.999792 | baseline |

**Statistical Significance**: p = 0.036, Cohen's d = 1.78 (large effect)

---

## 📖 **Publication**

This repository contains the complete implementation of the methods described in:

**Full Citation:**
> Jamadar IS, Kumar K, Khan SA, Khan A, Akhtar MN, Bakar EA. Quantum pressure and memory effects in cancer modeling: a fractional calculus neural network approach. *Results in Engineering*. 2025;27:106080. doi:10.1016/j.rineng.2025.106080

**Journal**: Results in Engineering (Elsevier)  
**Year**: 2025  
**Volume**: 27  
**Article**: 106080  
**DOI**: [10.1016/j.rineng.2025.106080](https://doi.org/10.1016/j.rineng.2025.106080)

**Authors:**
- Irshad Sikandar Jamadar
- Krishna Kumar
- Sher Afghan Khan
- Ambareen Khan
- Mohammad Nishat Akhtar
- Elmi Abu Bakar

---

## 🚀 **Quick Start**

### Installation:
```bash
git clone https://github.com/yourusername/fractional-cancer-dynamics.git
cd fractional-cancer-dynamics
pip install -r requirements.txt
```

### Basic Usage:
```python
from src.models import IntegerModel, FractionalModel
import numpy as np
from scipy.integrate import odeint

# Create models
integer_model = IntegerModel()
fractional_model = FractionalModel()

# Initial conditions: [Tumor, Immune, Memory, Suppressor]
initial_state = [50, 10, 20, 30]
time = np.linspace(0, 10, 100)

# Simulate
integer_traj = odeint(integer_model, initial_state, time)
fractional_traj = odeint(fractional_model, initial_state, time)

print(f"Integer final: {integer_traj[-1]}")
print(f"Fractional final: {fractional_traj[-1]}")
```

---

## 📁 **Repository Structure**
```
fractional-cancer-dynamics/
├── src/                       # Source code
│   ├── models/                # Mathematical models (3 files)
│   ├── fractional_derivatives/# 4 derivative types (5 files)
│   ├── neural_networks/       # NN components (2 files)
│   ├── analysis/              # Analysis tools (4 files)
│   └── visualization/         # Plotting (3 files)
├── studies/                   # Research studies (2 files)
├── config/                    # Parameters (1 file)
├── docs/                      # Documentation
├── examples/                  # Usage examples
└── tests/                     # Unit tests
```

---

## 🔬 **Scientific Contributions**

### Mathematical Models:
- Integer-order dynamics (Equations 1-4)
- Fractional-order enhancement (Equations 5-8)  
- 47-50% accuracy improvement

### Fractional Derivatives:
- Caputo, Riemann-Liouville, Grünwald-Letnikov, Hilfer
- Optimal: Hilfer with α=1.5, β=0.5

### Neural Network Validation:
- 5 networks, 30,000 samples, >99.97% accuracy
- Statistical significance: p=0.036, d=1.78

---

## 📚 **Citation**
```bibtex
@software{fractional_cancer_2025,
  title={Fractional-Order Cancer Dynamics with Neural Network Validation},
  author={Research Team},
  year={2025},
  url={https://github.com/yourusername/fractional-cancer-dynamics}
}
```

---

## 🛠️ **Requirements**

- Python 3.8+
- NumPy, SciPy, PyTorch, Matplotlib, Pandas, Scikit-learn

See `requirements.txt` for complete list.

---

## 📄 **License**

MIT License - see [LICENSE](LICENSE)

---

**⭐ Star this repository if useful for your research!**





