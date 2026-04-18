def rerank_documents(question: str, documents: list, top_k: int = 3):

    scores = []

    question_words = question.lower().split()

    for doc in documents:

        doc_lower = doc.lower()

        score = 0

        for word in question_words:
            if word in doc_lower:
                score += 1

        scores.append((score, doc))

    # sort by score
    scores.sort(reverse=True)

    # select top documents
    reranked = [doc for score, doc in scores[:top_k]]

    return reranked



    