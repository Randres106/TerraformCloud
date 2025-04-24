# 🧠 Clasificador de Noticias con Naïve Bayes – Proyecto Rafaelitos

Este proyecto implementa un sistema completo para clasificar noticias usando el algoritmo Naïve Bayes desde cero. Incluye un backend en Python (Flask), un frontend en React, y un motor de inferencia personalizado.

---

## 🚀 Uso

### 1. El usuario ingresa una noticia en el frontend (web).
### 2. La noticia se envía al backend vía `POST /classify`.
### 3. El backend la preprocesa y la evalúa con el modelo Naïve Bayes.
### 4. Devuelve:
- Categoría más probable
- Porcentaje de certeza
- (Opcional) Segunda categoría con alta probabilidad

---

## 🧱 Arquitectura



---

## 📁 Descripción de archivos y carpetas

### 📂 Analizador
- `api.py`: Servidor Flask, recibe texto y devuelve la predicción.
- `naive_bayes.py`: Implementación propia del clasificador Naïve Bayes.
- `train_model.py`: Entrena y guarda el modelo (`bbc_classifier.pkl`).
- `evaluate_model.py`: Evalúa el rendimiento del modelo.
- `preprocess_bbc_dataset.py`: Limpia y organiza el dataset original.
- `bbc_classifier.pkl`: Modelo entrenado con probabilidades.
- `preprocessed/`: Contiene `train_dataset.csv`, `test_dataset.csv`, y `vocabulary.txt`.

### 📂 Frontend
- `App.js`: Componente principal en React.
- `index.js`: Punto de entrada.
- `App.css`: Estilos generales.
- `assets/`: Imagen grupal del proyecto.

---

## 🧰 Tecnologías utilizadas

- **Python 3.13**
- **Flask + Flask-CORS**
- **React.js**
- **Naïve Bayes desde cero (sin sklearn)**
- **CSV y Pickle** para datos y modelos

---

## 📊 Evaluación del Modelo

- **Precisión general:** 98.32%
- **Recall general:** 98.32%
- **F1-Score general:** 98.31%

| Categoría     | Precisión | Recall   | F1-Score |
| ------------- | --------- | -------- | -------- |
| Business      | 97.04%    | 98.13%   | 97.58%   |
| Entertainment | 97.37%    | 99.11%   | 98.23%   |
| Politics      | 99.31%    | 96.96%   | 98.12%   |
| Sport         | 99.62%    | 100.00%  | 99.81%   |
| Tech          | 98.10%    | 97.79%   | 97.95%   |

---

## 📚 Dataset

Se utilizó el corpus **BBC News Summary**, con 5 categorías:
- `business`, `entertainment`, `politics`, `sport`, `tech`

El preprocesamiento incluyó:
- Normalización a minúsculas
- Eliminación de puntuación
- Filtro de stopwords y tokens no alfabéticos

---

## ⚙️ Instalación

### 🔽 Requisitos previos
- Python 3.8 o superior
- Node.js y npm

### 🐍 Backend
```bash
cd Analizador
pip install flask flask-cors


cd Frontend
npm install
cd Analizador
python api.py
![image](https://github.com/user-attachments/assets/c1d9233b-fb09-4da4-8ccf-fda654806ad9)


