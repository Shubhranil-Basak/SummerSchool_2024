# Summer School on Embedded Systems and Robotics

## This repo consists of the code and explaination to the questions asked in the aptitude test

# Table of content
- [Requirements](#requirements)
- [Question 1](#question-1)
    - [Explanation](?tab=readme-ov-file#explanation)
    - [code](squarewave/sqarewave.py)
- [Question 2](#question-2)
    - [Explanation](?tab=readme-ov-file#explanation-1)
    - [code](ADC.py)
- [Question 3](#question-3)
    - [Explanation](?tab=readme-ov-file#explanation-2)
    - [code](tukey)
- [Question 4](#question-4)
    - [Explanation](?tab=readme-ov-file#explanation-3)
    - [code]()
- [Question 5](#question-5)
    - [Explanation](?tab=readme-ov-file#explanation-4)
    - [code](OOK/OOK.py)
---

# Requirements
The requirements file can be found [here](requirements.txt)
Run this command on the cmd before running any of the python files:
```bash
pip install -r requirements.txt
```
---

# Question 1
Write a Python code to generate a square wave with user-defined amplitude, frequency, and samples per second. The code should plot the generated waveform and save it to a CSV file with two columns: time and amplitude.

## Explanation


# Question 2
Write a Python code that mimics the ADC (Analog-to-Digital Converter) calculator available at [https://circuitdigest.com/calculators/adc-analog-to-digital-convertercalculator](https://circuitdigest.com/calculators/adc-analog-to-digital-convertercalculator).

## Explanation
The formula of digital output is given by: $2^N \times \frac{Analog\~Input\~Voltage}{Reference\~Voltage}$.
<br>
<br>
The table that I was able to come up with for different values of Analog and Reference voltage is as follows:
<br>
<br>
|Analog Input Voltage|Reference Voltage|Output|
|---|---|---|
|Positive|Negative|Negative|
|Positive|Positive|Positive|
|Positive|Zero|Infinity|
|Negative|Negative|Positive|
|Negative|Positive|Negative|
|Negative|Zero|Infinity|
|Zero|Negative|Zero|
|Zero|Positive|Zero|
|Zero|Zero|NaN|

I have assumed that the the floating point calculations done by the calculator adhere to the IEEE 754 standards.
I have also assumed that the floating point answers are typecasted/converted to integer before being displayed.

# Question 3
Create a Python package that facilitates basic mathematical operations: addition, subtraction, and multiplication of two numbers. Upload this package to PyPI (Python Package Index). Provide the package name and its URL. Explain how to install and use the package.

## Explanation
The name of the package 'tukey' is named after famous American mathematician and statistician John Tukey.
As of now It support basic arithmatic operators including:
* Add
* Subtract
* Multiply
* Divide
* Modulo

I have plans of Expanding it do include functions and methods that can be helpful for data extraction and EDA.

refere [here](https://github.com/Shubhranil-Basak/tukey/) for the full documentation of the package

# Question 4
Describe how the current through a resistor, denoted as I(R), depends on the resistor value, R, when the resistor is connected across a voltage source, V, in a practical setting.

## Explanation


# Question 5
In communication systems, explain the need to modulate a signal with a carrier. Write a python code to demonstrate OOK (On-Off keying) modulation and demodulation.

## Explanation

