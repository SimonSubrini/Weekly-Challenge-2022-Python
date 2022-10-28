
# Forma 1

def tempConv(str):
    if '°C' in str or '°F' in str:
        num=str.split('°')
        if num[1]=='F':
            temp=(float(num[0])-32)*5/9
            txt='{:0.2f}°C'.format(temp)
        else:
            temp=(float(num[0])*(9/5)+32)
            txt='{:0.2f}°F'.format(temp)
        return txt
    else:
        return 'error, formato incorrecto'
        
# Forma 2 (Machine Learning)

import numpy as np
import tensorflow as tf

def entrenarModeloCel2fah():
    celcius=np.array([-40,-10,0,8,15,22,38],dtype=float)
    fahrenheit=np.array([-40,14,32,46,59,72,100],dtype=float)
    
    capa=tf.keras.layers.Dense(units=1,input_shape=[1]) #units: neuronas de salida, input_shape: neuronas de entrada
    cel2fah=tf.keras.Sequential([capa])
    
    cel2fah.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )
    cel2fah.fit(celcius,fahrenheit,epochs=1000,verbose=False)
    return cel2fah


def entrenarModeloFah2cel():
    celcius=np.array([-40,-10,0,8,15,22,38],dtype=float)
    fahrenheit=np.array([-40,14,32,46,59,72,100],dtype=float)
    
    capa=tf.keras.layers.Dense(units=1,input_shape=[1]) #units: neuronas de salida, input_shape: neuronas de entrada
    fah2cel=tf.keras.Sequential([capa])
    
    fah2cel.compile(
        optimizer=tf.keras.optimizers.Adam(0.1),
        loss='mean_squared_error'
    )
    fah2cel.fit(fahrenheit,celcius,epochs=1000,verbose=False)
    return fah2cel

def tempConvML(str):
    if '°C' in str or '°F' in str:
        num=float(str.split('°')[0])
        unit=str.split('°')[1]
        if unit=='F':
            temp=fah2cel.predict([num])[0][0]
            txt='{:0.2f}°C'.format(temp)
        else:
            temp=cel2fah.predict([num])[0][0]
            txt='{:0.2f}°F'.format(temp)
        return txt
    else:
        return 'error, formato incorrecto'
    
cel2fah=entrenarModeloCel2fah()
fah2cel=entrenarModeloFah2cel() 
    
print(tempConv('12°C'))
print(tempConv('55°F'))
print(tempConv('80'))
print(tempConvML('12°C'))
print(tempConvML('55°F'))
print(tempConvML('80'))
