Reproducible Python-based bioinformatics pipeline for detecting major carbapenemase genes (blaNDM, OXA-48-like variants, blaKPC) from ABRicate outputs of Indian clinical Klebsiella pneumoniae isolates.

## Why This Matters

Carbapenem resistance in Klebsiella pneumoniae is a major public health concern in India. This project demonstrates an automated workflow for genomic surveillance and resistance gene prevalence analysis.# Carbapenem Resistance Genomic Screening Pipeline

This project implements a Python-based pipeline for screening major carbapenemase genes (blaNDM, OXA-48-like variants, blaKPC) from ABRicate outputs of Indian clinical Klebsiella pneumoniae isolates.

## Project Overview

- Dataset: 64 publicly available Indian clinical isolates
- Input: ABRicate (ResFinder) output
- Output: Filtered carbapenemase gene dataset + prevalence counts

## Features

- Automated parsing of ABRicate output
- Extraction of carbapenemase genes
- Prevalence calculation
- Structured CSV output generation

## Tools Used

- Python 3
- pandas
- ABRicate
- ResFinder database

## Folder Structure

carbapenem_ml_pipeline/
│
├── data/                  # ABRicate outputs
├── results/               # Filtered outputs
├── scripts/               # Python pipeline
└── README.md

## How to Run

1. Place ABRicate output file in data/
2. Navigate to scripts/
3. Run:

   python3 pipeline.py
