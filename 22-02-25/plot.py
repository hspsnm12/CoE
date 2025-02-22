import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df  = pd.read_csv(r'C:\22b81a1218\22-02-25\inventory_data_noisy.csv')
## Handling numerical values
df['Quantity'].fillna(df['Quantity'].mean(),inplace=True)
df['Consumption'].fillna(df['Consumption'].mean(),inplace=True)
## Handling missing  values in Categorical values (most frequent value)
df['Location'].fillna(df['Location'].mode()[0],inplace=True)
## drop the duplicated values
df.drop_duplicates(inplace=True)
# Sample data (replace this with your actual data)

df_eda = df

# Initialize session state for both buttons
if 'show_histogram1' not in st.session_state:
    st.session_state['show_histogram1'] = False

if 'show_boxplot1' not in st.session_state:
    st.session_state['show_boxplot1'] = False

if 'show_histogram2' not in st.session_state:
    st.session_state['show_histogram2'] = False
if 'show_boxplot2' not in st.session_state:
    st.session_state['show_boxplot2'] = False

    

# Streamlit app
st.title("Histogram for finding outliers")

# Button under the Exploratory Data Analysis heading
if st.button('Show Histogram1'):
    st.session_state['show_histogram1'] = True

# Display histograms if the button has been clicked
if st.session_state['show_histogram1']:
    # Setting up the layout for two plots side by side
    col1, col2 = st.columns(2)

    # Plotting the first chart in the first column
    with col1:
        fig1, ax1 = plt.subplots()
        sns.histplot(df_eda['Quantity'], kde=True, color='blue', ax=ax1)
        ax1.set_title('Distribution of Quantity')
        st.pyplot(fig1)

    # Plotting the second chart in the second column
    with col2:
        fig2, ax2 = plt.subplots()
        sns.histplot(df_eda['Consumption'], kde=True, color='blue', ax=ax2)
        ax2.set_title('Distribution of Consumption')
        st.pyplot(fig2)

    st.text(''' Inventory Imbalance: 
-> The majority of items have low quantity and consumption, but a few have exceptionally high stock.

 Low Consumption Rate:
-> Since most consumption values are very small, this further confirms underutilization of available stock.

 Presence of Outliers:
-> These extreme values might need further investigation to understand why they exist.''')

# Adding a heading for the box plot section
st.title("Outliers using Box Plot")

# Button under the Outliers using Box Plot heading
if st.button('Show Box Plot1'):
    st.session_state['show_boxplot1'] = True

# Display box plots if the button has been clicked
if st.session_state['show_boxplot1']:
    # Setting up the layout for two box plots side by side
    col3, col4 = st.columns(2)

    # Plotting the first box plot in the first column
    with col3:
        fig3, ax3 = plt.subplots()
        sns.boxplot(data=df_eda, x='Quantity', color='blue', ax=ax3)
        ax3.set_title('Boxplot of Quantity')
        st.pyplot(fig3)

    # Plotting the second box plot in the second column
    with col4:
        fig4, ax4 = plt.subplots()
        sns.boxplot(data=df_eda, x='Consumption', color='blue', ax=ax4)
        ax4.set_title('Boxplot of Consumption')
        st.pyplot(fig4)

    st.text('''
## Presence of Outliers:

1. Both Quantity and Consumption have outliers (points beyond the whiskers).
2. This suggests that some products have significantly higher stock or usage than the majority.

## Skewed Distributions:

1. Both plots show a concentration of values towards the lower range with a few extreme values pulling the distribution.
2. This confirms a right-skewed distribution, as seen in the histograms.

## Narrow Interquartile Range (IQR):

1. The box (middle 50% of data) is quite compressed, showing that most products have similar stock and consumption levels.
2. A few high values create long whiskers and outliers.

## Significant Gap Between Typical Values and Outliers:

1. The majority of quantity and consumption values are quite low.
2. However, a few products have extreme stock levels and consumption rates.''')



