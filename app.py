import streamlit as st

# 1. Page Configuration (Sets the layout wide like Medikabazaar)
st.set_page_config(layout="wide", page_title="Medical Supply Corporate")

# 2. Mock Database (Placeholder products)
# Updated Mock Database with image URLs
mock_products = [
    {
        "name": "Advanced ICU Ventilator X1",
        "brand": "Philips Medical",
        "category": "Life Support",
        "price": "Contact for Pricing",
        "specs": "High-flow oxygen therapy, 12-inch touchscreen, backup battery.",
        "image": "Images/flower.jpg" # Medical machine photo
    },
    {
        "name": "Nitrile Medical Gloves (Box of 100)",
        "brand": "SafeTouch",
        "category": "Consumables",
        "price": "$12.50",
        "specs": "Powder-free, medical grade, textured fingertips, latex-free.",
        "image": "https://images.unsplash.com/photo-1581594693702-fbdc51b2763b?w=500" # Gloves photo
    },
    {
        "name": "Portable Ultrasound Machine Pro",
        "brand": "Chison",
        "category": "Imaging Systems",
        "price": "Contact for Pricing",
        "specs": "Color doppler, 2 transducer ports, lightweight corporate design.",
        "image": "https://images.unsplash.com/photo-1516549655169-df83a0774514?w=500" # Hospital screen photo
    },
    {
        "name": "Digital Blood Pressure Monitor",
        "brand": "Omron",
        "category": "Diagnostics",
        "price": "$45.00",
        "specs": "IntelliSense technology, memory storage for 2 users, irregular heartbeat detector.",
        "image": "https://images.unsplash.com/photo-1603398938378-e54eab446dde?w=500" # Doctor tool photo
    }
]
# 3. Corporate Header Block
st.title("🏥 Corporate Medical Supply Platform")
st.write("Authorized Institutional Distributor & Turnkey Healthcare Solutions")
st.divider()

# 4. Sidebar Configuration for Categories (Filtering Framework)
st.sidebar.header("📂 Navigation & Filters")
categories = ["All Categories", "Life Support", "Consumables", "Imaging Systems", "Diagnostics"]
selected_category = st.sidebar.selectbox("Select Product Sector:", categories)

# 5. Main Search Input (Search Framework)
search_query = st.text_input("🔍 Search our institutional catalog (e.g., 'Ventilator', 'Gloves')...")
# 6. Filter and Search Logic Processing Loop
filtered_list = []

for product in mock_products:
    # Logic condition A: Does the category match the sidebar filter?
    match_category = (selected_category == "All" or 
                      selected_category == "All Categories" or 
                      product["category"] == selected_category)
    
    # Logic condition B: Does search query match product details? (Case-insensitive)
    match_search = (search_query.lower() in product["name"].lower() or 
                    search_query.lower() in product["specs"].lower() or
                    search_query.lower() in product["brand"].lower())
    
    # If both conditions are met, push product to our active display queue
    if match_category and match_search:
        filtered_list.append(product)
# 7. Display Results in a Clean 2-Column Grid Array
st.write(f"Showing **{len(filtered_list)}** products matching your criteria.")

# Set layout parameters
columns_layout = st.columns(2)

for index, product in enumerate(filtered_list):
    # This math switches back and forth between Column 0 and Column 1
    current_col = columns_layout[index % 2]
    
    with current_col:
        with st.container(border=True):
            st.image(product["image"], use_container_width=True)
            st.subheader(product["name"])
            st.caption(f"Brand: {product['brand']} | Category: {product['category']}")
            st.write(f"💰 **Price Status:** {product['price']}")
            
            with st.expander("🔬 View Technical Specifications"):
                st.write(product["specs"])
            
            # Button Action Framework
            # 1. Define your uncle's business phone number (Use country code, no symbols or spaces)
# Replace this with his real number later! For now, using a placeholder.
company_phone = "8801700000000" 

# 2. Automatically format a custom message for the WhatsApp link
custom_message = f"Hello! I am interested in inquiring about the following institutional product:\n\n*Product:* {product['name']}\n*Brand:* {product['brand']}\n\nPlease provide availability and pricing details."

# 3. Clean up the text format so web browsers can read the spaces safely
import urllib.parse
encoded_message = urllib.parse.quote(custom_message)

# 4. Create the final dynamic URL string
whatsapp_url = f"https://wa.me/{company_phone}?text={encoded_message}"

# 5. Show a clean, clickable link styled as a call-to-action button
st.link_button("📥 Send Official WhatsApp Inquiry", whatsapp_url, use_container_width=True)