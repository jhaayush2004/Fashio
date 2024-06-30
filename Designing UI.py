# Center-aligning my  title 'FASHIO'
st.markdown(
    f"""
    <h1 style='text-align: center;'>FASHIO🎩</h1>
    <h3 style='text-align: center;'>🌟🌟Where style meets passion...</h3>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
query_text = st.text_input('Tell us how can we fashionize you 💫')

# Number of results selection using slider
k = st.slider('Number of picks? 👒 ', min_value=1, max_value=20, value=5)

# Performing similarity search on user input
if st.button('Click to Discover✨'):
    # Display processing message
    with st.spinner('Tailoring your preferences💫'):
        time.sleep(2)  # Simulating some processing time

    # Encoding query into our embedding
    query_embedding = model.encode([query_text])[0]

    # Performing similarity search using FAISS
    query_embedding = query_embedding.reshape(1, -1).astype(np.float32)
    distances, indices = index.search(query_embedding, k)

    # Displaying my  results
    st.subheader(f"Find your look with : '{query_text}'")
    for i in range(k):
        idx = indices[0][i]
        name = df.iloc[idx]['title']
        description = df.iloc[idx]['description']
        url = df.iloc[idx]['url']
        distance = distances[0][i]
        st.markdown(f"**{name}**")
        st.markdown(f"Go to: [link]({url})")
        st.markdown(f"**Likeness: {distance*100:.2f}%**")


faiss.write_index(index, 'product_embeddings.index')  #  saving index for later use