# Function to remove outliers using IQR
def remove_outliers_iqr(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)  # First quartile (25%)
        Q3 = df[col].quantile(0.75)  # Third quartile (75%)
        IQR = Q3 - Q1  # Interquartile range
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Filter out outliers
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    
    return df

# Select the columns for outlier removal (adjust as needed)
columns_to_filter = ["Quantity", "Consumption"]  
df= remove_outliers_iqr(df, columns_to_filter)


st.title("Histogram after removing outliers")

# Button under the Exploratory Data Analysis heading
if st.button('Show Histogram2'):
    st.session_state['show_histogram2'] = True

# Display histograms if the button has been clicked
if st.session_state['show_histogram2']:
    # Setting up the layout for two plots side by side
    col1, col2 = st.columns(2)

    # Plotting the first chart in the first column
    with col1:
        fig1, ax1 = plt.subplots()
        sns.histplot(df['Quantity'], kde=True, color='blue', ax=ax1)
        ax1.set_title('Distribution of Quantity')
        st.pyplot(fig1)

    # Plotting the second chart in the second column
    with col2:
        fig2, ax2 = plt.subplots()
        sns.histplot(df['Consumption'], kde=True, color='blue', ax=ax2)
        ax2.set_title('Distribution of Consumption')
        st.pyplot(fig2)



    st.title("Checking Outliers after removing them using Box Plot")

# Button under the Outliers using Box Plot heading
if st.button('Show Box Plot2'):
    st.session_state['show_boxplot2'] = True

# Display box plots if the button has been clicked
if st.session_state['show_boxplot2']:
    # Setting up the layout for two box plots side by side
    col3, col4 = st.columns(2)

    # Plotting the first box plot in the first column
    with col3:
        fig3, ax3 = plt.subplots()
        sns.boxplot(data=df, x='Quantity', color='blue', ax=ax3)
        ax3.set_title('Boxplot of Quantity')
        st.pyplot(fig3)

    # Plotting the second box plot in the second column
    with col4:
        fig4, ax4 = plt.subplots()
        sns.boxplot(data=df, x='Consumption', color='blue', ax=ax4)
        ax4.set_title('Boxplot of Consumption')
        st.pyplot(fig4)


## Adding column requirement based on Quantity and Consumption
low_threshold = df["Consumption"].quantile(0.33)
high_threshold = df["Consumption"].quantile(0.66)

def categorize_consumption(value):
    if value <= low_threshold:
        return "Low"
    elif value <= high_threshold:
        return "Medium"
    else:
        return "High"

df["Consumption_Level"] = df["Consumption"].apply(categorize_consumption)

df['Quantity_consumption_ratios'] = df['Quantity']/df['Consumption']


st.title("Visualization")
# Histogram & KDE
if st.button('Show Histogram & KDE'):
    st.session_state['show_histogram_kde'] = True

if st.session_state.get('show_histogram_kde', False):
    fig, axs = plt.subplots(1, 2, figsize=(15, 7))

    # First plot
    plt.subplot(121)
    sns.histplot(data=df, x='Quantity', bins=30, kde=True, color='g')
    plt.title('Histogram & KDE of Quantity')

    # Second plot with hue
    plt.subplot(122)
    sns.histplot(data=df, x='Quantity', kde=True, hue='Consumption_Level')
    plt.title('Histogram with KDE and Consumption Level')

    st.pyplot(fig)

    st.text('''

## Left Plot (Overall Quantity Distribution)
1. The Quantity values are evenly distributed across the entire range (from ~0 to 100).
2. The frequency of occurrences is relatively uniform, indicating that quantity values are not skewed toward any particular range.
3. The KDE curve is mostly flat, with minor fluctuations, reinforcing the idea of a near-uniform distribution.
4. There are no extreme peaks or dips, meaning no particular quantity range is overly dominant.

## Right Plot (Quantity Distribution by Consumption Level)
1. The Low Consumption Level (blue) has the highest frequency across most bins.
2. Medium Consumption (green) and High Consumption (orange) are distributed fairly evenly, but Medium Consumption is the least frequent.
3. The KDE curves suggest:
     1. Low Consumption is the most common category throughout.
     2. High Consumption is more concentrated in specific ranges.
     3. Medium Consumption is relatively stable but lower in frequency.
4. This indicates that most products or customers fall into the Low Consumption category, while High Consumption is less frequent.
## Key Takeaways
1. The overall distribution suggests a diverse range of quantities with no extreme bias.
2. Low Consumption dominates the dataset, meaning the model may predict this class more often.''')



