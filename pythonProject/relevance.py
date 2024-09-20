from sentence_transformers import SentenceTransformer

# Initialize the BERT model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')  # A lightweight BERT model for sentence similarity


def check_relevance(source_text, summarized_text):
    # Get the embeddings for both the source and summarized text
    source_embedding = model.encode([source_text])
    summary_embedding = model.encode([summarized_text])

    # Calculate cosine similarity between the embeddings
    similarity = model.similarity(source_embedding, summary_embedding)

    return similarity[0][0]  # Return the similarity score


# Example usage
source_text = "This is an English sentence. Another English sentence."
summarized_text = "This is an English sentence."

similarity_score = check_relevance(source_text, summarized_text)
print(f"Relevance Score: {similarity_score:.2f}")
