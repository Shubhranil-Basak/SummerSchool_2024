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

refer [here](https://github.com/Shubhranil-Basak/tukey/) for the full documentation of the package

# Question 4
Describe how the current through a resistor, denoted as I(R), depends on the resistor value, R, when the resistor is connected across a voltage source, V, in a practical setting.

## Explanation


# Question 5
In communication systems, explain the need to modulate a signal with a carrier. Write a python code to demonstrate OOK (On-Off keying) modulation and demodulation.

## Explanation
There are multiple reasons to modulate a signal with a carrier wave. A few of them are:
* **Frequency Translation**: Modulation can help to shift the frequency spectrum of the original frequency to a higher frequency range suitable for efficient transmission and reception. It is because the frequency of the original baseband signal is different from those used for communication purposes like frequency bands for Radio or microwaves.
* **Antenna Efficiency**: The use of a carrier wave at a higher frequency facilitates efficient transmission through antennas. Antennas are more effective at radiating EM waves at higher frequencies, especially when compared to the lower frequencies typical of baseband signals. This efficiency is crucial for long-range communication and for minimizing the size and complexity of antennas.
* **Signal integrity and noise immunity**: Modulation helps in preserving the integrity of the transmitted signal and makes it more immune to noise and interference. The carrier wave can carry the modulated signal over long distances without significant loss of information, as compared to direct transmission of baseband signals.
* **Multiplexing and channel allocation**: Modulating signals with different carrier frequencies enables multiplexing—simultaneously transmitting multiple signals over the same communication medium.
* **Comaptibility with transmission media**: Different transmission media (like cables, optical fibers, etc.) have specific characteristics that determine their suitability for transmitting signals at particular frequencies. By modulating a signal, we can match the characteristics of the transmission medium, optimizing the signal's propagation and minimizing data loss.

My assumptions:
1.	Considering there is no noise in carrier and signal wave.
2.	Considering there is noise only in modulated wave
3.	Considering smoothing od demodulated wave is necessary else it might have false signals because of noise.
