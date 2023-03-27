#importing laibraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

#loading the dataset

df = pd.read_csv(r"C:\Users\Sunanda Kar\PycharmProjects\hotel_bookings 2.csv")
df.head

#Exploratory data analysis and data cleaning

df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

df.describe(include = 'object')



for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('.'* 50)

df.isnull().sum()


df.drop(['company','agent'],axis = 1, inplace = True)
df.dropna(inplace = True)

df.isnull().sum()

df.describe()

df['adr'].plot(kind = 'box')


plt.figure(figsize = (8,4))
ax1= sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels,_= ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchor(1,1))
plt.title('Reservation status in different hotels', size = 20)
plt.xlabel('hotel')
plt.ylabel( number of reservations')
plt.show()


resort_hotel = df[df['hotel'] == 'City Hotel']
resort_hote1['is_canceled`].value_counts(normalize= True)


city_hotel 1 = df[df['hotel'] == 'City Hotel']
city_hote1['is_canceled'].value_counts(normalize = True)

resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()

plt.figure(figsize (20,8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(resort_hotel.index, resort_hotel['adr'], label = 'Resort Hotel')


df['month']= df['reservation_status_date'].dt.month
plt.figure(figsize (16,8))
ax1 = sns.countplot(x 'month', hue = 'is_canceled', data = df, palette = 'bright')
legend_labels,_ = ax1. get_legend_handles_labels()
ax1.legend(bbox_to_anchore=(1,1))
plt.title( 'Reservation status per month', size = 20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled', 'canceled'])
plt.show()


plt.figure(figsize = (15,8))
plt.title('ADR per month', fontsize = 30)
sns.barplot('month', 'adr', data = df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.show()


cancelled_data == df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt. figure(figsize (8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)
plt.show()


df['market_segment'].value_counts()

df['market_segment'].value_count(normalizze = True)

cancelled_data['market_segment'].value_count(normalizze = True)



cancelled_df_adr= cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace = True)
cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

not_cancelled_data = df[df['is_canceled'] == 0]
not_cancelled_df_adre = not_cancelled_data.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace = True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace = True)

plt.figure(figsize : (20,6))
plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'], label = 'cancelled')
plt.legend()