st.title("Overall consumption distribution")
    # Histogram & KDE for Consumption
if st.button('Show Consumption Histogram & KDE'):
    st.session_state['show_consumption_histogram_kde'] = True

if st.session_state.get('show_consumption_histogram_kde', False):
    fig, axs = plt.subplots(1, 2, figsize=(15, 7))

    # First plot
    plt.subplot(121)
    sns.histplot(data=df, x='Consumption', bins=30, kde=True, color='g')
    plt.title('Histogram & KDE of Consumption')

    # Second plot with hue
    plt.subplot(122)
    sns.histplot(data=df, x='Consumption', kde=True, hue='Consumption_Level')
    plt.title('Histogram with KDE and Consumption Level')

    st.pyplot(fig)

    st.text('''
## Left Plot (Overall Consumption Distribution)
1. The consumption values are spread out between 5 and 19.
2. The distribution is fairly uniform, with no significant peaks or dips.
3. The KDE curve is relatively stable, indicating that consumption values occur at almost equal frequencies.
4. There is no clear skew, meaning that all consumption levels appear to be relatively balanced.

## Right Plot (Consumption Distribution by Consumption Level)
1. The data is segmented into three categories: Low, Medium, and High Consumption Levels.
2. Low Consumption (blue) is dominant in the 5 to 10 range.
3. Medium Consumption (green) is concentrated between 11 and 14.
4. High Consumption (orange) starts around 15 and goes up to 19.
5. Each consumption level has a well-defined range with minimal overlap, meaning the categories are distinct.
6. The KDE curves indicate some oscillations in frequency, especially for Low and High consumption levels.

## Key Takeaways
1. The dataset has clear separation between Low, Medium, and High consumption levels.
2. Most data points in the Low category are clustered around 5-10, while High consumption is concentrated in the upper range (15-19).
3. There might be a potential threshold effect, where consumption values naturally fall into these three groups.
''')


st.title("Distribution Across Quantity")

# Subplots for Quantity distribution with hue='Consumption_Level' by different locations
if st.button('Show Quantity Distribution by Location'):
    st.session_state['show_quantity_by_location'] = True

if st.session_state.get('show_quantity_by_location', False):
    fig, axs = plt.subplots(1, 4, figsize=(25, 6))

    # Overall Quantity distribution
    plt.subplot(141)
    sns.histplot(data=df, x='Quantity', kde=True, hue='Consumption_Level')
    plt.title('Overall Quantity Distribution')

    # Chicago
    plt.subplot(142)
    sns.histplot(data=df[df.Location == 'Chicago'], x='Quantity', kde=True, hue='Consumption_Level')
    plt.title('Chicago Quantity Distribution')

    # Los Angeles
    plt.subplot(143)
    sns.histplot(data=df[df.Location == 'Los Angeles'], x='Quantity', kde=True, hue='Consumption_Level')
    plt.title('Los Angeles Quantity Distribution')

    # New York
    plt.subplot(144)
    sns.histplot(data=df[df.Location == 'New York'], x='Quantity', kde=True, hue='Consumption_Level')
    plt.title('New York Quantity Distribution')

    st.pyplot(fig)

    st.text('''
## Insights on above plots

### Balanced Distribution Across Quantity:

1. The Quantity values seem to be fairly evenly distributed across the three consumption levels.
2. There are no extreme skews or clear separations among the classes.

### Consumption Levels Overlap:

1. The three consumption categories (Low, Medium, High) show overlapping density curves.
2. This suggests that Quantity alone might not be a strong differentiator for Consumption_Level.

### Possible Trends in KDE Curves:

1. The Low Consumption (blue line) appears more frequent at lower quantity values.
2. The Medium Consumption (orange line) is spread across the middle.
3. The High Consumption (green line) has peaks toward the higher quantity values.
        ''')


