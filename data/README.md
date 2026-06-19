# Data Processing

To calculate the speed of sound ($c$) in humid air, use the Cramer equation or the fundamental Laplace-adiabatic equation adjusted for wet air. The most accurate direct calculation requires finding the isentropic exponent (ratio of specific heats) and the gas constant for the specific air mixture. [^1] [^2] 
Here is the step-by-step method to calculate it.

------------------------------

## 1. Find Saturation Vapor Pressure [^3]

First, calculate the saturation vapor pressure of water ($p_{sat}$) in Pascals using the temperature in Kelvin ($T$). You can use the Hardy or Buck equation:

```math
p_{sat} = 611.21 \cdot \exp\left(\frac{17.502 \cdot (T - 273.15)}{T - 32.18}\right)
```

## 2. Determine Actual Vapor Pressure [^4]

Multiply the saturation vapor pressure by your relative humidity ($RH$, expressed as a decimal between $0$ and $1$) to find the partial pressure of water vapor ($p_v$):

```math
p_v = \left(\frac{RH}{100}\right) \cdot p_{sat}
```

## 3. Calculate Mole Fraction of Water Vapor

Find the molar fraction of water vapor ($x_v$) by dividing the vapor pressure by the total air pressure ($p$):

```math
x_v = \frac{p_v}{p}
```

## 4. Compute Specific Gas Constant [^5]

Calculate the specific gas constant for the humid air mixture ($R_{mix}$). Dry air has a molar mass of $M_d \approx 0.028965\text{ kg/mol}$, and water vapor has $M_v \approx 0.018015\text{ kg/mol}$: [^6]

```math
\begin{aligned}
M_{mix} &= (1 - x_v) \cdot M_d + x_v \cdot M_v
\\
R_{mix} &= \frac{R_u}{M_{mix}}
\end{aligned}
```

(Where $R_u$ is the universal gas constant, $8.31446\text{ J/(mol}\cdot\text{K)}$) [^7]

## 5. Adjust the Isentropic Exponent

The ratio of specific heats ($\gamma$) changes slightly with humidity. For dry air, $\gamma_d \approx 1.400$. For water vapor, $\gamma_v \approx 1.333$. Approximate the mixture's exponent ($\gamma_{mix}$) using the mole fraction: [^8]

```math
\gamma_{mix} = (1 - x_v) \cdot 1.400 + x_v \cdot 1.333
```

## 6. Calculate Speed of Sound [^9]

Plug the mixture variables, temperature ($T$), air pressure ($p$), and density ($\rho$) into the ideal gas or hydrodynamic speed of sound formula:

```math
c = \sqrt{\frac{\gamma_{mix} \cdot p}{\rho}}
```

Alternatively, using the gas constant:

```math
c = \sqrt{\gamma_{mix} \cdot R_{mix} \cdot T}
```

## ✅ Speed of Sound Formula Summary

The final speed of sound in humid air is explicitly stated by the thermodynamic relationship:

```math
c = \sqrt{\frac{\gamma_{mix} \cdot p}{\rho}}
```

Where $c$ is the speed of sound in $\text{m/s}$, $\gamma_{mix}$ is the humidity-adjusted isentropic exponent, $p$ is the air pressure in $\text{Pa}$, and $\rho$ is the air density in $\text{kg/m}^3$. [^10] [^11] 

[^1]: [https://www.researchgate.net](https://www.researchgate.net/publication/352530307_Noise_Control_From_Concept_to_Application)
[^2]: [https://www.mh-aerotools.de](https://www.mh-aerotools.de/airfoils/perfred.htm)
[^3]: [https://turn2engineering.com](https://turn2engineering.com/calculators/relative-humidity-calculator)
[^4]: [https://www.fao.org](https://www.fao.org/4/x0490e/x0490e07.htm)
[^5]: [https://www.vaia.com](https://www.vaia.com/en-us/textbooks/physics/fluid-mechanics-7-edition/chapter-9/problem-46-a-one-dimensional-isentropic-airflow-has-the-foll/)
[^6]: [https://en.wikipedia.org](https://en.wikipedia.org/wiki/Density_of_air)
[^7]: [https://vulcan-cfd.larc.nasa.gov](https://vulcan-cfd.larc.nasa.gov/WebPage/Documentation/AIAA-2004-0267.pdf)
[^8]: [https://allen.in](https://allen.in/dn/qna/11750513)
[^9]: [https://allen.in](https://allen.in/dn/qna/648202972)
[^10]: [https://geo.libretexts.org](https://geo.libretexts.org/Bookshelves/Oceanography/Introduction_to_Physical_Oceanography_%28Stewart%29/03%3A_The_Physical_Setting/3.6%3A_Sound_in_the_Ocean)
[^11]: [https://basicairdata.eu](https://basicairdata.eu/knowledge-center/background-topics/density-and-air-temperature/)