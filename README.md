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

