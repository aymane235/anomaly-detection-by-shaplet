This is a project done in an internship under the supervision of Gangler Emmanuel,a very genius physicist/astrophysicist,who
worked on particle physics and now on astrophysics,especially on data analysis and anomaly detection.
## Project Summary

This project applies **shapelet-based time series classification** to analyze and categorize the complex X-ray light curves of **GRS 1915+105**, a microquasar known for its highly variable and repeatable behavior. The goal is to develop an interpretable and robust method for detecting characteristic patterns (modes) in light curves using **shapelets**, enabling classification of physical states and anomaly detection.

---

## Key Concepts

- **GRS 1915+105**: A black hole X-ray binary located $\sim 11{,}000$ parsecs away, exhibiting more than 14 variability classes in X-ray emission.
- **Light Curves**: Time series of photon count rates that capture brightness variations over time.
- **Shapelets**: Local subsequences extracted from time series data that are most representative of specific classes. Used for classification through pattern matching.
- **Chi-Square Distance**: The matching metric is computed as:

  `χ² = (1/dof) ∑ (L[i + d] − S[i])² / (σ_S² + σ_L²)`

- **Normalization**: Both light curves and shapelets are z-normalized to handle intensity shifts and scaling artifacts.
- **Efficient Cut**: A threshold $\chi^2_\text{cut}$ is defined to select valid matches, minimizing false positives in anomaly detection.

---

## Method Overview:

1. Select a shapelet from known ρ-class light curves.
2. Slide the shapelet over other curves and compute $\chi^2$ at each step.
3. Use minimum $\chi^2$ values to define matches.
4. Apply recursive sampling and averaging to refine shapelet dictionaries.
5. Encode full light curves as sequences of best-matching shapelets (symbolic sequence model).

---

## Future Possible Work:

- Explore anomaly detection via deviations from known shapelet patterns.

