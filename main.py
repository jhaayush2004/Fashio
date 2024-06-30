# Loading dataset with the file path
df = pd.read_csv(r"C:\Users\Ayush\Downloads\Preprocessed data.csv")

# Definined sentences as description contains info about product
sentences = df['description'].tolist()

# Loading Sentence Transformer model
model = SentenceTransformer('ShauryaNova/autotrain-ShauryaNova')

# Encoding my sentences into embeddings
embeddings = model.encode(sentences)

# Converting my embeddings to numpy array
embeddings = np.array(embeddings)

# Initialize FAISS index
d = embeddings.shape[1]  # Dimensionality of embeddings
index = faiss.IndexFlatIP(d)  # Inner product for similarity search
index.add(embeddings)