st.title("Multivariate analysis using pyplot")
# Multivariate analysis using pieplot
if st.button('Show Multivariate Analysis Pieplots'):
    st.session_state['show_multivariate_analysis'] = True

if st.session_state.get('show_multivariate_analysis', False):
    fig, axs = plt.subplots(1, 4, figsize=(30, 12))

    # Location pieplot
    size = df['Location'].value_counts()
    labels = ['Chicago', 'Los Angeles', 'New York']
    color = ['red', 'green', 'blue']
    axs[0].pie(size, colors=color, labels=labels, autopct='%1.2f%%')
    axs[0].set_title('Location', fontsize=20)
    axs[0].axis('off')

    # Dealer_ID pieplot
    size = df['Dealer_ID'].value_counts()
    labels = ['D000', 'D001', 'D002', 'D003', 'D004', 'D005', 'D006', 'D007', 'D008', 'D009']
    color = plt.cm.rainbow(np.linspace(0, 1, len(labels)))
    axs[1].pie(size, colors=color, labels=labels, autopct='%1.2f%%')
    axs[1].set_title('Dealer_ID', fontsize=20)
    axs[1].axis('off')

    # Product_ID pieplot
    size = df['Product_ID'].value_counts()
    labels = ['P000', 'P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007', 'P008', 'P009', 
              'P010', 'P011', 'P012', 'P013', 'P014', 'P015', 'P016', 'P017', 'P018', 'P019']
    color = plt.cm.rainbow(np.linspace(0, 1, len(labels)))
    axs[2].pie(size, colors=color, labels=labels, autopct='%1.2f%%')
    axs[2].set_title('Product_ID', fontsize=20)
    axs[2].axis('off')

    # Consumption_Level pieplot
    size = df['Consumption_Level'].value_counts()
    labels = ['Low', 'Medium', 'High']
    color = ['red', 'green', 'blue']
    axs[3].pie(size, colors=color, labels=labels, autopct='%1.2f%%')
    axs[3].set_title('Consumption Level', fontsize=20)
    axs[3].axis('off')

    plt.tight_layout()

    st.pyplot(fig)

    st.text('''
        ### Location Distribution:
    The data is almost evenly split among the three cities:
    1. Chicago (~33.6%)
    2. Los Angeles (~33.3%)
    3. New York (~33.1%)
    4. This suggests that sales or consumption data is well-balanced across locations, meaning location alone may not be a strong predictor of consumption behavior.
### Dealer_ID Distribution:
    1. All 10 dealers have nearly equal representation (~10%) in the dataset.
    2. This indicates that no single dealer dominates the sales, making the dataset more diverse and preventing dealer bias.
###  Product_ID Distribution:
    1. The distribution of products is almost uniform, with each product making up about 5% of the dataset.
    2. There is no extreme dominance of a single product, which suggests that different products contribute evenly to sales/consumption.
### Consumption Level Distribution:
    1. Low Consumption is the largest category (~39.8%).
    2. Medium Consumption makes up about 33.7%.
    3. High Consumption is the smallest group at 26.5%.
    The imbalance in consumption levels suggests that most products or locations tend to fall into the low-to-medium consumption range, while high consumption is less common''')


st.title("Feature wise Visulaization")
st.title("UNIVARIATE ANALYSIS ON LOCATION COLUMN")

# Countplot & Pie chart for Location
if st.button('Show Location Countplot & Pie Chart'):
    st.session_state['show_location_plots'] = True

