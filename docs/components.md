# Components Directory Documentation

## Overview
This document provides an overview of the `components` directory in the **BioRemPP** project. The directory contains reusable Dash components for structuring the user interface and providing interactivity. Below, you will find a clickable menu for navigating through each component, followed by a detailed explanation of their purpose and general functionality.

## Table of Contents
- [Components Directory Documentation](#components-directory-documentation)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview-1)
  - [Components](#components)
    - [Alerts](#alerts)
    - [Bioremediation](#bioremediation)
    - [Download Button](#download-button)
    - [Features](#features)
    - [Footer](#footer)
    - [Header](#header)
    - [Navbar](#navbar)
    - [Regulatory Agencies](#regulatory-agencies)
    - [Step Guide](#step-guide)
    - [Tooltip Sample](#tooltip-sample)

---

## Overview

The `components` directory houses reusable Python scripts that define UI elements of the **BioRemPP** application. These components simplify the application's development by modularizing the interface. Each file corresponds to a specific UI component or page section, offering high cohesion and easy maintenance.

---

## Components

### Alerts
**File**: `alerts.py`

This file contains pre-configured alert components using **Dash Bootstrap Components (DBC)**. The alerts are used to notify users about integrations with external databases, such as:
- **HADEG**: Displays information about gene/pathway data sourced from the HADEG repository.
- **ToxCSM**: Shows toxicity prediction data linked to the ToxCSM tool.

These alerts include descriptive messages and links for further details, styled with consistent formatting.

---

### Bioremediation
**File**: `bioremediation.py`

Defines the layout for the **Bioremediation** page, which includes:
- A high-level introduction to bioremediation.
- Key applications and benefits of bioremediation.
- An overview of organisms involved in bioremediation.
- Challenges and future directions in the field.

This page uses sections with headers, descriptive paragraphs, and structured lists for clarity.

---

### Download Button
**File**: `download_button.py`

Implements a simple button for downloading example data (`biorempp_sample_data.txt`). The button:
- Is styled for visibility.
- Includes attributes for file download and is linked directly to the static assets.

This component ensures easy access to example datasets for users.

---

### Features
**File**: `features.py`

Defines the layout for the **Features** page, including:
- A summary of the platform's functionalities.
- Sections detailing platform features such as data integration, pathway analysis, and expected results.
- Interactive elements and placeholders for visual components like tables, charts, and heatmaps.

This component provides an organized structure for showcasing the application's capabilities.

---

### Footer
**File**: `footer.py`

The footer component is responsible for displaying:
- Informational links (e.g., license, privacy policy, and terms of use).
- Navigation aids for quick access to essential sections.

The design ensures consistent branding and user accessibility across the application.

---

### Header
**File**: `header.py`

Defines the main application header, which includes:
- The application title and logo linking to the homepage.
- Navigation links for key sections like **Help**, **Features**, and **Contact**.
- A consistent and user-friendly structure for global navigation.

---

### Navbar
**File**: `navbar.py`

Creates a detailed navigation menu with links organized by categories, such as:
- **Data Tables**: Links to result tables and database integrations.
- **Pathway Analysis**: Links to gene/pathway visualization tools.
- **Interactions**: Highlights compound-gene-sample relationships.

Each menu section is styled with Bootstrap Cards for a clean and intuitive interface.

---

### Regulatory Agencies
**File**: `regulatory_agencies.py`

Provides the layout for the **Regulatory Agencies** page, which covers:
- A detailed introduction to priority pollutants and their environmental impacts.
- Highlights of key global agencies (e.g., EPA, IARC, CEPA).
- Links to resources and descriptions of their regulatory roles.

This component educates users on the regulatory context of bioremediation.

---

### Step Guide
**File**: `step_guide.py`

Implements a step-by-step guide for new users. Key features:
- Displays three steps: Upload, Submit, and View Results.
- Each step is a stylized card with a title, description, and clear instructions.

This component helps users navigate the application process effectively.

---

### Tooltip Sample
**File**: `tooltip_sample.py`

Creates tooltips for explaining specific application features, such as:
- Expected input data format for analysis.
- Examples of valid dataset structures using KEGG Orthology IDs (KO).

The tooltips include styled text, examples, and alerts to ensure user comprehension.

---
