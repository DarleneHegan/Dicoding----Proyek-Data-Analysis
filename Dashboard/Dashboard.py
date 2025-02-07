import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

data = pd.read_csv('dashboard.csv')
st.title('Bike Sharing Dashboard')


with st.sidebar:
    st.image('Bike Logo.png')
    
    dataset_choice = st.selectbox('Choose Dataset', ['Day', 'Hour'])

# Dataset Day :

if dataset_choice == 'Day':
    colors = ['#e21d1d', '#19CDE6']
    st.header('Performance 2011-2012')
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Total 2012', value='1243103')

    with col2:
        st.metric('Total 2012', value='2049576')

    # Bike Sharing Performance
    fig , ax = plt.subplots(figsize=(10,5))
    sns.lineplot(data=data, x='month_day', y='count_day', hue='year_day', marker='o', errorbar=None, palette=colors)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.legend(title='Year')
    ax.tick_params(axis='x', labelsize=10, rotation=45)
    ax.tick_params(axis='y')
    ax.grid()
    st.pyplot(fig)

    # Performance by Season
    st.header('Performance by Season')
    fig , ax = plt.subplots(figsize=(7,5))
    sns.barplot(data=data, x='season_day', y='count_day', hue='year_day', errorbar=None, palette=colors)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.legend(title='Year')
    ax.grid()
    st.pyplot(fig)

    # Bike Sharing
    st.header('Working day and Holiday')
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    sns.barplot(data=data, x='workingday_day', y='count_day', errorbar=None, ax=ax[0], palette=colors)
    ax[0].set_title('Working Day Column', fontsize=20)
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)
    ax[0].tick_params(axis='x', labelsize=15)

    sns.barplot(data=data, x='holiday_day', y='count_day', errorbar=None, ax=ax[1], palette=colors)
    ax[1].set_title('Holiday Column', fontsize=20)
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)
    ax[1].tick_params(axis='x', labelsize=15)
    st.pyplot(fig)

    # Proportion of Registered and Casual 
    st.header('User Registered and Casual')

    col1, col2 = st.columns(2)
    with col1:
        st.metric('Total Registered', value='2672662')
    with col2:
        st.metric('Total Casual', value='620017')
     
    count_registered = data['registered_day'].sum()
    count_casual     = data['casual_day'].sum()
    sizes = [count_registered, count_casual]
    labels = ['Registered', 'Casual']
    fig, ax= plt.subplots(figsize=(4,3))
    plt.pie(sizes, labels=labels, startangle=90, autopct= '%1.1f%%', textprops={'fontsize': 5}, radius=0.8, colors=colors)
    st.pyplot(fig)

    # Performance by Weather
    st.header('Performance by Weather')
    fig , ax = plt.subplots(figsize=(10,5))
    sns.barplot(data=data, x='weather_day', y='count_day', hue='year_day', errorbar=None, palette=colors)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.legend(title='Year')
    st.pyplot(fig)


    
# Dataset Hour :

else :
    colors = ['#F2D00D', '#0D2FF2']
    st.header('Bike Sharing Performance 2011-2012')
    col1, col2 = st.columns(2)

    with col1:
        st.metric('Total 2012', value='1243103')

    with col2:
        st.metric('Total 2012', value='2049576')

    # Performance 2011-2012
    fig , ax = plt.subplots(figsize=(10,5))
    sns.lineplot(data=data, x='month_hour', y='count_hour', hue='year_hour', marker='o', errorbar=None, palette=colors)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.legend(title='Year')
    ax.tick_params(axis='x', labelsize=10, rotation=45)
    ax.tick_params(axis='y')
    ax.grid()
    st.pyplot(fig)

    # Bike Sharing by Season
    st.header('Performance by Season')
    fig , ax = plt.subplots(figsize=(7,5))
    sns.barplot(data=data, x='season_hour', y='count_hour', hue='year_hour', errorbar=None, palette=colors)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.legend(title='Year')
    ax.grid()
    st.pyplot(fig)

    # Working Day and Holiday

    st.header('Working Day and Holiday')
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))

    sns.barplot(data=data, x='workingday_hour', y='count_hour', errorbar=None, ax=ax[0], palette=colors)
    ax[0].set_title('Working Day Column', fontsize=20)
    ax[0].set_xlabel(None)
    ax[0].set_ylabel(None)
    ax[0].tick_params(axis='x', labelsize=15)

    sns.barplot(data=data, x='holiday_hour', y='count_hour', errorbar=None, ax=ax[1], palette=colors)
    ax[1].set_title('Holiday Column', fontsize=20)
    ax[1].set_xlabel(None)
    ax[1].set_ylabel(None)
    ax[1].tick_params(axis='x', labelsize=15)

    st.pyplot(fig)

    # Proportion of Registered and Casual 

    st.header('User Registered and Casual')

    col1, col2 = st.columns(2)
    with col1:
        st.metric('Total Registered', value='2672662')
    with col2:
        st.metric('Total Casual', value='620017')
     
    count_registered = data['registered_hour'].sum()
    count_casual     = data['casual_hour'].sum()
    sizes = [count_registered, count_casual]
    labels = ['Registered', 'Casual']
    fig, ax= plt.subplots(figsize=(4,3))
    plt.pie(sizes, labels=labels, startangle=90, autopct= '%1.1f%%', textprops={'fontsize': 5}, radius=0.8, colors=colors)
    st.pyplot(fig)

    # Performance by Weather
    st.header('Performance by Weather')
    fig , ax = plt.subplots(figsize=(10,5))
    sns.barplot(data=data, x='weather_hour', y='count_hour', hue='year_hour', errorbar=None, palette=colors)
    ax.set_xlabel(None)
    ax.set_ylabel(None)
    ax.legend(title='Year')
    st.pyplot(fig)


    



  


