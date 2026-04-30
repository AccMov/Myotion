# Myotion Project Structure

Myotion is a comprehensive desktop application for motion analysis, designed for biomechanics analysis and clinical research. It provides a graphical user interface to import, process, analyze, and visualize motion capture data, with a focus on EMG and kinematic analysis.

## Main Directories

The project is organized into the following main directories:

-   **`/` (Root Directory)**: Contains the main application entry point (`main.py`), UI definition files (`.ui`), PyInstaller specification (`Myotion.spec`), and other configuration files.
-   **`/modules`**: The core of the application's logic.
-   **`/widgets` & `/themes`**: Contain custom UI components and styling for the application's Qt-based graphical interface.
-   **`/images`**: Stores icons and other graphical assets used in the UI.
-   **`/shiny`**: Contains an embedded R Shiny application for interactive data visualization.
-   **`/test`**: Includes test scripts and sample data for verifying the application's functionality.
-   **`/script`**: A collection of utility scripts for development tasks, such as managing language translations and creating application releases.

## Key Modules Explained

Here is a more detailed breakdown of the most important modules:

-   **`modules/app_functions.py`**: Manages UI-specific logic and behavior. This module is responsible for handling theme customizations and dynamically styling widgets.

-   **`modules/app_settings.py`**: A centralized configuration file that defines constants for the UI's appearance and animations, such as colors, component dimensions, and animation speeds.

-   **`modules/pyMotion/`**: A processing engine for handling biomechanics data. It contains submodules to read and parse various file formats (like C3D, MAT, and XML), perform EMG and frequency analysis, and manage kinematic data.

-   **`modules/kinematics/`**: The 3D rendering engine of the application. It takes processed kinematic data and visualizes it in a 3D space, managing everything from the camera and lighting to the 3D objects and their materials.

-   **`main.py`**: The main entry point of the application that initializes the Qt application, loads the main window, and connects all the different modules together.

-   **`rserver.py`**: This script launches and manages the R Shiny server as a background process, enabling the integration of interactive R-based plots directly within the Python application.

## Key Features

-   **Data Import**: Supports common biomechanics data formats, including C3D and MAT files.
-   **EMG Analysis**: Provides tools for processing and analyzing electromyography (EMG) data.
-   **Kinematic Analysis**: Includes features for calculating and visualizing kinematic parameters.
-   **3D Visualization**: Renders 3D models and motion data for intuitive analysis.
-   **Interactive Plotting**: Integrates an R Shiny application for flexible and interactive data visualization.
-   **Customizable UI**: The application uses a themed Qt interface for a modern look and feel.