if st.session_state.get('show_location_plots', False):
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))

    # Countplot for Location
    sns.countplot(x=df['Location'], data=df, palette='bright', ax=ax[0], saturation=0.95)
    for container in ax[0].containers:
        ax[0].bar_label(container, color='black', size=20)
    ax[0].set_title('Countplot of Location')

    # Pie chart for Location
    ax[1].pie(x=df['Location'].value_counts(), labels=['Chicago', 'Los Angeles', 'New York'],
              explode=[0, 0.1, 0], autopct='%1.1f%%', shadow=True, 
              colors=['#ff4d4d', '#ff8000', '#ff6000'])
    ax[1].set_title('Pie Chart of Location')

    st.pyplot(fig)

    st.text('''
        
## Insights from the Above Plot:
#### Bar Chart (Left Plot):

1. This represents the count of some category (possibly transactions, sales, or inventory) across three locations: Chicago, Los Angeles, and New York.

2. New York has the highest count (6081), followed by Los Angeles (5932), and Chicago (5906).

3. The differences among the locations are small, indicating a fairly even distribution.

#### Pie Chart (Right Plot):

1. This shows the percentage contribution of each location to the total count.

2. Chicago (33.9%) has the highest share, while Los Angeles (33.1%) and New York (33.0%) are nearly equal.

3. The Los Angeles slice is slightly exploded, possibly to highlight its contribution.

#### Key Takeaways:

1. The distribution of counts across the three locations is almost equal, with no significant outliers.

2. This indicates a balanced distribution of resources/sales/inventory across the locations.

3. If this represents sales data, it suggests all three cities contribute nearly equally to overall performance.''')


st.title("BIVARIATE ANALYSIS ( Is Location has any impact on Consumption ? )")

# Grouping by 'Location' and aggregating using the sum of the relevant columns
location_group = df.groupby('Location').sum()
# Extracting the required data from the aggregated DataFrame
chicago_scores = [
    location_group.loc['Chicago', 'Consumption'], 
    location_group.loc['Chicago', 'Quantity']
]
losangeles_scores = [
    location_group.loc['Los Angeles', 'Consumption'], 
    location_group.loc['Los Angeles', 'Quantity']
]
newyork_scores = [
    location_group.loc['New York', 'Consumption'], 
    location_group.loc['New York', 'Quantity']
]


# Bar plot for Consumption and Quantity Averages
if st.button('Show Consumption and Quantity Averages Bar Plot'):
    st.session_state['show_avg_bar_plot'] = True

if st.session_state.get('show_avg_bar_plot', False):
    fig, ax = plt.subplots(figsize=(10, 8))

    X = ['Consumption Average', 'Quantity Average']
    X_axis = np.arange(len(X))

    # Plot the bars with offsets for each city
    ax.bar(X_axis - 0.2, chicago_scores, 0.2, label='Chicago')
    ax.bar(X_axis, losangeles_scores, 0.2, label='Los Angeles')
    ax.bar(X_axis + 0.2, newyork_scores, 0.2, label='New York')

    # Set the x-axis labels and title
    ax.set_xticks(X_axis)
    ax.set_xticklabels(X)
    ax.set_ylabel("Scores")
    ax.set_title("Consumption Ratios vs Quantity", fontweight='bold')

    # Show legend
    ax.legend()

    st.pyplot(fig)

    st.text('''
#### The bar chart provides a comparison of Consumption Average and Quantity Average across three cities: Chicago, Los Angeles, and New York.

## Key Insights:
#### Higher Quantity Average:

1. The Quantity Average is significantly higher than the Consumption Average for all three cities.
2. This suggests that while consumption values are relatively low, the total quantity available or used is much larger.

#### Similar Trends Across Cities:

1. All three cities (Chicago, Los Angeles, New York) show very similar values for both metrics.
2. There is no major disparity between them, indicating uniform consumption and quantity patterns.

#### Slight Variation in Consumption Average:

1. New York has the highest Consumption Average, followed closely by Los Angeles and Chicago.
2. However, the differences are minimal, meaning that consumption per unit (or per capita) is fairly consistent.

#### Implication of the Trends:

1. The high quantity average might indicate a large supply base or distribution network.
2. The relatively lower consumption average suggests that not all available quantity is being consumed.        
''')

