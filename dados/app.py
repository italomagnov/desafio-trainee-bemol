import pandas as pd
import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title='Bemol - Desafio',  layout='wide', page_icon='../bemol-icon.png')

@st.cache( allow_output_mutation=True )
def data_collect(path) :
    data =  pd.read_csv(path, index_col=0 )

    return data


def header():
    st.image('../bemol-icon.png', width = 120)
    st.title("Bemol - Desafio Trainee")
    st.markdown( "Desafio proposto pela [Bemol](https://bemol.com.br/) para o processo seletivo da vaga de Trainee Digital" )
    st.markdown( "**cel:** (92) 99207-4901 **| github:** [italomagnov](https://github.com/italomagnov) | email: italomagnov@gmail.com" )
    return None

def data_overview(df_customers, df_geolocation, df_order_items, df_payments, df_orders, df_products, df_sellers, df_product_categories):
    df_customers = df_customers[['customer_id', 'customer_unique_id', 'customer_city', 'customer_state']]
    df_geolocation = df_geolocation[['geolocation_zip_code_prefix', 'geolocation_city', 'geolocation_state']]
    df_order_items = df_order_items[['order_id', 'product_id', 'seller_id', 'price', 'freight_value']]
    df_payments = df_payments[['order_id', 'payment_type', 'payment_installments', 'payment_value']]
    df_orders = df_orders[['order_id', 'customer_id', 'order_status', 'order_purchase_timestamp']]
    df_products = df_products[['product_id', 'product_category_name']]
    df_sellers = df_sellers[['seller_id', 'seller_city', 'seller_state']]
    df_product_categories = df_product_categories[['product_category_name']]    

    df_overview = pd.merge(df_orders, df_customers, on='customer_id')
    df_overview = pd.merge(df_overview, df_order_items, on='order_id')
    df_overview = pd.merge(df_overview, df_payments, on='order_id')

    df_overview = pd.merge(df_overview, df_products, on='product_id')

    df_overview = pd.merge(df_overview, df_sellers, on='seller_id')
    df_overview = pd.merge(df_overview, df_product_categories, on='product_category_name')
    
    fig = go.Figure(
            data = [go.Table (
                header = dict(
                 values = list(df_overview.columns),
                 font=dict(size=12, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 #text wrapping
                 height=20
                 )
              ,cells = dict(
                  values = [df_overview[K].tolist() for K in df_overview.columns], 
                  font=dict(size=12),
                  align = ['left','center'],
                  line_color = 'rgba(255,255,255,0.2)',
                  height=20))])
    
    fig.update_layout( title_text="Tabelas Gerais",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=480)
    st.plotly_chart(fig, use_container_width=True)
    
    return None

def sale_ticket(df_orders, df_order_items):
    df_merge = pd.merge(df_orders, df_order_items, on='order_id')
    df_merge['total_order_value']=df_merge['price']*df_merge['order_item_id']
    df_merge['order_purchase_timestamp']=pd.to_datetime(df_merge['order_purchase_timestamp'])
    df_merge['order_purchase_month']=df_merge['order_purchase_timestamp'].dt.to_period('M')
    df_average_ticket=df_merge.groupby('order_purchase_month')['total_order_value'].mean().reset_index()
    df_sale_volume=df_merge.groupby('order_purchase_month').size().reset_index()
    df_sale_volume['order_purchase_month']=df_sale_volume['order_purchase_month'].astype(str)
    df_average_ticket['order_purchase_month']=df_average_ticket['order_purchase_month'].astype(str)
    
    trace_sales=go.Bar(
        x=df_sale_volume['order_purchase_month'],
        y=df_sale_volume[0],
        name='Volume de Vendas',
        marker=dict(color='blue'),
        yaxis='y1'
    )
    trace_ticket=go.Scatter(
        x=df_average_ticket['order_purchase_month'],
        y=df_average_ticket['total_order_value'],
        mode='lines+markers',
        name='Ticket Médio (R$)',
        line=dict(color='green'),
        yaxis='y2'
    )
    layout=go.Layout(
        title='Volume de Vendas e Ticket Médio Mensal',
        xaxis=dict(title='Mês'),
        yaxis=dict(title='Vol. Vendas', titlefont=dict(color='blue'), tickfont=dict(color='blue'), side='left'),
        yaxis2=dict(title='Ticket Medio (R$)', titlefont=dict(color='green'), tickfont=dict(color='green'), overlaying='y', side='right'),
        legend=dict(x=0, y=1),
        template="plotly_white"
    )
    fig=go.Figure(data=[trace_sales, trace_ticket], layout=layout)
    
    st.plotly_chart(fig, use_container_width=True)
    
    return None
    
    
if __name__ == '__main__':   
    
    df_customers = pd.read_csv('./data/olist_customers_dataset.csv')
    df_geolocation = pd.read_csv('./data/olist_geolocation_dataset.csv')
    df_order_items = pd.read_csv('./data/olist_order_items_dataset.csv')
    df_payments = pd.read_csv('./data/olist_order_payments_dataset.csv')
    df_reviews = pd.read_csv('./data/olist_order_reviews_dataset.csv')
    df_orders = pd.read_csv('./data/olist_orders_dataset.csv')
    df_products = pd.read_csv('./data/olist_products_dataset.csv')
    df_sellers = pd.read_csv('./data/olist_sellers_dataset.csv')
    df_product_categories = pd.read_csv('./data/product_category_name_translation.csv')
     
    header()
    data_overview(df_customers, df_geolocation, df_order_items, df_payments, df_orders, df_products, df_sellers, df_product_categories)
    sale_ticket(df_orders, df_order_items)