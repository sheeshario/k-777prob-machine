import streamlit as st
import pandas as pd
import time
import random

st.write("""
# Simple Slot Machine Probability

Aplikasi berikut bertujuan untuk menghitung 
nilai **probabilitas** dari kemunculan angka jackpot(777)!
""")
st.write("""
> Kelompok 4 Probabilitas:
- Steven_205314172
- Wiliam_205314106
- Paulus C. Dito_205314159
- Agustinus Agung_205314163
- Mathys Jorge_205314174
- Hanjian Listanto_205314102
---
""")

st.sidebar.header('User Input Parameters / Slot')

def user_input_features():
    angka1 = st.sidebar.slider('Jumlah Angka 1', 0, 7, 5)
    angka2 = st.sidebar.slider('Jumlah Angka 2', 0, 6, 4)
    angka3 = st.sidebar.slider('Jumlah Angka 3', 0, 5, 3)
    angka4 = st.sidebar.slider('Jumlah Angka 4', 0, 4, 2)
    angka5 = st.sidebar.slider('Jumlah Angka 5', 0, 3, 1)
    angka7 = st.sidebar.slider('Jumlah Angka 7 (JACKPOT)', 0, 2, 1)
    data = {'Angka 1': [angka1, angka1*3],
            'Angka 2': [angka2, angka2*3],
            'Angka 3': [angka3, angka3*3],
            'Angka 4': [angka4, angka4*3],
            'Angka 5': [angka5, angka5*3],
            'Angka 7 (JACKPOT)': [angka7, angka7*3]}
    features = pd.DataFrame(data, index=['Jumlah', 'Total Data'])
    return features

df = user_input_features()

#calc totaldata
totalData = 0
totalDataPerSlot = 0
for i in range(6):
    totalData = totalData + df.iat[1,i]
    totalDataPerSlot = totalDataPerSlot + df.iat[0,i]

st.subheader('User Input parameters per slot')
st.write(df)
#desc
st.write("""Karena pada slot machine tersebut terdapat 3 kolom yang 
        berisikan masing - masing jumlah data yang telah dinpput. 
        Maka untuk mencari total data tinggal dikalikan 3 saja.""")
st.write("- Dari tabel tersebut didapatkan total data per slot sebanyak `{}` data.".format(str(totalDataPerSlot)))
st.write("- Dari tabel tersebut didapatkan total data sebanyak `{}` data.".format(str(totalData)))
st.write("---")

st.subheader('Probability of 777')

#data
valOf7 = df.iat[0,5]
prob = pow((valOf7/totalDataPerSlot),3)
kompProb = 1 - prob
calcString = str(valOf7) + "/" + str(totalDataPerSlot) + " * " + str(valOf7) + "/" + str(totalDataPerSlot) + " * " + str(valOf7) + "/" + str(totalDataPerSlot) + " = " + str(prob)

st.write('Kejadian tersebut merupakan kejadian saling bebas, sehingga dilakukan perhitungan sebagai berikut:')
st.write('Nilai dari 7 per slot = `{}`'.format(str(valOf7)))
st.write('Nilai dari total data per slot = `{}`'.format(str(totalDataPerSlot)))
st.write("""Sehingga dilakukan perhitungan `{}`""".format(calcString))
st.write("""yang merupakan nilai dari peluang munculnya angka 777""")
st.write("""Untuk nilai komplemen dari peluang di atas adalah `{}`""".format(kompProb))
st.write("---")


#777slot
def makeDataSet():
    loopAngka1 = df.iat[0,0]
    loopAngka2 = df.iat[0,1]
    loopAngka3 = df.iat[0,2]
    loopAngka4 = df.iat[0,3]
    loopAngka5 = df.iat[0,4]
    loopAngka7 = df.iat[0,5]

    listAng1 = []
    listAng2 = []
    listAng3 = []
    listAng4 = []
    listAng5 = []
    listAng7 = []
    dataSet = []
    for i in range(loopAngka1):
        listAng1.append(1)

    for i in range(loopAngka2):
        listAng1.append(2)

    for i in range(loopAngka3):
        listAng1.append(3)

    for i in range(loopAngka4):
        listAng1.append(4)

    for i in range(loopAngka5):
        listAng1.append(5)
        
    for i in range(loopAngka7):
        listAng1.append(7)

    dataSet.extend(listAng1)
    dataSet.extend(listAng2)
    dataSet.extend(listAng3)
    dataSet.extend(listAng4)
    dataSet.extend(listAng5)
    dataSet.extend(listAng7)
    return dataSet

#animation
def loadingTab():
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.005)
        progress.progress(i+1)

#generator machine
def generator_machine():
    slot1 = random.choice(dataSet)
    slot2 = random.choice(dataSet)
    slot3 = random.choice(dataSet)
    machineSlot = { 'Slot 1':slot1,
                'Slot 2':slot2, 
                'Slot 3':slot3}
    output = pd.DataFrame(machineSlot, index=['Rolls'])
    return output


st.subheader('777 Machine Slot - Prototype')
dataSet = makeDataSet()
st.write("Semesta per slot: `{}`".format(str(dataSet)))

if st.button('Roll!'):
    loadingTab()
    output = generator_machine()
    st.write(output)