st.title("Univariate analysis for dealers")
# Countplot and Pie Chart for Dealer_ID
if st.button('Show Dealer ID Distribution'):
    st.session_state['show_dealer_id_distribution'] = True

if st.session_state.get('show_dealer_id_distribution', False):
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))

    # Countplot on the first subplot
    sns.countplot(x=df['Dealer_ID'], data=df, palette='bright', ax=ax[0], saturation=0.95)
    for container in ax[0].containers:
        ax[0].bar_label(container, color='black', size=20)

    # Pie chart on the second subplot
    ax[1].pie(x=df['Dealer_ID'].value_counts(), labels=df['Dealer_ID'].value_counts().index,
              explode=[0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0], autopct='%1.1f%%', shadow=True)

    st.pyplot(fig)

    st.text('''
### Insights on the Above Plot
### The image contains two visualizations:

#### Left Plot (Bar Chart - Dealer ID vs. Count)
#### Right Plot (Pie Chart - Dealer ID Proportion)
1. Bar Chart (Left)
    -> This chart represents the count of occurrences for each Dealer ID (D000 to D009).
    -> The counts are almost equal across all dealers, ranging around 1780 to 1792.
    -> There is no significant variation, meaning all dealers have approximately the same level of activity.
    -> This suggests a well-distributed dataset where each dealer has nearly identical transaction or sales counts.
2. Pie Chart (Right)
    -> This pie chart confirms the equal distribution seen in the bar chart.
    -> Each dealer's share is almost 10%, which aligns with having 10 dealers with nearly equal counts.
    -> The slice labeled D003 is slightly larger (10.1%) and is also "exploded" for emphasis.
    -> Since the variations are minimal, no single dealer dominates the distribution.
#### Key Takeaways
    -> Uniform distribution: All dealers contribute almost equally to the dataset.
    -> Balanced dataset: No major outliers or significant disparities.
    -> D003 Slightly Higher: Though marginal, it has a slightly higher count than others.        
''')

st.title("BIVARIATE ANALYSIS ( Is Dealer  has any impact on consumption ? )")
# Barplots for Dealer_ID grouped by Quantity and Consumption
if st.button('Show Dealer ID Grouped Barplots'):
    st.session_state['show_dealer_id_grouped_barplots'] = True

if st.session_state.get('show_dealer_id_grouped_barplots', False):
    Group_data2 = df.groupby('Dealer_ID')

    fig, ax = plt.subplots(1, 2, figsize=(20, 8))

    # Barplot for Quantity
    sns.barplot(x=Group_data2['Quantity'].mean().index, y=Group_data2['Quantity'].mean().values, palette='mako', ax=ax[0])
    ax[0].set_title('Quantity', color='#005ce6', size=20)

    for container in ax[0].containers:
        ax[0].bar_label(container, color='black', size=15)

    # Barplot for Consumption
    sns.barplot(x=Group_data2['Consumption'].mean().index, y=Group_data2['Consumption'].mean().values, palette='flare', ax=ax[1])
    ax[1].set_title('Consumption', color='#005ce6', size=20)

    for container in ax[1].containers:
        ax[1].bar_label(container, color='black', size=15)

    st.pyplot(fig)

    st.text('''
### Insights on the Above Plot
### The image contains two bar charts:

### Left Chart -Quantity per Dealer
### Right Chart -Consumption per Dealer
1. Left Chart (Quantity)
    -> Represents the quantity of items associated with each Dealer ID (D000 to D009).
    -> The values are relatively close, with the range between 53.73 to 55.15.
    -> Dealer D004 has the highest quantity (55.15), while D003 has the lowest (53.73).
    -> The variation is minimal, indicating that all dealers handle almost the same quantity.
2. Right Chart (Consumption)
    -> Represents consumption per dealer.
    -> The values are again very close, ranging from 11.88 to 12.18.
    -> Dealer D009 has the highest consumption (12.18), while D005 has the lowest (11.88).
    -> The variation is very small, meaning all dealers have a nearly equal consumption rate.
### Key Takeaways
    -> Balanced Distribution: Both quantity and consumption are uniformly distributed across all dealers.
    -> No Major Outliers: The differences are minimal, meaning all dealers contribute equally to the dataset.
    -> D004 leads in Quantity, while D009 leads in Consumption, but the differences are not significant        
''')

