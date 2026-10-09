import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# -----------------------------
# Load government schemes
# -----------------------------
with open("government_schemes.csv", "r", encoding="utf-8-sig") as file:
    schemes = list(csv.DictReader(file))


# -----------------------------
# Create searchable text
# -----------------------------
documents = []

for scheme in schemes:
    text = " ".join(
        str(value)
        for value in scheme.values()
        if value
    )
    documents.append(text)


# -----------------------------
# Create TF-IDF model
# -----------------------------
vectorizer = TfidfVectorizer(
    stop_words="english"
)

document_vectors = vectorizer.fit_transform(documents)


# -----------------------------
# Search function
# -----------------------------
def search_schemes(query, top_k=3):

    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors
    )[0]

    ranked_indexes = similarities.argsort()[::-1]

    results = []

    for index in ranked_indexes[:top_k]:

        if similarities[index] > 0:

            results.append({
                "scheme": schemes[index],
                "score": similarities[index]
            })

    return results