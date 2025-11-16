# DevSecOps Assignment - Python Security Analysis

**IMPORTANTE**: Este proyecto contiene vulnerabilidades intencionales para propósitos educativos.

##  Objetivo

Implementar prácticas DevSecOps:
- **Nivel A**: Linting (Flake8, Pylint, Bandit)
- **Nivel E**: SCA (Dependabot, Snyk)
- **Nivel O**: Advanced (Trivy, Semgrep)

##  Estructura del Proyecto
```
devsecops-assignment/
├── src/                  # Código fuente
├── tests/                # Tests unitarios
├── reports/              # Reportes generados
├── config/               # Configuraciones
└── .github/              # GitHub Actions
```

##  Instalación
```bash
# Clonar repositorio
git clone https://github.com/alvaromendieta/devsecops-assignment.git
cd devsecops-assignment

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

##  Ejecutar Análisis
```bash
# Linting
flake8 src/
pylint src/
bandit -r src/

# SCA
safety check
snyk test

# Advanced
trivy fs .
semgrep --config=auto src/
```

##  Autor

Alvaro Mendieta - Noviembre 2024
