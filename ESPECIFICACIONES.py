import streamlit as st
import numpy as np
import pandas as pd

def ESPECIFICACIONES ():

    
    
    st.markdown(f"<h2 style='text-align: center;'> ESPECIFICACIONES DE LA RED TUBERÍAS </h2>", unsafe_allow_html=True)
    st.write ()
    st.markdown(f"<h3    style='text-align: center;'> Rugosidad </h3>", unsafe_allow_html=True)
    st.write ("Para los tubos y las tuberías disponibles comercialmente, el valor de diseño de la rugosidad promedio ε de la pared de la tubería se ha determinado como indica la tabla 8.2 del libro de Mott.")
    st.markdown(f"<h3    style='text-align: center;'> ¿Por qué tubería de acero? </h3>", unsafe_allow_html=True)
    st.write ()

    st.write ("Existen varias razones por las que se utilizará el acero como material para tuberías en las redes de tubería. Algunas de las razones son las siguientes:")
    st.write ("1.	Resistencia: El acero es un material muy resistente y duradero. Tiene una alta resistencia a la tracción, lo que significa que puede soportar una gran cantidad de peso y tensión sin deformarse o romperse.")
    st.write ("2.	Durabilidad: Las tuberías de acero son resistentes a la corrosión y pueden durar décadas sin necesidad de mantenimiento. Esto las hace ideales para su uso en aplicaciones de alta presión y temperatura.")
    st.write ("3.	Seguridad: Las tuberías de acero son muy seguras, ya que son resistentes al fuego y no se queman fácilmente. También son capaces de soportar terremotos y otros desastres naturales, lo que las convierte en una opción ideal para sistemas de tuberías en áreas de riesgo sísmico.")
    st.write ("4.	Economía: Aunque el costo inicial de la instalación de tuberías de acero puede ser mayor que el de otros materiales, su durabilidad y resistencia a largo plazo pueden hacer que sean más económicas a largo plazo. Además, el acero es fácil de fabricar y transportar, lo que puede ayudar a reducir los costos.")
    st.write ("5.	Versatilidad: Las tuberías de acero se pueden utilizar en una amplia variedad de aplicaciones, incluyendo sistemas de agua potable, gasoductos, oleoductos, sistemas de calefacción y refrigeración, entre otros. También pueden ser fabricadas en una variedad de tamaños y formas para adaptarse a las necesidades específicas de cada proyecto.")

    st.markdown(f"<h3    style='text-align: center;'> Cédula 40 </h3>", unsafe_allow_html=True)
    st.write ("La Cédula en tuberías de acero es un término que se refiere a la pared de la tubería y se utiliza para indicar su espesor. La cédula a usar, en nuestro caso, la cédula 40, se refiere a un espesor de pared de 0,109 pulgadas (2,77 mm) y es una de las cédulas más comunes utilizadas en tuberías de acero.")
    st.write ("La razón por la que la cédula 40 es tan común en tuberías de acero es porque tiene un equilibrio ideal entre resistencia y costo. Es lo suficientemente gruesa como para soportar la presión y el peso necesarios para muchas aplicaciones, pero no es tan gruesa que resulte prohibitivamente costosa.")
    st.write ("Además, la cédula 40 es compatible con muchos accesorios de tubería estándar, lo que facilita la instalación y el mantenimiento. También es comúnmente utilizada en aplicaciones de tubería que requieren una presión moderada, como en sistemas de agua y gas.")
    st.markdown(f"<h3    style='text-align: center;'> ¿Por qué se usan codos? </h3>", unsafe_allow_html=True)
    st.write ()
    st.markdown("<div style='display: flex; justify-content: center;'><img src='https://i.pinimg.com/564x/06/ef/c8/06efc875f59a0428d9f5b10a96b2a900.jpg' alt='Imagen centrada' style='width: 300px; height: 200px;'></div>", unsafe_allow_html=True)
    st.write ()
    st.write ("El diseño de la red de tubería tiene variaciones en la elevación por ende será necesario cambiar la dirección del flujo del fluido para ella (según el libro de Crane). Accesorios: Los acoplamientos o accesorios para conexión se clasifican en: de derivación, reducción, ampliación y desviación. Los accesorios como tes, cruces, codos con salida lateral, etc., pueden agruparse como accesorios de derivación. Los conectores de reducción o ampliación son aquellos que cambian la superficie de paso del fluido. En esta clase están las reducciones y los manguitos. Los accesorios de desvío, curvas, codos, curvas en D, etc., son los que cambian la dirección de flujo. Se pueden combinar algunos de los accesorios de la clasificación general antes mencionada. Además, hay accesorios como conexiones y uniones que no son resistentes al flujo, motivo por el cual no se consideran aquí.")
    st.write () 
    st.markdown(f"<h3    style='text-align: center;'> ¿Por qué se usan Válvulas de compuerta? </h3>", unsafe_allow_html=True)
    st.write ()
    st.markdown("<div style='display: flex; justify-content: center;'><img src='https://i.pinimg.com/564x/4e/57/f4/4e57f477a95471f033d9516d52b07b99.jpg' alt='Imagen centrada' style='width: 300px; height: 200px;'></div>", unsafe_allow_html=True)
    st.write ("Las válvulas de compuerta son una opción común para controlar el flujo en tuberías debido a las siguientes ventajas:")
    st.write ("1.	Bajo costo: Las válvulas de compuerta son relativamente económicas en comparación con otros tipos de válvulas de control de flujo.") 
    st.write ("2.	Bajo coeficiente de pérdida de carga: Las válvulas de compuerta tienen una pérdida de carga baja cuando están completamente abiertas, lo que significa que la resistencia al flujo es mínima y se requiere menos energía para transportar el fluido a través de la tubería.") 
    st.write ("3.	Alta capacidad de flujo: Las válvulas de compuerta tienen una abertura de paso completa y, por lo tanto, ofrecen una alta capacidad de flujo.") 
    st.write ("4.	Sellado efectivo: Las válvulas de compuerta están diseñadas para proporcionar un sellado efectivo contra el flujo no deseado en ambos sentidos, lo que las hace útiles en aplicaciones donde se requiere un alto grado de control de flujo.") 
    st.write ("5.	Durabilidad: Las válvulas de compuerta están diseñadas para soportar altas presiones y temperaturas, lo que las hace adecuadas para aplicaciones en tuberías de alta presión y alta temperatura.") 
    st.write ("6.	Facilidad de operación: Las válvulas de compuerta son fáciles de operar y se pueden abrir y cerrar con poco esfuerzo. Además, no requieren un dispositivo de retención de posicionamiento para mantener su posición abierta o cerrada.") 
    st.write ()
    st.markdown(f"<h3    style='text-align: center;'> Ubicaciones de los accesorios </h3>", unsafe_allow_html=True)
    st.write ("La ubicación del accesorio, en este caso las válvulas de compuerta tendrán la función de bloquear el flujo parcial o por completo del fluido, en su defecto modificando la presión para un propósito definido, para ello es necesario pues, que sean los más eficientes posibles colocando una en cada línea independiente a las otra. Las distancias de esté sobre la sección del tubo correspondiente no influirá en la eficiencia del sistema (a menos que hagamos cambiar el tamaño del tubo.")
    st.markdown("<div style='display: flex; justify-content: center;'><img src='https://i.pinimg.com/564x/ef/7f/26/ef7f26964e8fdb8f999e4cff787ba8b2.jpg' alt='Imagen centrada' style='width: 300px; height: 200px;'></div>", unsafe_allow_html=True)
    st.write ()
    st.write (" figura 2-1 muestra dos tramos de tubería del mismo diámetro y longitud. El tramo superior contiene una válvula de globo. Si las pérdidas de presión API y AP2 se miden entre los puntos indicados, se encuentra que API es mayor que AP2.") 
    st.write ()
    st.markdown(f"<h3    style='text-align: center;'> Presión </h3>", unsafe_allow_html=True)
    st.write ()
    st.write ()
    st.markdown("<div style='display: flex; justify-content: center;'><img src='https://i.pinimg.com/564x/d2/69/c4/d269c44ca95ddc1f966b792038ce0d4f.jpg' alt='Imagen centrada' style='width: 300px; height: 200px;'></div>", unsafe_allow_html=True)
    st.write ()
    st.write ()
    st.write ("La cantidad de presión que un tubo de acero de cédula 40 puede soportar dependerá de varios factores, como el diámetro y la longitud del tubo, así como la temperatura y el tipo de fluido que se está transportando a través de la tubería. En general, se puede decir que un tubo de acero de cédula 40 puede soportar una presión máxima de alrededor de 2,500 psi (libras por pulgada cuadrada) para aplicaciones de agua y alrededor de 7,000 psi para aplicaciones de gas. Sin embargo, es importante tener en cuenta que estos valores son solo una guía general y que la presión máxima real que puede soportar el tubo dependerá de muchos otros factores.")
    st.write ()
    
     
    


if __name__ == '__main__':
    ESPECIFICACIONES()