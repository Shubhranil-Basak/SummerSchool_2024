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
    - [Plot fo the readings](Ohms%20Law/IR_plot.py)
    - [Temperature dependednt plot](Ohms%20Law/IR_temp.py)
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
There are multiple ways to make squarewave plot like using op amp, Fourier series transformation, signum function, sum of harmonics etc.
The formula to compute the sum of the harmonics of sine wave is given by:
<br>
<br>
$$\frac{4}{\pi}\sum_{n\ =\ 1}^{N}\frac{1}{(2n\ -\ 1)}\sin{((2n\ -\ 1)\omega t)}$$
Here N is the number of harmonic to be used
<br>
$\omega\$ is equal to $2\times\pi$
<br>
t represents time
<br>

The other option which is similar to the sum of harmonics is Fourier transormation, the formula is given by:
<br>
$$f\left(t\right)=\frac{a_0}{2}+\sum_{n\ =\ 1}^{\infty}a_n\cos{\frac{2\pi\~nt}{T}}\ +\ b_n\sin{\frac{2\pi\~nt}{T}}$$
<br>
The Fourier coefficient ${a}\_{0}$, ${a}\_{n}$ and ${b}\_{n}$ can be calculated as follows:
<br>
$$a_0\ =\ \frac{2}{T}\int_{0}^{T}{f(t)\ dt}$$
$$a_n\ =\ \frac{2}{T}\int_{0}^{T}{f(t)\ \cos{\frac{2\pi\ nt}{T}}\ dt}$$
$$b_n\ =\ \frac{2}{T}\int_{0}^{T}{f(t)\ \sin{\frac{2\pi\ nt}{T}}\ dt}$$
<br>
The reason I choose sum of harmonics is because it is easy to compute as compared to Fourier transformation because we have to perform integration to find the Fourier coefficients which is computationally expensive and can give wrong answers with low/mid end hardaware as they might not be able to compute them properly.
<br>
The program consist of input field which can control the amplitude, frequency and duty cycle of the square wave. And there is a button that saves a CSV file with number of samples entered by the user.

# Question 2
Write a Python code that mimics the ADC (Analog-to-Digital Converter) calculator available at [https://circuitdigest.com/calculators/adc-analog-to-digital-convertercalculator](https://circuitdigest.com/calculators/adc-analog-to-digital-convertercalculator).

## Explanation
The formula of digital output is given by: $$2^N \times \frac{Analog\~Input\~Voltage}{Reference\~Voltage}$$.
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
In a practical setting where a resistor 𝑅 is connected across a voltage source V, the current I(R) through the resistor depends on the value of the resistor R according to Ohm's Law. Ohm's Law states that the current through a conductor between two points is directly proportional to the voltage across the two points and inversely proportional to the resistance.
<br>
<br>
Mathematically, Ohm’s law can be expressed as:
$$V\ =\ I\ x\ R$$

${V}$ is the voltage across the resistor
<br>
${I}$ is the current flowing through the resistor
<br>
${R}$ is the resistance of the resistor
<br>
If we rearrange the equation, we get:
$$I\ =\ \frac{V}{R}$$

This shows the if the voltage (V) is kept constant then the current (I) is inversly proportional to the Resistance (R)
<br>
To verify this, I along with some friends did an experiment (in CEEMS Lab, IIITB), and the readings we got are as follows:
|Voltage (V)|Resistance (k $\Omega$)|Conductance or 1/Resistance $(k \Omega)^{-1}$|Current (mA)|
|---|---|---|---|
|8.84|96.30|0.01|0.09|
|8.84|0.96|1.04|8.71|
|8.84|9.79|0.10|0.88|
|8.84|97.60|0.01|0.09|
|8.84|0.95|1.05|8.77|
|8.84|0.92|1.09|8.78|
|8.84|45.80|0.02|0.18|
|8.84|4.90|0.20|1.40|

On plotting the readings, we get this:
<br>
![temp](https://github.com/Shubhranil-Basak/SummerSchool_2024/assets/144095577/8e717a05-7d83-4fd9-9cba-81e07e32e80f)
As we can see, the graph is not perfectly linear, there might be many factors, some of the possible ones are:
* **Resistance of components**: In non-ideal/practical situations all the components like wires, battery, etc. have their own resistance that effect the overall resistance of the circuit.
* **Least count of multimemter**: The least count/error in the multimeter might lead to reading being displayed be different from the actual value of the current.
* **Temperature**: After using the resistor for some time, it starts heating (deterministic to some extent using Joule law of heating) as a result it effects the resistor thus changing its value while the experiment was being performed.

To take temperature into account, we have to go beyond the normal Ohm’s law.
The resistance (R) of a typical resistor can vary with temperature. This temperature dependency is often characterized by the temperature coefficient of the resistance (α), which describes how the resistance changes per degree Celsius (°C) of temperature change. The relationship between resistance (R), temperature (T), and the reference temperature ($T_0$) can be expressed as:

$$R\ =\ R_0[1+\ \alpha(T\ -\ T_0)]$$

Here,
<br>
$R_0$ is the resistance at reference temperature $T_0$.
<br>
$\alpha$ is the temeprature coefficient of the resistance.
<br>
$T$ is the current temperature.

#### Combining Ohm’s law with temperature dependence:

To incorporate temperature (T) into our analysis, we can substitute the expression for resistance (R) into Ohm’s law:

$$I\ =\ \frac{V}{R0[1 + α(T - T0)]}$$
#### Effect of temperature on current:
* If the temperature of the resistor increases, the effective resistance increases, thus the current flowing through the resistor decreases.
* If the temperature of the resistor decreases, the effective resistance decreases, thus the current flowing through the resistor increases.

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
