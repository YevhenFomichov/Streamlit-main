import streamlit as st
import matplotlib.pyplot as plt
from projects import combined_mdi, mdi, dpi, vx, ek, ek_old

def main():
    plt.rcParams["figure.figsize"] = (10, 4)

    st.sidebar.title("Menu")
    project = st.sidebar.radio('Which project would you like to test:', 
                               ['Combined MDI', 'MDI', 'DPI', 'VX', 'EK', 'EK_old'], 
                               key='project_selector')

    if project == 'Combined MDI':
        combined_mdi.run()
    elif project == 'MDI':
        mdi.run()
    elif project == 'DPI':
        dpi.run()
    elif project == 'VX':
        vx.run()
    elif project == 'EK':
        ek.run()
    #elif project == 'EK_old':
        #ek_old.run()

if __name__ == "__main__":
    main()