st.title("UNIVARIATE ANALYSIS ( What is the most product most used? )")
# Countplot for Product_ID
if st.button('Show Product ID Countplot'):
    st.session_state['show_product_id_countplot'] = True

if st.session_state.get('show_product_id_countplot', False):
    plt.rcParams['figure.figsize'] = (15, 9)
    plt.style.use('fivethirtyeight')

    fig, ax = plt.subplots()
    sns.countplot(x='Product_ID', data=df, palette='Blues', ax=ax)
    ax.set_title('Comparison of Product ID', fontweight='bold', fontsize=20)
    ax.set_xlabel('Product ID')
    ax.set_ylabel('Count')

    st.pyplot(fig)

    st.text('''
        ### Insights on the Above Plot
#### The image is a horizontal bar chart visualizing the count of different Product IDs (P000 to P019).

### Observations

### Gradient-Based Distribution:

1. The chart uses a dark-to-light gradient to represent the count.
2. P000 has the lowest count, while P019 has the highest count.
3. The values increase progressively from P000 to P019.

### Uniform Growth:

1. The counts seem to increase in a nearly linear fashion.
2. No major spikes or dips, suggesting a consistent trend.

### Top vs. Bottom Products:

1. P019, P018, and P017 have the highest counts.
2. P000, P001, and P002 have the lowest counts.
3. This might indicate that newer or more popular products have higher demand.

### Key Takeaways
1. Steady Demand Increase: Product counts increase systematically from P000 to P019, hinting at a possible product lifecycle trend.
2. Even Distribution: No major fluctuations indicate a controlled distribution process.
3. Market Trend? The higher count for later product IDs suggests they could be newer, better-performing, or more in demand.''')

st.title("BIVARIATE ANALYSIS ( Is product id  has any impact on consumption ? )")
# Barh plot for Product_ID aggregation
if st.button('Show Product ID Aggregation Bar Plot'):
    st.session_state['show_product_id_barh_plot'] = True

if st.session_state.get('show_product_id_barh_plot', False):
    fig, ax = plt.subplots(figsize=(10, 10))
    
    # Aggregating and plotting
    df.groupby('Product_ID').agg('sum').plot(kind='barh', ax=ax)
    
    # Adjust legend position
    ax.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    
    st.pyplot(fig)

    st.text('''
        ### Insights on the Above Plot
### This horizontal bar chart compares three key metrics for each Product ID (P000 to P019):

### Quantity (Blue)
1. Consumption (Red)
2. Quantity-to-Consumption Ratio (Yellow)
3. Observations

### Quantity is significantly higher than Consumption:

1. The blue bars (Quantity) dominate the chart, meaning more products are available than consumed.
2. This might indicate overproduction, stockpiling, or lower demand for certain products.

### Consumption is much lower:
1. The red bars (Consumption) are relatively short, suggesting only a small portion of the available quantity is actually used.
2. This pattern is consistent across all products.

### Quantity-to-Consumption Ratio (Yellow) is minimal:

1. The yellow bars are very short, meaning the ratio is low.
2. This means a large gap exists between production (or stock) and actual usage.
3. High ratios could indicate wastage, inefficiency, or poor demand forecasting.

### Consistent Trends Across Products:

1. The same trend is observed across all Product IDs.
2. No significant outliers, meaning the imbalance is a systematic issue rather than a product-specific one.

### Key Takeaways
✔ Potential Overstocking: Since Quantity >> Consumption, there could be excess inventory.
✔ Inefficiency in Demand Planning: A low consumption rate suggests demand is lower than expected.
✔ Opportunity to Optimize Production & Distribution: Reducing quantity or boosting consumption strategies (e.g., marketing, promotions) could help balance supply and demand.''')
