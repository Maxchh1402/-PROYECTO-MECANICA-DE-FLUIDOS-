import streamlit as st
import numpy as np
import pandas as pd

def INTRODUCCION():
    st.title("RED DE TUBERÍAS")
    st.write("La mecánica de fluidos es una rama de la física que estudia el comportamiento de los fluidos, tanto líquidos como gases, y las fuerzas que actúan sobre ellos. Se ocupa del estudio de las propiedades físicas de los fluidos, como la densidad, la presión, la viscosidad y el caudal, así como de los principios que rigen el flujo de los fluidos.")
    st.write("La mecánica de fluidos tiene una amplia gama de aplicaciones en diversas áreas de la ciencia y la ingeniería. Algunas de las aplicaciones generales de la mecánica de fluidos es el diseño de sistemas de suministro de agua y saneamiento, en la planificación de sistemas de drenaje y en el análisis de la resistencia de estructuras expuestas a corrientes de agua, como puentes y presas.")
   
    st.write("En esta web interactiva se busca determinar ciertos valores de una red de tuberías, a partir de ciertos principios manejados en un curso de mecánica extendido.")
    st.write("Una red de tuberías es un sistema de transporte de fluidos que consta de una serie de tubos interconectados que permiten el flujo de líquidos, gases u otros tipos de fluidos de un punto a otro. Estas redes se utilizan ampliamente en diversas aplicaciones, como el suministro de agua potable, el transporte de petróleo y gas, el sistema de alcantarillado, la distribución de productos químicos, entre otros.")
    st.write("La red que tenemos en este diseño, consta de material de acero, diámetros ajustables, longitudes y alturas definidas." )
    st.write("El objetivo es que quien entienda y haga uso del sistema, pueda agregar las especificaciones pertinentes, que le atribuirán un diseño de tuberías optimo; todo ello en función del caudal de alimentación desde el nodo A, por ende, las respectivas descargas en nodos J, M, U y Z. Asignando también la energía total por unidad de peso del fluido (agua e 25 a 60 °C), HGL de alimentación ") 
    st.write("Los distintos caminos por lo que fluirá el agua constan de secciones de tubo delimita por una letra mayúscula, así como también te numerosas válvulas de compuerta y codo de 90°. El sistema se muestra en un plano isométrico donde existen tres circuitos, en los que se supondrá ciertos sentidos iniciales de flujos, como estos mismos para el cálculo exacto de ellos, a partir del método de Hardy Cross y los balances de masa.")

    st.subheader('Hardy Cross')
    st.write("Este método consiste en el análisis de un sistema de tuberías empleando procedimiento de iteraciones. Para la aplicación de este método se requiere realizar un balance global de masa y un balance de pérdidas en cada circuito igualado a cero.")
    st.markdown("La biblioteca está ajustada y deseñada con el fin determinar la presión, HGL diámetro nominal, interno y tasas de flujo. Como se mostrara a continuación en la sección **PROGRAMA**.")
    
    st.markdown('_Balance global de masa._')
    
    col1, col2 = st.columns(2)
    col1.subheader('Ecuaciones de Balance')
    col1.write('  ')
    image_cau = "https://i.pinimg.com/564x/29/b6/0a/29b60a5e14eebfe31e0b80216dd2129c.jpg"
    col1.image(image_cau, width=220, caption="  ")
    
    col2.subheader('Balance Global')
    col2.write(' ')
    image_bg = "https://i.pinimg.com/564x/9e/51/ad/9e51ad004a6af9462cdcf6f3f8ec1464.jpg"
    col2.image(image_bg, width=220, caption="  ")
    
    

if __name__ == '__main__':
    INTRODUCCION()
