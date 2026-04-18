from app.services.qdrant_service import search_vectors


def hybrid_search(query_vector, question, top_k=5):

    vector_results = search_vectors(query_vector)

    keyword_results = []

    question_words = question.lower().split()

    for doc in vector_results:

        doc_lower = doc.lower()

        score = 0

        for word in question_words:
            if word in doc_lower:
                score += 1

        if score > 0:
            keyword_results.append(doc)

    # merge + remove duplicates
    results = list(dict.fromkeys(vector_results + keyword_results))

    return results[:top_k]