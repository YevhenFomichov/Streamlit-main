import streamlit as st
import matplotlib.pyplot as plt
from projects import combined_mdi, mdi, dpi, vx, ek, ek_old

def plot_old_new(old_data, new_data, title):
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    ax1.plot(old_data['x'], old_data['y'])
    ax1.set_title('Old Model ' + title)
    
    ax2.plot(new_data['x'], new_data['y'])
    ax2.set_title('New Model ' + title)
    
    st.pyplot(fig)

def main():
    plt.rcParams["figure.figsize"] = (10, 4)

    st.sidebar.title("Menu")
    project = st.sidebar.radio('Which project would you like to test:', 
                               ['Combined MDI', 'MDI', 'DPI', 'VX', 'EK'], 
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
        old_data = ek_old.run()
        new_data = ek.run()
        plot_old_new(old_data, new_data, 'EK')

if __name__ == "__main__":
    main()
