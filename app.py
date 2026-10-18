
import streamlit as st

st.set_page_config(
    page_title="Health Ashram | Cure India",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- COLOURS & DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background-color: #F3F8EF;
    color: #244B30;
}

.block-container {
    max-width: 1250px;
    padding: 2rem 2rem 4rem 2rem;
}

/* Larger, readable text */
html, body, [class*="css"] {
    font-size: 19px;
}

h1 {
    font-size: 46px !important;
    color: #FFFFFF !important;
}

h2 {
    font-size: 34px !important;
    color: #245C36 !important;
}

h3 {
    font-size: 25px !important;
    color: #245C36 !important;
}

p, label, li {
    font-size: 19px !important;
    line-height: 1.6 !important;
}

/* Hero banner */
.hero {
    background: linear-gradient(120deg, #17492A, #39784A);
    padding: 38px 24px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 30px;
}

.hero h1 {
    margin: 0;
    letter-spacing: 1px;
}

.hero p {
    color: #F1F8ED !important;
    font-size: 21px !important;
    margin: 10px 0 0 0;
}

/* Food cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    background-color: #FFFFFF;
    border: 1px solid #D8E8D2;
    border-radius: 18px;
    padding: 12px;
    box-shadow: 0 3px 12px rgba(36, 92, 54, 0.07);
}

/* Buttons: white text on dark green */
.stButton > button {
    background-color: #245C36 !important;
    color: #FFFFFF !important;
    border: 2px solid #245C36 !important;
    border-radius: 11px !important;
    min-height: 48px;
    font-size: 18px !important;
    font-weight: 700 !important;
}

.stButton > button p {
    color: #FFFFFF !important;
    font-size: 18px !important;
}

.stButton > button:hover {
    background-color: #39784A !important;
    border-color: #39784A !important;
    color: #FFFFFF !important;
}

/* Cart total */
.total-box {
    background-color: #DDEFD5;
    border: 2px solid #B8D9AE;
    border-radius: 16px;
    padding: 22px;
    color: #17492A;
    font-size: 28px;
    font-weight: 800;
    text-align: right;
}

/* Section separators */
hr {
    border-color: #D2E4CA;
    margin-top: 28px;
    margin-bottom: 28px;
}

@media (max-width: 700px) {
    .block-container {
        padding: 1rem 0.8rem 3rem 0.8rem;
    }

    h1 {
        font-size: 34px !important;
    }

    h2 {
        font-size: 28px !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- MENU DATA ----------------
# Replace these example prices with the actual prices.
# Add an image URL in "image" when you have one.

menu = [
    {
        "id": "thali",
        "name": "Healthy Thali",
        "price": 0,
        "image": "",
        "tag": "100% Vegetarian",
        "description": (
            "Basmati rice, 2 multi-millet rotis, seasonal vegetables, "
            "salad, chole, dal and pickle."
        )
    },
    {
        "id": "roti-sabji-channa",
        "name": "Roti – Sabji – Channa",
        "price": 0,
        "image": "",
        "tag": "Student Favourite",
        "description": (
            "2 multi-millet rotis, seasonal vegetables, salad, "
            "chole and pickle."
        )
    },
    {
        "id": "honey-roll",
        "name": "Honey Roll",
        "price": 0,
        "image": "",
        "tag": "Healthy Snack",
        "description": (
            "2 multi-millet rotis with peanut butter "
            "and organic mountain honey."
        )
    },
    {
        "id": "power-breakfast",
        "name": "Power Breakfast",
        "price": 0,
        "image": "",
        "tag": "Start Your Day Right",
        "description": (
            "Traditional rice flour with coconut, dried nuts, "
            "organic mountain honey and warm cow milk."
        )
    },
    {
        "id": "aloo-paratha",
        "name": "Aloo Paratha",
        "price": 0,
        "image": "",
        "tag": "Classic Favourite",
        "description": (
            "Fine wholewheat atta roti with select spices "
            "and potatoes."
        )
    },
    {
        "id": "energy-meal",
        "name": "Energy Meal",
        "price": 0,
        "image": "",
        "tag": "Wholesome Meal",
        "description": (
            "A semi-fluid meal made with lentils, legumes, leaves, "
            "garlic, ginger, herbs and spices."
        )
    },
    {
        "id": "salad",
        "name": "Salad with Steamed Vegetables",
        "price": 0,
        "image": "",
        "tag": "Fresh & Colourful",
        "description": (
            "Seasonal steamed and fresh vegetables "
            "with Health Ashram's secret seasoning."
        )
    }
]


# ---------------- SESSION CART ----------------
if "cart" not in st.session_state:
    st.session_state.cart = {}


# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <h1>🌿 CURE INDIA</h1>
    <p><b>HEALTH ASHRAM</b></p>
    <p>Eat Healthy. Live Better. Build a Healthier India.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("## 🍃 Our Menu")
st.write(
    "Fresh, nourishing food for your everyday well-being. "
    "Choose your favourites and add them to your cart."
)

st.write("")


# ---------------- MENU FILTER ----------------
search = st.text_input(
    "🔎 Search your favourite food",
    placeholder="Try thali, paratha, salad..."
)

filtered_menu = [
    item for item in menu
    if search.lower() in (
        item["name"] + " " + item["description"] + " " + item["tag"]
    ).lower()
]

if not filtered_menu:
    st.warning("No food items found. Try another search.")


# ---------------- FOOD CARDS ----------------
# Two cards per row, adapting to the screen.

for start in range(0, len(filtered_menu), 2):
    columns = st.columns(2)

    for offset, item in enumerate(filtered_menu[start:start + 2]):
        with columns[offset]:
            with st.container(border=True):

                # Add your own image URL in the menu data above.
                if item["image"]:
                    st.image(item["image"], use_container_width=True)
                else:
                    st.markdown(
                        "<div style='background:#E8F3E2;"
                        "border-radius:12px;padding:28px 8px;"
                        "text-align:center;font-size:48px;'>🥗</div>",
                        unsafe_allow_html=True
                    )

                st.markdown(f"### {item['name']}")
                st.caption(f"🌱 {item['tag']}")
                st.write(item["description"])

                st.markdown(
                    f"<h3 style='color:#245C36;'>₹{item['price']}</h3>",
                    unsafe_allow_html=True
                )

                if st.button(
                    "＋ Add to Cart",
                    key=f"add_{item['id']}",
                    use_container_width=True
                ):
                    if item["id"] in st.session_state.cart:
                        st.session_state.cart[item["id"]]["quantity"] += 1
                    else:
                        st.session_state.cart[item["id"]] = {
                            "name": item["name"],
                            "price": item["price"],
                            "quantity": 1
                        }

                    st.toast(f"{item['name']} added to your cart!")
                    st.rerun()


# ---------------- SHOPPING CART ----------------
st.divider()

cart_count = sum(
    item["quantity"]
    for item in st.session_state.cart.values()
)

st.markdown(f"## 🛒 Your Cart ({cart_count} items)")

cart = st.session_state.cart

if not cart:
    st.info(
        "Your cart is waiting! 💚 "
        "Add a delicious meal from our menu to get started."
    )

else:
    total = 0

    for item_id, details in list(cart.items()):
        price = details["price"]
        quantity = details["quantity"]
        subtotal = price * quantity
        total += subtotal

        with st.container(border=True):
            name_col, qty_col, subtotal_col = st.columns([3, 1, 1])

            with name_col:
                st.markdown(f"### {details['name']}")
                st.write(f"₹{price} per item")

            with qty_col:
                st.write("**Quantity**")
                st.write(str(quantity))

            with subtotal_col:
                st.write("**Subtotal**")
                st.write(f"₹{subtotal}")

            minus_col, plus_col, remove_col = st.columns(3)

            with minus_col:
                if st.button("− Reduce", key=f"minus_{item_id}"):
                    if quantity <= 1:
                        del st.session_state.cart[item_id]
                    else:
                        st.session_state.cart[item_id]["quantity"] -= 1
                    st.rerun()

            with plus_col:
                if st.button("＋ Add one", key=f"plus_{item_id}"):
                    st.session_state.cart[item_id]["quantity"] += 1
                    st.rerun()

            with remove_col:
                if st.button("Remove item", key=f"remove_{item_id}"):
                    del st.session_state.cart[item_id]
                    st.rerun()

    st.markdown(
        f"<div class='total-box'>Total: ₹{total}</div>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("🗑️ Clear Entire Cart"):
        st.session_state.cart = {}
        st.rerun()


# ---------------- FOOTER ----------------
st.divider()

st.markdown("""
<div style="text-align:center;padding:20px;color:#245C36;">
    <h3>🌿 Health Ashram</h3>
    <p>CURE INDIA · Healthy food for a healthier tomorrow.</p>
</div>
""", unsafe_allow_html=True)
