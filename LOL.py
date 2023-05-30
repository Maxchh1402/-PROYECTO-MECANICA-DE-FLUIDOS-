import math
import streamlit as st
import numpy as np
import pandas as pd

def LOL():

    
      st.write()
      st.markdown("<h3 style='text-align: center;'>RED DE TUBERÍAS</h3>", unsafe_allow_html=True)
      st.write()
      st.markdown("<div style='display: flex; justify-content: center;'><img src='https://i.pinimg.com/564x/55/ab/fc/55abfc7f7bd7c1140aa9a87a40e9dd47.jpg' alt='Imagen centrada' style='width: 400px; height: 350px;'></div>", unsafe_allow_html=True)
     
      st.write("Aquí, se proporciona un croquis isométrico de la red de tuberías como ayuda visual."
            " Sin embargo, se necesitan algunas especificaciones para estas tuberías y "
            "esta es la situación de diseño que debe enfrentar  un ingeniero.")
      st.write()

      st.write("El objetivo de la red es suministrar agua en cuatro puntos  "
            "diferentes de una gran planta de proceso como parte de los servicios. "
            "Se han ideado unas válvulas de compuerta en la red, como se muestra, "
            "para que se pueda cortar el suministro en cualquiera de los cuatro puntos diferentes.")
      st.write()

      st.write(" Se estableció la disposición de la red de tuberías al considerar "
            "el equipo de proceso instalado, los soportes mecánicos de tubería "
            "plausibles y la seguridad. "
            "Sin embargo, no se determinaron los tamaños de las tuberías.")
      st.write()
      st.markdown("<h4 style='text-align: center;'>Datos de entrada</h4>", unsafe_allow_html=True)
      st.write()   
      st.write("(Siempre ingrese los valores de entrada de principio como recomendación para mejor análisis de los datos y que la app empiece a calcular).")
      st.write()  
      # Solicitar al usuario el valor de QA (caudal de alimentación)
      QA = st.number_input("Ingrese el valor de QA (caudal de alimentación): ", step= 0.00001)
      st.write()
      st.write("QA=",QA,"L/min")
      st.write("QA=",QA/6000,"m^3/s")
      # Solicitar al usuario el valor de HGL en metros
      HGL = st.number_input("Ingrese el valor de HGL de alimentación (en metros): ")
      QA=QA/6000
      st.write("HGL=",HGL,"m") 
               
      #DATOS
      # Declarar las variables de longitud de tuberías
      L1 = 74
      L2 = 113
      L3 = 73
      L4 = 198
      L5 = 22
      L6 = 13
      L7 = 61
      L8 = 33

      # Definir la velocidad constante
      velocidad = 1.5
      #PESO ESPECIFICO
      y=991*9.81
      # Declarar los valores para gravedad, rugosidad, y viscosidad
      g= 9.81 # en m/s^2
      e= 4.60E-05  # en metros
      v= 1.085000E-06  # en m^2/s

      st.markdown("<h4 style='text-align: center;'>Propiedades del fluido</h4>", unsafe_allow_html=True)
      st.write()
      st.write("Aqui se muestra una tabla de las propiedades del fluido que se encuentra en la red de tuberías con una rugosidad de",e,"metros." )
      data = {
        "Fluido": ["Agua (42.5°C)"],
      "Densidad promedio (kg/m^3)": ["991"],
      "Gravedad (m/s^2)": ["9.81"],
      "Peso Específico (N/m^3)": [y],
      "Viscosidad (m^2/s)": [1.085000E-06],

            }
    
      # Mostrar los valores en forma de tabla
      st.table(data)

      
          
       # Calcular las variables establecidas
      Q6 = QA * 0.35
      Q7 = QA * 0.5
      Q8 = Q6 * 0.35

      # Sustituir en los demás caudales
      Q1 = QA - Q6
      Q2 = QA - Q6 + Q7
      Q3 = (3/4) * QA + Q8 + Q7 - Q6
      Q4 = Q6 - Q7 - Q8 - (1/2) * QA
      Q5 = Q6 - (1/4) * QA


      # Imprimir los resultados

      st.write()

      # Mostrar los valores asignados
      st.markdown("<h4 style='text-align: center;'>Diseño</h4>", unsafe_allow_html=True)
      st.write()
      st.write("Valores de longitud de cada sección de tubería, diametro en función al caudal de alimentación:")
      data = {
        "Tubería": ["1", "2", "3", "4", "5", "6", "7", "8"],
      "Longitud (m)": [L1, L2, L3, L4, L5, L6, L7, L8],
      "Caudal (L/min)": ["{:.8f}".format(Q1*6000), "{:.8f}".format(Q2*6000), "{:.8f}".format(Q3*6000), "{:.8f}".format(Q4*6000), "{:.8f}".format(Q5*6000), "{:.8f}".format(Q6*6000), "{:.8f}".format(Q7*6000), "{:.8f}".format(Q8*6000)],

            }
    
      # Mostrar los valores en forma de tabla
      st.table(data)
      st.write("Los valores de caudales supuestos que se reportan luego de hacer el cálculo, con signo negativo, fueron modificados respecto al sentido de flujo que se predestino en el diagrama.")  
 

      def asignar_diametro(*caudales):
          data = [
              (0.00001, 0.00013, "1/8"),
              (0.00013, 0.00019, "3/8"),
              (0.00019, 0.00038, "1/2"),
              (0.00038, 0.00063, "3/4"),
              (0.00063, 0.00158, "1"),
              (0.00158, 0.00284, "1 1/2"),
              (0.00284, 0.00789, "2"),
              (0.00789, 0.01577, "3"),
              (0.01577, 0.03469, "5"),
              (0.03469, 0.08832, "6"),
              (0.08832, 0.15772, "14"),
              (0.15772, 0.28402, "16"),
              (0.28402, 0.50461, "20"),
              (0.50461, 1.17685, "24")
          ]

          diametros = []
          for caudal in caudales:
              diametro = None
              for item in data:
                  if item[0] <= caudal <= item[1]:
                      diametro = item[2]
                      break
              diametros.append(diametro)

          return diametros

      # Asignación de caudal
      caudal1 = abs(Q1)
      caudal2 = abs(Q2)
      caudal3 = abs(Q3)
      caudal4 = abs(Q4)
      caudal5 = abs(Q5)
      caudal6 = abs(Q6)
      caudal7 = abs(Q7)
      caudal8 = abs(Q8)


      diametros_asignados = asignar_diametro(caudal1, caudal2, caudal3, caudal4, caudal5, caudal6, caudal7, caudal8)

      # Guardar los valores de diámetro en una variable
      diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, diametro7, diametro8 = diametros_asignados

      # Imprimir los valores de diámetro guardados en las variables

      st.write()

      def asignar_diametro_interno(diametros_nominales):
          resultados = []

          for d1 in diametros_nominales:
              if d1 == "1/8":
                  ID = 0.0068
              elif d1 == "1/4":
                  ID = 0.0092
              elif d1 == "3/8":
                  ID = 0.0125
              elif d1 == "1/2":
                  ID = 0.0158
              elif d1 == "3/4":
                  ID = 0.021
              elif d1 == "1":
                  ID = 0.0266
              elif d1 == "1 1/4":
                  ID = 0.0351
              elif d1 == "1 1/2":
                  ID = 0.0409
              elif d1 == "2":
                  ID = 0.0525
              elif d1 == "2 1/2":
                  ID = 0.0627
              elif d1 == "3":
                  ID = 0.0779
              elif d1 == "3 1/2":
                  ID = 0.0901
              elif d1 == "4":
                  ID = 0.1023
              elif d1 == "5":
                  ID = 0.1282
              elif d1 == "6":
                  ID = 0.1541
              elif d1 == "8":
                  ID = 0.2027
              elif d1 == "10":
                  ID = 0.2545
              elif d1 == "12":
                  ID = 0.3033
              elif d1 == "14":
                  ID = 0.3333
              elif d1 == "16":
                  ID = 0.381
              elif d1 == "18":
                  ID = 0.4287
              elif d1 == "20":
                  ID = 0.4778
              elif d1 == "24":
                  ID = 0.5746   

              else:
                  ID = "Indefinido"

              resultados.append(ID)

          return resultados

      # Obtener los valores de diámetro interno
      diametros_nominales = [diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, diametro7, diametro8]
      diametros_internos = asignar_diametro_interno(diametros_nominales)

      # Guardar los valores de diámetro interno en variables individuales
      ID1, ID2, ID3, ID4, ID5, ID6, ID7, ID8 = diametros_internos

      # Imprimir los valores de diámetro interno

      st.write()

       

      # Mostrar los valores asignados
      st.write("Valores de longitud de cada sección de tubería, diametro en función al caudal de alimentación, obtenidos de tablas tomando como criterio de diseño una velocidad constante para el agua (aproximadamente 1.5 m/s).")
      data = {
        "Tubería": ["1", "2", "3", "4", "5", "6", "7", "8"],
      "Longitud (m)": [L1, L2, L3, L4, L5, L6, L7, L8],
      "Caudal (L/min)": ["{:.8f}".format(Q1*6000), "{:.8f}".format(Q2*6000), "{:.8f}".format(Q3*6000), "{:.8f}".format(Q4*6000), "{:.8f}".format(Q5*6000), "{:.8f}".format(Q6*6000), "{:.8f}".format(Q7*6000), "{:.8f}".format(Q8*6000)],
      "Diámetro (mm)": [ID1*1000, ID2*1000, ID3*1000, ID4*1000, ID5*1000, ID6*1000, ID7*1000, ID8*1000],
      "ND (in)": [diametro1, diametro2, diametro3, diametro4, diametro5, diametro6, diametro7, diametro8],

            }
    
      # Mostrar los valores en forma de tabla
      st.table(data)

      st.write("Con todos estos valores se calculan los caudales reales de cada rama, para eso se hace uso del método de Hardy Cross")
      st.write()

      def calcular_area_diametro(diametro):
          radio = diametro / 2
          area = math.pi * (radio ** 2)
          return area


      A1 = calcular_area_diametro(ID1)
      A2 = calcular_area_diametro(ID2)
      A3 = calcular_area_diametro(ID3)
      A4 = calcular_area_diametro(ID4)
      A5 = calcular_area_diametro(ID5)
      A6 = calcular_area_diametro(ID6)
      A7 = calcular_area_diametro(ID7)
      A8 = calcular_area_diametro(ID8)

      st.write("Áreas transversales:")
      st.write("Tubo 1:", A1,"mts^2")
      st.write("Tubo 2:", A2,"mts^2")
      st.write("Tubo 3:", A3,"mts^2")
      st.write("Tubo 4:", A4,"mts^2")
      st.write("Tubo 5:", A5,"mts^2")
      st.write("Tubo 6:", A6,"mts^2")
      st.write("Tubo 7:", A7,"mts^2")
      st.write("Tubo 8:", A8,"mts^2")
      st.write()
       
     #Codos

      Codo1=3
      Codo2=4
      Codo3=2
      Codo4=7
      Codo5=0
      Codo6=0
      Codo7=4
      Codo8=0

      #Valores de K para accesorios

      kcodo=30
      kválvula=8



       
      #HARDY CROSS
      

      st.write("Cálculo de los caudales reales:")
      st.write("Para el cálculo de los nuevos caudales se realiza un proceso iterativo donde se incluye ajustar los valores iniciales para caudal a través de una corrección gracias al cálculo de los hL (pérdidas del tubo correspondiente), igualando la suma de aquellos a 0.")
      

      # ITERACIONES
      st.markdown("<h3 style='text-align: center;'>Instrucciones </h3>", unsafe_allow_html=True)
      st.write()
      st.write("Para la búsqueda de los caudales reales:")
      st.write("1.- Calcular los valores de los caudales en función al flujo.")
      st.write("2.- Calcular el valor respectivo de número de Raynolds, con las dimensiones, el caudal y la viscosidad del fluido.")
      st.write("3.- Obtener el valor de factor de fricción para el respectivo tubo.")
      st.write("4.- Realizar la operación que ayuda a determinar la pérdida de fricción K del tubo. Se sabe que en cada ramal existen accesorios, tanto codos como válvulas, para aquellos que tienen dichos artículos se asignan.")
      data = {
        "k codo": ["30 fT"],
        "k válvula ": ["8 fT"],

         }
      # Mostrar los valores en forma de tabla
      st.table(data)
      st.write()
      st.write("fT es el factor de fricción correspondiente a esa sección de tubo.")
      st.write("Tanto codos como válvulas se manejan el mismo dieño (90° y válvulas completamente abiertas), por que es despreciable diferenciarlas si no es por la influencia del fT en este.")
      st.write()
      st.write("5.- Con el valor K, tabular el hL del tubo.")
      st.write("6.- Determinar la corrección para el caudal, renombrarlo y continuar con la siguiente iteración.")
      st.write("7.- En caso de tener un caudal en más de un circuito usar la corrección común para caudal total de este.")
      st.write()
      
      st.markdown("<h4 style='text-align: center;'>Tablas de respuestas</h4>", unsafe_allow_html=True)
      st.write()
      st.write()
      
      
      
      # Cálculo de D/e
      D_e_1 = ID1/e
      D_e_2 = ID2/e
      D_e_3 = ID3/e
      D_e_4 = ID4/e
      D_e_5 = ID5/e
      D_e_6 = ID6/e
      D_e_7 = ID7/e
      D_e_8 = ID8/e

      #ITERACIÓN 1

      I=1




      #CIRCUITO 1
      Q1_I1=Q1
      Q7_I7=-1*Q7
      Q5_I5=-1*Q5
      Q6_I6=-1*Q6


      #CIRCUITO 1 (signos)



      Signo1=Q1_I1/(abs(Q1_I1))
      Signo7=Q7_I7/(abs(Q7_I7))
      Signo5=Q5_I5/(abs(Q5_I5))
      Signo6=Q6_I6/(abs(Q6_I6))




      # Calcular números de Raynolds
      Nre1= (abs(Q1_I1*ID1))/(A1*v)
      Nre7= (abs(Q7_I7*ID7))/(A7*v)
      Nre5= (abs(Q5_I5*ID5))/(A5*v)
      Nre6= (abs(Q6_I6*ID6))/(A6*v)

      # Calcular el factor de fricción fT

      fT1 = (0.25 / (math.log10(1 / (3.7 * D_e_1) + 5.74 / (Nre1 ** 0.9))) ** 2)
      fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
      fT5 = (0.25 / (math.log10(1 / (3.7 * D_e_5) + 5.74 / (Nre5 ** 0.9))) ** 2)
      fT6 = (0.25 / (math.log10(1 / (3.7 * D_e_6) + 5.74 / (Nre6 ** 0.9))) ** 2)

      K1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2)) +kválvula*fT1 * (1 / (2 * g * A1 ** 2)) +fT1 * (L1 / ID1) * (1 / (2 * g * A1 ** 2))
      K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
      K5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2)) +kválvula*fT5 * (1 / (2 * g * A5 ** 2)) +fT5 * (L5 / ID5) * (1 / (2 * g * A5 ** 2))
      K6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2)) +fT6 * (L6 / ID6) * (1 / (2 * g * A6 ** 2))





      # Calcular de hL de los tubos, considerando el sentido del flujo

      hL1=K1*(Q1_I1**2)*Signo1
      hL7=K7*(Q7_I7**2)*Signo7
      hL5=K5*(Q5_I5**2)*Signo5
      hL6=K6*(Q6_I6**2)*Signo6




      # Calcular de 2kQ de los tubos, sin considerar el signo

      kQ1=2*K1*abs(Q1_I1)
      kQ7=2*K7*abs(Q7_I7)
      kQ5=2*K5*abs(Q5_I5)
      kQ6=2*K6*abs(Q6_I6)




      # Calcular de deltaQ CIRCUITO 1

      SUMAhL1=hL1+hL7+hL5+hL6
      SUMA2kQ1=kQ1+kQ7+kQ5+kQ6

      DeltaQ1=(SUMAhL1/SUMA2kQ1)




      Q1_I1=Q1_I1-DeltaQ1
      Q7_I7=Q7_I7-DeltaQ1
      Q5_I5=Q5_I5-DeltaQ1
      Q6_I6=Q6_I6-DeltaQ1





      #CIRCUITO 2
      Q2_I2=Q2
      Q7_I7_2=Q7
      Q8_I8=-1*Q8




      #CIRCUITO 2 (signos)
      Signo2=Q2_I2/(abs(Q2_I2))
      Signo7=Q7_I7_2/(abs(Q7_I7_2))
      Signo8=Q8_I8/(abs(Q8_I8))




      # Calcular números de Raynolds
      Nre2= (abs(Q2_I2*ID2))/(A2*v)
      Nre7= (abs(Q7_I7_2*ID7))/(A7*v)
      Nre8= (abs(Q8_I8*ID8))/(A8*v)


      # Calcular el factor de fricción fT

      fT2 = (0.25 / (math.log10(1 / (3.7 * D_e_2) + 5.74 / (Nre2 ** 0.9))) ** 2)
      fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
      fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)


      K2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2)) +fT2 * (L2 / ID2) * (1 / (2 * g * A2 ** 2))
      K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
      K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2)) +fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))





      # Calcular de hL de los tubos, considerando el sentido del flujo

      hL2=K2*(Q2_I2**2)*Signo2
      hL7=K7*(Q7_I7_2**2)*Signo7
      hL8=K8*(Q8_I8**2)*Signo8



      # Calcular de 2kQ de los tubos, sin considerar el signo

      kQ2=2*K2*abs(Q2_I2)
      kQ7=2*K7*abs(Q7_I7_2)
      kQ8=2*K8*abs(Q8_I8)



      # Calcular de deltaQ CIRCUITO 2

      SUMAhL1=hL2+hL7+hL8
      SUMA2kQ1=kQ2+kQ7+kQ8

      DeltaQ2=(SUMAhL1/SUMA2kQ1)

      Q2_I2=Q2_I2-DeltaQ2
      Q7_I7_2=Q7_I7_2-DeltaQ2
      Q8_I8=Q8_I8-DeltaQ2



      #CIRCUITO 3
      Q3_I3=Q3
      Q8_I8_2=Q8
      Q4_I4=-1*Q4



      #CIRCUITO 3 (signos)
      Signo3=Q3_I3/(abs(Q3_I3))
      Signo8=Q8_I8_2/(abs(Q8_I8_2))
      Signo4=Q4_I4/(abs(Q4_I4))



      # Calcular números de Raynolds
      Nre3= (abs(Q3_I3*ID3))/(A3*v)
      Nre8= (abs(Q8_I8_2*ID8))/(A8*v)
      Nre4= (abs(Q4_I4*ID4))/(A4*v)


      # Calcular el factor de fricción fT

      fT3 = (0.25 / (math.log10(1 / (3.7 * D_e_3) + 5.74 / (Nre3 ** 0.9))) ** 2)
      fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)
      fT4 = (0.25 / (math.log10(1 / (3.7 * D_e_4) + 5.74 / (Nre4 ** 0.9))) ** 2)


      K3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2)) +fT3 * (L3 / ID3) * (1 / (2 * g * A3 ** 2))
      K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2))+fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))
      K4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2)) +kválvula*fT4 * (1 / (2 * g * A4 ** 2)) +fT4 * (L4 / ID4) * (1 / (2 * g * A4 ** 2))





      # Calcular de hL de los tubos, considerando el sentido del flujo

      hL3=K3*(Q3_I3**2)*Signo3
      hL8=K8*(Q8_I8_2**2)*Signo8
      hL4=K4*(Q4_I4**2)*Signo4



      # Calcular de 2kQ de los tubos, sin considerar el signo

      kQ3=2*K3*abs(Q3_I3)
      kQ8=2*K8*abs(Q8_I8_2)
      kQ4=2*K4*abs(Q4_I4)



      # Calcular de deltaQ CIRCUITO 3

      SUMAhL1=hL3+hL8+hL4
      SUMA2kQ1=kQ3+kQ8+kQ4

      DeltaQ3=(SUMAhL1/SUMA2kQ1)

      Q3_I3=Q3_I3-DeltaQ3
      Q8_I8_2=Q8_I8_2-DeltaQ3
      Q4_I4=Q4_I4-DeltaQ3




      #Caudales comunes

      Q7_I7=Q7_I7+DeltaQ2
      Q7_I7_2=Q7_I7_2+DeltaQ1
      Q8_I8=Q8_I8+DeltaQ3
      Q8_I8_2=Q8_I8_2+DeltaQ2



      #PORCENTAJES DE ERROR

      Chg1=(DeltaQ1/(Q1_I1+DeltaQ1))*100
      Chg2=(DeltaQ2/(Q2_I2+DeltaQ2))*100
      Chg3=(DeltaQ3/(Q3_I3+DeltaQ3))*100
      Chg4=(DeltaQ3/(Q4_I4+DeltaQ3))*100
      Chg5=(DeltaQ1/(Q5_I5+DeltaQ1))*100
      Chg6=(DeltaQ1/(Q6_I6+DeltaQ1))*100
      Chg7=(DeltaQ1/(Q7_I7+DeltaQ1-DeltaQ2))*100
      Chg7_2=(DeltaQ2/(Q7_I7_2+DeltaQ2-DeltaQ1))*100
      Chg8=(DeltaQ2/(Q8_I8+DeltaQ2-DeltaQ3))*100
      Chg8_2=(DeltaQ3/(Q8_I8_2+DeltaQ3-DeltaQ2))*100





      #ITERACIÓN 2,3,4... (COPIAR CAUDALES ANTERIORES SOLAMENTE)
      iteracion = 2
      while iteracion <= 99:


          # Resto del código...

          #CIRCUITO 1 (signos)

          Signo1=Q1_I1/(abs(Q1_I1))
          Signo7=Q7_I7/(abs(Q7_I7))
          Signo5=Q5_I5/(abs(Q5_I5))
          Signo6=Q6_I6/(abs(Q6_I6))

          # Calcular números de Raynolds
          Nre1= (abs(Q1_I1*ID1))/(A1*v)
          Nre7= (abs(Q7_I7*ID7))/(A7*v)
          Nre5= (abs(Q5_I5*ID5))/(A5*v)
          Nre6= (abs(Q6_I6*ID6))/(A6*v)

          # Calcular el factor de fricción fT

          fT1 = (0.25 / (math.log10(1 / (3.7 * D_e_1) + 5.74 / (Nre1 ** 0.9))) ** 2)
          fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
          fT5 = (0.25 / (math.log10(1 / (3.7 * D_e_5) + 5.74 / (Nre5 ** 0.9))) ** 2)
          fT6 = (0.25 / (math.log10(1 / (3.7 * D_e_6) + 5.74 / (Nre6 ** 0.9))) ** 2)

          K1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2)) +kválvula*fT1 * (1 / (2 * g * A1 ** 2)) +fT1 * (L1 / ID1) * (1 / (2 * g * A1 ** 2))
          K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
          K5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2)) +kválvula*fT5 * (1 / (2 * g * A5 ** 2)) +fT5 * (L5 / ID5) * (1 / (2 * g * A5 ** 2))
          K6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2)) +fT6 * (L6 / ID6) * (1 / (2 * g * A6 ** 2))

          # Calcular de hL de los tubos, considerando el sentido del flujo

          hL1=K1*(Q1_I1**2)*Signo1
          hL7=K7*(Q7_I7**2)*Signo7
          hL5=K5*(Q5_I5**2)*Signo5
          hL6=K6*(Q6_I6**2)*Signo6

          # Calcular de 2kQ de los tubos, sin considerar el signo

          kQ1=2*K1*abs(Q1_I1)
          kQ7=2*K7*abs(Q7_I7)
          kQ5=2*K5*abs(Q5_I5)
          kQ6=2*K6*abs(Q6_I6)

          # Calcular de deltaQ CIRCUITO 1

          SUMAhL1=hL1+hL7+hL5+hL6
          SUMA2kQ1=kQ1+kQ7+kQ5+kQ6

          DeltaQ1=(SUMAhL1/SUMA2kQ1)

          Q1_I1=Q1_I1-DeltaQ1
          Q7_I7=Q7_I7-DeltaQ1
          Q5_I5=Q5_I5-DeltaQ1
          Q6_I6=Q6_I6-DeltaQ1

          #CIRCUITO 2

          #CIRCUITO 2 (signos)
          Signo2=Q2_I2/(abs(Q2_I2))
          Signo7=Q7_I7_2/(abs(Q7_I7_2))
          Signo8=Q8_I8/(abs(Q8_I8))

          # Calcular números de Raynolds
          Nre2= (abs(Q2_I2*ID2))/(A2*v)
          Nre7= (abs(Q7_I7_2*ID7))/(A7*v)
          Nre8= (abs(Q8_I8*ID8))/(A8*v)

          # Calcular el factor de fricción fT

          fT2 = (0.25 / (math.log10(1 / (3.7 * D_e_2) + 5.74 / (Nre2 ** 0.9))) ** 2)
          fT7 = (0.25 / (math.log10(1 / (3.7 * D_e_7) + 5.74 / (Nre7 ** 0.9))) ** 2)
          fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)

          K2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2)) +fT2 * (L2 / ID2) * (1 / (2 * g * A2 ** 2))
          K7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2)) +fT7 * (L7 / ID7) * (1 / (2 * g * A7 ** 2))
          K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2)) +fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))

          # Calcular de hL de los tubos, considerando el sentido del flujo

          hL2 = K2 * (Q2_I2 ** 2) * Signo2
          hL7 = K7 * (Q7_I7_2 ** 2) * Signo7
          hL8 = K8 * (Q8_I8 ** 2) * Signo8

          # Calcular de 2kQ de los tubos, sin considerar el signo

          kQ2=2*K2*abs(Q2_I2)
          kQ7=2*K7*abs(Q7_I7_2)
          kQ8=2*K8*abs(Q8_I8)

          # Calcular de deltaQ CIRCUITO 2

          SUMAhL1=hL2+hL7+hL8
          SUMA2kQ1=kQ2+kQ7+kQ8

          DeltaQ2=(SUMAhL1/SUMA2kQ1)

          Q2_I2=Q2_I2-DeltaQ2
          Q7_I7_2=Q7_I7_2-DeltaQ2
          Q8_I8=Q8_I8-DeltaQ2

          #CIRCUITO 3

          #CIRCUITO 3 (signos)
          Signo3=Q3_I3/(abs(Q3_I3))
          Signo8=Q8_I8_2/(abs(Q8_I8_2))
          Signo4=Q4_I4/(abs(Q4_I4))

          # Calcular números de Raynolds
          Nre3= (abs(Q3_I3*ID3))/(A3*v)
          Nre8= (abs(Q8_I8_2*ID8))/(A8*v)
          Nre4= (abs(Q4_I4*ID4))/(A4*v)

          # Calcular el factor de fricción fT

          fT3 = (0.25 / (math.log10(1 / (3.7 * D_e_3) + 5.74 / (Nre3 ** 0.9))) ** 2)
          fT8 = (0.25 / (math.log10(1 / (3.7 * D_e_8) + 5.74 / (Nre8 ** 0.9))) ** 2)
          fT4 = (0.25 / (math.log10(1 / (3.7 * D_e_4) + 5.74 / (Nre4 ** 0.9))) ** 2)

          K3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2)) +fT3 * (L3 / ID3) * (1 / (2 * g * A3 ** 2))
          K8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2)) +kválvula*fT8 * (1 / (2 * g * A8 ** 2))+fT8 * (L8 / ID8) * (1 / (2 * g * A8 ** 2))
          K4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2)) +kválvula*fT4 * (1 / (2 * g * A4 ** 2)) +fT4 * (L4 / ID4) * (1 / (2 * g * A4 ** 2))

          # Calcular de hL de los tubos, considerando el sentido del flujo

          hL3=K3*(Q3_I3**2)*Signo3
          hL8=K8*(Q8_I8_2**2)*Signo8
          hL4=K4*(Q4_I4**2)*Signo4

          # Calcular de 2kQ de los tubos, sin considerar el signo

          kQ3=2*K3*abs(Q3_I3)
          kQ8=2*K8*abs(Q8_I8_2)
          kQ4=2*K4*abs(Q4_I4)

          # Calcular de deltaQ CIRCUITO 3

          SUMAhL1=hL3+hL8+hL4
          SUMA2kQ1=kQ3+kQ8+kQ4

          DeltaQ3=(SUMAhL1/SUMA2kQ1)

          Q3_I3=Q3_I3-DeltaQ3
          Q8_I8_2=Q8_I8_2-DeltaQ3
          Q4_I4=Q4_I4-DeltaQ3

          #Caudales comunes

          Q7_I7=Q7_I7+DeltaQ2
          Q7_I7_2=Q7_I7_2+DeltaQ1
          Q8_I8=Q8_I8+DeltaQ3
          Q8_I8_2=Q8_I8_2+DeltaQ2

          #PORCENTAJES DE ERROR

          Chg1=(DeltaQ1/(Q1_I1+DeltaQ1))*100
          Chg2=(DeltaQ2/(Q2_I2+DeltaQ2))*100
          Chg3=(DeltaQ3/(Q3_I3+DeltaQ3))*100
          Chg4=(DeltaQ3/(Q4_I4+DeltaQ3))*100
          Chg5=(DeltaQ1/(Q5_I5+DeltaQ1))*100
          Chg6=(DeltaQ1/(Q6_I6+DeltaQ1))*100
          Chg7=(DeltaQ1/(Q7_I7+DeltaQ1-DeltaQ2))*100
          Chg7_2=(DeltaQ2/(Q7_I7_2+DeltaQ2-DeltaQ1))*100
          Chg8=(DeltaQ2/(Q8_I8+DeltaQ2-DeltaQ3))*100
          Chg8_2=(DeltaQ3/(Q8_I8_2+DeltaQ3-DeltaQ2))*100

      # Actualizar el valor de iteracion
          iteracion += 1
            
      st.markdown(f"<h4 style='text-align: center;'>(ITERACIÓN No. {iteracion}) </h4>", unsafe_allow_html=True)
      st.write()

      st.markdown(f"<h5 style='text-align: center;'> De nodo a nodo </h5>", unsafe_allow_html=True)
      st.write()
      # CAUDALES FINALES


      st.write()

      # PÉRDIDAS TOTALES POR LOS TUBOS Y ACCESORIOS


      st.write()


      #DIRECCIONES

      #SIGNOS DE CAUDALES SEGÚN CONVENCIÓN

      SQ1=1
      SQ2=1
      SQ3=1
      SQ4=-1
      SQ5=-1
      SQ6=-1
      SQ7=-1
      SQ8=-1
       

      # Q1
      if Q1_I1 * SQ1 > 0:
          
          D1="AE"
      else:
          
          D1="EA"
      # Q2
      if Q2_I2 * SQ2 > 0:
          
          D2="EJ"
      else:
          
          D2="JE"

      # Q3
      if Q3_I3 * SQ3 > 0:
          
          D3="JM"
      else:
          
          D3="MJ"

      # Q4
      if Q4_I4 * SQ4 > 0:
          
          D4="UM"
      else:
          
          D4="MU"

      # Q5
      if Q5_I5 * SQ5 > 0:
          
          D5="ZU"
      else:
          
          D5="UZ"

      # Q6
      if Q6_I6 * SQ6 > 0:
          
          D6="AZ"
      else:
          
          D6="ZA"

      # Q7
      if Q7_I7 * SQ7 > 0:
          
          D7="UE"
      else:
          
          D7="EU"

      # Q8
      if Q8_I8 * SQ8 > 0:
          
          D8="UJ"
      else:
          
          D8="JU"

      data = {
        "Sección": ["1", "2", "3", "4", "5", "6", "7", "8"],
        "Dirección flujo":[D1, D2, D3, D4, D5, D6, D7, D8],
        "Caudal (m^3/s)": ["{:.8f}".format(Q1_I1), "{:.8f}".format(Q2_I2), "{:.8f}".format(Q3_I3), "{:.8f}".format(Q4_I4), "{:.8f}".format(Q5_I5), "{:.8f}".format(Q6_I6), "{:.8f}".format(Q7_I7), "{:.8f}".format(Q8_I8)],
        "hL (m)": [abs(hL1), abs(hL2), abs(hL3), abs(hL4), abs(hL5), abs(hL6), abs(hL7), abs(hL8)]

            }

      
      # Mostrar los valores en forma de tabla
      st.table(data)
      st.write("Para los valores que indican el flujo por medio del signo, en caso de corregirse al incialmente definido, se maneja la columna """"Dirección flujo"""" la cuál evalua el caudal para definir el sentido correcto (este se determina como todo lo demás).")
      #CÁLCULO DE HGL
      

      
      #CÁLCULO DE PRESIONES

 

      #ALTURAS DE CADA PUNTO

      A=0
      B = 0
      C = -13
      D = -13
      E = -13
      F = -13
      G = 12
      H = 12
      I = -5
      J = -13
      K = -13
      L = -13
      M = -29
      N = -29
      O = -13
      P = -13
      Q = -26
      R = -26
      S = -26
      T = -26
      U = -13
      Z = -13
      V = -13
      X = -13
      Y = -13
      W = -13
      J = -13

      #LONGITUDES DE CADA SECCIÓN DE TUBERÍA

      AB = 25
      BC = 13
      CD = 14
      DE = 22
      EF = 8
      FG = 12
      GH = 33
      HI = 52
      IJ = 8
      JK = 7
      KL = 50
      LM = 16
      MN = 73
      NO = 16
      OP = 25
      PQ = 13
      QR = 14
      RS = 25
      ST = 19
      TU = 13
      UZ = 22
      UV = 10
      VX = 8.5
      XY = 15
      YW = 8.5
      WE = 19
      ZA = 13
      UJ = 33

      #CALCULOS DE Kde cada sección

      KAB = fT1 * (AB / ID1) * (1 / (2 * g * A1 ** 2))
      KBC = fT1 * (BC / ID1) * (1 / (2 * g * A1 ** 2))+(8*fT1)* (1 / (2 * g * A1 ** 2))
      KCD = fT1 * (CD / ID1) * (1 / (2 * g * A1 ** 2))
      KDE = fT1 * (DE / ID1) * (1 / (2 * g * A1 ** 2))

      KEF = fT2 * (EF / ID2) * (1 / (2 * g * A2 ** 2))
      KFG = fT2 * (FG / ID2) * (1 / (2 * g * A2 ** 2))
      KGH = fT2 * (GH / ID2) * (1 / (2 * g * A2 ** 2))
      KHI = fT2 * (HI / ID2) * (1 / (2 * g * A2 ** 2))
      KIJ = fT2 * (IJ / ID2) * (1 / (2 * g * A2 ** 2))

      KJK = fT3 * (JK / ID3) * (1 / (2 * g * A3 ** 2))
      KKL = fT3 * (KL / ID3) * (1 / (2 * g * A3 ** 2))
      KLM = fT3 * (LM / ID3) * (1 / (2 * g * A3 ** 2))

      KMN = fT4 * (MN / ID4) * (1 / (2 * g * A4 ** 2))
      KNO = fT4 * (NO / ID4) * (1 / (2 * g * A4 ** 2))
      KOP = fT4 * (OP / ID4) * (1 / (2 * g * A4 ** 2))
      KPQ = fT4 * (PQ / ID4) * (1 / (2 * g * A4 ** 2))
      KQR = fT4 * (QR / ID4) * (1 / (2 * g * A4 ** 2))
      KRS = fT4 * (RS / ID4) * (1 / (2 * g * A4 ** 2))
      KST = fT4 * (ST / ID4) * (1 / (2 * g * A4 ** 2))+(8*fT4)* (1 / (2 * g * A4 ** 2))
      KTU = fT4 * (TU / ID4) * (1 / (2 * g * A4 ** 2))

      KUZ = fT5 * (UZ / ID5) * (1 / (2 * g * A5 ** 2))+(8*fT5)* (1 / (2 * g * A5 ** 2))

      KUV = fT7 * (UV / ID7) * (1 / (2 * g * A7 ** 2))
      KVX = fT7 * (VX / ID7) * (1 / (2 * g * A7 ** 2))
      KXY = fT7 * (XY / ID7) * (1 / (2 * g * A7 ** 2))
      KYW = fT7 * (YW / ID7) * (1 / (2 * g * A7 ** 2))
      KWE = fT7 * (WE / ID7) * (1 / (2 * g * A7 ** 2))

      KZA = fT6 * (ZA / ID6) * (1 / (2 * g * A6 ** 2))

      KUJ = fT8 * (UJ / ID8) * (1 / (2 * g * A8 ** 2))+(8*fT8)* (1 / (2 * g * A8 ** 2))

      #CALCULO DE hL de cada sección

      hLAB=KAB*(abs(Q1_I1))**2
      hLBC=KBC*(abs(Q1_I1))**2
      hLCD=KCD*(abs(Q1_I1))**2
      hLDE=KDE*(abs(Q1_I1))**2

      hLEF=KEF*(abs(Q2_I2))**2
      hLFG=KFG*(abs(Q2_I2))**2
      hLGH=KGH*(abs(Q2_I2))**2
      hLHI=KHI*(abs(Q2_I2))**2
      hLIJ=KIJ*(abs(Q2_I2))**2

      hLJK=KJK*(abs(Q3_I3))**2
      hLKL=KKL*(abs(Q3_I3))**2
      hLLM=KLM*(abs(Q3_I3))**2

      hLMN=KMN*(abs(Q4_I4))**2
      hLNO=KNO*(abs(Q4_I4))**2
      hLOP=KOP*(abs(Q4_I4))**2
      hLPQ=KPQ*(abs(Q4_I4))**2
      hLQR=KQR*(abs(Q4_I4))**2
      hLRS=KRS*(abs(Q4_I4))**2
      hLST=KST*(abs(Q4_I4))**2
      hLTU=KTU*(abs(Q4_I4))**2

      hLUZ=KUZ*(abs(Q5_I5))**2

      hLUV=KUV*(abs(Q7_I7))**2
      hLVX=KVX*(abs(Q7_I7))**2
      hLXY=KXY*(abs(Q7_I7))**2
      hLYW=KYW*(abs(Q7_I7))**2
      hLWE=KWE*(abs(Q7_I7))**2

      hLZA=KZA*(abs(Q6_I6))**2

      hLUJ=KUJ*(abs(Q8_I8))**2

      #KCODOS

      KC1 = Codo1*kcodo*fT1 * (1 / (2 * g * A1 ** 2))
      KC2 = Codo2*kcodo*fT2 * (1 / (2 * g * A2 ** 2))
      KC3 = Codo3*kcodo*fT3 * (1 / (2 * g * A3 ** 2))
      KC4 = Codo4*kcodo*fT4 * (1 / (2 * g * A4 ** 2))
      KC5 = Codo5*kcodo*fT5 * (1 / (2 * g * A5 ** 2))
      KC6 = Codo6*kcodo*fT6 * (1 / (2 * g * A6 ** 2))
      KC7 = Codo7*kcodo*fT7 * (1 / (2 * g * A7 ** 2))
      KC8 = Codo8*kcodo*fT8 * (1 / (2 * g * A8 ** 2))

      #hLCODOS

      hLC1=KC1*(abs(Q1_I1)**2)
      hLC2=KC2*(abs(Q2_I2)**2)
      hLC3=KC3*(abs(Q3_I3)**2)
      hLC4=KC4*(abs(Q4_I4)**2)
      hLC5=KC5*(abs(Q5_I5)**2)
      hLC6=KC6*(abs(Q6_I6)**2)
      hLC7=KC7*(abs(Q7_I7)**2)
      hLC8=KC8*(abs(Q8_I8)**2)

      #PRESIONES
      PA=(HGL*y)-A

      #PAE
      if Q1_I1*SQ1 > 0:
          #PE=P2
          PB = ((PA / y) + A - B - (hLAB+1/3*hLC1)) * y
          PC = ((PB / y) + B - C - (hLBC+1/3*hLC1)) * y
          PD = ((PC / y) + C - D - (hLCD+1/3*hLC1)) * y
          PE = ((PD / y) + D - E - (hLDE)) * y

      else:# PE=P1
          PB = ((PA / y) + A - B + (hLAB + 1 / 3 * hLC1)) * y
          PC = ((PB / y) + B - C + (hLBC + 1 / 3 * hLC1)) * y
          PD = ((PC / y) + C - D + (hLCD + 1 / 3 * hLC1)) * y
          PE = ((PD / y) + D - E + (hLDE)) * y

      #PEJ
      if Q2_I2*SQ2 > 0:
          #PJ=P2
          PF = ((PE / y) + E - F - (hLEF+1/4*hLC2)) * y
          PG = ((PF / y) + F - G - (hLFG+1/4*hLC2)) * y
          PH = ((PG / y) + G - H - (hLGH+1/4*hLC2)) * y
          PI = ((PH / y) + H - I - (hLHI+1/4*hLC2)) * y
          PJ = ((PI / y) + I - J - (hLIJ)) * y

      else:# PJ=P1
          PF = ((PE / y) + E - F + (hLEF + 1 / 4 * hLC2)) * y
          PG = ((PF / y) + F - G + (hLFG + 1 / 4 * hLC2)) * y
          PH = ((PG / y) + G - H + (hLGH + 1 / 4 * hLC2)) * y
          PI = ((PH / y) + H - I + (hLHI + 1 / 4 * hLC2)) * y
          PJ = ((PI / y) + I - J + (hLIJ)) * y

      #PJM
      if Q3_I3*SQ3 > 0:
          #PM=P2
          PK = ((PJ / y) + J - K - (hLJK+1/2*hLC3)) * y
          PL = ((PK / y) + K - L - (hLKL+1/2*hLC3)) * y
          PM = ((PL / y) + L - M - (hLLM)) * y

      else:# PM=P1
          PK = ((PJ / y) + J - K + (hLJK + 1 / 2 * hLC3)) * y
          PL = ((PK / y) + K - L + (hLKL + 1 / 2 * hLC3)) * y
          PM = ((PL / y) + L - M + (hLLM)) * y

      #PMU
      if Q4_I4*SQ4 > 0:
          #PU=P1
          PN = ((PM / y) + M - N + (hLMN + 1 / 7 * hLC4)) * y
          PO = ((PN / y) + N - O + (hLNO + 1 / 7 * hLC4)) * y
          PP = ((PO / y) + O - P + (hLOP + 1 / 7 * hLC4)) * y
          PpQ = ((PP / y) + P - Q + (hLPQ + 1 / 7 * hLC4)) * y
          PR = ((PpQ / y) + Q - R + (hLQR + 1 / 7 * hLC4)) * y
          PS = ((PR / y) + R - S + (hLRS + 1 / 7 * hLC4)) * y
          PT = ((PS / y) + S - T + (hLST + 1 / 7 * hLC4)) * y
          PU = ((PT / y) + T - U + (hLTU)) * y

      else:# PU=P2
          PN = ((PM / y) + M - N - (hLMN + 1 / 7 * hLC4)) * y
          PO = ((PN / y) + N - O - (hLNO + 1 / 7 * hLC4)) * y
          PP = ((PO / y) + O - P - (hLOP + 1 / 7 * hLC4)) * y
          PpQ = ((PP / y) + P - Q - (hLPQ + 1 / 7 * hLC4)) * y
          PR = ((PpQ / y) + Q - R - (hLQR + 1 / 7 * hLC4)) * y
          PS = ((PR / y) + R - S - (hLRS + 1 / 7 * hLC4)) * y
          PT = ((PS / y) + S - T - (hLST + 1 / 7 * hLC4)) * y
          PU = ((PT / y) + T - U - (hLTU)) * y

      #PUZ
      if Q5_I5*SQ5 > 0:
          #PZ=P1
          PZ = ((PU / y) + U - Z + (hLUZ)) * y

      else:# PU=P2
          PZ = ((PU / y) + U - Z - (hLUZ)) * y

      #PUE
      if Q7_I7*SQ7 > 0:
          #PU=P1
          PV =  ((PU / y) + U - V - (hLUV + 1 / 4 * hLC7)) * y
          PX =  ((PV / y) + V - X - (hLVX + 1 / 4 * hLC7)) * y
          PY =  ((PX / y) + X - Y - (hLXY + 1 / 4 * hLC7)) * y
          PW =  ((PY / y) + Y - W - (hLYW + 1 / 4 * hLC7)) * y
          PE2 = ((PW / y) + W - E - (hLWE)) * y

      else:# PU=P2
          PV = ((PU / y) + U - V +  (hLUV + 1 / 4 * hLC7)) * y
          PX = ((PV / y) + V - X +  (hLVX + 1 / 4 * hLC7)) * y
          PY = ((PX / y) + X - Y +  (hLXY + 1 / 4 * hLC7)) * y
          PW = ((PY / y) + Y - W +  (hLYW + 1 / 4 * hLC7)) * y
          PE2 = ((PW / y) + W - E + (hLWE)) * y

      #PZA
      if Q6_I6*SQ6 > 0:
          #PZ=P2
          PZ2 = ((PA / y) + A - Z - (hLZA)) * y

      else:# PZ=P1
          PZ2 = ((PA / y) + A - Z + (hLZA)) * y

      #PUJ
      if Q8_I8*SQ8 > 0:
          #PJ=P2
          PU2 = ((PJ / y) + U - J + (hLUJ)) * y

      else:# PU=P2
          PU2 = ((PJ / y) + U - J - (hLUJ)) * y

      # CONVERSION A PSI

      #CALCULO DE HGL

      HGLB=(PB/y)+B
      HGLC=(PC/y)+C
      HGLD=(PD/y)+D
      HGLE=(PE/y)+E
      HGLF=(PF/y)+F
      HGLG=(PG/y)+G
      HGLH=(PH/y)+H
      HGLI=(PI/y)+I
      HGLJ=(PJ/y)+J
      HGLK=(PK/y)+K
      HGLL=(PL/y)+L
      HGLM=(PM/y)+M
      HGLN=(PN/y)+N
      HGLO=(PO/y)+O
      HGLP=(PP/y)+P
      HGLQ=(PQ/y)+Q
      HGLR=(PR/y)+R
      HGLS=(PS/y)+S
      HGLT=(PT/y)+T
      HGLU=(PU/y)+U
      HGLZ=(PZ/y)+Z
      HGLV=(PV/y)+V
      HGLX=(PX/y)+X
      HGLY=(PY/y)+Y
      HGLW=(PW/y)+W
      HGLE2=(PE2/y)+E
      HGLZ2=(PZ2/y)+Z
      HGLU2=(PU2/y)+U

      st.write()
      st.write("Esta primero tabla nos muestra información importante; se trata de determinar el caudal total que fluje por un conjunto delimitado de tuberia por puntos de bifurcacion descarga o alimentacion. Con ello es posible entonces calcular los datos por cada tubo independiente.") 
      st.markdown(f"<h5 style='text-align: center;'> Por sección de tubería </h5>", unsafe_allow_html=True)
      st.write()

      st.write("Considerando el punto de alimentación como el origen tabulamos y reportamos los datos:")
      st.write()
      data = {
        "Nodo": ["A"],
        "Altura (m)": ["0"],
        "Presión (N/m^2)":[PA],
        "Presión (psi)":[PA/6894.76],
        "HGL": [HGL],

            }
      # Mostrar los valores en forma de tabla
      st.table(data)

      data = {
        "Sección": ["AB", "BC", "CD", "DE", "EF", "FG", "GH", "HI","IJ","JK","KL","LM","MN","NO","OP","PQ","QR","RS","ST","TU","UZ","UV","VX","XY","YW","WE","ZA","UJ"],
        "Altura (m)": [B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, Z, V, X, Y, W, E, Z, J],
        "Longitud (m)":[AB, BC, CD, DE, EF, FG, GH, HI, IJ, JK, KL, LM, MN, NO, OP, PQ, QR, RS, ST, TU, UZ, UV, VX, XY, YW, WE, ZA, UJ],
        "hL (m)": [abs(hLAB), abs(hLBC), abs(hLCD), abs(hLDE), abs(hLEF), abs(hLFG), abs(hLGH), abs(hLHI),abs(hLIJ), abs(hLJK), abs(hLKL), abs(hLLM), abs(hLMN), abs(hLNO), abs(hLOP), abs(hLPQ),abs(hLQR), abs(hLRS), abs(hLST), abs(hLTU), abs(hLUZ), abs(hLUV), abs(hLVX), abs(hLXY),abs(hLYW), abs(hLWE), abs(hLZA), abs(hLUJ)]

            }

      
      # Mostrar los valores en forma de tabla
      st.table(data)

      st.markdown(f"<h6 style='text-align: center;'> Presiones y HGL </h6>", unsafe_allow_html=True)
      st.write()
      data = {
        "Sección": ["AB", "BC", "CD", "DE", "EF", "FG", "GH", "HI","IJ","JK","KL","LM","MN","NO","OP","PQ","QR","RS","ST","TU","UZ","UV","VX","XY","YW","WE","ZA","UJ"],
        "Presión (N/m^2)": [PB, PC, PD, PE, PF, PG, PH, PI, PJ, PK, PL, PM, PN, PO, PP, PpQ, PR, PS, PT, PU, PZ, PV, PX, PY, PW, PE, PZ, PJ],
        "Presión (psi)":[PB/6894.76, PC/6894.76, PD/6894.76, PE/6894.76, PF/6894.76, PG/6894.76, PH/6894.76, PI/6894.76, PJ/6894.76, PK/6894.76, PL/6894.76, PM/6894.76, PN/6894.76, PO/6894.76, PP/6894.76, PpQ/6894.76, PR/6894.76, PS/6894.76, PT/6894.76, PU/6894.76, PZ/6894.76, PV/6894.76, PX/6894.76, PY/6894.76, PW/6894.76, PE/6894.76, PZ/6894.76, PJ/6894.76],
        "HGL (m)": [HGLB, HGLC, HGLD, HGLE, HGLF, HGLG, HGLH, HGLI, HGLJ, HGLK, HGLL, HGLM, HGLN, HGLO, HGLP, HGLQ, HGLR, HGLS, HGLT, HGLU, HGLZ, HGLV, HGLX, HGLY, HGLW, HGLE2, HGLZ2, HGLU2 ],
            }

      
      # Mostrar los valores en forma de tabla
      st.table(data)
    
      st.write("Los valores obtenidos son variados, en el sentido que es posible hacer un cálculo de presiones a partir de dos nodos o por secciones de tubo, en este caso se manejó por tubo, añadiendo en cada tubo la afección del accesorio correspondiente, tanto válvulas como codos en el sistema. ")
      st.write()
      
     
if __name__ == "__main__":
    LOL()
